<script lang="ts">
	/** Inline explanatory block. Used where a bare "empty state" would otherwise appear. */
	import type { ComponentType } from 'svelte';
	import { Info } from 'lucide-svelte';

	export let title = '';
	export let text = '';
	export let icon: ComponentType = Info;
	export let tone: 'neutral' | 'accent' = 'neutral';
</script>

<div class="notice" class:accent={tone === 'accent'}>
	<span class="icon"><svelte:component this={icon} size={18} /></span>
	<div>
		{#if title}<p class="title">{title}</p>{/if}
		<p class="text">{text}</p>
		<slot />
	</div>
</div>

<style>
	.notice {
		display: flex;
		gap: var(--sp-3);
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		margin: var(--sp-4) var(--sp-4) 0;
	}

	.notice.accent {
		border-left: 2px solid var(--accent);
	}

	.icon {
		color: var(--fg-subtle);
		flex: 0 0 auto;
		margin-top: 2px;
	}

	.accent .icon {
		color: var(--accent);
	}

	.title {
		font-size: var(--fs-body);
		font-weight: 500;
	}

	.text {
		font-size: var(--fs-small);
		line-height: 1.5;
		color: var(--fg-muted);
		margin-top: 2px;
	}
</style>
