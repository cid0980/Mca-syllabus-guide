<script lang="ts">
	import { subjects, totals, plural } from '$lib/content';
	import { progress, streak, accuracyByIds, percentSeenByIds, seenCountByIds } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import ProgressRing from '$lib/components/ProgressRing.svelte';
	import ListRow from '$lib/components/ListRow.svelte';
	import Notice from '$lib/components/Notice.svelte';
	import { Flame, Target, BookOpen } from 'lucide-svelte';

	$: allCardIds = subjects.flatMap((s) => s.cardIds);
	$: overallSeen = seenCountByIds(allCardIds, $progress);
	$: overallRead = subjects.reduce((n, s) => n + s.counts.subtopics, 0);
	$: overallAccuracy = accuracyByIds(allCardIds, $progress);
	$: activeSubjects = subjects.filter((s) => s.counts.cards > 0);

</script>

<svelte:head><title>Progress — StudyFeed</title></svelte:head>

<AppBar title="Progress" subtitle={`${totals.topics} topics · ${totals.subtopics + totals.types} subtopics in the library`} />

<main class="page">
	<section class="gutter tiles">
		<div class="tile">
			<ProgressRing percent={$hydrated && allCardIds.length ? Math.round((overallSeen / allCardIds.length) * 100) : 0} size={52} stroke={4} />
			<div>
				<p class="tile-value nums">{overallSeen}/{allCardIds.length}</p>
				<p class="tile-label">cards seen</p>
			</div>
		</div>
		<div class="tile">
			<span class="tile-icon"><Target size={20} /></span>
			<div>
				<p class="tile-value nums">{overallAccuracy.answered ? `${overallAccuracy.percent}%` : '—'}</p>
				<p class="tile-label">quiz accuracy</p>
			</div>
		</div>
		<div class="tile">
			<span class="tile-icon"><Flame size={20} /></span>
			<div>
				<p class="tile-value nums">{streakLabel($streak.count)}</p>
				<p class="tile-label">day streak</p>
			</div>
		</div>
		<div class="tile">
			<span class="tile-icon"><BookOpen size={20} /></span>
			<div>
				<p class="tile-value nums">{overallRead}</p>
				<p class="tile-label">subtopics mapped</p>
			</div>
		</div>
	</section>

	{#if $hydrated && overallSeen === 0}
		<Notice
			tone="accent"
			title="No studying recorded yet"
			text={`Cards you swipe through are counted here. ${plural(allCardIds.length, 'card')} are ready — opening a deck takes about two minutes.`}
		>
			<a class="btn btn--primary btn--sm" href="/feed/CSCA%20411/I">Start the first deck</a>
		</Notice>
	{/if}

	<p class="section-label">By subject</p>
	<div class="group">
		{#each subjects as subject}
			<ListRow
				href={`/subject/${encodeURIComponent(subject.code)}`}
				title={subject.subject}
				subtitle={subject.counts.cards
					? `${seenCountByIds(subject.cardIds, $progress)} of ${subject.counts.cards} cards seen · ${accuracyByIds(subject.cardIds, $progress).answered ? `${accuracyByIds(subject.cardIds, $progress).percent}% accuracy` : 'no quiz attempts yet'}`
					: `${subject.counts.topics} topics mapped · cards pending`}
				value={subject.counts.cards
					? `${$hydrated ? percentSeenByIds(subject.cardIds, $progress) : 0}%`
					: `${subject.counts.topics}`}
				chevron
			>
				<span slot="lead" class="course nums">{subject.code.replace('CSCA ', '')}</span>
			</ListRow>
		{/each}
	</div>

	<p class="section-label">Modules with cards</p>
	<div class="group">
		{#each activeSubjects as subject}
			{#each subject.modules.filter((m) => m.cards > 0) as module}
				<ListRow
					href={`/feed/${encodeURIComponent(subject.code)}/${module.module}`}
					title={`${subject.code} · Module ${module.module}`}
					subtitle={module.title}
					value={`${percentSeenByIds(module.cardIds, $progress)}%`}
					lines={2}
					chevron
				/>
			{/each}
		{/each}
	</div>

	<p class="footnote">
		Everything on this screen is computed from this browser's local storage — no account, no server.
	</p>
</main>

<style>
	.tiles {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--sp-2);
		padding-top: var(--sp-4);
	}

	.tile {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3);
		background: var(--bg-subtle);
		border: 1px solid var(--border);
		border-radius: var(--radius);
	}

	.tile-icon {
		display: grid;
		place-items: center;
		width: 40px;
		height: 40px;
		border-radius: var(--radius-full);
		background: var(--fill);
		color: var(--fg-muted);
		flex: 0 0 auto;
	}

	.tile-value {
		font-size: var(--fs-title);
		font-weight: 600;
	}

	.tile-label {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.course {
		display: grid;
		place-items: center;
		width: 36px;
		height: 36px;
		border-radius: var(--radius-full);
		background: var(--fill);
		color: var(--fg-muted);
		font-size: var(--fs-caption);
		font-weight: 600;
	}

	.footnote {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		padding: var(--sp-6) var(--sp-4) 0;
	}
</style>

<script lang="ts" context="module">
	export function streakLabel(count: number): string {
		return count === 1 ? '1 day' : `${count} days`;
	}
</script>
