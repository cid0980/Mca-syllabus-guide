<script lang="ts">
	import type { PageData } from './$types';
	import { ListChecks, ChevronRight, Shuffle, RotateCcw, Play, Trophy } from 'lucide-svelte';
	import { plural, totals } from '$lib/content';
	import { progress } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import {
		lastSession,
		readSessions,
		bestSessionFor,
		moduleScope,
		type QuizSession
	} from '$lib/quiz';
	import AppBar from '$lib/components/AppBar.svelte';
	import Notice from '$lib/components/Notice.svelte';

	export let data: PageData;

	/** "wrong" mode needs the questions the student got wrong; ids come from the progress map */
	$: wrongIds = Object.entries($progress)
		.filter(([, p]) => p.quizWrong > 0)
		.map(([id]) => id);
	$: last = $hydrated ? lastSession() : null;

	/**
	 * Finished runs live in the browser, so this waits for hydration - rendering it on the server
	 * would mean a different first paint. Nothing here writes storage.
	 */
	let sessions: QuizSession[] = [];
	$: sessions = $hydrated ? readSessions() : [];

	const sizes = [5, 10, 0];
	function sizeLabel(n: number): string {
		return n === 0 ? 'All' : `${n} questions`;
	}
</script>

<svelte:head><title>Quiz — StudyFeed</title></svelte:head>

<AppBar
	title="Quiz"
	subtitle={data.totalQuestions
		? `${data.totalQuestions} questions from ${plural(data.cardCount, 'card')}`
		: 'Questions come from the saved cards'}
/>

<main class="page">
	{#if data.totalQuestions === 0}
		<Notice
			title="No quiz questions yet"
			text="Quiz mode reads the questions saved on each card, so it fills up as cards are written. The syllabus and every definition are already readable."
		/>
		<div class="gutter">
			<a class="btn btn--primary btn--block" href="/explore">Browse the syllabus</a>
		</div>
	{:else}
		{#if last}
			<div class="gutter last">
				<Trophy size={16} />
				<span class="grow">
					Last run: <strong class="nums">{last.correct}/{last.total}</strong> · {last.scope}
				</span>
			</div>
		{/if}

		<p class="section-label">Mixed practice</p>
		<div class="gutter modes">
			<a class="mode" href="/quiz/mixed?n=10">
				<span class="mode-icon"><Shuffle size={18} /></span>
				<span class="grow">
					<span class="mode-title">10 random questions</span>
					<span class="mode-sub">Pulled from every subject that has cards</span>
				</span>
				<span class="chev"><ChevronRight size={18} /></span>
			</a>
			<a class="mode" href="/quiz/mixed?n=20">
				<span class="mode-icon"><ListChecks size={18} /></span>
				<span class="grow">
					<span class="mode-title">20 random questions</span>
					<span class="mode-sub">A longer mixed set before an exam</span>
				</span>
				<span class="chev"><ChevronRight size={18} /></span>
			</a>
			{#if $hydrated && wrongIds.length}
				<a class="mode" href="/quiz/mixed?mode=wrong">
					<span class="mode-icon warn"><RotateCcw size={18} /></span>
					<span class="grow">
						<span class="mode-title">Retry what I missed</span>
						<span class="mode-sub nums">{plural(wrongIds.length, 'card')} with a wrong answer recorded</span>
					</span>
					<span class="chev"><ChevronRight size={18} /></span>
				</a>
			{/if}
		</div>

		<p class="section-label">By module</p>
		<div class="group">
			{#each data.decks as deck}
				{@const best = bestSessionFor(sessions, moduleScope(deck.code, deck.module), deck.questions)}
				<a class="deck pressable" href={`/quiz/${encodeURIComponent(deck.code)}/${deck.module}`}>
					<span class="avatar" aria-hidden="true">{deck.module}</span>
					<span class="grow">
						<span class="deck-title">{deck.moduleTitle}</span>
						<span class="deck-sub">
							{deck.code} · {plural(deck.questions, 'question')} from {plural(deck.cards, 'card')}
						</span>
					</span>
					{#if best}
						<span class="best nums">Best {best.correct}/{best.total}</span>
					{/if}
					<span class="chev"><ChevronRight size={18} /></span>
				</a>
			{/each}
		</div>

		<div class="gutter note">
			<a class="btn btn--secondary btn--block" href="/feed/CSCA%20411/I">
				<Play size={16} /> Study the cards before quizzing
			</a>
			<p class="fineprint">
				Every answer is recorded per card, so the Progress screen shows accuracy per subject and per
				module. Wrong answers can be retried at the end of any run.
			</p>
		</div>
	{/if}
</main>

<style>
	.last {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		margin-top: var(--sp-4);
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
		font-size: var(--fs-small);
		color: var(--fg-muted);
	}

	.modes {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.mode {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
		transition: background-color var(--dur-press) var(--ease-standard), transform var(--dur-press) var(--ease-standard);
	}

	.mode:active {
		background: var(--fill);
		transform: scale(0.99);
	}

	.mode-icon {
		display: grid;
		place-items: center;
		width: 36px;
		height: 36px;
		border-radius: var(--radius-full);
		background: var(--fill);
		color: var(--fg-muted);
		flex: 0 0 auto;
	}

	.mode-icon.warn {
		color: var(--warning);
	}

	.mode-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 600;
	}

	.mode-sub {
		display: block;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.deck {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		min-height: 60px;
		padding: var(--sp-3) var(--sp-4);
	}

	.deck-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 600;
		line-height: 1.35;
	}

	.deck-sub {
		display: block;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.chev {
		display: inline-flex;
		color: var(--fg-subtle);
		flex: 0 0 auto;
	}

	.best {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		flex: 0 0 auto;
	}

	.note {
		padding-top: var(--sp-6);
	}

	.fineprint {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		margin-top: var(--sp-3);
	}
</style>
