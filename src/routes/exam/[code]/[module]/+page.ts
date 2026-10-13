import type { PageLoad } from './$types';
import { loadTree, cardsOfModule, indexSubject, type DeckCard } from '$lib/content';

export const load: PageLoad = async ({ params }) => {
	const code = params.code;
	const module = params.module;
	const summary = indexSubject(code);
	const tree = await loadTree(code);
	const cards: DeckCard[] = cardsOfModule(tree, module);
	return { code, module, summary: summary ?? null, cards };
};
