<script lang="ts">
	/**
	 * Vertical feed: one card per screen, natural heights, ONE scroll container.
	 *
	 * Changes from user feedback:
	 *  - cards are no longer forced to exactly 100% height, so a long card can never overlap the
	 *    next one and nothing scrolls inside a card
	 *  - `scroll-snap-type: y proximity` instead of `mandatory`: snapping still aligns cards, but
	 *    the scroll can never be trapped or yanked while reading
	 *  - the progress bar is sticky, so it stays visible on tall cards
	 */
	import { onMount } from 'svelte';
	import { ChevronDown, ChevronUp } from 'lucide-svelte';
	import type { DeckCard } from '$lib/content';
	import { markSeen } from '$lib/stores/progress';
	import { bookmarks, toggleBookmark } from '$lib/stores/bookmarks';
	import { hydrated } from '$lib/stores/hydrate';
	import Post from '$lib/components/Post.svelte';
	import AskSheet from '$lib/components/AskSheet.svelte';

	export let cards: DeckCard[] = [];
	export let initialIndex = 0;
	export let examMode = false;

	let scroller: HTMLDivElement;
	let active = 0;
	let io: IntersectionObserver | null = null;
	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;
	let askOpen = false;

	$: total = cards.length;
	$: currentCard = cards[active] ?? null;

	onMount(() => {
		globalThis.addEventListener('keydown', onKey);
		io = new IntersectionObserver(
			(entries) => {
				for (const entry of entries) {
					if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
						setActive(Number((entry.target as HTMLElement).dataset.i ?? 0));
					}
				}
			},
			{ root: scroller, threshold: [0.5] }
		);
		for (const el of Array.from(scroller.querySelectorAll('[data-i]'))) io.observe(el);
		if (initialIndex > 0) requestAnimationFrame(() => goTo(initialIndex, false));
		return () => {
			io?.disconnect();
			globalThis.removeEventListener('keydown', onKey);
		};
	});

	function setActive(i: number) {
		active = i;
		if (cards[i]) markSeen(cards[i].id);
	}

	function notify(message: string) {
		toast = message;
		clearTimeout(toastTimer);
		toastTimer = setTimeout(() => (toast = ''), 1400);
	}

	function goTo(i: number, smooth = true) {
		const el = scroller?.querySelector<HTMLElement>(`[data-i="${i}"]`);
		if (!el) return;
		el.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', block: 'start' });
		if (!smooth) setActive(i);
	}

	function step(by: number) {
		const next = Math.min(total - 1, Math.max(0, active + by));
		if (next !== active) goTo(next);
	}

	function onKey(e: KeyboardEvent) {
		if (e.target instanceof HTMLElement && e.target.closest('input, textarea')) return;
		if (e.key === 'ArrowDown' || e.key === 'PageDown') {
			e.preventDefault();
			step(1);
		} else if (e.key === 'ArrowUp' || e.key === 'PageUp') {
			e.preventDefault();
			step(-1);
		}
	}

	function onSave(id: string) {
		notify(toggleBookmark(id) ? 'Saved' : 'Removed');
	}
</script>

<div class="feed" bind:this={scroller} aria-label="Study cards">
	<div class="bar">
		<div class="track"><div class="fill" style={`width:${total ? ((active + 1) / total) * 100 : 0}%`}></div></div>
	</div>

	{#each cards as card, i (card.id)}
		<section class="snap" data-i={i} aria-label={`Card ${i + 1} of ${total}`}>
			{#if $hydrated}
				<Post
					{card}
					{examMode}
					index={i}
					{total}
					saved={$bookmarks.includes(card.id)}
					on:save={() => onSave(card.id)}
					on:ask={() => (askOpen = true)}
				/>
			{:else}
				<div class="stub"></div>
			{/if}
		</section>
	{/each}
</div>

{#if total > 1}
	<div class="jump">
		<button class="jump-btn" disabled={active === 0} on:click={() => step(-1)} aria-label="Previous card">
			<ChevronUp size={18} />
		</button>
		<button class="jump-btn" disabled={active >= total - 1} on:click={() => step(1)} aria-label="Next card">
			<ChevronDown size={18} />
		</button>
	</div>
{/if}

<AskSheet open={askOpen} card={currentCard} on:close={() => (askOpen = false)} />

{#if toast}<div class="toast" role="status">{toast}</div>{/if}

<style>
	.feed {
		position: relative;
		flex: 1;
		min-height: 0;
		overflow-y: auto;
		overscroll-behavior-y: contain;
		/* proximity: never trap or yank the scroll, but still align cards */
		scroll-snap-type: y proximity;
		-webkit-overflow-scrolling: touch;
		scrollbar-width: none;
	}

	.feed::-webkit-scrollbar {
		display: none;
	}

	/* sticky so tall cards still show how far along you are */
	.bar {
		position: sticky;
		top: 0;
		height: 2px;
		z-index: 5;
		pointer-events: none;
	}

	.track {
		height: 100%;
		background: transparent;
	}

	.fill {
		height: 100%;
		background: var(--accent);
		transition: width var(--dur-quick) var(--ease-standard);
	}

	/* natural height: as tall as the card needs, at least a screen */
	.snap {
		min-height: 100%;
		scroll-snap-align: start;
		display: flex;
		flex-direction: column;
	}

	.snap + .snap {
		border-top: 1px solid var(--border);
	}

	.stub {
		min-height: 60vh;
		margin: var(--sp-4);
		border-radius: var(--radius-lg);
		background: var(--fill);
	}

	.jump {
		position: fixed;
		right: var(--sp-3);
		bottom: calc(var(--nav-h) + var(--sp-4) + env(safe-area-inset-bottom));
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
		z-index: 45;
	}

	.jump-btn {
		display: grid;
		place-items: center;
		width: 40px;
		height: 40px;
		border-radius: var(--radius-full);
		background: var(--fill);
		color: var(--fg);
		box-shadow: var(--shadow-pop);
		transition: transform var(--dur-press) var(--ease-standard), opacity var(--dur-press) var(--ease-standard);
	}

	.jump-btn:active {
		transform: scale(0.9);
	}

	.jump-btn[disabled] {
		opacity: 0.35;
		pointer-events: none;
	}
</style>
