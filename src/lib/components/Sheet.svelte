<script lang="ts">
	/**
	 * Bottom sheet. Travels up from the bottom edge over ~240ms and leaves in ~180ms
	 * (skills/MOTION.md) — it never appears out of thin air.
	 *
	 * Handles: escape to close, backdrop tap, body scroll lock, focus move, and a short
	 * closing animation before the parent unsets `open`.
	 */
	import { createEventDispatcher, onDestroy, onMount, tick } from 'svelte';
	import { browser } from '$app/environment';
	import { X } from 'lucide-svelte';

	export let open = false;
	export let title = '';
	export let subtitle = '';

	const dispatch = createEventDispatcher<{ close: void }>();
	let closing = false;
	let panel: HTMLElement;
	let previous = '';

	// reactive statements also run during SSR, so this only ever touches the DOM in the browser
	$: if (browser && open && !closing) mountPanel();

	function requestClose() {
		if (closing) return;
		closing = true;
		setTimeout(() => {
			closing = false;
			dispatch('close');
		}, 180);
	}

	async function mountPanel() {
		if (!browser) return;
		previous = document.activeElement instanceof HTMLElement ? document.activeElement.tagName : '';
		await tick();
		document.body.style.overflow = 'hidden';
		const focusable = panel?.querySelector<HTMLElement>('[data-autofocus], button, input, textarea, a[href]');
		focusable?.focus({ preventScroll: true });
	}

	function onKey(e: KeyboardEvent) {
		if (!open) return;
		if (e.key === 'Escape') {
			e.preventDefault();
			requestClose();
			return;
		}
		// keep focus inside the sheet while it is open
		if (e.key === 'Tab' && panel) {
			const nodes = Array.from(
				panel.querySelectorAll<HTMLElement>('button, a[href], input, textarea, [tabindex]:not([tabindex="-1"])')
			).filter((el) => !el.hasAttribute('disabled'));
			if (nodes.length === 0) return;
			const first = nodes[0];
			const last = nodes[nodes.length - 1];
			if (e.shiftKey && document.activeElement === first) {
				e.preventDefault();
				last.focus();
			} else if (!e.shiftKey && document.activeElement === last) {
				e.preventDefault();
				first.focus();
			}
		}
	}

	onMount(() => {
		globalThis.addEventListener('keydown', onKey);
		return () => {
			globalThis.removeEventListener('keydown', onKey);
			document.body.style.overflow = '';
		};
	});

	onDestroy(() => {
		if (browser) document.body.style.overflow = '';
	});
</script>

{#if open}
	<div
		class="backdrop"
		class:closing
		role="presentation"
		on:click={requestClose}
		on:keydown={(e) => e.key === 'Enter' && requestClose()}
	></div>
	<section class="sheet" class:closing bind:this={panel} role="dialog" aria-modal="true" aria-label={title}>
		<div class="grip-wrap"><span class="sheet-grip"></span></div>
		<header class="sheet-head">
			<div class="grow">
				<h2 class="sheet-title">{title}</h2>
				{#if subtitle}<p class="sheet-sub">{subtitle}</p>{/if}
			</div>
			<button class="icon-btn" on:click={requestClose} aria-label="Close">
				<X size={20} />
			</button>
		</header>
		<div class="sheet-body">
			<slot />
		</div>
		{#if $$slots.foot}
			<footer class="sheet-foot">
				<slot name="foot" />
			</footer>
		{/if}
	</section>
{/if}

<style>
	.grip-wrap {
		padding: var(--sp-2) 0 0;
		background: var(--bg);
		border-top-left-radius: var(--radius-lg);
		border-top-right-radius: var(--radius-lg);
	}
</style>
