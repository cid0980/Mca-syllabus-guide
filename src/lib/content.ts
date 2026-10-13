/**
 * Content access. Two layers, per skills/DATA.md:
 *
 *  1. index.json  — tiny, eager. Counts, card ids, module lists. Home/Saved/Progress use this only.
 *  2. tree/<CODE>.json — lazy dynamic import, cached per subject. Explore/Topic/Feed use this.
 *
 * Ids encode their subject ("CSCA411-M2-06"), so a deep link can resolve its tree without help.
 */
import indexRaw from '$lib/data/index.json';
import type { QuizQuestion } from '$lib/types';

export type NodeKind = 'topic' | 'subtopic' | 'type';

export interface CardContent {
	explanation: string;
	example: string;
	quiz: QuizQuestion[];
	examTip: string;
	verified: boolean;
}

export interface TopicNode {
	id: string;
	title: string;
	kind: NodeKind;
	definition: string;
	children?: TopicNode[];
	card?: CardContent;
}

export interface ModuleNode {
	module: string;
	title: string;
	topics: TopicNode[];
}

export interface SubjectTree {
	code: string;
	subject: string;
	semester: number;
	modules: ModuleNode[];
}

/* ---------------- index ---------------- */

export interface IndexModule {
	module: string;
	title: string;
	topics: number;
	subtopics: number;
	types: number;
	cards: number;
	cardIds: string[];
}

export interface IndexSubject {
	code: string;
	subject: string;
	semester: number;
	counts: { modules: number; topics: number; subtopics: number; cards: number };
	cardIds: string[];
	modules: IndexModule[];
}

export interface SubjectIndex {
	generatedAt: string;
	totals: { subjects: number; modules: number; topics: number; subtopics: number; types: number; cards: number };
	subjects: IndexSubject[];
}

export const index = indexRaw as SubjectIndex;
export const subjects = index.subjects;
export const totals = index.totals;

export function indexSubject(code: string): IndexSubject | undefined {
	return subjects.find((s) => s.code === code);
}

export function subjectsOfSemester(semester: number): IndexSubject[] {
	return subjects.filter((s) => s.semester === semester);
}

export function semesterLabel(n: number): string {
	return n === 1 ? '1st Semester' : n === 2 ? '2nd Semester' : n === 3 ? '3rd Semester' : `${n}th Semester`;
}

/* ---------------- module chain ---------------- */

export interface ModuleRef {
	code: string;
	subject: string;
	module: string;
	title: string;
	cards: number;
}

/** One module as a reference: enough to label a link and build its feed address. */
export function moduleRef(code: string, module: string): ModuleRef | null {
	const subject = indexSubject(code);
	const m = subject?.modules.find((x) => x.module === module);
	if (!subject || !m) return null;
	return {
		code: subject.code,
		subject: subject.subject,
		module: m.module,
		title: m.title,
		cards: m.cards
	};
}

/**
 * Every module that has cards, as one list in study order: subjects in semester order (1st, 2nd,
 * 3rd), modules in their own order inside each subject. Modules with no cards are left out, so the
 * previous and next buttons in a deck always land on something readable.
 */
export function moduleChain(): ModuleRef[] {
	const chain: ModuleRef[] = [];
	const semesters = [...new Set(subjects.map((s) => s.semester))].sort((a, b) => a - b);
	for (const semester of semesters) {
		for (const subject of subjectsOfSemester(semester)) {
			for (const m of subject.modules) {
				if (m.cards > 0) {
					chain.push({
						code: subject.code,
						subject: subject.subject,
						module: m.module,
						title: m.title,
						cards: m.cards
					});
				}
			}
		}
	}
	return chain;
}

/** The written module before this one and after it, for the end of a deck. */
export function moduleNeighbours(code: string, module: string): { prev: ModuleRef | null; next: ModuleRef | null } {
	const chain = moduleChain();
	const i = chain.findIndex((m) => m.code === code && m.module === module);
	if (i < 0) return { prev: null, next: null };
	return { prev: chain[i - 1] ?? null, next: chain[i + 1] ?? null };
}

/* ---------------- id helpers ---------------- */

/** ids look like CSCA411-M1-01 / CSCA411-M1-01-s2 — module numbers are arabic in ids. */
const ID_RE = /^([A-Z]{4})(\d{3})-M(\d+)/;

const ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'];

/** "CSCA 411" from "CSCA411-M1-01". */
export function codeFromId(id: string): string | null {
	const m = ID_RE.exec(id);
	return m ? `${m[1]} ${m[2]}` : null;
}

/** Module label as used by the feed routes ("I", "II") from "CSCA411-M1-01". */
export function moduleFromId(id: string): string | null {
	const m = ID_RE.exec(id);
	if (!m) return null;
	const n = Number(m[3]);
	return ROMAN[n - 1] ?? m[3];
}

/** "CSCA 411" -> "CSCA411" (icon / file naming) */
export function codeDigits(code: string): string {
	return code.replace(/[^0-9]/g, '');
}

/* ---------------- tree loading ---------------- */

const treeLoaders = import.meta.glob<{ default: SubjectTree }>('$lib/data/tree/*.json');

const cache = new Map<string, SubjectTree>();
const inflight = new Map<string, Promise<SubjectTree>>();

function fileFor(code: string): string | undefined {
	const key = `/src/lib/data/tree/${code.replace(/\s+/g, '')}.json`;
	if (treeLoaders[key]) return key;
	// tolerate a different glob key shape
	return Object.keys(treeLoaders).find((k) => k.endsWith(`${code.replace(/\s+/g, '')}.json`));
}

export function treeIfLoaded(code: string): SubjectTree | undefined {
	return cache.get(code);
}

export function loadTree(code: string): Promise<SubjectTree> {
	const cached = cache.get(code);
	if (cached) return Promise.resolve(cached);
	const pending = inflight.get(code);
	if (pending) return pending;

	const key = fileFor(code);
	if (!key) return Promise.reject(new Error(`No syllabus file for ${code}`));

	const p = treeLoaders[key]()
		.then((mod) => {
			const tree = mod.default;
			cache.set(code, tree);
			inflight.delete(code);
			return tree;
		})
		.catch((err) => {
			inflight.delete(code);
			throw new Error(`Could not load the syllabus for ${code}. ${(err as Error).message ?? ''}`.trim());
		});

	inflight.set(code, p);
	return p;
}

export function loadTreeById(id: string): Promise<SubjectTree> {
	const code = codeFromId(id);
	if (!code) return Promise.reject(new Error(`Unrecognised id: ${id}`));
	return loadTree(code);
}

let allTrees: Promise<SubjectTree[]> | null = null;

/** Loads every tree once — needed for search. Cached afterwards. */
export function loadAllTrees(): Promise<SubjectTree[]> {
	if (!allTrees) {
		allTrees = Promise.all(subjects.map((s) => loadTree(s.code)));
	}
	return allTrees;
}

/* ---------------- node lookups within a tree ---------------- */

export interface NodeHit {
	node: TopicNode;
	parent: TopicNode | null;
	module: ModuleNode;
	tree: SubjectTree;
}

export function findInTree(tree: SubjectTree, id: string): NodeHit | undefined {
	for (const module of tree.modules) {
		for (const topic of module.topics) {
			if (topic.id === id) return { node: topic, parent: null, module, tree };
			for (const child of topic.children ?? []) {
				if (child.id === id) return { node: child, parent: topic, module, tree };
			}
		}
	}
	return undefined;
}

export function nodesInOrder(tree: SubjectTree): NodeHit[] {
	const out: NodeHit[] = [];
	for (const module of tree.modules) {
		for (const topic of module.topics) {
			out.push({ node: topic, parent: null, module, tree });
			for (const child of topic.children ?? []) out.push({ node: child, parent: topic, module, tree });
		}
	}
	return out;
}

export function modulesOf(tree: SubjectTree): ModuleNode[] {
	return tree.modules;
}

/* ---------------- cards ---------------- */

export interface DeckCard {
	id: string;
	subjectCode: string;
	semester: number;
	module: string;
	topic: string;
	definition: string;
	explanation: string;
	example: string;
	quiz: QuizQuestion[];
	examTip: string;
	verified: boolean;
}

export function cardsOfTree(tree: SubjectTree): DeckCard[] {
	const out: DeckCard[] = [];
	for (const m of tree.modules) {
		for (const t of m.topics) {
			if (!t.card) continue;
			out.push({
				id: t.id,
				subjectCode: tree.code,
				semester: tree.semester,
				module: m.module,
				topic: t.title,
				definition: t.definition,
				explanation: t.card.explanation,
				example: t.card.example,
				quiz: t.card.quiz,
				examTip: t.card.examTip,
				verified: t.card.verified
			});
		}
	}
	return out;
}

export function cardsOfModule(tree: SubjectTree, module: string): DeckCard[] {
	return cardsOfTree(tree).filter((c) => c.module === module);
}

export async function cardsForSubject(code: string): Promise<DeckCard[]> {
	const tree = await loadTree(code);
	return cardsOfTree(tree);
}

/* ---------------- search ---------------- */

export interface SearchHit extends NodeHit {
	score: number;
}

const haystack = new WeakMap<TopicNode, string>();

export async function searchNodes(query: string, limit = 40): Promise<SearchHit[]> {
	const q = query.trim().toLowerCase();
	if (q.length < 2) return [];
	const words = q.split(/\s+/);
	const trees = await loadAllTrees();
	const hits: SearchHit[] = [];

	for (const tree of trees) {
		for (const module of tree.modules) {
			for (const topic of module.topics) {
				const candidates: { node: TopicNode; parent: TopicNode | null }[] = [
					{ node: topic, parent: null },
					...(topic.children ?? []).map((c) => ({ node: c, parent: topic }))
				];
				for (const { node, parent } of candidates) {
					let hay = haystack.get(node);
					if (!hay) {
						hay = `${node.title} ${node.definition} ${parent?.title ?? ''} ${tree.subject} ${
							tree.code
						}`.toLowerCase();
						haystack.set(node, hay);
					}
					let score = 0;
					for (const w of words) {
						if (!hay.includes(w)) {
							score = 0;
							break;
						}
						score += node.title.toLowerCase().includes(w) ? 4 : 1;
					}
					if (score > 0) hits.push({ node, parent, module, tree, score });
				}
			}
		}
	}

	return hits.sort((a, b) => b.score - a.score || a.node.title.localeCompare(b.node.title)).slice(0, limit);
}

/* ---------------- progress maths (pure) ---------------- */

export function percent(part: number, whole: number): number {
	if (whole <= 0) return 0;
	return Math.min(100, Math.round((part / whole) * 100));
}

export function plural(n: number, one: string, many = `${one}s`): string {
	return `${n} ${n === 1 ? one : many}`;
}
