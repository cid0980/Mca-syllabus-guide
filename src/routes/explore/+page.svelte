<script lang="ts">
	import { Search, X, ChevronRight } from 'lucide-svelte';
	import { indexSubject, subjectsOfSemester, semesterLabel, totals, searchNodes, type SearchHit } from '$lib/content';
	import { progress, percentSeenByIds } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	let semester = 1;
	let query = '';
	let hits: SearchHit[] = [];
	let searching = false;
	let searchError: string | null = null;
	let debounce: ReturnType<typeof setTimeout>;

	$: semesterSubjects = subjectsOfSemester(semester);

	function runSearch() {
		const q = query.trim();
		if (q.length < 2) {
			hits = [];
			searching = false;
			searchError = null;
			return;
		}
		searching = true;
		searchError = null;
		searchNodes(q)
			.then((result) => (hits = result))
			.catch((err) => {
				searchError = err instanceof Error ? err.message : 'Search failed.';
			})
			.finally(() => (searching = false));
	}

	function onInput() {
		clearTimeout(debounce);
		searching = true;
		debounce = setTimeout(runSearch, 180);
	}

	function clearSearch() {
		query = '';
		hits = [];
		searching = false;
		searchError = null;
	}
</script>

<svelte:head><title>Syllabus — StudyFeed</title></svelte:head>

<AppBar
	title="Syllabus"
	subtitle={`${totals.subjects} subjects · ${totals.topics} topics · ${totals.subtopics + totals.types} subtopics`}
/>

<main class="page">
	<div class="gutter search-wrap">
		<label class="input">
			<span class="search-icon"><Search size={18} /></span>
			<input
				type="search"
				placeholder="Search topics, subtopics and types"
				bind:value={query}
				on:input={onInput}
				on:keydown={(e) => e.key === 'Enter' && runSearch()}
				aria-label="Search the syllabus"
			/>
			{#if query}
				<button class="icon-btn clear" on:click={clearSearch} aria-label="Clear search"><X size={16} /></button>
			{/if}
		</label>
	</div>

	{#if query.trim().length >= 2}
		{#if searching}
			<p class="section-label">Searching</p>
			<Skeleton variant="rows" count={5} />
		{:else if searchError}
			<ErrorState title="Search failed" message={searchError} on:retry={runSearch} />
		{:else if hits.length === 0}
			<p class="section-label">No matches</p>
			<p class="hint gutter">
				Nothing in the syllabus matches “{query.trim()}”. Try a shorter word, or open a subject
				below and read its module list.
			</p>
		{:else}
			<p class="section-label">{hits.length} matches</p>
			<div class="group long-list">
				{#each hits as hit}
					<a class="res pressable" href={`/topic/${hit.node.id}`}>
						<span class="grow">
							<span class="res-title">{hit.node.title}</span>
							<span class="res-def truncate">{hit.node.definition}</span>
							<span class="res-meta nums">
								{hit.tree.code} · Module {hit.module.module}{hit.parent ? ` · ${hit.parent.title}` : ''}
							</span>
						</span>
						<span class="chev"><ChevronRight size={18} /></span>
					</a>
				{/each}
			</div>
		{/if}
	{:else}
		<div class="gutter seg-wrap">
			<div class="seg" role="group" aria-label="Semester">
				{#each [1, 2, 3] as s}
					<button aria-pressed={semester === s} on:click={() => (semester = s)}>{semesterLabel(s)}</button>
				{/each}
			</div>
		</div>

		<p class="section-label">{semesterLabel(semester)}</p>
		<div class="grid gutter">
			{#each semesterSubjects as subject}
				{@const pct = $hydrated ? percentSeenByIds(subject.cardIds, $progress) : 0}
				<a class="tile" href={`/explore/${encodeURIComponent(subject.code)}`}>
					<span class="tile-top">
						<span class="ring" class:accent={subject.counts.cards > 0 && pct < 100}>
							<span class="avatar nums">{subject.code.replace('CSCA ', '')}</span>
						</span>
						{#if subject.counts.cards}
							<span class="badge nums">{pct}%</span>
						{:else}
							<span class="badge">defs</span>
						{/if}
					</span>
					<span class="tile-name">{subject.subject}</span>
					<span class="tile-meta nums">
						{subject.counts.modules} modules · {subject.counts.topics} topics ·
						{subject.counts.subtopics} subtopics
					</span>
				</a>
			{/each}
		</div>
		<p class="footnote">
			Tap a subject to open its modules, then any topic to read its subtopics and types — every entry
			has its own definition.
		</p>
	{/if}
</main>

<style>
	.search-wrap {
		padding-top: var(--sp-3);
	}

	.search-icon {
		display: inline-flex;
		color: var(--fg-subtle);
		flex: 0 0 auto;
	}

	.clear {
		width: 28px;
		height: 28px;
		flex: 0 0 auto;
	}

	.seg-wrap {
		padding-top: var(--sp-3);
	}

	.hint {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
		padding-top: var(--sp-1);
	}

	/* ---------- subject grid ---------- */

	.grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--sp-2);
	}

	.tile {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
		padding: var(--sp-3);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
		transition: background-color 0.12s ease, transform 0.12s ease;
	}

	.tile:active {
		background: var(--fill);
		transform: scale(0.985);
	}

	.tile-top {
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.ring {
		display: grid;
		place-items: center;
		width: 42px;
		height: 42px;
		border-radius: var(--radius-full);
		padding: 2px;
		border: 2px solid var(--border);
	}

	.ring.accent {
		border-color: var(--accent);
	}

	.ring .avatar {
		width: 100%;
		height: 100%;
	}

	.tile-name {
		font-size: var(--fs-small);
		font-weight: 600;
		line-height: 1.35;
	}

	.tile-meta {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		line-height: 1.45;
	}

	/* ---------- search results ---------- */

	.res {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		min-height: 56px;
		padding: var(--sp-2) var(--sp-4);
	}

	.res-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 600;
	}

	.res-def {
		display: block;
		font-size: var(--fs-small);
		color: var(--fg-muted);
		margin-top: 1px;
	}

	.res-meta {
		display: block;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		margin-top: 2px;
	}

	.chev {
		display: inline-flex;
		color: var(--fg-subtle);
		flex: 0 0 auto;
	}
</style>
