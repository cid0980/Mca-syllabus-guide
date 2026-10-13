/**
 * Small localStorage helpers. Every StudyFeed browser key starts with "sf:".
 * All reads are defensive - a corrupt value must never break the app.
 */
import { browser } from '$app/environment';

export const KEYS = {
	progress: 'sf:progress',
	bookmarks: 'sf:bookmarks',
	streak: 'sf:streak',
	settings: 'sf:settings',
	lastOpened: 'sf:lastOpened',
	ai: 'sf:ai',
	/** finished quiz runs; also written by $lib/quiz.ts, which uses this same key */
	quiz: 'sf:quiz'
} as const;

export function readJSON<T>(key: string, fallback: T): T {
	if (!browser) return fallback;
	try {
		const raw = localStorage.getItem(key);
		if (!raw) return fallback;
		return JSON.parse(raw) as T;
	} catch {
		return fallback;
	}
}

export function writeJSON(key: string, value: unknown): void {
	if (!browser) return;
	try {
		localStorage.setItem(key, JSON.stringify(value));
	} catch {
		/* quota or private mode - ignore, app stays usable for this session */
	}
}

export function removeKey(key: string): void {
	if (!browser) return;
	try {
		localStorage.removeItem(key);
	} catch {
		/* ignore */
	}
}

/** Today's date as YYYY-MM-DD in the device's local timezone. */
export function todayKey(d: Date = new Date()): string {
	const y = d.getFullYear();
	const m = String(d.getMonth() + 1).padStart(2, '0');
	const day = String(d.getDate()).padStart(2, '0');
	return `${y}-${m}-${day}`;
}

/** Whole days between two YYYY-MM-DD strings (b - a). */
export function daysBetween(a: string, b: string): number {
	const da = new Date(`${a}T00:00:00`);
	const db = new Date(`${b}T00:00:00`);
	return Math.round((db.getTime() - da.getTime()) / 86_400_000);
}
