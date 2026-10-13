/**
 * Progress, streak and derived stats.
 *
 * key `sf:progress` -> { [nodeId]: { seen, lastSeen, quizCorrect, quizWrong } }
 * key `sf:streak`   -> { count, lastDay }
 *
 * The stores start empty and are filled by initProgress() in onMount, so the first
 * render is identical on the server and in the browser.
 * Derived helpers take the progress map as an argument, which keeps templates reactive.
 */
import { browser } from '$app/environment';
import { get, writable } from 'svelte/store';
import type { ProgressMap, StreakState } from '$lib/types';
import { KEYS, daysBetween, readJSON, todayKey, writeJSON } from '$lib/storage';

export const progress = writable<ProgressMap>({});
export const streak = writable<StreakState>({ count: 0, lastDay: '' });

let ready = false;

export function initProgress(): void {
	if (!browser || ready) return;
	ready = true;
	progress.set(readJSON<ProgressMap>(KEYS.progress, {}));
	streak.set(readJSON<StreakState>(KEYS.streak, { count: 0, lastDay: '' }));
	refreshStreak();
	// debounced: writing on every card view was showing up as jank while scrolling
	let saveTimer: ReturnType<typeof setTimeout> | undefined;
	const flush = () => writeJSON(KEYS.progress, get(progress));
	progress.subscribe(() => {
		clearTimeout(saveTimer);
		saveTimer = setTimeout(flush, 300);
	});
	streak.subscribe((v) => {
		clearTimeout(saveTimer);
		saveTimer = setTimeout(() => {
			writeJSON(KEYS.progress, get(progress));
			writeJSON(KEYS.streak, v);
		}, 300);
	});
}

export function markSeen(nodeId: string): void {
	progress.update((map) => {
		const prev = map[nodeId];
		return {
			...map,
			[nodeId]: {
				seen: true,
				lastSeen: Date.now(),
				quizCorrect: prev?.quizCorrect ?? 0,
				quizWrong: prev?.quizWrong ?? 0
			}
		};
	});
	touchStreak();
}

export function recordQuiz(nodeId: string, correct: boolean): void {
	progress.update((map) => {
		const prev = map[nodeId] ?? { seen: true, lastSeen: Date.now(), quizCorrect: 0, quizWrong: 0 };
		return {
			...map,
			[nodeId]: {
				seen: true,
				lastSeen: Date.now(),
				quizCorrect: prev.quizCorrect + (correct ? 1 : 0),
				quizWrong: prev.quizWrong + (correct ? 0 : 1)
			}
		};
	});
	touchStreak();
}

export function touchStreak(): void {
	const today = todayKey();
	streak.update((s) => {
		if (s.lastDay === today) return s;
		if (!s.lastDay) return { count: 1, lastDay: today };
		const gap = daysBetween(s.lastDay, today);
		if (gap === 1) return { count: s.count + 1, lastDay: today };
		if (gap > 1) return { count: 1, lastDay: today };
		return s;
	});
}

export function refreshStreak(): void {
	const today = todayKey();
	streak.update((s) => {
		if (!s.lastDay) return s;
		return daysBetween(s.lastDay, today) > 1 ? { count: 0, lastDay: s.lastDay } : s;
	});
}

/* -------- derived stats (pure: pass the map in) -------- */

export function seenCountByIds(ids: string[], map: ProgressMap = {}): number {
	let n = 0;
	for (const id of ids) if (map[id]?.seen) n++;
	return n;
}

export function percentSeenByIds(ids: string[], map: ProgressMap = {}): number {
	if (ids.length === 0) return 0;
	return Math.round((seenCountByIds(ids, map) / ids.length) * 100);
}

export interface Accuracy {
	correct: number;
	wrong: number;
	answered: number;
	percent: number;
}

export function accuracyByIds(ids: string[], map: ProgressMap = {}): Accuracy {
	let correct = 0;
	let wrong = 0;
	for (const id of ids) {
		correct += map[id]?.quizCorrect ?? 0;
		wrong += map[id]?.quizWrong ?? 0;
	}
	const answered = correct + wrong;
	return { correct, wrong, answered, percent: answered ? Math.round((correct / answered) * 100) : 0 };
}

export function clearProgress(): void {
	progress.set({});
	streak.set({ count: 0, lastDay: '' });
}
