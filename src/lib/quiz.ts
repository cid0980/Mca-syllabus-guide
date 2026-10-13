/**
 * Quiz sessions.
 *
 * Questions live on the saved cards (`card.quiz`), so a quiz is only ever as good as the cards.
 * Per-card results go into `sf:progress` (already used by the Progress screen); finished sessions
 * go into `sf:quiz` so the picker can say what last time looked like.
 */
import type { ProgressMap, QuizQuestion } from '$lib/types';

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

/* ---------------- selection ---------------- */

/**
 * Which band a card sits in, used to order a run:
 *
 *   0  answered wrongly before  — mistakes come first, they are the point of a quiz
 *   1  never opened             — new material comes next
 *   2  seen and not wrong       — revision comes last
 *
 * The signal already exists in `sf:progress`, so nothing new is stored.
 */
export function cardBand(cardId: string, progress: ProgressMap = {}): 0 | 1 | 2 {
	const p = progress[cardId];
	if (p && p.quizWrong > 0) return 0;
	if (!p || !p.seen) return 1;
	return 2;
}

export interface CardGroup {
	cardId: string;
	items: QuizItem[];
	band: 0 | 1 | 2;
	/** questions already asked for this card — used to rotate which one comes next */
	answered: number;
	lastSeen: number;
}

export function groupByCard(items: QuizItem[]): CardGroup[] {
	const map = new Map<string, CardGroup>();
	for (const item of items) {
		let group = map.get(item.cardId);
		if (!group) {
			group = { cardId: item.cardId, items: [], band: 2, answered: 0, lastSeen: 0 };
			map.set(item.cardId, group);
		}
		group.items.push(item);
	}
	return [...map.values()];
}

/**
 * Cards ordered worst-first: wrong answers, then unseen, then the rest. Inside a band the
 * card seen longest ago wins, and equal timestamps are shuffled so two runs of the same
 * size are not identical.
 */
export function rankCards(items: QuizItem[], progress: ProgressMap = {}): CardGroup[] {
	const groups = groupByCard(items).map((group) => {
		const p = progress[group.cardId];
		return {
			...group,
			band: cardBand(group.cardId, progress),
			answered: (p?.quizCorrect ?? 0) + (p?.quizWrong ?? 0),
			lastSeen: p?.lastSeen ?? 0
		};
	});

	const bands: [CardGroup[], CardGroup[], CardGroup[]] = [[], [], []];
	for (const group of groups) bands[group.band].push(group);

	const ordered: CardGroup[] = [];
	for (const band of bands) {
		const decorated = band.map((group) => ({ group, tie: Math.random() }));
		decorated.sort((a, b) => a.group.lastSeen - b.group.lastSeen || a.tie - b.tie);
		for (const d of decorated) ordered.push(d.group);
	}
	return ordered;
}

/**
 * Builds a run of `limit` questions (0 = every question in the pool).
 *
 * Questions are handed out one per card per round, walking the ranked card list, so a run of
 * 10 or 20 never asks the same card twice while there are cards left. A card only contributes
 * a second question once every card has contributed one - that is what makes an all-questions
 * module run spread a card's four questions apart instead of sitting them in a row.
 *
 * `answered` rotates the starting question per card, so a card seen twice in one day does not
 * open with the same question every time. It comes from the existing per-card counters.
 */
export function pickQuestions(items: QuizItem[], limit: number, progress: ProgressMap = {}): QuizItem[] {
	if (items.length === 0) return [];
	const total = limit > 0 ? Math.min(limit, items.length) : items.length;
	const ranked = rankCards(items, progress);
	const out: QuizItem[] = [];

	let round = 0;
	while (out.length < total && round < 64) {
		let placed = false;
		for (const group of ranked) {
			if (out.length >= total) break;
			const count = group.items.length;
			if (round >= count) continue;
			const start = group.answered % count;
			out.push(group.items[(start + round) % count]);
			placed = true;
		}
		if (!placed) break;
		round++;
	}
	return out;
}

export interface PrioritySummary {
	wrong: number;
	unseen: number;
	reviewed: number;
}

/** Card counts per band for the pool, so a run can say what it prioritised. */
export function prioritySummary(items: QuizItem[], progress: ProgressMap = {}): PrioritySummary {
	const summary: PrioritySummary = { wrong: 0, unseen: 0, reviewed: 0 };
	for (const group of groupByCard(items)) {
		const band = cardBand(group.cardId, progress);
		if (band === 0) summary.wrong++;
		else if (band === 1) summary.unseen++;
		else summary.reviewed++;
	}
	return summary;
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

export interface BestScore {
	correct: number;
	total: number;
}

/** The scope string a module deck records its finished runs under. */
export function moduleScope(code: string, module: string): string {
	return `${code} Module ${module}`;
}

/**
 * Best completed run for one module, at the question count the deck asks today.
 *
 * `sf:progress` counts answers per card cumulatively, so it cannot rebuild a single run's score.
 * `sf:quiz` already stores one record per finished run (`at`, `scope`, `correct`, `total`), which
 * is exactly a score, so nothing new is stored and the format is untouched.
 *
 * Only runs of exactly `total` questions count. That keeps two things out of the way: runs from
 * before a card set grew (an old "19/20" on a deck that now asks 47), and retry-missed runs, which
 * share the module's scope but ask only the questions that were missed.
 */
export function bestSessionFor(sessions: QuizSession[], scope: string, total: number): BestScore | null {
	let best: QuizSession | null = null;
	for (const session of sessions) {
		if (session.scope !== scope || session.total !== total) continue;
		if (!best || session.correct > best.correct) best = session;
	}
	return best ? { correct: best.correct, total: best.total } : null;
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
