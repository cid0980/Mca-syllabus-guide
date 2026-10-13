<script lang="ts">
	import type { PageData } from './$types';
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import { plural } from '$lib/content';
	import { hydrated } from '$lib/stores/hydrate';
	import { KEYS, readJSON, writeJSON } from '$lib/storage';
	import AppBar from '$lib/components/AppBar.svelte';
	import SwipeFeed from '$lib/components/SwipeFeed.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';

	export let data: PageData;

	onMount(() => {
		writeJSON(KEYS.lastOpened, { code: data.code, module: data.module, at: Date.now() });
	});

	/** `?card=<id>` jumps straight to one card; otherwise resume at the first unseen card. */
	function startIndex(): number {
		if (!browser) return 0;
		const requested = new URLSearchParams(location.search).get('card');
		if (requested) {
			const i = data.cards.findIndex((c) => c.id === requested);
			if (i >= 0) return i;
		}
		const map = readJSON<Record<string, { seen?: boolean }>>(KEYS.progress, {});
		const first = data.cards.findIndex((c) => !map[c.id]?.seen);
		return first < 0 ? 0 : first;
	}
</script>

<svelte:head>
	<title>{data.summary ? data.summary.subject : data.code} · Module {data.module} — StudyFeed</title>
</svelte:head>

<AppBar
	title={data.summary ? data.summary.subject : data.code}
	subtitle={`Module ${data.module} · ${plural(data.cards.length, 'card')}`}
	back={data.cards.length ? `/subject/${encodeURIComponent(data.code)}` : `/explore/${encodeURIComponent(data.code)}`}
/>

{#if data.cards.length === 0}
	<main class="page">
		<section class="gutter empty">
			<h2>No cards in Module {data.module} yet</h2>
			<p>
				The topics for this module are already stored with their definitions. Read them now, or jump
				to a module that has cards written.
			</p>
			<div class="empty-actions">
				<a class="btn btn--primary" href={`/explore/${encodeURIComponent(data.code)}`}>
					Read the topic list
				</a>
				<a class="btn btn--secondary" href={`/subject/${encodeURIComponent(data.code)}`}>All modules</a>
			</div>
		</section>

		{#if data.otherModules.length}
			<p class="section-label">Modules with cards</p>
			<div class="group">
				{#each data.otherModules as m}
					<a class="module-link" href={`/feed/${encodeURIComponent(data.code)}/${m.module}`}>
						<span class="module-no nums">{m.module}</span>
						<span class="grow">
							<span class="module-title">{m.title}</span>
							<span class="module-meta nums">{plural(m.cards, 'card')}</span>
						</span>
					</a>
				{/each}
			</div>
		{/if}
	</main>
{:else}
	<main class="feed-page">
		{#if $hydrated}
			<SwipeFeed cards={data.cards} initialIndex={startIndex()} />
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
	}

	.empty h2 {
		font-size: var(--fs-title);
		font-weight: 600;
		margin-bottom: var(--sp-2);
	}

	.empty p {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.empty-actions {
		display: flex;
		gap: var(--sp-2);
		margin-top: var(--sp-4);
	}

	.empty-actions .btn {
		flex: 1;
	}

	.module-link {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		min-height: 56px;
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
	}

	.module-link + .module-link {
		border-top: 1px solid var(--border);
	}

	.module-link:hover {
		background: var(--bg-hover);
	}

	.module-no {
		display: grid;
		place-items: center;
		width: 32px;
		height: 32px;
		border-radius: var(--radius-full);
		background: var(--bg-element);
		color: var(--fg-muted);
		font-size: var(--fs-caption);
		font-weight: 600;
		flex: 0 0 auto;
	}

	.module-title {
		display: block;
		font-size: var(--fs-small);
		font-weight: 500;
	}

	.module-meta {
		display: block;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}
</style>
