<script lang="ts">
	import { Settings, ListTree, ChevronRight, BookOpen } from 'lucide-svelte';
	import { indexSubject, subjectsOfSemester, semesterLabel, totals, plural } from '$lib/content';
	import { progress, percentSeenByIds, streak } from '$lib/stores/progress';
	import { KEYS, readJSON } from '$lib/storage';
	import { hydrated } from '$lib/stores/hydrate';
	import ProgressRing from '$lib/components/ProgressRing.svelte';

	let semester = 1;
	let last: { code: string; module: string } | null = null;

	$: if ($hydrated) last = readJSON<{ code: string; module: string } | null>(KEYS.lastOpened, null);
	$: semesterSubjects = subjectsOfSemester(semester);

	function pct(ids: string[]): number {
		return $hydrated ? percentSeenByIds(ids, $progress) : 0;
	}
</script>

<svelte:head><title>StudyFeed</title></svelte:head>

<header class="appbar">
	<div class="inner">
		<img src="/logo.svg" alt="" width="24" height="24" />
		<h1 class="wordmark grow">StudyFeed</h1>
		{#if $hydrated && $streak.count > 0}
			<span class="streak nums">{$streak.count}d</span>
		{/if}
		<a class="icon-btn" href="/settings" aria-label="Settings"><Settings size={20} /></a>
	</div>
</header>

<main class="page">
	{#if last}
		{@const subject = indexSubject(last.code)}
		{#if subject}
			<a class="continue" href={`/feed/${encodeURIComponent(last.code)}/${last.module}`}>
				<ProgressRing percent={pct(subject.cardIds)} size={44} stroke={3} />
				<span class="grow">
					<span class="continue-label">Continue studying</span>
					<span class="continue-title truncate">{subject.subject}</span>
					<span class="continue-sub">Module {last.module} · {pct(subject.cardIds)}% seen</span>
				</span>
				<span class="chev"><ChevronRight size={18} /></span>
			</a>
		{/if}
	{/if}

	<div class="gutter seg-wrap">
		<div class="seg" role="group" aria-label="Semester">
			{#each [1, 2, 3] as s}
				<button aria-pressed={semester === s} on:click={() => (semester = s)}>{semesterLabel(s)}</button>
			{/each}
		</div>
	</div>

	<p class="section-label">{semesterLabel(semester)} subjects</p>
	<div class="group">
		{#each semesterSubjects as subject}
			<a class="subj pressable" href={`/subject/${encodeURIComponent(subject.code)}`}>
				<span class="avatar" aria-hidden="true">{subject.code.replace('CSCA ', '')}</span>
				<span class="grow">
					<span class="subj-title">{subject.subject}</span>
					<span class="subj-sub truncate">
						{plural(subject.counts.modules, 'module')} · {plural(subject.counts.topics, 'topic')} ·
						{plural(subject.counts.subtopics, 'subtopic')}
					</span>
					<span class="subj-meta nums">
						{subject.counts.cards ? `${subject.counts.cards} cards` : 'definitions ready'} · {pct(subject.cardIds)}% seen
					</span>
				</span>
				<ProgressRing percent={pct(subject.cardIds)} size={34} stroke={2.5} />
				<span class="chev"><ChevronRight size={18} /></span>
			</a>
		{/each}
	</div>

	<p class="section-label">Whole syllabus</p>
	<div class="group">
		<a class="subj pressable" href="/explore">
			<span class="avatar" aria-hidden="true"><ListTree size={18} /></span>
			<span class="grow">
				<span class="subj-title">Syllabus tree</span>
				<span class="subj-sub">
					{totals.subjects} subjects · {totals.topics} topics · {totals.subtopics + totals.types} subtopics and types
				</span>
				<span class="subj-meta">Browse subject, module, topic, subtopic, type</span>
			</span>
			<span class="chev"><ChevronRight size={18} /></span>
		</a>
		<a class="subj pressable" href="/feed/CSCA%20411/I">
			<span class="avatar" aria-hidden="true"><BookOpen size={18} /></span>
			<span class="grow">
				<span class="subj-title">Start the deck</span>
				<span class="subj-sub">Data Structures and Algorithms · Module I</span>
				<span class="subj-meta">{totals.cards} cards written so far</span>
			</span>
			<span class="chev"><ChevronRight size={18} /></span>
		</a>
	</div>
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
		height: var(--bar-h);
		max-width: 600px;
		margin: 0 auto;
		padding: 0 var(--sp-4);
	}

	.wordmark {
		font-size: var(--fs-title);
		font-weight: 700;
		letter-spacing: -0.02em;
	}

	.streak {
		font-size: var(--fs-small);
		font-weight: 700;
		color: var(--fg);
		background: var(--fill);
		border-radius: var(--radius-full);
		padding: 2px 10px;
	}

	.continue {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		margin: var(--sp-4);
		padding: var(--sp-3);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
		transition: background-color 0.12s ease, transform 0.12s ease;
	}

	.continue:active {
		background: var(--fill);
		transform: scale(0.99);
	}

	.continue-label {
		display: block;
		font-size: var(--fs-caption);
		font-weight: 700;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--accent);
	}

	.continue-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 700;
		margin-top: 1px;
	}

	.continue-sub {
		display: block;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.seg-wrap {
		padding-top: var(--sp-2);
	}

	.subj {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3) var(--sp-4);
	}

	.subj-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 600;
		line-height: 1.35;
	}

	.subj-sub {
		display: block;
		font-size: var(--fs-small);
		color: var(--fg-muted);
		margin-top: 1px;
	}

	.subj-meta {
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
