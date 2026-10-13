<script lang="ts">
	import type { PageData } from './$types';
	import { semesterLabel, plural } from '$lib/content';
	import { progress, percentSeenByIds, accuracyByIds } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import ListRow from '$lib/components/ListRow.svelte';
	import ProgressRing from '$lib/components/ProgressRing.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	export let data: PageData;
</script>

<svelte:head><title>{data.found ? data.summary.subject : data.code} — StudyFeed</title></svelte:head>

<AppBar
	title={data.found ? data.summary.subject : data.code}
	subtitle={data.found ? `${data.code} · ${semesterLabel(data.summary.semester)}` : data.code}
	back="/"
/>

<main class="page">
	{#if !data.found}
		<ErrorState
			title="Subject not found"
			message="This subject is not in the syllabus index."
			retryLabel="Home"
			on:retry={() => (location.href = '/')}
		/>
	{:else}
		{@const summary = data.summary}
		{@const accuracy = accuracyByIds(summary.cardIds, $progress)}
		<section class="gutter summary">
			<ProgressRing percent={$hydrated ? percentSeenByIds(summary.cardIds, $progress) : 0} size={56} stroke={4} />
			<dl class="facts">
				<div><dt>Topics</dt><dd class="nums">{summary.counts.topics}</dd></div>
				<div><dt>Subtopics</dt><dd class="nums">{summary.counts.subtopics}</dd></div>
				<div><dt>Cards</dt><dd class="nums">{summary.counts.cards}</dd></div>
				<div><dt>Quiz</dt><dd class="nums">{$hydrated && accuracy.answered ? `${accuracy.percent}%` : '—'}</dd></div>
			</dl>
		</section>

		{#if summary.counts.cards}
			<div class="gutter actions">
				<a class="btn btn--primary" href={`/feed/${encodeURIComponent(data.code)}/I`}>Start studying</a>
				<a class="btn btn--secondary" href={`/explore/${encodeURIComponent(data.code)}`}>Syllabus</a>
			</div>
		{:else}
			<div class="gutter actions">
				<a class="btn btn--primary" href={`/explore/${encodeURIComponent(data.code)}`}>Read the syllabus</a>
			</div>
			<aside class="gutter notice">
				<p class="notice-title">Definitions ready, cards pending</p>
				<p class="notice-text">
					Every topic and subtopic of {data.code} is stored with its own definition and is readable
					now. Swipe cards with examples, quizzes and exam tips are generated in build step 5.
				</p>
			</aside>
		{/if}

		<p class="section-label">Modules</p>
		<div class="group">
			{#each data.rows as row}
				<ListRow
					href={row.cardIds.length
						? `/feed/${encodeURIComponent(data.code)}/${row.module}`
						: `/explore/${encodeURIComponent(data.code)}#M${row.module}`}
					title={row.title}
					subtitle={`${plural(row.topics, 'topic')} · ${plural(row.subtopics, 'subtopic')} · ${plural(row.cardIds.length, 'card')}`}
					meta={row.cardIds.length ? `${row.cardIds.length} cards ready` : 'definitions ready'}
					chevron
				>
					<span slot="lead" class="module-no nums">{row.module}</span>
					<span slot="trail">
						{#if row.cardIds.length}
							<ProgressRing percent={$hydrated ? percentSeenByIds(row.cardIds, $progress) : 0} size={34} stroke={2.5} />
						{/if}
					</span>
				</ListRow>
			{/each}
		</div>
	{/if}
</main>

<style>
	.summary {
		display: flex;
		align-items: center;
		gap: var(--sp-4);
		padding-top: var(--sp-4);
	}

	.facts {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--sp-2) var(--sp-4);
		margin: 0;
		flex: 1;
	}

	.facts div {
		display: flex;
		align-items: baseline;
		justify-content: space-between;
		gap: var(--sp-2);
	}

	dt {
		font-size: var(--fs-small);
		color: var(--fg-muted);
	}

	dd {
		margin: 0;
		font-size: var(--fs-body);
		font-weight: 500;
	}

	.actions {
		display: flex;
		gap: var(--sp-2);
		padding-top: var(--sp-4);
	}

	.actions .btn {
		flex: 1;
	}

	.notice {
		padding-top: var(--sp-4);
	}

	.notice-title {
		font-size: var(--fs-caption);
		text-transform: uppercase;
		letter-spacing: 0.06em;
		color: var(--accent);
		margin-bottom: var(--sp-2);
	}

	.notice-text {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.module-no {
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
