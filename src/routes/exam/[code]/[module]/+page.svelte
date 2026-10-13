<script lang="ts">
	import type { PageData } from './$types';
	import AppBar from '$lib/components/AppBar.svelte';
	import Feed from '$lib/components/Feed.svelte';

	export let data: PageData;
</script>

<svelte:head><title>Exam mode — StudyFeed</title></svelte:head>

{#if data.cards.length === 0}
	<AppBar
		title="Exam mode"
		subtitle={`${data.summary ? data.summary.subject : data.code} · Module ${data.module}`}
		back={`/subject/${encodeURIComponent(data.code)}`}
	/>
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
	<div class="feed-page">
		<AppBar
			title="Exam mode"
			subtitle={`${data.summary ? data.summary.subject : data.code} · Module ${data.module}`}
			back={`/subject/${encodeURIComponent(data.code)}`}
		/>
		<Feed cards={data.cards} initialIndex={0} examMode />
	</div>
{/if}

<style>
	.feed-page {
		display: flex;
		flex-direction: column;
		height: 100dvh;
		max-width: 600px;
		margin: 0 auto;
		padding-bottom: calc(var(--nav-h) + env(safe-area-inset-bottom));
		background: var(--bg);
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
		font-weight: 700;
	}

	.empty p {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}
</style>
