import type { PageLoad } from './$types';
import { loadTree, cardsOfModule, indexSubject } from '$lib/content';
import { buildItems } from '$lib/quiz';

export const load: PageLoad = async ({ params }) => {
	const code = params.code;
	const module = params.module;
	const tree = await loadTree(code);
	const summary = indexSubject(code);
	const cards = cardsOfModule(tree, module);

	return {
		code,
		module,
		subject: tree.subject,
		moduleTitle: tree.modules.find((m) => m.module === module)?.title ?? `Module ${module}`,
		cardCount: summary?.counts.cards ?? 0,
		items: buildItems(cards)
	};
};
