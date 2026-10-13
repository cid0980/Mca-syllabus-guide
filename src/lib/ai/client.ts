/** Talks to /api/ask (never to a provider directly) and caches the answer. */
import type { ProviderId } from './providers';
import { cacheKey, readAnswer, writeAnswer } from './cache';

export interface AskRequest {
	provider: ProviderId;
	model: string;
	/** omitted for the `server` provider, which uses the hosting environment key */
	key?: string;
	question: string;
	cardId?: string;
	/** the saved card text the answer must stay inside */
	context: string;
}

export interface AskResult {
	answer: string;
	cached: boolean;
}

export async function ask(req: AskRequest, signal?: AbortSignal): Promise<AskResult> {
	const key = cacheKey(['v1', req.provider, req.model, req.cardId, req.question.trim().toLowerCase()]);
	const cached = await readAnswer(key);
	if (cached) return { answer: cached, cached: true };

	const res = await fetch('/api/ask', {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(req),
		signal
	});

	const data = (await res.json().catch(() => ({}))) as { answer?: string; error?: string };
	if (!res.ok || !data.answer) {
		throw new Error(data.error || `The request failed (${res.status}).`);
	}

	await writeAnswer(key, data.answer, {
		provider: req.provider,
		model: req.model,
		cardId: req.cardId ?? '',
		question: req.question
	});
	return { answer: data.answer, cached: false };
}

export async function listModels(provider: ProviderId, key?: string): Promise<string[]> {
	const res = await fetch('/api/ai/models', {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify({ provider, key })
	});
	const data = (await res.json().catch(() => ({}))) as { models?: string[]; error?: string };
	if (!res.ok || !data.models) throw new Error(data.error || `Could not list models (${res.status}).`);
	return data.models;
}
