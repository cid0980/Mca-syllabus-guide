<script lang="ts">
	/**
	 * One card in the feed, laid out like an Instagram post.
	 *
	 * Fixes from user feedback:
	 *  - the card is natural height; nothing overlaps the next card and nothing scrolls inside it
	 *  - tapping only flips when the finger did not move (scrolling must not change the face)
	 *  - the quiz always offers a labelled way back to the card, and after the last answer it
	 *    shows the score with the next actions
	 */
	import { createEventDispatcher } from 'svelte';
	import {
		Bookmark,
		BookmarkCheck,
		MessageSquare,
		ListChecks,
		RotateCcw,
		CircleCheck,
		CircleX,
		Lightbulb
	} from 'lucide-svelte';
	import type { DeckCard } from '$lib/content';
	import { shortName } from '$lib/labels';
	import { recordQuiz } from '$lib/stores/progress';

	const dispatch = createEventDispatcher<{ save: boolean; ask: void }>();

	export let card: DeckCard;
	export let examMode = false;
	export let saved = false;
	export let index = 0;
	export let total = 1;

	let face: 'front' | 'back' = 'front';
	let picked: number[] = [];
	let burst = false;
	let lastTap = 0;
	let tapTimer: ReturnType<typeof setTimeout> | undefined;
	let burstTimer: ReturnType<typeof setTimeout> | undefined;

	$: if (card) picked = card.quiz.map(() => -1);
	$: avatar = card ? shortName(card.subjectCode) : '';
	$: answered = picked.filter((v) => v !== -1).length;
	$: correct = card ? picked.filter((v, i) => v !== -1 && v === card.quiz[i].answer).length : 0;
	$: allDone = card ? picked.length > 0 && answered === card.quiz.length : false;

	function choose(qi: number, oi: number, answer: number) {
		if (picked[qi] !== -1) return;
		picked = picked.map((v, i) => (i === qi ? oi : v));
		recordQuiz(card.id, oi === answer);
	}

	function flip() {
		if (examMode) return;
		face = face === 'front' ? 'back' : 'front';
		if (face === 'back') picked = card.quiz.map(() => -1);
	}

	function save() {
		dispatch('save', !saved);
		burst = true;
		clearTimeout(burstTimer);
		burstTimer = setTimeout(() => (burst = false), 620);
	}

	/** Tap = flip, double tap = save — but never while the user is scrolling. */
	let downAt = { x: 0, y: 0, t: 0 };

	function onDown(e: PointerEvent) {
		downAt = { x: e.clientX, y: e.clientY, t: Date.now() };
	}

	function onClick(e: MouseEvent) {
		const target = e.target as HTMLElement | null;
		if (target?.closest('button, a, input, textarea')) return;
		const moved = Math.abs(e.clientX - downAt.x) + Math.abs(e.clientY - downAt.y);
		if (moved > 8) return; // that was a scroll, not a tap
		const now = Date.now();
		if (now - lastTap < 320) {
			clearTimeout(tapTimer);
			lastTap = 0;
			save();
			return;
		}
		lastTap = now;
		tapTimer = setTimeout(() => {
			if (lastTap === now) {
				lastTap = 0;
				flip();
			}
		}, 320);
	}
</script>

<article class="post">
	<header class="head">
		<span class="avatar" aria-hidden="true">{avatar}</span>
		<div class="grow">
			<p class="who-title truncate">{card.subjectCode}</p>
			<p class="who-sub truncate">
				Module {card.module} · {examMode ? 'definitions only' : face === 'back' ? `quiz · ${answered}/${card.quiz.length}` : 'study card'}
			</p>
		</div>
		{#if !card.verified}<span class="badge draft">draft</span>{/if}
	</header>

	<div
		class="body"
		on:pointerdown={onDown}
		on:click={onClick}
		role="button"
		tabindex="0"
		aria-label={face === 'back' ? 'Tap to go back to the card' : 'Tap to open the quiz'}
		on:keydown={(e) => (e.key === 'Enter' || e.key === ' ') && flip()}
	>
		<h2 class="topic">{card.topic}</h2>
		<p class="definition">{card.definition}</p>

		{#if face === 'back' && !examMode}
			<div class="quiz expand-in">
				{#each card.quiz as q, qi}
					<div class="q">
						<p class="q-text">{q.q}</p>
						<div class="options">
							{#each q.options as option, oi}
								{@const done = picked[qi] !== -1}
								<button
									class="option"
									class:correct={done && oi === q.answer}
									class:wrong={done && oi === picked[qi] && oi !== q.answer}
									class:dim={done && oi !== q.answer && oi !== picked[qi]}
									disabled={done}
									on:click|stopPropagation={() => choose(qi, oi, q.answer)}
								>
									<span class="letter">{'ABCD'[oi]}</span>
									<span class="grow">{option}</span>
									{#if done && oi === q.answer}<span class="mark ok"><CircleCheck size={16} /></span>{/if}
									{#if done && oi === picked[qi] && oi !== q.answer}<span class="mark no"><CircleX size={16} /></span>{/if}
								</button>
							{/each}
						</div>
						{#if picked[qi] !== -1}
							<p class="why">
								<strong>{picked[qi] === q.answer ? 'Correct.' : 'Not quite.'}</strong> {q.why}
							</p>
						{/if}
					</div>
				{/each}

				{#if allDone}
					<div class="score">
						<span class="grow nums">You got {correct}/{card.quiz.length} right.</span>
						<button class="btn btn--secondary btn--sm" on:click|stopPropagation={flip}>
							<RotateCcw size={13} /> Back to card
						</button>
					</div>
				{/if}
			</div>
		{:else}
			<p class="text">{card.explanation}</p>
			<p class="text example"><span class="inline-tag">Example</span> {card.example}</p>
			<p class="text tip">
				<span class="tip-icon"><Lightbulb size={13} /></span>
				<span class="inline-tag accent">Exam tip</span> {card.examTip}
			</p>

			{#if !examMode}
				<button class="quiz-cta" on:click|stopPropagation={flip}>
					<ListChecks size={16} />
					<span class="grow">Take the quiz · {card.quiz.length} question{card.quiz.length === 1 ? '' : 's'}</span>
				</button>
			{/if}
		{/if}
	</div>

	<div class="actions">
		<button class="act" class:on={saved} on:click|stopPropagation={save} aria-pressed={saved} aria-label={saved ? 'Remove from saved' : 'Save card'}>
			{#if saved}<BookmarkCheck size={22} />{:else}<Bookmark size={22} />{/if}
		</button>
		<button class="act" on:click|stopPropagation={() => dispatch('ask')} aria-label="Ask about this card">
			<MessageSquare size={22} />
		</button>
		{#if !examMode}
			<button class="act" on:click|stopPropagation={flip} aria-label={face === 'back' ? 'Back to the card' : 'Show the quiz'}>
				{#if face === 'back'}<RotateCcw size={22} />{:else}<ListChecks size={22} />{/if}
			</button>
		{/if}
		<span class="grow"></span>
		<span class="counter nums">{index + 1}/{total}</span>
	</div>

	{#if burst}
		<span class="save-burst" aria-hidden="true">{saved ? 'Saved' : 'Removed'}</span>
	{/if}
</article>

<style>
	.post {
		position: relative;
		display: flex;
		flex-direction: column;
		background: var(--bg);
	}

	.head {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-2) var(--sp-4);
	}

	.who-title {
		font-size: var(--fs-body);
		font-weight: 700;
		letter-spacing: -0.01em;
	}

	.who-sub {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		margin-top: 1px;
	}

	/* natural height: the card grows, the page scrolls, nothing overlaps */
	.body {
		padding: var(--sp-1) var(--sp-4) var(--sp-3);
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
		outline: none;
		cursor: pointer;
	}

	.body:focus-visible {
		outline: 2px solid var(--accent);
		outline-offset: -2px;
		border-radius: var(--radius);
	}

	.topic {
		font-size: var(--fs-title);
		font-weight: 700;
		line-height: 1.3;
		letter-spacing: -0.01em;
	}

	.definition {
		font-size: var(--fs-def);
		font-weight: 600;
		line-height: 1.4;
		letter-spacing: -0.01em;
	}

	.text {
		font-size: var(--fs-body);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.example {
		border-left: 2px solid var(--border);
		padding-left: var(--sp-3);
	}

	.tip-icon {
		display: inline-flex;
		vertical-align: -1px;
		margin-right: 3px;
		color: var(--warning);
	}

	.inline-tag {
		font-size: var(--fs-caption);
		font-weight: 700;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--fg-subtle);
		margin-right: 2px;
	}

	.inline-tag.accent {
		color: var(--accent);
	}

	/* the way into the quiz is a labelled control, visible without scrolling */
	.quiz-cta {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		width: 100%;
		min-height: 44px;
		padding: var(--sp-2) var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
		font-size: var(--fs-small);
		font-weight: 600;
		transition: transform var(--dur-press) var(--ease-standard), background-color var(--dur-press) var(--ease-standard);
	}

	.quiz-cta:active {
		transform: scale(0.985);
		background: var(--fill-strong);
	}

	/* ---------- quiz ---------- */

	.quiz {
		display: flex;
		flex-direction: column;
		gap: var(--sp-4);
	}

	.q {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.q-text {
		font-size: var(--fs-body);
		font-weight: 600;
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
		background: var(--fill);
		border-radius: var(--radius);
		font-size: var(--fs-small);
		line-height: 1.45;
		transition: background-color var(--dur-press) var(--ease-standard), transform var(--dur-press) var(--ease-standard);
	}

	.option:not(:disabled):active {
		transform: scale(0.985);
	}

	.letter {
		font-weight: 700;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		padding-top: 3px;
	}

	.option.correct {
		background: transparent;
		box-shadow: inset 0 0 0 1px var(--success);
	}

	.option.wrong {
		background: transparent;
		box-shadow: inset 0 0 0 1px var(--danger);
	}

	.option.dim {
		opacity: 0.5;
	}

	.mark {
		display: inline-flex;
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
		font-weight: 600;
	}

	.score {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		padding: var(--sp-2) var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
		font-size: var(--fs-small);
		font-weight: 600;
	}

	/* ---------- action row ---------- */

	.actions {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
		padding: var(--sp-1) var(--sp-3);
		border-top: 1px solid var(--border);
	}

	.act {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		width: 42px;
		height: 42px;
		border-radius: var(--radius-full);
		color: var(--fg);
		transition: background-color var(--dur-press) var(--ease-standard), transform var(--dur-press) var(--ease-standard),
			opacity var(--dur-press) var(--ease-standard);
	}

	.act:active {
		transform: scale(0.9);
		opacity: 0.65;
	}

	.act.on {
		color: var(--accent);
	}

	.counter {
		font-size: var(--fs-caption);
		font-weight: 600;
		color: var(--fg-subtle);
		padding-right: var(--sp-2);
	}

	.save-burst {
		position: absolute;
		top: 44px;
		left: 50%;
		transform: translateX(-50%);
		background: var(--fg);
		color: var(--bg);
		font-size: var(--fs-caption);
		font-weight: 700;
		letter-spacing: 0.04em;
		text-transform: uppercase;
		padding: var(--sp-1) var(--sp-3);
		border-radius: var(--radius-full);
		animation: burst var(--dur-slow) var(--ease-standard) both;
		pointer-events: none;
	}

	@keyframes burst {
		0% {
			opacity: 0;
			transform: translate(-50%, -6px) scale(0.9);
		}
		18% {
			opacity: 1;
			transform: translate(-50%, 0) scale(1);
		}
		70% {
			opacity: 1;
		}
		100% {
			opacity: 0;
			transform: translate(-50%, -4px) scale(0.98);
		}
	}
</style>
