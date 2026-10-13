/**
 * Quiz sessions.
 *
 * Questions live on the saved cards (`card.quiz`), so a quiz is only ever as good as the cards.
 * Per-card results go into `sf:progress` (already used by the Progress screen); finished sessions
 * go into `sf:quiz` so the picker can say what last time looked like.
 */
import type { QuizQuestion } from '$lib/types';

export interface QuizItem {
	cardId: string;
	subjectCode: string;
	subject: string;
	module: string;
	topic: string;
	question: QuizQuestion;
}

export interface QuizSession {
	at: number;
	scope: string;
	correct: number;
	total: number;
}

const KEY = 'sf:quiz';
const MAX_SESSIONS = 20;

export function buildItems(
	cards: {
		id: string;
		subjectCode: string;
		module: string;
		topic: string;
		quiz: QuizQuestion[];
	}[],
	subjectLabel: (code: string) => string = (code) => code
): QuizItem[] {
	const items: QuizItem[] = [];
	for (const card of cards) {
		for (const question of card.quiz) {
			items.push({
				cardId: card.id,
				subjectCode: card.subjectCode,
				subject: subjectLabel(card.subjectCode),
				module: card.module,
				topic: card.topic,
				question
			});
		}
	}
	return items;
}

export function shuffle<T>(list: T[]): T[] {
	const out = [...list];
	for (let i = out.length - 1; i > 0; i--) {
		const j = Math.floor(Math.random() * (i + 1));
		[out[i], out[j]] = [out[j], out[i]];
	}
	return out;
}

export function readSessions(): QuizSession[] {
	if (typeof localStorage === 'undefined') return [];
	try {
		const raw = localStorage.getItem(KEY);
		const parsed = raw ? (JSON.parse(raw) as QuizSession[]) : [];
		return Array.isArray(parsed) ? parsed : [];
	} catch {
		return [];
	}
}

export function recordSession(session: QuizSession): void {
	if (typeof localStorage === 'undefined') return;
	try {
		const next = [session, ...readSessions()].slice(0, MAX_SESSIONS);
		localStorage.setItem(KEY, JSON.stringify(next));
	} catch {
		/* storage full or private mode - the per-card result is still saved */
	}
}

export function lastSession(): QuizSession | null {
	return readSessions()[0] ?? null;
}

export function scoreMessage(correct: number, total: number): string {
	if (total === 0) return '';
	const pct = correct / total;
	if (pct === 1) return 'Full marks. That topic is ready for the exam.';
	if (pct >= 0.8) return 'Strong. Re-read the ones you missed and you are done with this set.';
	if (pct >= 0.5) return 'Halfway. Retry the missed questions, then run the deck again.';
	if (pct > 0) return 'Worth another pass: read the card explanations, then retry.';
	return 'No right answers this time. Read the cards first, then come back.';
}
