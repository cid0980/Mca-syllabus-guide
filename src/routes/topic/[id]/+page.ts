import type { PageLoad } from './$types';
import { loadTreeById, findInTree, nodesInOrder, type TopicNode, type CardContent } from '$lib/content';

export interface TopicData {
	found: true;
	code: string;
	subject: string;
	semester: number;
	module: { module: string; title: string };
	node: TopicNode & { card?: CardContent };
	parent: { id: string; title: string } | null;
	prev: { id: string; title: string } | null;
	next: { id: string; title: string } | null;
}

export const load: PageLoad = async ({ params }) => {
	const id = params.id;
	const tree = await loadTreeById(id);
	const hit = findInTree(tree, id);
	if (!hit) return { found: false as const, id };

	const order = nodesInOrder(tree);
	const pos = order.findIndex((h) => h.node.id === id);

	const payload: TopicData = {
		found: true,
		code: tree.code,
		subject: tree.subject,
		semester: tree.semester,
		module: { module: hit.module.module, title: hit.module.title },
		node: hit.node,
		parent: hit.parent ? { id: hit.parent.id, title: hit.parent.title } : null,
		prev: pos > 0 ? { id: order[pos - 1].node.id, title: order[pos - 1].node.title } : null,
		next:
			pos >= 0 && pos < order.length - 1
				? { id: order[pos + 1].node.id, title: order[pos + 1].node.title }
				: null
	};
	return payload;
};
