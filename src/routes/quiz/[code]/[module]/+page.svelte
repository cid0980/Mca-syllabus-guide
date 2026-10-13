<script lang="ts">
	import type { PageData } from './$types';
	import { goto } from '$app/navigation';
	import { progress } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import QuizRunner from '$lib/components/QuizRunner.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';

	export let data: PageData;
</script>

<svelte:head><title>Quiz · {data.subject} Module {data.module} — StudyFeed</title></svelte:head>

<div class="quiz-page">
	<AppBar
		title="Quiz"
		subtitle={`${data.subject} · Module ${data.module}`}
		onBack={() => goto(`/subject/${encodeURIComponent(data.code)}`)}
	/>
	{#if !$hydrated}
		<div class="loading"><Skeleton variant="card" /></div>
	{:else}
		<QuizRunner
			items={data.items}
			progressMap={$progress}
			prioritise
			scope={`${data.code} Module ${data.module}`}
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
