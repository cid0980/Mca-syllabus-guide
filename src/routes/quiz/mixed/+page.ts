import type { PageLoad } from './$types';
import { subjects, loadTree, cardsOfTree } from '$lib/content';
import { buildItems, type QuizItem } from '$lib/quiz';

/**
 * Mixed quiz: every written question across all subjects, so the runner can sample from it
 * or filter it down to the questions that were answered wrongly before (?mode=wrong).
 */
export const load: PageLoad = async () => {
	const items: QuizItem[] = [];
	for (const subject of subjects.filter((s) => s.counts.cards > 0)) {
		const tree = await loadTree(subject.code);
		items.push(...buildItems(cardsOfTree(tree), (c) => subjects.find((s) => s.code === c)?.subject ?? c));
	}
	return { items };
};
