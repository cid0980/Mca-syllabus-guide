<script lang="ts">
	/**
	 * The quiz runner: one question per screen, immediate feedback with the reason, a score at the
	 * end, and a review of exactly what was missed. Question-to-question movement is a real
	 * transition (skills/MOTION.md) instead of an instant swap.
	 */
	import { createEventDispatcher, onMount } from 'svelte';
	import {
		CircleCheck,
		CircleX,
		ChevronRight,
		RotateCcw,
		ListChecks,
		BookOpen,
		Trophy,
		Target
	} from 'lucide-svelte';
	import { recordQuiz } from '$lib/stores/progress';
	import {
		recordSession,
		scoreMessage,
		shuffle,
		pickQuestions,
		prioritySummary,
		type PrioritySummary,
		type QuizItem
	} from '$lib/quiz';
	import type { ProgressMap } from '$lib/types';
	import ProgressRing from '$lib/components/ProgressRing.svelte';

	const dispatch = createEventDispatcher<{ exit: void }>();

	export let items: QuizItem[] = [];
	/** how many questions this run should ask (0 = all of them) */
	export let limit = 0;
	export let scope = 'quiz';
	/** saved progress, read once to order the run; nothing is written to it from here */
	export let progressMap: ProgressMap = {};
	/** ask the cards you got wrong and the cards you never opened first, one question per card */
	export let prioritise = false;
	export let emptyTitle = 'No questions here yet';
	export let emptyText =
		'This set has no quiz questions because the cards for it have not been written. The topics and their definitions are still readable in the syllabus.';

	type Answer = { item: QuizItem; chosen: number; correct: boolean };

	let queue: QuizItem[] = [];
	let index = 0;
	let picked: number | null = null;
	let answers: Answer[] = [];
	let phase: 'ask' | 'done' = 'ask';
	let startedWith: QuizItem[] | null = null;
	/** snapshot for the order note; taken once so answering cannot rewrite it mid-run */
	const summary: PrioritySummary | null = prioritise ? prioritySummary(items, progressMap) : null;

	$: total = queue.length;
	$: correctCount = answers.filter((a) => a.correct).length;
	$: wrong = answers.filter((a) => !a.correct);
	$: progress = total ? ((index + (picked !== null ? 1 : 0)) / total) * 100 : 0;

	function buildQueue(questions: QuizItem[], n: number): QuizItem[] {
		return n > 0 && n < questions.length ? questions.slice(0, n) : [...questions];
	}

	/**
	 * Priority run. `pickQuestions` does the ordering and the card de-duplication, so this is the
	 * finished queue. It only ever runs in the browser: both quiz screens wait for hydration
	 * before they mount this component, so the server never renders a random order.
	 */
	function startPicked(questions: QuizItem[], n: number) {
		queue = pickQuestions(questions, n, progressMap);
		index = 0;
		picked = null;
		answers = [];
		phase = 'ask';
		if (questions.length) startedWith = questions;
	}

	function begin(questions: QuizItem[]) {
		if (prioritise) startPicked(questions, limit);
		else start(questions, limit, false);
	}

	function rerun() {
		if (prioritise) startPicked(items, limit);
		else start(items);
	}

	function start(questions: QuizItem[], n = limit, randomise = true) {
		const pool = randomise ? shuffle(questions) : [...questions];
		queue = buildQueue(pool, n);
		index = 0;
		picked = null;
		answers = [];
		phase = 'ask';
		if (questions.length) startedWith = questions;
	}

	/**
	 * Init is deliberately NOT random: this code runs on the server too, and a different shuffle
	 * there would break hydration. The first question is stable; the rest are shuffled once the
	 * page is live, so a second run still feels fresh.
	 */
	if (items.length) begin(items);
	$: if (items !== startedWith) begin(items);

	function choose(oi: number) {
		const current = queue[index];
		if (picked !== null || !current) return;
		picked = oi;
		const correct = oi === current.question.answer;
		answers = [...answers, { item: current, chosen: oi, correct }];
		recordQuiz(current.cardId, correct);
	}

	function next() {
		if (picked === null) return;
		if (index + 1 >= total) {
			phase = 'done';
			recordSession({
				at: Date.now(),
				scope,
				correct: answers.filter((a) => a.correct).length,
				total
			});
			return;
		}
		index += 1;
		picked = null;
	}

	function retryWrong() {
		start(wrong.map((a) => a.item), 0, false);
		phase = 'ask';
	}

	function onKey(e: KeyboardEvent) {
		if (e.target instanceof HTMLElement && e.target.closest('input, textarea')) return;
		if (phase === 'done') return;
		const key = e.key.toLowerCase();
		const map: Record<string, number> = { '1': 0, '2': 1, '3': 2, '4': 3, a: 0, b: 1, c: 2, d: 3 };
		if (key in map && picked === null) {
			e.preventDefault();
			choose(map[key]);
		} else if ((e.key === 'Enter' || e.key === ' ') && picked !== null) {
			e.preventDefault();
			next();
		}
	}

	onMount(() => {
		globalThis.addEventListener('keydown', onKey);
		// a priority queue is already randomised by the engine; plain decks are shuffled here,
		// keeping the question already on screen where it is
		if (!prioritise) {
			const ahead = queue.slice(index + 1);
			if (ahead.length > 1) queue = [...queue.slice(0, index + 1), ...shuffle(ahead)];
		}
		return () => globalThis.removeEventListener('keydown', onKey);
	});
</script>

<div class="runner">
	<div class="bar" aria-hidden="true"><div class="fill" style={`width:${phase === 'done' ? 100 : progress}%`}></div></div>

	{#if phase === 'ask' && queue[index]}
		{@const item = queue[index]}
		<header class="head">
			<div class="grow">
				<p class="crumb nums">
					{index + 1} of {total} · {item.subjectCode} · Module {item.module}
				</p>
				<p class="topic truncate">{item.topic}</p>
			</div>
			<span class="score nums" class:good={correctCount > answers.length / 2}>{correctCount} right</span>
			<button class="exit" on:click={() => dispatch('exit')}>Exit</button>
		</header>
	{/if}

	{#if phase === 'ask' && queue[index]}
		{@const item = queue[index]}
		<div class="body">
			{#if prioritise && index === 0 && summary && summary.wrong + summary.unseen > 0}
				<p class="priority">
					<Target size={14} />
					<span>
						Picked for you:
						{#if summary.wrong}<strong>{summary.wrong} {summary.wrong === 1 ? 'card' : 'cards'}</strong> you answered wrongly{#if summary.unseen}, {/if}{/if}
						{#if summary.unseen}<strong>{summary.unseen}</strong> not opened yet{/if}
					</span>
				</p>
			{/if}
			{#key index}
				<section class="question expand-in">
					<h2 class="q-text">{item.question.q}</h2>
					<div class="options">
						{#each item.question.options as option, oi}
							{@const done = picked !== null}
							<button
								class="option"
								class:correct={done && oi === item.question.answer}
								class:wrong={done && oi === picked && oi !== item.question.answer}
								class:dim={done && oi !== item.question.answer && oi !== picked}
								disabled={done}
								on:click={() => choose(oi)}
								aria-label={`Option ${'ABCD'[oi]}: ${option}`}
							>
								<span class="letter">{'ABCD'[oi]}</span>
								<span class="grow">{option}</span>
								{#if done && oi === item.question.answer}<span class="mark ok"><CircleCheck size={17} /></span>{/if}
								{#if done && oi === picked && oi !== item.question.answer}<span class="mark no"><CircleX size={17} /></span>{/if}
							</button>
						{/each}
					</div>

					{#if picked !== null}
						<div class="why expand-in">
							<p class="verdict" class:on={picked === item.question.answer}>
								{#if picked === item.question.answer}
									<CircleCheck size={15} /> Correct
								{:else}
									<CircleX size={15} /> The answer is {item.question.options[item.question.answer]}
								{/if}
							</p>
							<p class="why-text">{item.question.why}</p>
						</div>
					{/if}
				</section>
			{/key}
		</div>

		<footer class="foot">
			{#if picked === null}
				<p class="hint">Pick an option — keys 1-4 or A-D work too.</p>
			{:else}
				<button class="btn btn--primary btn--block" on:click={next}>
					{index + 1 >= total ? 'See results' : 'Next question'} <ChevronRight size={16} />
				</button>
			{/if}
		</footer>
	{:else if phase === 'done'}
		<div class="body done">
			<section class="result expand-in">
				<ProgressRing percent={total ? Math.round((correctCount / total) * 100) : 0} size={92} stroke={6} label={`${correctCount}/${total}`} labelSize={20} />
				<h2 class="result-title">
					{correctCount === total ? 'Perfect run' : correctCount >= total / 2 ? 'Good progress' : 'Keep going'}
				</h2>
				<p class="result-text">{scoreMessage(correctCount, total)}</p>
			</section>

			{#if wrong.length}
				<section class="review">
					<h3 class="review-title">Review · {wrong.length} missed</h3>
					{#each wrong as w}
						<article class="review-item">
							<p class="review-q">{w.item.question.q}</p>
							<p class="review-line bad">
								<CircleX size={14} /> You picked {w.item.question.options[w.chosen]}
							</p>
							<p class="review-line good">
								<CircleCheck size={14} /> {w.item.question.options[w.item.question.answer]}
							</p>
							<p class="review-why">{w.item.question.why}</p>
						</article>
					{/each}
				</section>
			{/if}

			<div class="result-actions">
				{#if wrong.length}
					<button class="btn btn--primary btn--block" on:click={retryWrong}>
						<RotateCcw size={16} /> Retry the {wrong.length} missed
					</button>
				{/if}
				<button class="btn btn--secondary btn--block" on:click={rerun}>
					<ListChecks size={16} /> Run it again
				</button>
				<button class="btn btn--secondary btn--block" on:click={() => dispatch('exit')}>
					<BookOpen size={16} /> Back to the quiz menu
				</button>
			</div>
		</div>
	{:else}
		<div class="body empty">
			<Trophy size={20} />
			<h2 class="result-title">{emptyTitle}</h2>
			<p class="result-text">{emptyText}</p>
			<button class="btn btn--primary" on:click={() => dispatch('exit')}>Back</button>
		</div>
	{/if}
</div>

<style>
	.runner {
		display: flex;
		flex-direction: column;
		flex: 1;
		min-height: 0;
		position: relative;
		background: var(--bg);
	}

	.bar {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		height: 3px;
		background: var(--fill);
		z-index: 5;
	}

	.fill {
		height: 100%;
		background: var(--accent);
		transition: width var(--dur-enter) var(--ease-standard);
	}

	.head {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		padding: var(--sp-3) var(--sp-3) var(--sp-2) var(--sp-4);
		border-bottom: 1px solid var(--border);
		margin-top: 3px;
	}

	.crumb {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		letter-spacing: 0.02em;
	}

	.topic {
		font-size: var(--fs-small);
		font-weight: 600;
	}

	.score {
		font-size: var(--fs-caption);
		font-weight: 700;
		color: var(--fg-subtle);
		background: var(--fill);
		border-radius: var(--radius-full);
		padding: 3px 10px;
		flex: 0 0 auto;
	}

	.exit {
		flex: 0 0 auto;
		min-height: 36px;
		padding: 0 var(--sp-3);
		border-radius: var(--radius);
		background: var(--fill);
		font-size: var(--fs-small);
		font-weight: 600;
		transition: transform var(--dur-press) var(--ease-standard), background-color var(--dur-press) var(--ease-standard);
	}

	.exit:active {
		transform: scale(0.95);
		background: var(--fill-strong);
	}

	.body {
		flex: 1;
		min-height: 0;
		overflow-y: auto;
		-webkit-overflow-scrolling: touch;
		padding: var(--sp-4);
		display: flex;
		flex-direction: column;
		gap: var(--sp-4);
	}

	.question {
		display: flex;
		flex-direction: column;
		gap: var(--sp-4);
	}

	.q-text {
		font-size: 18px;
		font-weight: 700;
		line-height: 1.35;
		letter-spacing: -0.01em;
	}

	.options {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.option {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-3);
		min-height: 52px;
		width: 100%;
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
		font-size: var(--fs-body);
		line-height: 1.45;
		transition: background-color var(--dur-press) var(--ease-standard), transform var(--dur-press) var(--ease-standard);
	}

	.option:not(:disabled):active {
		transform: scale(0.98);
		background: var(--fill-strong);
	}

	.letter {
		display: grid;
		place-items: center;
		width: 22px;
		height: 22px;
		border-radius: var(--radius-sm);
		background: var(--bg);
		font-size: var(--fs-caption);
		font-weight: 700;
		color: var(--fg-muted);
		flex: 0 0 auto;
	}

	.option.correct {
		background: transparent;
		box-shadow: inset 0 0 0 1.5px var(--success);
	}

	.option.correct .letter {
		background: var(--success);
		color: #fff;
	}

	.option.wrong {
		background: transparent;
		box-shadow: inset 0 0 0 1.5px var(--danger);
	}

	.option.wrong .letter {
		background: var(--danger);
		color: #fff;
	}

	.option.dim {
		opacity: 0.5;
	}

	.mark {
		display: inline-flex;
		flex: 0 0 auto;
		margin-top: 2px;
	}

	.mark.ok {
		color: var(--success);
	}

	.mark.no {
		color: var(--danger);
	}

	.why {
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
	}

	.verdict {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		font-weight: 700;
		color: var(--danger);
		margin-bottom: var(--sp-2);
	}

	.verdict.on {
		color: var(--success);
	}

	.why-text {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.foot {
		flex: 0 0 auto;
		padding: var(--sp-3) var(--sp-4) var(--sp-4);
		border-top: 1px solid var(--border);
	}

	.hint {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		text-align: center;
		padding: var(--sp-2) 0;
	}

	.priority {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-2);
		padding: var(--sp-2) var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
		font-size: var(--fs-caption);
		line-height: 1.5;
		color: var(--fg-subtle);
	}

	.priority strong {
		font-weight: 700;
		color: var(--fg-muted);
	}

	/* ---------- results ---------- */

	.done {
		gap: var(--sp-6);
	}

	.result {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: var(--sp-3);
		padding-top: var(--sp-4);
		text-align: center;
	}

	.result-title {
		font-size: var(--fs-title);
		font-weight: 700;
	}

	.result-text {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
		max-width: 42ch;
	}

	.review-title {
		font-size: var(--fs-caption);
		font-weight: 700;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--fg-subtle);
		margin-bottom: var(--sp-2);
	}

	.review-item {
		padding: var(--sp-3) 0;
		border-top: 1px solid var(--border);
	}

	.review-q {
		font-size: var(--fs-small);
		font-weight: 600;
		margin-bottom: var(--sp-2);
	}

	.review-line {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		line-height: 1.45;
	}

	.review-line.bad {
		color: var(--danger);
	}

	.review-line.good {
		color: var(--success);
	}

	.review-why {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-muted);
		margin-top: var(--sp-2);
	}

	.result-actions {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
		padding-bottom: var(--sp-4);
	}

	.empty {
		align-items: flex-start;
		justify-content: center;
		gap: var(--sp-3);
		color: var(--fg-subtle);
	}
</style>
