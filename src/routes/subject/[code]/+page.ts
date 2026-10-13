import type { PageLoad } from './$types';
import { loadTree, indexSubject, cardsOfModule } from '$lib/content';

export const load: PageLoad = async ({ params }) => {
	const code = params.code;
	const summary = indexSubject(code);
	if (!summary) return { found: false as const, code, rows: [] };

	const tree = await loadTree(code);
	const rows = tree.modules.map((m) => ({
		module: m.module,
		title: m.title,
		topics: m.topics.length,
		subtopics: m.topics.reduce((n, t) => n + (t.children?.length ?? 0), 0),
		cardIds: cardsOfModule(tree, m.module).map((c) => c.id)
	}));

	return { found: true as const, code, summary, rows };
};
