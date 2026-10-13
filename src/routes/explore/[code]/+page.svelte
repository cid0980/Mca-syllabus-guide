<script lang="ts">
	import { ChevronRight } from 'lucide-svelte';
	import type { PageData } from './$types';
	import { semesterLabel, plural } from '$lib/content';
	import { progress, percentSeenByIds } from '$lib/stores/progress';
	import { hydrated } from '$lib/stores/hydrate';
	import AppBar from '$lib/components/AppBar.svelte';
	import ProgressRing from '$lib/components/ProgressRing.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	export let data: PageData;

	/** topic id -> expanded */
	let open: Record<string, boolean> = {};

	function toggle(id: string) {
		open = { ...open, [id]: !open[id] };
	}

	function expandAll() {
		const next: Record<string, boolean> = {};
		for (const m of data.modules) for (const t of m.topics) next[t.id] = true;
		open = next;
	}

	function collapseAll() {
		open = {};
	}
</script>

<svelte:head><title>{data.found ? data.summary.subject : data.code} syllabus — StudyFeed</title></svelte:head>

<AppBar
	title={data.found ? data.summary.subject : data.code}
	subtitle={data.found ? `${data.code} · ${semesterLabel(data.summary.semester)}` : data.code}
	back="/explore"
/>

<main class="page page-in">
	{#if !data.found}
		<ErrorState
			title="Subject not found"
			message="This course code is not in the syllabus index."
			retryLabel="Back to syllabus"
			on:retry={() => history.back()}
		/>
	{:else}
		{@const summary = data.summary}
		<div class="gutter summary">
			<ProgressRing percent={$hydrated ? percentSeenByIds(summary.cardIds, $progress) : 0} size={52} stroke={4} />
			<dl class="facts">
				<div><dt>Modules</dt><dd class="nums">{summary.counts.modules}</dd></div>
				<div><dt>Topics</dt><dd class="nums">{summary.counts.topics}</dd></div>
				<div><dt>Subtopics</dt><dd class="nums">{summary.counts.subtopics}</dd></div>
				<div><dt>Cards</dt><dd class="nums">{summary.counts.cards}</dd></div>
			</dl>
		</div>

		<div class="gutter actions">
			<button class="btn btn--secondary btn--sm" on:click={expandAll}>Expand all</button>
			<button class="btn btn--secondary btn--sm" on:click={collapseAll}>Collapse all</button>
			<a class="btn btn--primary btn--sm" href={`/subject/${encodeURIComponent(data.code)}`}>Subject page</a>
		</div>

		{#each data.modules as module}
			<section>
				<p class="section-label">Module {module.module} · {plural(module.topics.length, 'topic')}</p>
				<div class="gutter module-head">
					<h2>{module.title}</h2>
					<span class="ring-wrap">
						<ProgressRing percent={$hydrated ? percentSeenByIds(module.cardIds, $progress) : 0} size={34} stroke={2.5} />
					</span>
				</div>

				<div class="group long-list">
					{#each module.topics as topic}
						<div class="topic">
							<button class="topic-head" aria-expanded={!!open[topic.id]} on:click={() => toggle(topic.id)}>
								<span class="chev" class:open={!!open[topic.id]}><ChevronRight size={18} /></span>
								<span class="grow">
									<span class="topic-title">{topic.title}</span>
									<span class="topic-def">{topic.definition}</span>
								</span>
								<span class="counts">
									{#if topic.hasCard}<span class="badge">card</span>{/if}
									{#if topic.children.length}<span class="badge nums">{topic.children.length}</span>{/if}
								</span>
							</button>

							{#if open[topic.id]}
								{@const plain = topic.children.filter((c) => c.kind !== 'type')}
								{@const types = topic.children.filter((c) => c.kind === 'type')}
								<div class="children">
									{#each plain as child}
										<a class="child" href={`/topic/${child.id}`}>
											<span class="rail" aria-hidden="true"></span>
											<span class="grow">
												<span class="child-title">{child.title}</span>
												<span class="child-def">{child.definition}</span>
											</span>
										</a>
									{/each}
									{#if types.length}
										<p class="child-group">Types</p>
										{#each types as child}
											<a class="child" href={`/topic/${child.id}`}>
												<span class="rail" aria-hidden="true"></span>
												<span class="grow">
													<span class="child-title">{child.title}</span>
													<span class="child-def">{child.definition}</span>
												</span>
											</a>
										{/each}
									{/if}
									<a class="open-topic" href={`/topic/${topic.id}`}>Open topic</a>
								</div>
							{/if}
						</div>
					{/each}
				</div>
			</section>
		{/each}
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
		flex-wrap: wrap;
	}

	.actions .btn {
		flex: 1;
		min-width: 92px;
	}

	.module-head {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: var(--sp-3);
		padding-bottom: var(--sp-2);
	}

	.module-head h2 {
		font-size: var(--fs-body);
		font-weight: 500;
		color: var(--fg-muted);
		line-height: 1.4;
	}

	.ring-wrap {
		display: inline-flex;
		flex: 0 0 auto;
	}

	.topic + .topic {
		border-top: 1px solid var(--border);
	}

	.topic-head {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-2);
		width: 100%;
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
	}

	.topic-head:hover {
		background: var(--fill);
	}

	.chev {
		display: inline-flex;
		color: var(--fg-subtle);
		flex: 0 0 auto;
		margin-top: 1px;
		transition: transform 0.16s ease-out;
	}

	.chev.open {
		transform: rotate(90deg);
	}

	.topic-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 500;
		line-height: 1.35;
	}

	.topic-def {
		display: block;
		font-size: var(--fs-small);
		color: var(--fg-muted);
		line-height: 1.45;
		margin-top: 2px;
	}

	.counts {
		display: flex;
		gap: var(--sp-1);
		flex: 0 0 auto;
	}

	.children {
		padding: 0 var(--sp-4) var(--sp-3) calc(var(--sp-4) + 18px + var(--sp-2));
		display: flex;
		flex-direction: column;
	}

	.child {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-2) 0;
		border-top: 1px solid var(--border);
		min-height: 48px;
	}

	.child:active {
		background: var(--fill);
	}

	/* hairline rail = the visual tree connection to the parent topic */
	.rail {
		width: 2px;
		align-self: stretch;
		background: var(--border);
		border-radius: var(--radius-full);
		flex: 0 0 auto;
		margin: var(--sp-1) 0;
	}

	.child-title {
		display: block;
		font-size: var(--fs-small);
		font-weight: 500;
	}

	.child-def {
		display: block;
		font-size: var(--fs-small);
		color: var(--fg-muted);
		line-height: 1.5;
		margin-top: 1px;
	}

	.child-group {
		font-size: var(--fs-caption);
		text-transform: uppercase;
		letter-spacing: 0.06em;
		color: var(--fg-subtle);
		padding-top: var(--sp-3);
	}

	.open-topic {
		font-size: var(--fs-small);
		color: var(--accent);
		padding-top: var(--sp-3);
	}
</style>
