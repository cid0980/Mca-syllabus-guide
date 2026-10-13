<script lang="ts">
	/**
	 * One row of a group. Full-bleed on the outside, text aligned to the 16px gutter.
	 * min-height 56px for two lines, 48px for one — both above the 44/48px touch minimum.
	 */
	import { ChevronRight } from 'lucide-svelte';

	export let href: string | null = null;
	export let title = '';
	export let subtitle = '';
	export let meta = '';
	export let value = '';
	export let chevron = false;
	export let lines: 1 | 2 = 2;
	export let disabled = false;
</script>

<svelte:element
	this={href ? 'a' : 'div'}
	href={href ?? undefined}
	class="row-item"
	class:one={lines === 1}
	class:disabled
	aria-disabled={disabled || undefined}
>
	<span class="lead"><slot name="lead" /></span>
	<span class="body">
		<span class="title">{title}</span>
		{#if subtitle}<span class="subtitle">{subtitle}</span>{/if}
		{#if meta}<span class="meta">{meta}</span>{/if}
	</span>
	<span class="trail">
		<slot name="trail" />
		{#if value}<span class="value nums">{value}</span>{/if}
		{#if chevron}<span class="chev"><ChevronRight size={18} /></span>{/if}
	</span>
</svelte:element>

<style>
	.row-item {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		min-height: 56px;
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		color: var(--fg);
		transition: background-color 0.14s ease;
	}

	.row-item.one {
		min-height: 48px;
		padding-top: var(--sp-2);
		padding-bottom: var(--sp-2);
	}

	@media (hover: hover) {
		a.row-item:hover {
			background: var(--bg-hover);
		}
	}

	a.row-item:active {
		background: var(--bg-active);
	}

	.row-item.disabled {
		opacity: 0.55;
		pointer-events: none;
	}

	.lead {
		flex: 0 0 auto;
		display: flex;
		align-items: center;
	}

	.lead:empty {
		display: none;
	}

	.body {
		flex: 1;
		min-width: 0;
		display: flex;
		flex-direction: column;
		gap: 2px;
	}

	.title {
		font-size: var(--fs-body);
		font-weight: 500;
		letter-spacing: -0.005em;
		line-height: 1.35;
	}

	.subtitle {
		font-size: var(--fs-small);
		line-height: 1.4;
		color: var(--fg-muted);
	}

	.meta {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		margin-top: 1px;
	}

	.trail {
		flex: 0 0 auto;
		display: flex;
		align-items: center;
		gap: var(--sp-2);
	}

	.trail:empty {
		display: none;
	}

	.value {
		font-size: var(--fs-small);
		color: var(--fg-muted);
	}

	.chev {
		color: var(--fg-subtle);
		flex: 0 0 auto;
	}
</style>
