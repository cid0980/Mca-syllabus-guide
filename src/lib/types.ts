/** Shared types. Content shapes live in $lib/content.ts; this file is storage + settings. */

export interface QuizQuestion {
	/** The question text. */
	q: string;
	/** Exactly four options. */
	options: string[];
	/** Index (0-3) of the correct option. */
	answer: number;
	/** One line explaining why that answer is correct. */
	why: string;
}

/** Per-node learning record. Stored in localStorage under `sf:progress`. */
export interface CardProgress {
	seen: boolean;
	lastSeen: number;
	quizCorrect: number;
	quizWrong: number;
}

export type ProgressMap = Record<string, CardProgress>;

/** Stored under `sf:streak`. `lastDay` is a local YYYY-MM-DD string. */
export interface StreakState {
	count: number;
	lastDay: string;
}

/** Stored under `sf:settings`. */
export interface Settings {
	theme: 'dark' | 'light' | 'system';
	reminder: ReminderSettings;
}

/**
 * The daily study reminder.
 *
 * `hour`/`minute` is the local time of the first nudge of the day. After it fires the reminder
 * repeats every `repeatHours` hours until the goal is met or the day runs out (the last slot is
 * 23:00), so `repeatHours: 0` means exactly one nudge.
 */
export interface ReminderSettings {
	enabled: boolean;
	hour: number;
	minute: number;
	/** Cards to mark as read before the day counts as done. */
	goal: number;
	repeatHours: number;
}

/**
 * Stored under `sf:reminder`. Which slots have already fired today, so a reload (or the service
 * worker waking up) does not send the same nudge twice.
 */
export interface ReminderState {
	day: string;
	fired: number[];
}
