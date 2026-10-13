import type { PageLoad } from './$types';
import { loadTree, cardsOfModule, indexSubject, type DeckCard } from '$lib/content';

export interface FeedModule {
	module: string;
	title: string;
	cards: number;
}

export const load: PageLoad = async ({ params }) => {
	const code = params.code;
	const module = params.module;
	const summary = indexSubject(code);
	const tree = await loadTree(code);
	const cards: DeckCard[] = cardsOfModule(tree, module);
	const otherModules: FeedModule[] = tree.modules
		.map((m) => ({ module: m.module, title: m.title, cards: cardsOfModule(tree, m.module).length }))
		.filter((m) => m.cards > 0 && m.module !== module);

	return { code, module, summary: summary ?? null, cards, otherModules };
};
