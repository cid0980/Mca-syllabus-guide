<script lang="ts">
	import { Bookmark } from 'lucide-svelte';
	import { loadAllTrees, findInTree } from '$lib/content';
	import { bookmarks } from '$lib/stores/bookmarks';
	import { hydrated } from '$lib/stores/hydrate';
	import { progress } from '$lib/stores/progress';
	import AppBar from '$lib/components/AppBar.svelte';
	import ListRow from '$lib/components/ListRow.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	let treesPromise = loadAllTrees();

	interface SavedItem {
		id: string;
		title: string;
		definition: string;
		subject: string;
		module: string;
		seen: boolean;
	}

	$: itemsPromise = treesPromise.then((trees) =>
		$bookmarks
			.map((id) => {
				for (const tree of trees) {
					const hit = findInTree(tree, id);
					if (hit) {
						return {
							id,
							title: hit.node.title,
							definition: hit.node.definition,
							subject: tree.subject,
							module: hit.module.module,
							seen: !!$progress[id]?.seen
						} satisfies SavedItem;
					}
				}
				return null;
			})
			.filter((x): x is SavedItem => x !== null)
	);
</script>

<svelte:head><title>Saved — StudyFeed</title></svelte:head>

<AppBar title="Saved" subtitle={$bookmarks.length ? `${$bookmarks.length} saved` : undefined} />

<main class="page page-in">
	{#if !$hydrated}
		<p class="section-label">Loading your saved items</p>
		<Skeleton variant="rows" count={4} />
	{:else if $bookmarks.length === 0}
		<section class="gutter intro">
			<span class="icon"><Bookmark size={20} /></span>
			<h2>Nothing saved yet</h2>
			<p>
				Tap the bookmark button on a card (or double tap the card itself) to keep it here. Saved
				items are stored in this browser, so they work offline.
			</p>
			<div class="intro-actions">
				<a class="btn btn--primary" href="/feed/CSCA%20411/I">Study the first deck</a>
				<a class="btn btn--secondary" href="/explore">Browse the syllabus</a>
			</div>
		</section>
		<p class="section-label">Recently added to the library</p>
		<div class="group long-list">
			<ListRow href="/topic/CSCA411-M2-06" title="Circular Queue and Its Need" subtitle="Data Structures and Algorithms · Module II" />
			<ListRow href="/topic/CSCA413-M2-T07" title="Normal Forms" subtitle="Database Management Systems · Module II" />
			<ListRow href="/topic/CSCA422-M2-T05" title="Deadlocks" subtitle="Operating Systems · Module II" />
		</div>
	{:else}
		{#await itemsPromise}
			<p class="section-label">Loading saved items</p>
			<Skeleton variant="rows" count={4} />
		{:then items}
			<div class="group long-list">
				{#each items as item}
					<ListRow
						href={`/topic/${item.id}`}
						title={item.title}
						subtitle={item.definition}
						meta={`${item.subject} · Module ${item.module}${item.seen ? '' : ' · not seen yet'}`}
						chevron
					/>
				{/each}
			</div>
		{:catch error}
			<ErrorState
				title="Could not read your saved items"
				message={error.message}
				on:retry={() => (treesPromise = loadAllTrees())}
			/>
		{/await}
	{/if}
</main>

<style>
	.intro {
		padding-top: var(--sp-8);
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.icon {
		color: var(--fg-subtle);
	}

	.intro h2 {
		font-size: var(--fs-title);
		font-weight: 600;
	}

	.intro p {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.intro-actions {
		display: flex;
		gap: var(--sp-2);
		margin-top: var(--sp-2);
	}

	.intro-actions .btn {
		flex: 1;
	}
</style>
