/**
 * Builds src/lib/data/index.json — a tiny summary of every subject tree.
 *
 * Home, Progress and Saved read this file instead of importing full trees, so the first
 * screen paints without downloading any syllabus content.
 *
 * Run: npm run data:index   (also runs automatically before dev and build)
 */
import { readFile, writeFile, readdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const treeDir = join(root, 'src/lib/data/tree');
const outFile = join(root, 'src/lib/data/index.json');

const files = (await readdir(treeDir)).filter((f) => f.endsWith('.json')).sort();

const subjects = [];
const totals = { subjects: 0, modules: 0, topics: 0, subtopics: 0, types: 0, cards: 0 };
const seenIds = new Set();
const problems = [];
const warnings = [];

for (const file of files) {
	const tree = JSON.parse(await readFile(join(treeDir, file), 'utf8'));
	if (!tree.code || !tree.subject || !tree.semester || !Array.isArray(tree.modules)) {
		problems.push(`${file}: missing subject fields`);
		continue;
	}

	const cardIds = [];
	const modules = [];

	for (const m of tree.modules) {
		const moduleCardIds = [];
		let topics = 0;
		let subtopics = 0;
		let types = 0;

		for (const t of m.topics ?? []) {
			topics++;
			checkNode(t, `${file} ${m.module}`);
			if (t.card) {
				moduleCardIds.push(t.id);
				cardIds.push(t.id);
				checkCard(t.card, t.id);
			}
			for (const c of t.children ?? []) {
				checkNode(c, `${file} ${m.module}`);
				if (c.kind === 'type') types++;
				else if (c.kind === 'subtopic') subtopics++;
				else problems.push(`${c.id}: bad kind "${c.kind}"`);
			}
		}

		modules.push({
			module: m.module,
			title: m.title ?? '',
			topics,
			subtopics,
			types,
			cards: moduleCardIds.length,
			cardIds: moduleCardIds
		});

		totals.modules++;
		totals.topics += topics;
		totals.subtopics += subtopics;
		totals.types += types;
		totals.cards += moduleCardIds.length;
	}

	subjects.push({
		code: tree.code,
		subject: tree.subject,
		semester: tree.semester,
		counts: {
			modules: modules.length,
			topics: modules.reduce((n, m) => n + m.topics, 0),
			subtopics: modules.reduce((n, m) => n + m.subtopics + m.types, 0),
			cards: cardIds.length
		},
		cardIds,
		modules
	});
}

function checkNode(node, where) {
	if (!node.id) problems.push(`${where}: node without id`);
	else if (seenIds.has(node.id)) problems.push(`${node.id}: duplicate id`);
	else seenIds.add(node.id);
	if (!node.title) problems.push(`${node.id}: no title`);
	if (!node.definition) problems.push(`${node.id}: no definition`);
}

function checkCard(card, id) {
	if (!card.explanation) problems.push(`${id}: card without explanation`);
	if (!card.example) problems.push(`${id}: card without example`);
	if (!card.examTip) problems.push(`${id}: card without examTip`);
	if (typeof card.verified !== 'boolean') problems.push(`${id}: verified must be boolean`);
	if (!Array.isArray(card.quiz) || card.quiz.length === 0) problems.push(`${id}: card without quiz`);

	// Every card is meant to carry four questions (five where the topic has a real count or cost).
	// This is a warning rather than an error so the subjects still being written can be filled in
	// gradually without breaking the build.
	if (Array.isArray(card.quiz) && card.quiz.length > 0 && card.quiz.length < 4) {
		warnings.push(`${id}: ${card.quiz.length} quiz questions, four or more expected`);
	}

	const stems = new Set();
	for (const [i, q] of (card.quiz ?? []).entries()) {
		if (!q.q || !q.why) problems.push(`${id} q${i}: missing question or why`);
		if (!Array.isArray(q.options) || q.options.length !== 4) problems.push(`${id} q${i}: needs 4 options`);
		if (!(q.answer >= 0 && q.answer <= 3)) problems.push(`${id} q${i}: answer index out of range`);
		if (stems.has(q.q)) problems.push(`${id} q${i}: duplicate question text`);
		stems.add(q.q);
		const options = (q.options ?? []).map((o) => String(o).toLowerCase());
		if (new Set(options).size !== options.length) problems.push(`${id} q${i}: duplicate option text`);
	}
}

subjects.sort((a, b) => a.semester - b.semester || a.code.localeCompare(b.code));
totals.subjects = subjects.length;

if (problems.length) {
	console.error(`index: ${problems.length} content problems:`);
	for (const p of problems.slice(0, 25)) console.error('  -', p);
	process.exitCode = 1;
}

if (warnings.length) {
	console.warn(`index: ${warnings.length} content warnings:`);
	for (const w of warnings.slice(0, 25)) console.warn('  -', w);
}

await writeFile(
	outFile,
	JSON.stringify({ generatedAt: new Date().toISOString(), totals, subjects }, null, 2) + '\n'
);

const kb = (JSON.stringify(subjects).length / 1024).toFixed(1);
console.log(
	`index: ${totals.subjects} subjects · ${totals.modules} modules · ${totals.topics} topics · ` +
		`${totals.subtopics + totals.types} subtopics/types · ${totals.cards} cards (${kb} KB)`
);
