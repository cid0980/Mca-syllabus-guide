import type { PageLoad } from './$types';
import { loadTreeById, findInTree, indexSubject, type DeckCard } from '$lib/content';

/**
 * The card this chat is about, plus a safe place to go back to.
 *
 * `?card=<id>` is the whole identity of the page, so the chat has a stable, shareable URL and a
 * reload restores it. `?from=` is only honoured when it is a path on this site, so it can never be
 * used to bounce a visitor to another origin.
 */
export const load: PageLoad = async ({ url }) => {
	const id = url.searchParams.get('card') ?? '';
	if (!id) return { found: false as const, id: '' };

	try {
		const tree = await loadTreeById(id);
		const hit = findInTree(tree, id);
		const node = hit?.node;
		if (!node?.card) return { found: false as const, id };

		const summary = indexSubject(tree.code);
		const card: DeckCard = {
			id: node.id,
			subjectCode: tree.code,
			semester: tree.semester,
			module: hit!.module.module,
			topic: node.title,
			definition: node.definition,
			explanation: node.card.explanation,
			example: node.card.example,
			quiz: node.card.quiz,
			examTip: node.card.examTip,
			verified: node.card.verified
		};

		const fallback = `/feed/${encodeURIComponent(tree.code)}/${hit!.module.module}?card=${encodeURIComponent(node.id)}`;
		const requested = url.searchParams.get('from') ?? '';
		const safe = requested.startsWith('/') && !requested.startsWith('//') && !requested.startsWith('/ask');
		const position = summary?.modules.find((m) => m.module === hit!.module.module);

		return {
			found: true as const,
			card,
			from: safe ? requested : fallback,
			moduleTitle: hit!.module.title,
			cardIndex: position ? position.cardIds.indexOf(node.id) + 1 : 0,
			cardCount: position?.cardIds.length ?? 0
		};
	} catch {
		return { found: false as const, id };
	}
};

/** Not prerendered: the chat page needs IndexedDB and a network model. */
export const prerender = false;
