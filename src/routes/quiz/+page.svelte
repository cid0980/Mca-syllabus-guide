<script lang="ts">
	import { ListChecks, Play, Shuffle } from 'lucide-svelte';
	import { subjects, cardsOfModule, loadTree } from '$lib/content';
	import AppBar from '$lib/components/AppBar.svelte';
	import ListRow from '$lib/components/ListRow.svelte';
	import Notice from '$lib/components/Notice.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	/** Quiz needs card counts per module, so load every tree once (cached after). */
	let treesPromise = Promise.all(subjects.map((s) => loadTree(s.code).then((t) => ({ code: s.code, tree: t }))));

	$: quizSubjectsPromise = treesPromise.then((entries) =>
		entries
			.map(({ code, tree }) => ({
				code,
				subject: tree.subject,
				modules: tree.modules
					.map((m) => ({ module: m.module, title: m.title, cards: cardsOfModule(tree, m.module).length }))
					.filter((m) => m.cards > 0)
			}))
			.filter((s) => s.modules.length > 0)
	);
</script>

<svelte:head><title>Quiz — StudyFeed</title></svelte:head>

<AppBar title="Quiz" subtitle="Questions come from the saved cards" />

<main class="page">
	<Notice
		tone="accent"
		title="Quiz mode is build step 4"
		text="Question banks, scoring and the wrong-answer review list are built on the cards you already have. The decks below are ready to be quizzed."
	/>
	{#await quizSubjectsPromise}
		<p class="section-label">Loading decks</p>
		<Skeleton variant="rows" count={4} />
	{:then list}
		{#each list as subject}
			<p class="section-label">{subject.subject}</p>
			<div class="group">
				{#each subject.modules as module}
					<ListRow
						href={`/feed/${encodeURIComponent(subject.code)}/${module.module}`}
						title={`Module ${module.module} — ${module.title}`}
						subtitle={`${module.cards} question cards available`}
						chevron
					>
						<span slot="lead" class="mod nums">{module.module}</span>
					</ListRow>
				{/each}
			</div>
		{/each}
	{:catch error}
		<ErrorState
			title="Could not load the question bank"
			message={error.message}
			on:retry={() => (treesPromise = Promise.all(subjects.map((s) => loadTree(s.code).then((t) => ({ code: s.code, tree: t })))))}
		/>
	{/await}

	<section class="gutter actions">
		<a class="btn btn--secondary" href="/feed/CSCA%20411/I"><Shuffle size={16} /> Practice in the feed</a>
		<a class="btn btn--primary" href="/feed/CSCA%20411/I"><Play size={16} /> Start with DSA Module I</a>
	</section>
</main>

<style>
	.mod {
		display: grid;
		place-items: center;
		width: 34px;
		height: 34px;
		border-radius: var(--radius-full);
		background: var(--fill);
		color: var(--fg-muted);
		font-size: var(--fs-caption);
		font-weight: 600;
	}

	.actions {
		display: flex;
		gap: var(--sp-2);
		padding-top: var(--sp-6);
	}

	.actions .btn {
		flex: 1;
		min-width: 0;
		font-size: var(--fs-small);
	}
</style>
