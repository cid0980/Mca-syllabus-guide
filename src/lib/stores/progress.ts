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
import { KEYS, daysBetween, readJSON, removeKey, todayKey, writeJSON } from '$lib/storage';
import { forgetLastOpened } from '$lib/stores/lastOpened';

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
	progress.subscribe(() => {
		clearTimeout(saveTimer);
		saveTimer = setTimeout(flushProgress, 300);
	});
	streak.subscribe(() => {
		clearTimeout(saveTimer);
		saveTimer = setTimeout(flushProgress, 300);
	});

	/**
	 * A phone can kill the tab without warning, and the 300ms write delay is enough to lose the last
	 * thing the student did. Flush when the page is hidden or unloaded.
	 */
	const flushNow = () => flushProgress();
	globalThis.addEventListener('pagehide', flushNow);
	document.addEventListener('visibilitychange', () => {
		if (document.visibilityState === 'hidden') flushProgress();
	});
}

/** Writes progress and streak to localStorage immediately, skipping the debounce. */
export function flushProgress(): void {
	writeJSON(KEYS.progress, get(progress));
	writeJSON(KEYS.streak, get(streak));
}

/**
 * Marks a card read, or takes the mark back.
 *
 * This is only ever called from the button on the card. Scrolling past a card used to mark it, which
 * made the completion numbers meaningless, so the decision belongs to the student.
 */
export function setSeen(nodeId: string, seen: boolean): void {
	progress.update((map) => {
		const prev = map[nodeId];
		return {
			...map,
			[nodeId]: {
				seen,
				lastSeen: Date.now(),
				quizCorrect: prev?.quizCorrect ?? 0,
				quizWrong: prev?.quizWrong ?? 0
			}
		};
	});
	// unmarking must not count as a study day
	if (seen) touchStreak();
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

/**
 * Erases everything the student produced by studying, and nothing else.
 *
 * The write is immediate: the debounced writer used to leave the old values in localStorage for a
 * moment, so clearing and reloading quickly brought the numbers back. The quiz run log and the
 * continue point go too - they are study history as well. Saved cards and AI keys are not touched.
 */
export function clearProgress(): void {
	progress.set({});
	streak.set({ count: 0, lastDay: '' });
	removeKey(KEYS.quiz);
	forgetLastOpened();
	flushProgress();
}
