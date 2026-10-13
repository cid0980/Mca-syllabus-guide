/**
 * Answer cache in IndexedDB, so a question that was already answered is never paid for twice.
 * Falls back to memory when IndexedDB is unavailable (private mode, sandboxed iframe).
 */
const DB = 'studyfeed';
const STORE = 'aiAnswers';
const STORE_THREADS = 'aiThreads';
/** v2 adds the chat threads store; v1 databases upgrade in place and keep their answers. */
const VERSION = 2;

/** Both IndexedDB stores, so callers never hardcode a name. */
export const AI_STORES = { answers: STORE, threads: STORE_THREADS } as const;
const memory = new Map<string, string>();

let dbPromise: Promise<IDBDatabase | null> | null = null;

function db(): Promise<IDBDatabase | null> {
	if (typeof indexedDB === 'undefined') return Promise.resolve(null);
	if (!dbPromise) {
		dbPromise = new Promise((resolve) => {
			try {
				const req = indexedDB.open(DB, VERSION);
				req.onupgradeneeded = () => {
					const d = req.result;
					if (!d.objectStoreNames.contains(STORE)) d.createObjectStore(STORE, { keyPath: 'key' });
					if (!d.objectStoreNames.contains(STORE_THREADS))
						d.createObjectStore(STORE_THREADS, { keyPath: 'cardId' });
				};
				req.onsuccess = () => resolve(req.result);
				req.onerror = () => resolve(null);
			} catch {
				resolve(null);
			}
		});
	}
	return dbPromise;
}

/** Shared with $lib/ai/threads.ts so one connection serves both stores. */
export function openDb(): Promise<IDBDatabase | null> {
	return db();
}

export function cacheKey(parts: (string | undefined)[]): string {
	return parts.filter(Boolean).join('|');
}

export async function readAnswer(key: string): Promise<string | null> {
	if (memory.has(key)) return memory.get(key) ?? null;
	const d = await db();
	if (!d) return null;
	return new Promise((resolve) => {
		try {
			const req = d.transaction(STORE, 'readonly').objectStore(STORE).get(key);
			req.onsuccess = () => resolve((req.result?.answer as string) ?? null);
			req.onerror = () => resolve(null);
		} catch {
			resolve(null);
		}
	});
}

export async function writeAnswer(key: string, answer: string, meta: Record<string, string> = {}): Promise<void> {
	memory.set(key, answer);
	const d = await db();
	if (!d) return;
	try {
		d.transaction(STORE, 'readwrite')
			.objectStore(STORE)
			.put({ key, answer, at: Date.now(), ...meta });
	} catch {
		/* quota or blocked - the memory cache still works for this session */
	}
}

export async function clearAnswers(): Promise<void> {
	memory.clear();
	const d = await db();
	if (!d) return;
	await new Promise<void>((resolve) => {
		try {
			const req = d.transaction(STORE, 'readwrite').objectStore(STORE).clear();
			req.onsuccess = () => resolve();
			req.onerror = () => resolve();
		} catch {
			resolve();
		}
	});
}

export async function countAnswers(): Promise<number> {
	const d = await db();
	if (!d) return memory.size;
	return new Promise((resolve) => {
		try {
			const req = d.transaction(STORE, 'readonly').objectStore(STORE).count();
			req.onsuccess = () => resolve(req.result);
			req.onerror = () => resolve(memory.size);
		} catch {
			resolve(memory.size);
		}
	});
}
