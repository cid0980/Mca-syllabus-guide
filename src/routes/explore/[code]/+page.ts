import type { PageLoad } from './$types';
import { loadTree, indexSubject, cardsOfModule } from '$lib/content';

export interface ExploreTopic {
	id: string;
	title: string;
	kind: 'topic' | 'subtopic' | 'type';
	definition: string;
	hasCard: boolean;
	children: { id: string; title: string; kind: 'topic' | 'subtopic' | 'type'; definition: string }[];
}

export interface ExploreModule {
	module: string;
	title: string;
	cardIds: string[];
	topics: ExploreTopic[];
}

/**
 * The whole syllabus for one subject is rendered on the server so the page arrives
 * complete. Card bodies are dropped here - they are only needed inside the feed.
 */
export const load: PageLoad = async ({ params }) => {
	const code = params.code;
	const summary = indexSubject(code);
	if (!summary) return { found: false as const, code, modules: [] as ExploreModule[] };

	const tree = await loadTree(code);
	const modules: ExploreModule[] = tree.modules.map((m) => ({
		module: m.module,
		title: m.title,
		cardIds: cardsOfModule(tree, m.module).map((c) => c.id),
		topics: m.topics.map((t) => ({
			id: t.id,
			title: t.title,
			kind: t.kind,
			definition: t.definition,
			hasCard: !!t.card,
			children: (t.children ?? []).map((c) => ({
				id: c.id,
				title: c.title,
				kind: c.kind,
				definition: c.definition
			}))
		}))
	}));

	return { found: true as const, code, summary, modules };
};
