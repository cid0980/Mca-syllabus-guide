<script lang="ts">
	import type { PageData } from './$types';
	import { plural } from '$lib/content';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import SwipeFeed from '$lib/components/SwipeFeed.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';

	export let data: PageData;
</script>

<svelte:head><title>Exam mode — StudyFeed</title></svelte:head>

<AppBar
	title="Exam mode"
	subtitle={`${data.summary ? data.summary.subject : data.code} · Module ${data.module}`}
	back={`/subject/${encodeURIComponent(data.code)}`}
/>

{#if data.cards.length === 0}
	<main class="page">
		<section class="gutter empty">
			<h2>Nothing to revise in Module {data.module} yet</h2>
			<p>
				This module has no written cards, so there is no definition set to scan. The topics and their
				definitions are still worth reading.
			</p>
			<a class="btn btn--primary" href={`/explore/${encodeURIComponent(data.code)}`}>Read the topics</a>
		</section>
	</main>
{:else}
	<main class="feed-page">
		{#if $hydrated}
			<SwipeFeed cards={data.cards} initialIndex={0} examMode />
		{:else}
			<Skeleton variant="card" />
		{/if}
	</main>
{/if}

<style>
	.feed-page {
		display: flex;
		flex-direction: column;
		height: 100dvh;
		max-width: 600px;
		margin: 0 auto;
		padding: var(--sp-3) var(--sp-4) 0;
		padding-bottom: calc(var(--nav-h) + var(--sp-3) + env(safe-area-inset-bottom));
	}

	.empty {
		padding-top: var(--sp-8);
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
		align-items: flex-start;
	}

	.empty h2 {
		font-size: var(--fs-title);
		font-weight: 600;
	}

	.empty p {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}
</style>
