<script lang="ts">
	import { Settings } from 'lucide-svelte';
	import { indexSubject, subjectsOfSemester, semesterLabel, totals, plural } from '$lib/content';
	import { progress, percentSeenByIds, streak } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import { KEYS, readJSON } from '$lib/storage';
	import { browser } from '$app/environment';
	import ListRow from '$lib/components/ListRow.svelte';
	import ProgressRing from '$lib/components/ProgressRing.svelte';

	let semester = 1;
	let last: { code: string; module: string } | null = null;

	$: if ($hydrated) last = readJSON<{ code: string; module: string } | null>(KEYS.lastOpened, null);
	$: semesterSubjects = subjectsOfSemester(semester);
	$: libraryCards = totals.cards;

	function pctFor(cardIds: string[]): number {
		return percentSeenByIds(cardIds, $progress);
	}
</script>

<svelte:head><title>StudyFeed</title></svelte:head>

<header class="appbar">
	<div class="inner">
		<img src="/logo.svg" alt="" width="26" height="26" />
		<div class="grow">
			<h1>StudyFeed</h1>
			<p class="sub">MCA · Pondicherry University</p>
		</div>
		{#if $hydrated && $streak.count > 0}
			<span class="streak nums" title="Day streak">
				{$streak.count}
				<span class="streak-label">{$streak.count === 1 ? 'day' : 'days'}</span>
			</span>
		{/if}
		<a class="icon-btn" href="/settings" aria-label="Settings"><Settings size={20} /></a>
	</div>
</header>

<main class="page">
	{#if last}
		{@const subject = indexSubject(last.code)}
		{#if subject}
			<div class="gutter resume">
				<a class="resume-card" href={`/feed/${encodeURIComponent(last.code)}/${last.module}`}>
					<ProgressRing percent={$hydrated ? pctFor(subject.cardIds) : 0} size={40} stroke={3} />
					<span class="grow">
						<span class="resume-label">Continue</span>
						<span class="resume-title truncate">{subject.subject} · Module {last.module}</span>
					</span>
				</a>
			</div>
		{/if}
	{/if}

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
				href={`/subject/${encodeURIComponent(subject.code)}`}
				title={subject.subject}
				subtitle={`${plural(subject.counts.topics, 'topic')} · ${plural(
					subject.counts.subtopics,
					'subtopic'
				)} · ${plural(subject.counts.cards, 'card')}`}
				chevron
			>
				<span slot="lead" class="course">
					<span class="course-code nums">{subject.code.replace('CSCA ', '')}</span>
				</span>
				<span slot="trail">
					<ProgressRing percent={$hydrated ? pctFor(subject.cardIds) : 0} size={34} stroke={2.5} />
				</span>
			</ListRow>
		{/each}
	</div>

	<a class="link-row gutter" href="/explore">
		Browse all subjects and modules
	</a>

	<p class="section-label">Library</p>
	<div class="group">
		<div class="stats">
			<div><strong class="nums">{totals.topics}</strong><span>topics</span></div>
			<div><strong class="nums">{totals.subtopics + totals.types}</strong><span>subtopics</span></div>
			<div><strong class="nums">{libraryCards}</strong><span>cards</span></div>
			<div><strong class="nums">{$hydrated ? pctFor(subjectsOfSemester(1).flatMap((s) => s.cardIds)) : 0}%</strong><span>seen</span></div>
		</div>
	</div>

	<p class="footnote">
		Definitions for every syllabus entry are stored in the app and work offline. Cards marked
		<em>draft</em> are your own study material — check them against the textbook and mark them verified.
	</p>
</main>

<style>
	.appbar {
		position: sticky;
		top: 0;
		z-index: 30;
		background: var(--bg);
		border-bottom: 1px solid var(--border);
		padding-top: env(safe-area-inset-top);
	}

	.inner {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		min-height: var(--bar-h);
		max-width: 600px;
		margin: 0 auto;
		padding: 0 var(--sp-4);
	}

	h1 {
		font-size: var(--fs-title);
		font-weight: 600;
		letter-spacing: -0.01em;
	}

	.sub {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.streak {
		font-size: var(--fs-small);
		font-weight: 500;
		color: var(--fg-muted);
		display: inline-flex;
		align-items: baseline;
		gap: 3px;
	}

	.streak-label {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.resume {
		padding-top: var(--sp-4);
	}

	.resume-card {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		border: 1px solid var(--border);
		border-radius: var(--radius);
	}

	.resume-card:active {
		background: var(--bg-hover);
	}

	.resume-label {
		display: block;
		font-size: var(--fs-caption);
		text-transform: uppercase;
		letter-spacing: 0.06em;
		color: var(--fg-subtle);
	}

	.resume-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 500;
		margin-top: 1px;
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

	.link-row {
		display: block;
		padding-top: var(--sp-3);
		padding-bottom: var(--sp-1);
		font-size: var(--fs-small);
		color: var(--accent);
	}

	.stats {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: var(--sp-2);
		padding: var(--sp-4);
	}

	.stats div {
		display: flex;
		flex-direction: column;
		gap: 2px;
	}

	.stats strong {
		font-size: var(--fs-title);
		font-weight: 600;
	}

	.stats span {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.footnote {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		padding: var(--sp-6) var(--sp-4) 0;
	}

	.footnote em {
		font-style: normal;
		color: var(--fg-muted);
	}
</style>
