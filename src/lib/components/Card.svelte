<script lang="ts">
	/** The study card: header, definition, explanation, example, quiz, exam tip. */
	import type { DeckCard } from '$lib/content';
	import { Lightbulb, CircleCheck, CircleX } from 'lucide-svelte';

	export let card: DeckCard;
	export let face: 'front' | 'back' = 'front';
	export let examMode = false;
	export let quizRecord: (correct: boolean) => void = () => {};

	let picked: number[] = [];

	$: if (card) picked = card.quiz.map(() => -1);

	function choose(qi: number, oi: number, answer: number) {
		if (picked[qi] !== -1) return;
		picked = picked.map((v, i) => (i === qi ? oi : v));
		quizRecord(oi === answer);
	}
</script>

<article class="card">
	<header class="head">
		<span class="badge">{card.subjectCode} · Mod {card.module}</span>
		{#if !card.verified}<span class="badge draft">draft</span>{/if}
	</header>

	<h2 class="topic">{card.topic}</h2>

	{#if face === 'front'}
		<p class="definition">{card.definition}</p>
		<p class="body">{card.explanation}</p>

		<section class="block">
			<h3 class="block-title">Example</h3>
			<p class="body">{card.example}</p>
		</section>

		{#if !examMode}
			<section class="block tip">
				<h3 class="block-title"><Lightbulb size={14} /> Exam tip</h3>
				<p class="body">{card.examTip}</p>
			</section>
		{/if}
	{:else}
		<section class="block tip">
			<h3 class="block-title"><Lightbulb size={14} /> Exam tip</h3>
			<p class="body">{card.examTip}</p>
		</section>

		{#each card.quiz as q, qi}
			<section class="quiz">
				<h3 class="q-text">{q.q}</h3>
				<div class="options">
					{#each q.options as option, oi}
						{@const answered = picked[qi] !== -1}
						<button
							class="option"
							class:correct={answered && oi === q.answer}
							class:wrong={answered && oi === picked[qi] && oi !== q.answer}
							class:dim={answered && oi !== q.answer && oi !== picked[qi]}
							disabled={answered}
							on:click={() => choose(qi, oi, q.answer)}
						>
							<span class="letter">{'ABCD'[oi]}</span>
							<span>{option}</span>
							{#if answered && oi === q.answer}<span class="mark ok"><CircleCheck size={16} /></span>{/if}
							{#if answered && oi === picked[qi] && oi !== q.answer}<span class="mark no"><CircleX size={16} /></span>{/if}
						</button>
					{/each}
				</div>
				{#if picked[qi] !== -1}
					<p class="why"><strong>{picked[qi] === q.answer ? 'Correct.' : 'Not quite.'}</strong> {q.why}</p>
				{/if}
			</section>
		{/each}
	{/if}
</article>

<style>
	.card {
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
		background: var(--bg-subtle);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
		padding: var(--sp-4);
		overflow-y: auto;
		-webkit-overflow-scrolling: touch;
	}

	.head {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
	}

	.badge.draft {
		color: var(--warning);
	}

	.topic {
		font-size: var(--fs-title);
		font-weight: 600;
		line-height: 1.3;
		letter-spacing: -0.01em;
	}

	.definition {
		font-size: var(--fs-def);
		font-weight: 500;
		line-height: 1.4;
		letter-spacing: -0.01em;
	}

	.body {
		font-size: var(--fs-body);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.block {
		border-top: 1px solid var(--border);
		padding-top: var(--sp-3);
	}

	.block-title {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
		font-size: var(--fs-caption);
		font-weight: 500;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--fg-subtle);
		margin-bottom: var(--sp-2);
	}

	.tip .block-title {
		color: var(--accent);
	}

	.quiz {
		border-top: 1px solid var(--border);
		padding-top: var(--sp-3);
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.q-text {
		font-size: var(--fs-body);
		font-weight: 500;
		line-height: 1.4;
	}

	.options {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.option {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-2);
		min-height: 44px;
		width: 100%;
		padding: var(--sp-2) var(--sp-3);
		background: var(--bg-element);
		border: 1px solid transparent;
		border-radius: var(--radius);
		font-size: var(--fs-small);
		line-height: 1.4;
		transition: background-color 0.14s ease;
	}

	.option:not(:disabled):hover {
		background: var(--bg-hover);
	}

	.option:disabled {
		cursor: default;
	}

	.letter {
		font-weight: 600;
		color: var(--fg-subtle);
		font-size: var(--fs-caption);
		padding-top: 2px;
	}

	.option.correct {
		border-color: var(--success);
		background: transparent;
	}

	.option.wrong {
		border-color: var(--danger);
		background: transparent;
	}

	.option.dim {
		opacity: 0.55;
	}

	.mark {
		margin-left: auto;
		flex: 0 0 auto;
	}

	.mark.ok {
		color: var(--success);
	}

	.mark.no {
		color: var(--danger);
	}

	.why {
		font-size: var(--fs-small);
		line-height: 1.5;
		color: var(--fg-muted);
	}

	.why strong {
		color: var(--fg);
		font-weight: 500;
	}
</style>
