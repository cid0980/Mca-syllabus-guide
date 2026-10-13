<script lang="ts">
	import type { PageData } from './$types';
	import { ChevronLeft, ChevronRight, ListTree, GitBranch, Layers } from 'lucide-svelte';
	import type { DeckCard } from '$lib/content';
	import { progress } from '$lib/stores/progress';
	import { bookmarks, toggleBookmark } from '$lib/stores/bookmarks';
	import { hydrated } from '$lib/stores/hydrate';
	import { goto } from '$app/navigation';
	import AppBar from '$lib/components/AppBar.svelte';
	import Post from '$lib/components/Post.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	export let data: PageData;

	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;

	$: card = deckCard(data);
	$: saved = data.found ? $bookmarks.includes(data.node.id) : false;

	function deckCard(d: PageData): DeckCard | null {
		if (!d.found || !d.node.card) return null;
		return {
			id: d.node.id,
			subjectCode: d.code,
			semester: d.semester,
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

	function notify(message: string) {
		toast = message;
		clearTimeout(toastTimer);
		toastTimer = setTimeout(() => (toast = ''), 1500);
	}

	function save(next: boolean) {
		if (!data.found) return;
		toggleBookmark(data.node.id);
		notify(next ? 'Saved' : 'Removed');
	}

	/** The ask page carries the card and the way back to this page. */
	function openAsk(id: string) {
		goto(`/ask?card=${encodeURIComponent(id)}&from=${encodeURIComponent(`/topic/${id}`)}`);
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

	<AppBar
		title={node.title}
		subtitle={`${data.code} · Module ${data.module.module}`}
		back={`/explore/${encodeURIComponent(data.code)}`}
		crumbs={[
			{ label: data.subject, href: `/explore/${encodeURIComponent(data.code)}` },
			{ label: `Module ${data.module.module}`, href: `/explore/${encodeURIComponent(data.code)}` }
		]}
	/>

	<main class="page">
		<section class="head gutter">
			<div class="tags">
				<span class="badge">{node.kind === 'type' ? 'Type' : node.kind === 'subtopic' ? 'Subtopic' : 'Topic'}</span>
				{#if node.card}<span class="badge">card</span>{/if}
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
			<p class="section-label">
				<span class="ico"><Layers size={12} /></span> Subtopics · {plain.length}
			</p>
			<div class="tree group">
				{#each plain as child}
					<a class="branch" href={`/topic/${child.id}`}>
						<span class="rail" aria-hidden="true"></span>
						<span class="grow">
							<span class="branch-title">{child.title}</span>
							<span class="branch-def">{child.definition}</span>
						</span>
						<span class="chev"><ChevronRight size={16} /></span>
					</a>
				{/each}
			</div>
		{/if}

		{#if types.length}
			<p class="section-label">
				<span class="ico"><GitBranch size={12} /></span> Types · {types.length}
			</p>
			<div class="tree group">
				{#each types as child}
					<a class="branch" href={`/topic/${child.id}`}>
						<span class="rail" aria-hidden="true"></span>
						<span class="grow">
							<span class="branch-title">{child.title}</span>
							<span class="branch-def">{child.definition}</span>
						</span>
						<span class="chev"><ChevronRight size={16} /></span>
					</a>
				{/each}
			</div>
		{/if}

		{#if card}
			<p class="section-label"><span class="ico"><ListTree size={12} /></span> Study card</p>
			<div class="post-wrap">
				<Post
					card={card}
					{saved}
					index={0}
					total={1}
					read={$progress[node.id]?.seen ?? false}
					on:save={(e) => save(e.detail)}
					on:read={(e) => notify(e.detail ? 'Marked as read' : 'Mark removed')}
					on:ask={() => openAsk(node.id)}
				/>
			</div>
			<div class="gutter">
				<a
					class="btn btn--secondary btn--block feed-link"
					href={`/feed/${encodeURIComponent(data.code)}/${data.module.module}?card=${node.id}`}
				>
					Open in the feed
				</a>
			</div>
		{:else}
			<section class="gutter note">
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
			{$hydrated && $progress[node.id]?.seen
				? 'You marked this card as read.'
				: 'Reading this page does not mark anything. Use the button on the card when you have understood it.'}
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

	.tags {
		display: flex;
		gap: var(--sp-2);
	}

	.definition {
		font-size: var(--fs-def);
		font-weight: 600;
		line-height: 1.45;
		letter-spacing: -0.01em;
	}

	.parent {
		display: inline-flex;
		align-items: center;
		gap: 2px;
		font-size: var(--fs-small);
		color: var(--accent);
	}

	.section-label {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
	}

	.ico {
		display: inline-flex;
		color: var(--fg-subtle);
	}

	.branch {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		min-height: 56px;
		padding: var(--sp-2) var(--sp-4);
	}

	/* the visual "tree": a hairline rail down the left of every child row */
	.rail {
		width: 2px;
		align-self: stretch;
		background: var(--border);
		border-radius: var(--radius-full);
		flex: 0 0 auto;
		margin: var(--sp-1) 0;
	}

	.branch-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 600;
	}

	.branch-def {
		display: block;
		font-size: var(--fs-small);
		color: var(--fg-muted);
		line-height: 1.5;
		margin-top: 1px;
	}

	.chev {
		display: inline-flex;
		color: var(--fg-subtle);
		flex: 0 0 auto;
	}

	.post-wrap {
		margin: var(--sp-2) 0 0;
		border-top: 1px solid var(--border);
		border-bottom: 1px solid var(--border);
	}

	.feed-link {
		margin-top: var(--sp-3);
	}

	.note {
		padding-top: var(--sp-4);
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
</style>
