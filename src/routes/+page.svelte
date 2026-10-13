<script lang="ts">
	import { Settings, ListTree, ChevronRight, BookOpen, Flame } from 'lucide-svelte';
	import { indexSubject, subjectsOfSemester, semesterLabel, totals, plural } from '$lib/content';
	import { shortName } from '$lib/labels';
	import { progress, percentSeenByIds, streak } from '$lib/stores/progress';
	import { KEYS, readJSON } from '$lib/storage';
	import { hydrated } from '$lib/stores/hydrate';

	let semester = 1;
	let last: { code: string; module: string } | null = null;

	$: if ($hydrated) last = readJSON<{ code: string; module: string } | null>(KEYS.lastOpened, null);
	$: semesterSubjects = subjectsOfSemester(semester);

	/** The deck the "Study the first deck" button links to. */
	const FIRST_DECK = { code: 'CSCA 411', module: 'I' };

	/**
	 * Card count for ONE module, straight from index.json.
	 * Never use the subject total here: CSCA 411 has 51 cards across five modules,
	 * Module I alone has 10.
	 */
	function cardsIn(code: string, module: string): number {
		return indexSubject(code)?.modules.find((m) => m.module === module)?.cards ?? 0;
	}

	/** story ring state — like an unwatched / watched story */
	function ringState(cards: number, pct: number): 'accent' | 'muted' | 'done' {
		if (cards === 0) return 'muted';
		return pct >= 100 ? 'done' : 'accent';
	}
</script>

<svelte:head><title>StudyFeed</title></svelte:head>

<header class="appbar">
	<div class="inner">
		<img src="/logo.svg" alt="" width="24" height="24" />
		<h1 class="wordmark grow">StudyFeed</h1>
		{#if $hydrated && $streak.count > 0}
			<!-- the pill counts consecutive study days (sf:streak), so the flame sits inside it -->
			<span
				class="streak"
				role="img"
				title="Daily study streak"
				aria-label={`${$streak.count}-day study streak`}
			>
				<Flame size={14} aria-hidden="true" />
				<span class="nums" aria-hidden="true">{$streak.count}d</span>
			</span>
		{/if}
		<a class="icon-btn" href="/settings" aria-label="Settings"><Settings size={20} /></a>
	</div>
</header>

<main class="page">
	<!-- subject "stories": a coloured ring means there is something to study -->
	<div class="stories">
		{#each semesterSubjects as subject}
			{@const pct = $hydrated ? percentSeenByIds(subject.cardIds, $progress) : 0}
			{@const state = ringState(subject.counts.cards, pct)}
			<a class="story pressable" href={`/subject/${encodeURIComponent(subject.code)}`}>
				<span class="ring" class:accent={state === 'accent'} class:done={state === 'done'}>
					<span class="avatar nums">{subject.code.replace('CSCA ', '')}</span>
				</span>
				<span class="story-label" title={subject.subject}>{shortName(subject.code)}</span>
			</a>
		{/each}
		<a class="story pressable" href="/explore">
			<span class="ring muted">
				<span class="avatar"><ListTree size={18} /></span>
			</span>
			<span class="story-label">All</span>
		</a>
	</div>

	{#if last}
		{@const subject = indexSubject(last.code)}
		{#if subject}
			{@const pct = $hydrated ? percentSeenByIds(subject.cardIds, $progress) : 0}
			<a class="continue" href={`/feed/${encodeURIComponent(last.code)}/${last.module}`}>
				<span class="continue-ring">
					<svg viewBox="0 0 40 40" width="44" height="44" aria-hidden="true">
						<circle cx="20" cy="20" r="18" fill="none" stroke="var(--fill)" stroke-width="3" />
						{#if pct > 0}
							<circle
								cx="20"
								cy="20"
								r="18"
								fill="none"
								stroke="var(--accent)"
								stroke-width="3"
								stroke-linecap="round"
								stroke-dasharray={2 * Math.PI * 18}
								stroke-dashoffset={2 * Math.PI * 18 * (1 - pct / 100)}
								transform="rotate(-90 20 20)"
							/>
						{/if}
					</svg>
					<span class="continue-pct nums">{pct}%</span>
				</span>
				<span class="grow">
					<span class="continue-label">Continue studying</span>
					<span class="continue-title truncate">{subject.subject}</span>
					<span class="continue-sub">Module {last.module} · {plural(cardsIn(last.code, last.module), 'card')}</span>
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
			{@const pct = $hydrated ? percentSeenByIds(subject.cardIds, $progress) : 0}
			<a class="subj pressable" href={`/subject/${encodeURIComponent(subject.code)}`}>
				<span class="avatar" aria-hidden="true">{subject.code.replace('CSCA ', '')}</span>
				<span class="grow">
					<span class="subj-head">
						<span class="subj-title">{subject.subject}</span>
						{#if subject.counts.cards === 0}
							<span class="badge">Syllabus only</span>
						{/if}
					</span>
					<span class="subj-sub truncate">
						{plural(subject.counts.topics, 'topic')} · {plural(subject.counts.subtopics, 'subtopic')}
					</span>
					<span class="subj-meta nums">
						{subject.counts.cards ? `${subject.counts.cards} cards · ${pct}% seen` : 'definitions ready · cards pending'}
					</span>
				</span>
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
					{totals.subjects} subjects · {totals.topics} topics
				</span>
				<span class="subj-meta nums">{totals.subtopics + totals.types} subtopics and types, each defined</span>
			</span>
			<span class="chev"><ChevronRight size={18} /></span>
		</a>
		<a class="subj pressable" href={`/feed/${encodeURIComponent(FIRST_DECK.code)}/${FIRST_DECK.module}`}>
			<span class="avatar" aria-hidden="true"><BookOpen size={18} /></span>
			<span class="grow">
				<span class="subj-title">Study the first deck</span>
				<span class="subj-sub">
					{indexSubject(FIRST_DECK.code)?.subject ?? FIRST_DECK.code} · Module {FIRST_DECK.module}
				</span>
				<span class="subj-meta nums">
					{plural(cardsIn(FIRST_DECK.code, FIRST_DECK.module), 'card')} written
				</span>
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
		letter-spacing: -0.03em;
	}

	.streak {
		display: inline-flex;
		align-items: center;
		gap: var(--sp-1);
		height: 24px;
		padding: 0 var(--sp-2) 0 6px;
		background: var(--fill);
		border-radius: var(--radius-full);
		font-size: var(--fs-small);
		font-weight: 700;
		color: var(--fg-muted);
		flex: 0 0 auto;
	}

	/* ---------- story row ---------- */

	.stories {
		display: flex;
		gap: var(--sp-4);
		overflow-x: auto;
		scrollbar-width: none;
		padding: var(--sp-3) var(--sp-4) var(--sp-2);
	}

	.stories::-webkit-scrollbar {
		display: none;
	}

	.story {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: var(--sp-1);
		width: 64px;
		flex: 0 0 auto;
		border-radius: var(--radius);
	}

	.ring {
		display: grid;
		place-items: center;
		width: 60px;
		height: 60px;
		border-radius: var(--radius-full);
		padding: 2px;
		border: 2px solid var(--border);
		transition: border-color 0.12s ease;
	}

	/* unwatched = coloured ring, finished or empty = grey, exactly like a story ring */
	.ring.accent {
		border-color: var(--accent);
	}

	.ring.done,
	.ring.muted {
		border-color: var(--border);
	}

	.ring .avatar {
		width: 100%;
		height: 100%;
		font-size: var(--fs-small);
	}

	.story-label {
		font-size: var(--fs-caption);
		color: var(--fg-muted);
		max-width: 64px;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	/* ---------- continue ---------- */

	.continue {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		margin: 0 var(--sp-4) var(--sp-2);
		padding: var(--sp-3);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
		transition: background-color 0.12s ease, transform 0.12s ease;
	}

	.continue:active {
		background: var(--fill);
		transform: scale(0.99);
	}

	.continue-ring {
		position: relative;
		display: grid;
		place-items: center;
		flex: 0 0 auto;
	}

	.continue-ring > * {
		grid-area: 1 / 1;
	}

	.continue-pct {
		font-size: var(--fs-caption);
		font-weight: 700;
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

	/* ---------- subject rows ---------- */

	.subj {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3) var(--sp-4);
	}

	.subj-head {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		gap: var(--sp-2);
	}

	.subj-title {
		font-size: var(--fs-body);
		font-weight: 600;
		line-height: 1.35;
		min-width: 0;
	}

	.subj-head .badge {
		flex: 0 0 auto;
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
