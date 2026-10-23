/**
 * Daily study reminder.
 *
 * The goal: two cards a day. One nudge at the set time, then another every `repeatHours` hours
 * until the goal is met or the day runs out (the last slot is 23:00, so a 9pm start with a
 * two-hour repeat gives 9pm and 11pm).
 *
 * Three ways a nudge can reach you, in order of how much machinery they need:
 *
 *  1. While the app is open — this module schedules it with a timer. No setup at all.
 *  2. With the app closed — `periodicSync` in the service worker. The browser wakes the worker
 *     every so often (Chrome, Android, installed app only) and the worker posts the notification
 *     itself after reading today's status from IndexedDB. Still no setup.
 *  3. Real push from a server — see $lib/push.ts. Needs VAPID keys and a daily trigger, so it
 *     stays off until those exist.
 *
 * Whatever the route, the same rule decides: has the goal been met, and has this slot already
 * fired today. `sf:reminder` remembers the slots that fired so a reload never double-nudges.
 */
import { browser } from '$app/environment';
import { get, writable } from 'svelte/store';
import type { ProgressMap, ReminderSettings, ReminderState } from '$lib/types';
import { KEYS, readJSON, todayKey, writeJSON } from '$lib/storage';
import { settings, setReminder } from '$lib/stores/settings';
import { progress } from '$lib/stores/progress';
import { writeMirror } from '$lib/reminder-db';

/** What the UI needs to draw the daily-goal banner. */
export interface DayStatus {
	day: string;
	done: number;
	goal: number;
	remaining: number;
	met: boolean;
	/** when the next nudge is due, or null when the goal is met / reminders are off */
	nextNudgeAt: Date | null;
}

const FALLBACK: DayStatus = {
	day: '',
	done: 0,
	goal: 2,
	remaining: 2,
	met: false,
	nextNudgeAt: null
};

export const today = writable<DayStatus>(FALLBACK);

/* ---------------- pure helpers ---------------- */

/** Cards marked as read today. `lastSeen` is stamped when the card is marked, so it is today's work. */
export function cardsReadToday(map: ProgressMap, day: string = todayKey()): number {
	let n = 0;
	for (const key in map) {
		const entry = map[key];
		if (!entry?.seen || !entry.lastSeen) continue;
		if (todayKey(new Date(entry.lastSeen)) === day) n++;
	}
	return n;
}

/** Slot id: minutes since midnight. Stable within a day, which is all we need. */
export function slotId(d: Date): number {
	return d.getHours() * 60 + d.getMinutes();
}

/**
 * The nudge times for one day: the reminder time, then every `repeatHours` up to and including
 * 23:00. A reminder set later than 23:00 is pulled back to 23:00 so it always has one slot.
 */
export function slotsForDay(cfg: ReminderSettings, day: Date): Date[] {
	const start = new Date(day);
	start.setHours(cfg.hour, cfg.minute, 0, 0);
	const last = new Date(day);
	last.setHours(23, 0, 0, 0);

	const out: Date[] = [];
	const step = Math.max(0, cfg.repeatHours) * 3_600_000;
	for (let t = start.getTime(); t <= last.getTime(); t += step) {
		out.push(new Date(t));
		if (!step) break;
	}
	if (!out.length) out.push(new Date(Math.min(start.getTime(), last.getTime())));
	return out;
}

function readState(day: string): ReminderState {
	const stored = readJSON<ReminderState>(KEYS.reminder, { day, fired: [] });
	return stored.day === day ? stored : { day, fired: [] };
}

/** The earliest slot that is already due and has not fired today. */
export function dueSlot(cfg: ReminderSettings, now: Date = new Date()): Date | null {
	const day = todayKey(now);
	const fired = readState(day).fired;
	for (const slot of slotsForDay(cfg, now)) {
		if (slot.getTime() <= now.getTime() && !fired.includes(slotId(slot))) return slot;
	}
	return null;
}

/** The next slot still in the future, for "next nudge at 11:00 PM". */
export function nextSlot(cfg: ReminderSettings, now: Date = new Date()): Date | null {
	for (const slot of slotsForDay(cfg, now)) {
		if (slot.getTime() > now.getTime()) return slot;
	}
	return null;
}

export function statusFor(cfg: ReminderSettings, map: ProgressMap, now: Date = new Date()): DayStatus {
	const day = todayKey(now);
	const done = cardsReadToday(map, day);
	const remaining = Math.max(0, cfg.goal - done);
	return {
		day,
		done,
		goal: cfg.goal,
		remaining,
		met: remaining === 0,
		nextNudgeAt: cfg.enabled && remaining > 0 ? nextSlot(cfg, now) : null
	};
}

function markFired(id: number): void {
	const day = todayKey();
	const state = readState(day);
	if (!state.fired.includes(id)) writeJSON(KEYS.reminder, { day, fired: [...state.fired, id] });
}

/* ---------------- notification ---------------- */

export function permissionState(): NotificationPermission | 'unsupported' {
	if (!browser || typeof Notification === 'undefined') return 'unsupported';
	return Notification.permission;
}

export function notificationsSupported(): boolean {
	return browser && typeof Notification !== 'undefined' && 'serviceWorker' in navigator;
}

export function nudgeLabel(remaining: number): string {
	return remaining === 1 ? '1 card to go today' : `${remaining} cards to go today`;
}

export function nudgeBody(remaining: number, streakCount = 0): string {
	const what = remaining === 1 ? 'One card' : `${remaining} cards`;
	return streakCount > 1
		? `${what} left. Keep your ${streakCount}-day streak going.`
		: `${what} left. Two minutes and you are done for the day.`;
}

async function showNudge(remaining: number): Promise<void> {
	const title = 'StudyFeed — ' + nudgeLabel(remaining);
	const body = nudgeBody(remaining);
	// `renotify` is a real Notification option (it makes a same-tag notification re-alert) but it
	// is missing from TypeScript's DOM types, hence the cast.
	const options = {
		body,
		tag: 'studyfeed-daily',
		renotify: true,
		icon: '/icon-192.png',
		badge: '/favicon.svg',
		data: { url: '/' }
	} as NotificationOptions;
	try {
		const reg = await navigator.serviceWorker?.getRegistration();
		if (reg) await reg.showNotification(title, options);
		else new Notification(title, options);
	} catch {
		/* the platform refused (iOS before 16.4, or a non-installed browser) - banner still shows */
	}
}

/** Sends a nudge right now. Used by the "send me a test" button in Settings. */
export async function sendTestNudge(): Promise<boolean> {
	if (permissionState() !== 'granted') return false;
	const status = get(today);
	await showNudge(Math.max(1, status.remaining));
	return true;
}

/* ---------------- scheduling ---------------- */

let timer: ReturnType<typeof setInterval> | undefined;
let started = false;

async function tick(): Promise<void> {
	const cfg = get(settings).reminder;
	const map = get(progress);
	const now = new Date();
	const status = statusFor(cfg, map, now);
	today.set(status);

	// the service worker has no access to localStorage, so leave today's answer where it can look
	await writeMirror({
		day: status.day,
		done: status.done,
		goal: cfg.goal,
		enabled: cfg.enabled,
		hour: cfg.hour,
		minute: cfg.minute,
		repeatHours: cfg.repeatHours,
		updatedAt: Date.now()
	});

	if (!cfg.enabled || status.met) return;
	if (permissionState() !== 'granted') return; // no permission yet - don't burn the slot
	const due = dueSlot(cfg, now);
	if (!due) return;
	await showNudge(status.remaining);
	markFired(slotId(due));
}

export function initReminders(): void {
	if (!browser || started) return;
	started = true;

	const run = () => void tick();
	run();
	// cheap: a minute's drift on a daily nudge is invisible, and it survives the phone sleeping
	timer = setInterval(run, 60_000);

	document.addEventListener('visibilitychange', () => {
		if (document.visibilityState === 'visible') run();
	});
	globalThis.addEventListener('focus', run);

	// marking a card read should update the banner immediately, not up to a minute later
	let debounce: ReturnType<typeof setTimeout> | undefined;
	progress.subscribe(() => {
		clearTimeout(debounce);
		debounce = setTimeout(run, 150);
	});
	settings.subscribe(() => run());
}

export function stopReminders(): void {
	if (timer) clearInterval(timer);
	timer = undefined;
	started = false;
}

/* ---------------- opting in ---------------- */

/**
 * Periodic background sync is the one way a *closed* web app can still nudge, with no server and
 * no setup: the browser wakes the service worker on its own schedule and the worker decides what
 * to post. Chrome on Android only, installed app only, and the browser is free to skip it, so it
 * is a bonus rather than a guarantee.
 */
export async function registerPeriodicSync(): Promise<boolean> {
	if (!browser || !('serviceWorker' in navigator)) return false;
	try {
		const reg = await navigator.serviceWorker.ready;
		const ps = (reg as unknown as { periodicSync?: { register: (t: string, o: { minInterval: number }) => Promise<void> } })
			.periodicSync;
		if (!ps) return false;
		// 12 hours is the browser's floor; asking for less throws
		await ps.register('studyfeed-daily', { minInterval: 12 * 60 * 60 * 1000 });
		return true;
	} catch {
		return false;
	}
}

export async function unregisterPeriodicSync(): Promise<void> {
	if (!browser || !('serviceWorker' in navigator)) return;
	try {
		const reg = await navigator.serviceWorker.ready;
		const ps = (reg as unknown as { periodicSync?: { unregister: (t: string) => Promise<void> } })
			.periodicSync;
		await ps?.unregister('studyfeed-daily');
	} catch {
		/* nothing to unregister */
	}
}

/** Asks for notification permission and turns the reminder on. */
export async function enableReminders(): Promise<NotificationPermission | 'unsupported'> {
	if (!notificationsSupported()) return 'unsupported';
	const result = await Notification.requestPermission();
	if (result === 'granted') {
		setReminder({ enabled: true });
		await registerPeriodicSync();
		await tick();
	}
	return result;
}

export async function disableReminders(): Promise<void> {
	setReminder({ enabled: false });
	await unregisterPeriodicSync();
}
