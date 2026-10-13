<script lang="ts">
	/** Sticky page header. Solid background, hairline bottom border, no blur. */
	import { ChevronLeft } from 'lucide-svelte';

	export let title = '';
	export let subtitle = '';
	export let back: string | null = null;
	export let onBack: (() => void) | null = null;
	export let crumbs: { label: string; href: string }[] = [];
</script>

<header class="bar">
	<div class="inner">
		{#if back || onBack}
			<svelte:element
				this={onBack ? 'button' : 'a'}
				class="icon-btn back"
				href={back ?? undefined}
				role={onBack ? 'button' : undefined}
				aria-label="Go back"
				on:click={onBack ?? undefined}
			>
				<ChevronLeft size={22} />
			</svelte:element>
		{/if}
		<div class="titles">
			<h1 class="title truncate">{title}</h1>
			{#if subtitle}<p class="subtitle truncate">{subtitle}</p>{/if}
		</div>
		<div class="actions">
			<slot name="actions" />
		</div>
	</div>
	{#if crumbs.length}
		<nav class="crumbs" aria-label="Breadcrumb">
			{#each crumbs as c, i}
				{#if i > 0}<span class="sep" aria-hidden="true">/</span>{/if}
				<a href={c.href}>{c.label}</a>
			{/each}
		</nav>
	{/if}
</header>

<style>
	.bar {
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
		gap: var(--sp-2);
		min-height: var(--bar-h);
		max-width: 600px;
		margin: 0 auto;
		padding: 0 var(--sp-3);
	}

	.back {
		margin-left: calc(var(--sp-2) * -1);
	}

	.titles {
		flex: 1;
		min-width: 0;
		padding-right: var(--sp-2);
	}

	.title {
		font-size: var(--fs-title);
		font-weight: 600;
		letter-spacing: -0.01em;
	}

	.subtitle {
		font-size: var(--fs-small);
		color: var(--fg-muted);
		margin-top: 1px;
	}

	.actions {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
	}

	.crumbs {
		max-width: 600px;
		margin: 0 auto;
		padding: 0 var(--sp-4) var(--sp-2);
		display: flex;
		gap: var(--sp-2);
		overflow-x: auto;
		scrollbar-width: none;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		white-space: nowrap;
	}

	.crumbs::-webkit-scrollbar {
		display: none;
	}

	.crumbs a {
		color: var(--fg-subtle);
	}

	.crumbs a:last-child {
		color: var(--fg-muted);
	}

	.sep {
		opacity: 0.6;
	}
</style>
