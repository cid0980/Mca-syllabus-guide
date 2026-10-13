<script lang="ts">
	import { Search, X } from 'lucide-svelte';
	import { totals, subjectsOfSemester, semesterLabel, searchNodes, type SearchHit } from '$lib/content';
	import { progress, percentSeenByIds } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import ListRow from '$lib/components/ListRow.svelte';
	import ProgressRing from '$lib/components/ProgressRing.svelte';
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

<AppBar title="Syllabus" subtitle={`${totals.subjects} subjects · ${totals.topics} topics · ${totals.subtopics + totals.types} subtopics`} />

<main class="page">
	<div class="gutter search-wrap">
		<label class="input">
			<span class="search-icon"><Search size={18} /></span>
			<input
				type="search"
				placeholder="Search topics and subtopics"
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
				Nothing in the syllabus matches “{query.trim()}”. Try a shorter word, or open the subject
				below and read its module list.
			</p>
		{:else}
			<p class="section-label">{hits.length} matches</p>
			<div class="group long-list">
				{#each hits as hit}
					<ListRow
						href={`/topic/${hit.node.id}`}
						title={hit.node.title}
						subtitle={hit.node.definition}
						meta={`${hit.tree.code} · ${hit.module.module}${hit.parent ? ' · ' + hit.parent.title : ''}`}
					/>
				{/each}
			</div>
		{/if}
	{:else}
		<div class="gutter">
			<div class="seg" role="group" aria-label="Semester">
				{#each [1, 2, 3] as s}
					<button aria-pressed={semester === s} on:click={() => (semester = s)}>{semesterLabel(s)}</button>
				{/each}
			</div>
		</div>

		<p class="section-label">{semesterLabel(semester)}</p>
		<div class="group">
			{#each semesterSubjects as subject}
				<ListRow
					href={`/explore/${encodeURIComponent(subject.code)}`}
					title={subject.subject}
					subtitle={`${subject.counts.modules} modules · ${subject.counts.topics} topics · ${subject.counts.subtopics} subtopics`}
					meta={subject.counts.cards
						? `${subject.counts.cards} study cards ready`
						: 'syllabus mapped · cards pending'}
					chevron
				>
					<span slot="lead" class="course"><span class="nums">{subject.code.replace('CSCA ', '')}</span></span>
					<span slot="trail">
						<ProgressRing percent={$hydrated ? percentSeenByIds(subject.cardIds, $progress) : 0} size={34} stroke={2.5} />
					</span>
				</ListRow>
			{/each}
		</div>
	{/if}
</main>

<style>
	.search-wrap {
		padding-top: var(--sp-3);
	}

	.search-icon {
		color: var(--fg-subtle);
		flex: 0 0 auto;
	}

	.clear {
		width: 28px;
		height: 28px;
		flex: 0 0 auto;
	}

	.hint {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
		padding-top: var(--sp-1);
	}

	.course {
		display: grid;
		place-items: center;
		width: 36px;
		height: 36px;
		border-radius: var(--radius-full);
		background: var(--bg-element);
		color: var(--fg-muted);
		font-size: var(--fs-caption);
		font-weight: 600;
	}
</style>
