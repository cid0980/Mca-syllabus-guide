import type { PageLoad } from './$types';
import { subjects, loadTree, cardsOfTree } from '$lib/content';

export interface QuizDeck {
	code: string;
	subject: string;
	module: string;
	moduleTitle: string;
	questions: number;
	cards: number;
}

/** Only the subjects that actually have written cards contribute quiz decks. */
export const load: PageLoad = async () => {
	const decks: QuizDeck[] = [];

	for (const subject of subjects.filter((s) => s.counts.cards > 0)) {
		const tree = await loadTree(subject.code);
		for (const module of tree.modules) {
			const cards = cardsOfTree(tree).filter((c) => c.module === module.module);
			const questions = cards.reduce((n, c) => n + c.quiz.length, 0);
			if (questions === 0) continue;
			decks.push({
				code: tree.code,
				subject: tree.subject,
				module: module.module,
				moduleTitle: module.title,
				questions,
				cards: cards.length
			});
		}
	}

	return {
		decks,
		totalQuestions: decks.reduce((n, d) => n + d.questions, 0),
		cardCount: subjects.reduce((n, s) => n + s.counts.cards, 0)
	};
};
