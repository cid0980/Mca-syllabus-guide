/**
 * POST /api/ai/models — lists the model ids a provider offers with the given key.
 * Used by Settings so nobody has to guess a model name (they change often).
 */
import { json, type RequestHandler } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

type ProviderId = 'server' | 'gemini' | 'openrouter' | 'nvidia';

export const POST: RequestHandler = async ({ request }) => {
	let body: { provider?: ProviderId; key?: string };
	try {
		body = (await request.json()) as { provider?: ProviderId; key?: string };
	} catch {
		return json({ error: 'Malformed request.' }, { status: 400 });
	}

	const provider = body.provider ?? 'gemini';
	let key = (body.key ?? '').trim();

	if (provider === 'server') {
		key = env.STUDYFEED_AI_KEY || env.OPENROUTER_API_KEY || env.NVIDIA_API_KEY || env.GEMINI_API_KEY || '';
	}
	if (!key) return json({ error: 'Add an API key first.' }, { status: 400 });

	try {
		if (provider === 'gemini' || provider === 'server') {
			const res = await fetch('https://generativelanguage.googleapis.com/v1beta/models?pageSize=200', {
				headers: { 'x-goog-api-key': key }
			});
			const data = (await res.json().catch(() => ({}))) as {
				models?: { name?: string; supportedGenerationMethods?: string[] }[];
				error?: { message?: string };
			};
			if (!res.ok) return json({ error: data.error?.message ?? `Google returned ${res.status}.` }, { status: res.status });
			const models = (data.models ?? [])
				.filter((m) => (m.supportedGenerationMethods ?? []).includes('generateContent'))
				.map((m) => (m.name ?? '').replace('models/', ''))
				.filter((m) => m && !m.includes('embedding') && !m.includes('aqa'))
				.slice(0, 60);
			return json({ models });
		}

		const base =
			provider === 'openrouter' ? 'https://openrouter.ai/api/v1' : 'https://integrate.api.nvidia.com/v1';
		const res = await fetch(`${base}/models`, { headers: { authorization: `Bearer ${key}` } });
		const data = (await res.json().catch(() => ({}))) as {
			data?: { id?: string }[];
			error?: { message?: string };
		};
		if (!res.ok) {
			const msg = typeof data.error === 'object' ? data.error?.message : undefined;
			return json({ error: msg ?? `The provider returned ${res.status}.` }, { status: res.status });
		}
		const models = (data.data ?? [])
			.map((m) => m.id ?? '')
			.filter(Boolean)
			.sort();
		return json({ models: models.slice(0, 200) });
	} catch (err) {
		return json({ error: (err as Error).message }, { status: 500 });
	}
};
