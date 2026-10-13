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
}
