/**
 * Per-card chat threads.
 *
 * The answer cache (`aiAnswers`) already made a repeated question free, but nothing kept the
 * conversation itself: closing the ask panel lost it. A thread is stored per card, so closing the
 * chat — or the whole app — and coming back shows exactly what was asked and answered.
 *
 * Lives in the same IndexedDB database as the answer cache, in its own store, so the two never
 * fight over version numbers. Falls back to memory when IndexedDB is unavailable.
 */
import { AI_STORES, openDb } from './cache';

export interface ChatMessage {
	role: 'user' | 'assistant';
	text: string;
	at: number;
	/** the answer came from the cache, so it cost nothing */
	cached?: boolean;
	/** the provider call failed; the bubble offers a retry */
	failed?: boolean;
}

export interface ChatThread {
	cardId: string;
	updatedAt: number;
	messages: ChatMessage[];
}

/** Long enough for a real study conversation, short enough to stay cheap to write. */
export const MAX_MESSAGES = 40;

const memory = new Map<string, ChatThread>();

function capped(messages: ChatMessage[]): ChatMessage[] {
	return messages.length <= MAX_MESSAGES ? messages : messages.slice(messages.length - MAX_MESSAGES);
}

export async function loadThread(cardId: string): Promise<ChatThread | null> {
	const mem = memory.get(cardId);
	if (mem) return mem;
	const d = await openDb();
	if (!d) return null;
	return new Promise((resolve) => {
		try {
			const req = d.transaction(AI_STORES.threads, 'readonly').objectStore(AI_STORES.threads).get(cardId);
			req.onsuccess = () => resolve((req.result as ChatThread) ?? null);
			req.onerror = () => resolve(null);
		} catch {
			resolve(null);
		}
	});
}

export async function saveThread(cardId: string, messages: ChatMessage[]): Promise<void> {
	const thread: ChatThread = { cardId, updatedAt: Date.now(), messages: capped(messages) };
	memory.set(cardId, thread);
	const d = await openDb();
	if (!d) return;
	try {
		d.transaction(AI_STORES.threads, 'readwrite').objectStore(AI_STORES.threads).put(thread);
	} catch {
		/* quota or blocked - the in-memory copy still holds this session */
	}
}

export async function clearThread(cardId: string): Promise<void> {
	memory.delete(cardId);
	const d = await openDb();
	if (!d) return;
	await new Promise<void>((resolve) => {
		try {
			const req = d.transaction(AI_STORES.threads, 'readwrite').objectStore(AI_STORES.threads).delete(cardId);
			req.onsuccess = () => resolve();
			req.onerror = () => resolve();
		} catch {
			resolve();
		}
	});
}

export async function clearThreads(): Promise<void> {
	memory.clear();
	const d = await openDb();
	if (!d) return;
	await new Promise<void>((resolve) => {
		try {
			const req = d.transaction(AI_STORES.threads, 'readwrite').objectStore(AI_STORES.threads).clear();
			req.onsuccess = () => resolve();
			req.onerror = () => resolve();
		} catch {
			resolve();
		}
	});
}

export async function countThreads(): Promise<number> {
	const d = await openDb();
	if (!d) return memory.size;
	return new Promise((resolve) => {
		try {
			const req = d.transaction(AI_STORES.threads, 'readonly').objectStore(AI_STORES.threads).count();
			req.onsuccess = () => resolve(req.result);
			req.onerror = () => resolve(memory.size);
		} catch {
			resolve(memory.size);
		}
	});
}
