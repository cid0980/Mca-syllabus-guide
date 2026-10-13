/**
 * The progress backup file: shape, validation and cleaning.
 *
 * Pure functions only — no DOM, no storage, no framework imports — so the format can be unit
 * tested and can never break the app if a file is malformed. The browser side (starting the
 * download, reading the picked file, writing to localStorage) lives in BackupPanel.svelte.
 *
 * The AI keys in `sf:ai` are deliberately NOT included: a progress file gets copied around, and
 * credentials must never travel inside one.
 */

export const BACKUP_APP = 'studyfeed';
export const BACKUP_VERSION = 1;

export interface BackupProgressEntry {
	seen: boolean;
	lastSeen: number;
	quizCorrect: number;
	quizWrong: number;
}

export type BackupProgress = Record<string, BackupProgressEntry>;

export interface BackupQuizRun {
	at: number;
	scope: string;
	correct: number;
	total: number;
}

export interface BackupSettings {
	theme: 'dark' | 'light' | 'system';
}

export interface BackupStreak {
	count: number;
	lastDay: string;
}

/** What actually goes into the JSON file. */
export interface BackupFile {
	app: typeof BACKUP_APP;
	version: number;
	exportedAt: string;
	progress: BackupProgress;
	bookmarks: string[];
	streak: BackupStreak;
	settings: BackupSettings;
	quizzes: BackupQuizRun[];
}

export interface BackupCounts {
	cards: number;
	bookmarks: number;
	quizRuns: number;
}

export type SanitiseResult =
	| { ok: true; progress: BackupProgress; bookmarks: string[]; streak: BackupStreak; settings: BackupSettings; quizzes: BackupQuizRun[] }
	| { ok: false; error: string };

const MAX_BOOKMARKS = 5000;
const MAX_QUIZ_RUNS = 20;
const THEMES: BackupSettings['theme'][] = ['dark', 'light', 'system'];
const DAY_RE = /^\d{4}-\d{2}-\d{2}$/;

function isRecord(value: unknown): value is Record<string, unknown> {
	return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function wholeNumber(value: unknown, fallback = 0): number {
	const n = Number(value);
	return Number.isFinite(n) && n > 0 ? Math.floor(n) : fallback;
}

export function cleanProgress(raw: unknown): BackupProgress {
	const out: BackupProgress = {};
	if (!isRecord(raw)) return out;
	for (const [id, value] of Object.entries(raw)) {
		if (typeof id !== 'string' || id.length === 0 || id.length > 120) continue;
		if (!isRecord(value)) continue;
		const seen = value.seen === true;
		const quizCorrect = wholeNumber(value.quizCorrect);
		const quizWrong = wholeNumber(value.quizWrong);
		// a card with no flags and no answers carries no information
		if (!seen && quizCorrect === 0 && quizWrong === 0) continue;
		out[id] = {
			seen,
			lastSeen: wholeNumber(value.lastSeen),
			quizCorrect,
			quizWrong
		};
	}
	return out;
}

export function cleanBookmarks(raw: unknown): string[] {
	if (!Array.isArray(raw)) return [];
	const seen = new Set<string>();
	const out: string[] = [];
	for (const value of raw) {
		if (typeof value !== 'string' || value.length === 0 || value.length > 120) continue;
		if (seen.has(value)) continue;
		seen.add(value);
		out.push(value);
		if (out.length >= MAX_BOOKMARKS) break;
	}
	return out;
}

export function cleanStreak(raw: unknown): BackupStreak {
	if (!isRecord(raw)) return { count: 0, lastDay: '' };
	const lastDay = typeof raw.lastDay === 'string' && DAY_RE.test(raw.lastDay) ? raw.lastDay : '';
	return { count: wholeNumber(raw.count), lastDay };
}

export function cleanSettings(raw: unknown): BackupSettings {
	if (!isRecord(raw)) return { theme: 'system' };
	const theme = THEMES.includes(raw.theme as BackupSettings['theme'])
		? (raw.theme as BackupSettings['theme'])
		: 'system';
	return { theme };
}

export function cleanQuizzes(raw: unknown): BackupQuizRun[] {
	if (!Array.isArray(raw)) return [];
	const out: BackupQuizRun[] = [];
	for (const value of raw) {
		if (!isRecord(value)) continue;
		const total = wholeNumber(value.total);
		if (total === 0) continue;
		out.push({
			at: wholeNumber(value.at),
			scope: typeof value.scope === 'string' ? value.scope.slice(0, 60) : 'quiz',
			correct: Math.min(wholeNumber(value.correct), total),
			total
		});
		if (out.length >= MAX_QUIZ_RUNS) break;
	}
	return out;
}

/** Everything a screen has to hand over to write a file. */
export function buildBackup(input: {
	progress: unknown;
	bookmarks: unknown;
	streak: unknown;
	settings: unknown;
	quizzes: unknown;
	now?: Date;
}): BackupFile {
	return {
		app: BACKUP_APP,
		version: BACKUP_VERSION,
		exportedAt: (input.now ?? new Date()).toISOString(),
		progress: cleanProgress(input.progress),
		bookmarks: cleanBookmarks(input.bookmarks),
		streak: cleanStreak(input.streak),
		settings: cleanSettings(input.settings),
		quizzes: cleanQuizzes(input.quizzes)
	};
}

/**
 * Reads a parsed JSON file. Anything unexpected is either dropped field by field or refused with a
 * sentence the user can act on — this never throws, whatever the file contains.
 */
export function sanitiseBackup(raw: unknown): SanitiseResult {
	if (!isRecord(raw)) {
		return { ok: false, error: 'That file is not a StudyFeed backup (it is not a JSON object).' };
	}
	const looksLikeBackup =
		raw.app === BACKUP_APP ||
		'progress' in raw ||
		'bookmarks' in raw ||
		'quizzes' in raw;
	if (!looksLikeBackup) {
		return { ok: false, error: 'That JSON file has none of the StudyFeed progress fields in it.' };
	}
	if (typeof raw.version === 'number' && raw.version > BACKUP_VERSION) {
		return { ok: false, error: `That backup was written by a newer version (v${raw.version}). Update the app first.` };
	}

	const progress = cleanProgress(raw.progress);
	const bookmarks = cleanBookmarks(raw.bookmarks);
	const quizzes = cleanQuizzes(raw.quizzes);
	if (Object.keys(progress).length === 0 && bookmarks.length === 0 && quizzes.length === 0) {
		return { ok: false, error: 'That backup is empty: no cards, saved items or quiz runs in it.' };
	}

	return {
		ok: true,
		progress,
		bookmarks,
		streak: cleanStreak(raw.streak),
		settings: cleanSettings(raw.settings),
		quizzes
	};
}

export function countsOf(parts: {
	progress?: BackupProgress;
	bookmarks?: string[];
	quizzes?: BackupQuizRun[];
}): BackupCounts {
	return {
		cards: Object.keys(parts.progress ?? {}).length,
		bookmarks: (parts.bookmarks ?? []).length,
		quizRuns: (parts.quizzes ?? []).length
	};
}

/** e.g. studyfeed-progress-2026-10-13.json */
export function backupFileName(now: Date = new Date()): string {
	const day = now.toISOString().slice(0, 10);
	return `studyfeed-progress-${day}.json`;
}
