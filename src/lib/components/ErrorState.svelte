<script lang="ts">
	/** Every async view needs this: what failed, why, and a way out. */
	import { createEventDispatcher } from 'svelte';
	import { TriangleAlert, RotateCcw } from 'lucide-svelte';

	export let title = 'Something went wrong';
	export let message = '';
	export let retryLabel = 'Try again';
	export let retrying = false;

	const dispatch = createEventDispatcher<{ retry: void }>();
</script>

<div class="wrap" role="alert">
	<span class="icon"><TriangleAlert size={22} /></span>
	<div class="text">
		<p class="title">{title}</p>
		{#if message}<p class="msg">{message}</p>{/if}
	</div>
	<button class="btn btn--secondary btn--sm" on:click={() => dispatch('retry')} aria-busy={retrying}>
		<span class={retrying ? 'spin' : ''}><RotateCcw size={16} /></span>
		{retrying ? 'Retrying' : retryLabel}
	</button>
</div>

<style>
	.wrap {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-3);
		margin: var(--sp-4);
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		border: 1px solid var(--border);
		border-left: 2px solid var(--danger);
		border-radius: var(--radius);
	}

	.icon {
		color: var(--danger);
		flex: 0 0 auto;
		margin-top: 2px;
	}

	.text {
		flex: 1;
		min-width: 0;
	}

	.title {
		font-size: var(--fs-body);
		font-weight: 500;
	}

	.msg {
		font-size: var(--fs-small);
		color: var(--fg-muted);
		margin-top: 2px;
	}

	@media (max-width: 380px) {
		.wrap {
			flex-wrap: wrap;
		}
	}
</style>
