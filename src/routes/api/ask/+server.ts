/**
 * POST /api/ask — the only place a provider key is used.
 *
 * The browser sends { provider, model, key?, question, context }. The key comes from the user's
 * own Settings (localStorage) or, when provider is "server", from the hosting environment.
 * Nothing is logged, nothing is stored server-side.
 *
 * Provider endpoints (verified Oct 2026):
 *   gemini      POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent
 *               header x-goog-api-key
 *   openai-like POST {baseUrl}/chat/completions   (OpenRouter, NVIDIA NIM)  Bearer token
 */
import { json, type RequestHandler } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

const GEMINI_BASE = 'https://generativelanguage.googleapis.com/v1beta';
const OPENAI_BASE = {
	openrouter: 'https://openrouter.ai/api/v1',
	nvidia: 'https://integrate.api.nvidia.com/v1'
} as const;

const SYSTEM = `You are StudyFeed's study helper for a Pondicherry University MCA student.

Answer ONLY from the saved card the student is looking at, which is provided as CONTEXT.
If the answer is not in the context, say plainly that the saved card does not cover it and
suggest the closest topic that does. Never invent syllabus facts.

Style: short paragraphs, max 120 words, plain language, no markdown headings, no emoji.
Spell out any acronym the first time you use it. If the student asks about a quiz option, explain
why the correct option is right and why the others fail.`;

type ProviderId = 'server' | 'gemini' | 'openrouter' | 'nvidia';

interface Body {
	provider?: ProviderId;
	model?: string;
	key?: string;
	question?: string;
	context?: string;
	cardId?: string;
}

function serverProvider(): { provider: ProviderId; key: string; model: string } | null {
	const key =
		env.STUDYFEED_AI_KEY || env.OPENROUTER_API_KEY || env.NVIDIA_API_KEY || env.GEMINI_API_KEY || env.ANTHROPIC_API_KEY || '';
	if (!key) return null;
	const provider = (env.STUDYFEED_AI_PROVIDER as ProviderId) || (env.OPENROUTER_API_KEY ? 'openrouter' : env.NVIDIA_API_KEY ? 'nvidia' : 'gemini');
	return { provider, key, model: env.STUDYFEED_AI_MODEL || '' };
}

async function gemini(key: string, model: string, prompt: string, signal: AbortSignal): Promise<string> {
	const res = await fetch(`${GEMINI_BASE}/models/${encodeURIComponent(model)}:generateContent`, {
		method: 'POST',
		signal,
		headers: { 'content-type': 'application/json', 'x-goog-api-key': key },
		body: JSON.stringify({
			systemInstruction: { parts: [{ text: SYSTEM }] },
			contents: [{ role: 'user', parts: [{ text: prompt }] }],
			generationConfig: { temperature: 0.3, maxOutputTokens: 700 }
		})
	});
	const data = (await res.json().catch(() => ({}))) as {
		candidates?: { content?: { parts?: { text?: string }[] } }[];
		error?: { message?: string };
	};
	if (!res.ok) throw new HttpError(res.status, data.error?.message || `Gemini returned ${res.status}.`);
	const text = data.candidates?.[0]?.content?.parts?.map((p) => p.text ?? '').join('').trim();
	if (!text) throw new HttpError(502, 'Gemini returned an empty answer.');
	return text;
}

async function openaiLike(
	base: string,
	key: string,
	model: string,
	prompt: string,
	signal: AbortSignal
): Promise<string> {
	const headers: Record<string, string> = {
		'content-type': 'application/json',
		authorization: `Bearer ${key}`
	};
	// OpenRouter asks for these so usage can be attributed; harmless elsewhere.
	if (base.includes('openrouter')) {
		headers['HTTP-Referer'] = 'https://studyfeed.app';
		headers['X-Title'] = 'StudyFeed';
	}
	const res = await fetch(`${base}/chat/completions`, {
		method: 'POST',
		signal,
		headers,
		body: JSON.stringify({
			model,
			temperature: 0.3,
			max_tokens: 700,
			messages: [
				{ role: 'system', content: SYSTEM },
				{ role: 'user', content: prompt }
			]
		})
	});
	const data = (await res.json().catch(() => ({}))) as {
		choices?: { message?: { content?: string } }[];
		error?: { message?: string } | string;
	};
	if (!res.ok) {
		const msg = typeof data.error === 'string' ? data.error : data.error?.message;
		throw new HttpError(res.status, msg || `The provider returned ${res.status}.`);
	}
	const text = data.choices?.[0]?.message?.content?.trim();
	if (!text) throw new HttpError(502, 'The provider returned an empty answer.');
	return text;
}

class HttpError extends Error {
	status: number;
	constructor(status: number, message: string) {
		super(message);
		this.status = status;
	}
}

function friendly(err: unknown): { status: number; message: string } {
	if (err instanceof HttpError) {
		if (err.status === 401 || err.status === 403)
			return { status: 401, message: 'That API key was rejected. Check it in Settings.' };
		if (err.status === 404) return { status: 404, message: 'That model id does not exist for this provider.' };
		if (err.status === 429) return { status: 429, message: 'Rate limited or out of quota. Try again in a moment.' };
		return { status: err.status, message: err.message };
	}
	if ((err as Error)?.name === 'AbortError') return { status: 504, message: 'The provider took too long to answer.' };
	return { status: 500, message: (err as Error)?.message || 'Something went wrong.' };
}

export const POST: RequestHandler = async ({ request }) => {
	let body: Body;
	try {
		body = (await request.json()) as Body;
	} catch {
		return json({ error: 'Malformed request.' }, { status: 400 });
	}

	const question = (body.question ?? '').trim();
	const context = (body.context ?? '').trim();
	if (question.length < 2) return json({ error: 'Ask a question first.' }, { status: 400 });
	if (context.length < 20) return json({ error: 'No card context to answer from.' }, { status: 400 });

	let provider = body.provider ?? 'gemini';
	let key = (body.key ?? '').trim();
	let model = (body.model ?? '').trim();

	if (provider === 'server') {
		const s = serverProvider();
		if (!s) {
			return json(
				{
					error:
						'No server key is configured. Add your own key in Settings, or set STUDYFEED_AI_KEY (and STUDYFEED_AI_PROVIDER) in the hosting environment.'
				},
				{ status: 400 }
			);
		}
		provider = s.provider;
		key = s.key;
		model = model || s.model;
	}

	if (!key) return json({ error: 'No API key for that provider. Add one in Settings.' }, { status: 400 });
	if (provider === 'gemini' && !model) model = 'gemini-3.5-flash';
	if (!model && provider !== 'gemini') {
		return json({ error: 'No model selected for that provider.' }, { status: 400 });
	}

	const prompt = `CONTEXT (the saved card the student is looking at):\n${context}\n\nQUESTION: ${question}`;
	const controller = new AbortController();
	const timer = setTimeout(() => controller.abort(), 45_000);

	try {
		const answer =
			provider === 'gemini'
				? await gemini(key, model, prompt, controller.signal)
				: await openaiLike(OPENAI_BASE[provider as 'openrouter' | 'nvidia'], key, model, prompt, controller.signal);
		return json({ answer, provider, model });
	} catch (err) {
		const { status, message } = friendly(err);
		return json({ error: message }, { status });
	} finally {
		clearTimeout(timer);
	}
};
