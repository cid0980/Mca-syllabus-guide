<script lang="ts">
	import type { PageData } from './$types';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { progress } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import { buildItems, type QuizItem } from '$lib/quiz';
	import AppBar from '$lib/components/AppBar.svelte';
	import QuizRunner from '$lib/components/QuizRunner.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';

	export let data: PageData;

	$: mode = $page.url.searchParams.get('mode') ?? 'random';
	$: n = Number($page.url.searchParams.get('n') ?? (mode === 'wrong' ? 0 : 10));
	$: wrongIds = Object.entries($progress)
		.filter(([, p]) => p.quizWrong > 0)
		.map(([id]) => id);

	/**
	 * The wrong-answer set can only be known in the browser (it reads your progress), so the
	 * runner waits for hydration before it starts.
	 */
	$: filtered =
		mode === 'wrong' ? data.items.filter((i) => wrongIds.includes(i.cardId)) : data.items;

	$: title = mode === 'wrong' ? 'Retry missed questions' : n > 0 ? `${n} random questions` : 'Mixed quiz';
</script>

<svelte:head><title>Quiz — StudyFeed</title></svelte:head>

<div class="quiz-page">
	<AppBar title="Quiz" subtitle={title} onBack={() => goto('/quiz')} />
	{#if mode === 'wrong' && !$hydrated}
		<div class="loading"><Skeleton variant="card" /></div>
	{:else}
		<QuizRunner
			items={filtered}
			limit={n}
			emptyTitle={mode === 'wrong' ? 'Nothing to retry' : 'No questions yet'}
			emptyText={mode === 'wrong'
				? 'You have no wrong answers recorded yet. Answer a few questions first, or run a mixed set.'
				: 'No cards with questions have been written yet. The syllabus and every definition are readable in the meantime.'}
			scope={mode === 'wrong' ? 'missed questions' : 'mixed' + (n ? ` (${n})` : '')}
			on:exit={() => goto('/quiz')}
		/>
	{/if}
</div>

<style>
	.quiz-page {
		display: flex;
		flex-direction: column;
		height: 100dvh;
		max-width: 600px;
		margin: 0 auto;
		padding-bottom: calc(var(--nav-h) + env(safe-area-inset-bottom));
		background: var(--bg);
	}

	.loading {
		padding: var(--sp-4);
	}
</style>
