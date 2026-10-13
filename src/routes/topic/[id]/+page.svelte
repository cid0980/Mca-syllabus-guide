<script lang="ts">
	import type { PageData } from './$types';
	import { onMount } from 'svelte';
	import { Bookmark, BookmarkCheck, Lightbulb, ChevronLeft, ChevronRight } from 'lucide-svelte';
	import { browser } from '$app/environment';
	import type { DeckCard } from '$lib/content';
	import { markSeen, recordQuiz, progress } from '$lib/stores/progress';
	import { bookmarks, isBookmarked, toggleBookmark } from '$lib/stores/bookmarks';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import Card from '$lib/components/Card.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	export let data: PageData;

	$: card = deckCard(data);
	$: saved = data.found ? isBookmarked(data.node.id, $bookmarks) : false;

	/** The stored node as a feed card, so the topic page can show the same study card. */
	function deckCard(d: PageData): DeckCard | null {
		if (!d.found || !d.node.card) return null;
		return {
			id: d.node.id,
			subjectCode: d.code,
			semester: 1,
			module: d.module.module,
			topic: d.node.title,
			definition: d.node.definition,
			explanation: d.node.card.explanation,
			example: d.node.card.example,
			quiz: d.node.card.quiz,
			examTip: d.node.card.examTip,
			verified: d.node.card.verified
		};
	}

	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;

	function notify(message: string) {
		toast = message;
		clearTimeout(toastTimer);
		toastTimer = setTimeout(() => (toast = ''), 1600);
	}

	onMount(() => {
		if (data.found && data.node.card) markSeen(data.node.id);
	});

	function save() {
		if (!data.found) return;
		const added = toggleBookmark(data.node.id);
		notify(added ? 'Saved' : 'Removed from saved');
	}
</script>

<svelte:head><title>{data.found ? data.node.title : 'Topic'} — StudyFeed</title></svelte:head>

{#if !data.found}
	<AppBar title="Topic not found" back="/explore" />
	<main class="page">
		<ErrorState
			title="Topic not found"
			message="This id is not part of the stored syllabus. It may have been renamed."
			retryLabel="Browse the syllabus"
			on:retry={() => (location.href = '/explore')}
		/>
	</main>
{:else}
	{@const node = data.node}
	{@const children = node.children ?? []}
	{@const plain = children.filter((c) => c.kind !== 'type')}
	{@const types = children.filter((c) => c.kind === 'type')}
	{@const saved = isBookmarked(node.id, $bookmarks)}

	<AppBar
		title={node.title}
		subtitle={`${data.code} · Module ${data.module.module}${data.parent ? ` · ${data.parent.title}` : ''}`}
		back={`/explore/${encodeURIComponent(data.code)}`}
	>
		<button
			slot="actions"
			class="icon-btn"
			class:icon-btn--on={$hydrated && saved}
			on:click={save}
			aria-label={$hydrated && saved ? 'Remove from saved' : 'Save topic'}
		>
			{#if $hydrated && saved}<BookmarkCheck size={20} />{:else}<Bookmark size={20} />{/if}
		</button>
	</AppBar>

	<main class="page">
		<section class="gutter head">
			<div class="badges">
				<span class="badge">{node.kind === 'type' ? 'Type' : node.kind === 'subtopic' ? 'Subtopic' : 'Topic'}</span>
				{#if node.card && !node.card.verified}<span class="badge draft">draft</span>{/if}
			</div>
			<p class="definition">{node.definition}</p>
			{#if data.parent}
				<a class="parent" href={`/topic/${data.parent.id}`}>
					<ChevronLeft size={14} />
					Part of {data.parent.title}
				</a>
			{/if}
		</section>

		{#if plain.length}
			<p class="section-label">Subtopics · {plain.length}</p>
			<div class="group long-list">
				{#each plain as child}
					<a class="child-row" href={`/topic/${child.id}`}>
						<span class="child-title">{child.title}</span>
						<span class="child-def">{child.definition}</span>
					</a>
				{/each}
			</div>
		{/if}

		{#if types.length}
			<p class="section-label">Types · {types.length}</p>
			<div class="group long-list">
				{#each types as child}
					<a class="child-row" href={`/topic/${child.id}`}>
						<span class="child-title">{child.title}</span>
						<span class="child-def">{child.definition}</span>
					</a>
				{/each}
			</div>
		{/if}

		{#if card}
			<p class="section-label">Study card</p>
			<div class="gutter">
				<Card {card} quizRecord={(correct) => recordQuiz(node.id, correct)} />
				<a
					class="btn btn--secondary btn--block feed-link"
					href={`/feed/${encodeURIComponent(data.code)}/${data.module.module}?card=${node.id}`}
				>
					Open in the swipe feed
				</a>
			</div>
		{:else}
			<section class="gutter note">
				<p class="note-title"><Lightbulb size={14} /> Definition only</p>
				<p class="note-text">
					This entry carries its own syllabus definition. The full card — explanation, example,
					quiz and exam tip — is written when the content pipeline runs for {data.code}.
				</p>
			</section>
		{/if}

		<nav class="pager gutter">
			{#if data.prev}
				<a class="btn btn--secondary pager-btn" href={`/topic/${data.prev.id}`}>
					<ChevronLeft size={16} />
					<span class="truncate">{data.prev.title}</span>
				</a>
			{/if}
			{#if data.next}
				<a class="btn btn--secondary pager-btn right" href={`/topic/${data.next.id}`}>
					<span class="truncate">{data.next.title}</span>
					<ChevronRight size={16} />
				</a>
			{/if}
		</nav>

		<p class="footnote">
			{$hydrated && $progress[node.id]?.seen ? 'Marked as seen.' : 'Opening this page marks it as seen.'}
		</p>
	</main>
{/if}

{#if toast}<div class="toast" role="status">{toast}</div>{/if}

<style>
	.head {
		padding-top: var(--sp-4);
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
	}

	.badges {
		display: flex;
		gap: var(--sp-2);
	}

	.badge.draft {
		color: var(--warning);
	}

	.definition {
		font-size: var(--fs-def);
		font-weight: 500;
		line-height: 1.45;
		letter-spacing: -0.01em;
	}

	.parent {
		display: inline-flex;
		align-items: center;
		gap: var(--sp-1);
		font-size: var(--fs-small);
		color: var(--fg-muted);
	}

	.child-row {
		display: flex;
		flex-direction: column;
		gap: 2px;
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		min-height: 56px;
	}

	.child-row + .child-row {
		border-top: 1px solid var(--border);
	}

	.child-row:hover {
		background: var(--bg-hover);
	}

	.child-title {
		font-size: var(--fs-small);
		font-weight: 500;
	}

	.child-def {
		font-size: var(--fs-small);
		color: var(--fg-muted);
		line-height: 1.5;
	}

	.feed-link {
		margin-top: var(--sp-3);
	}

	.note {
		padding-top: var(--sp-4);
	}

	.note-title {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
		font-size: var(--fs-caption);
		text-transform: uppercase;
		letter-spacing: 0.06em;
		color: var(--accent);
		margin-bottom: var(--sp-2);
	}

	.note-text {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.pager {
		display: flex;
		gap: var(--sp-2);
		padding-top: var(--sp-6);
	}

	.pager-btn {
		flex: 1;
		min-width: 0;
		font-size: var(--fs-small);
		padding: 0 var(--sp-2);
	}

	.pager-btn.right {
		justify-content: flex-end;
	}

	.footnote {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		padding: var(--sp-4) var(--sp-4) 0;
	}
</style>
