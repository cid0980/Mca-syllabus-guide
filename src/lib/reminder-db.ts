/**
 * A tiny IndexedDB mirror of "how is today going".
 *
 * localStorage is invisible to a service worker, so when the browser wakes the worker up
 * (periodic background sync, or a push) it has no way to know whether the daily goal is met.
 * The page writes the answer here after every change; the worker reads it before it decides
 * whether to post a notification.
 *
 * Everything is defensive: this is a nice-to-have for a background nudge, so a failure here must
 * never break the app.
 */

const DB_NAME = 'studyfeed';
const STORE = 'reminder';
const KEY = 'today';

export interface ReminderMirror {
	/** local YYYY-MM-DD this record describes */
	day: string;
	done: number;
	goal: number;
	enabled: boolean;
	hour: number;
	minute: number;
	repeatHours: number;
	updatedAt: number;
}

function open(): Promise<IDBDatabase | null> {
	return new Promise((resolve) => {
		if (typeof indexedDB === 'undefined') return resolve(null);
		let req: IDBOpenDBRequest;
		try {
			req = indexedDB.open(DB_NAME, 1);
		} catch {
			return resolve(null);
		}
		req.onupgradeneeded = () => {
			const db = req.result;
			if (!db.objectStoreNames.contains(STORE)) db.createObjectStore(STORE);
		};
		req.onsuccess = () => resolve(req.result);
		req.onerror = () => resolve(null);
		req.onblocked = () => resolve(null);
	});
}

export async function writeMirror(value: ReminderMirror): Promise<void> {
	const db = await open();
	if (!db) return;
	await new Promise<void>((resolve) => {
		try {
			const tx = db.transaction(STORE, 'readwrite');
			tx.objectStore(STORE).put(value, KEY);
			tx.oncomplete = () => resolve();
			tx.onerror = () => resolve();
			tx.onabort = () => resolve();
		} catch {
			resolve();
		}
	});
	db.close();
}

export async function readMirror(): Promise<ReminderMirror | null> {
	const db = await open();
	if (!db) return null;
	const value = await new Promise<ReminderMirror | null>((resolve) => {
		try {
			const tx = db.transaction(STORE, 'readonly');
			const req = tx.objectStore(STORE).get(KEY);
			req.onsuccess = () => resolve((req.result as ReminderMirror) ?? null);
			req.onerror = () => resolve(null);
		} catch {
			resolve(null);
		}
	});
	db.close();
	return value;
}
