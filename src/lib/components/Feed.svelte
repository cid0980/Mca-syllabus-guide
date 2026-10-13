<script lang="ts">
	/**
	 * Instagram-style vertical feed: one card per screen, native scroll-snap, no per-frame
	 * JavaScript. An IntersectionObserver reports which card is on screen; everything else
	 * (progress bar, seen-marking, next/prev buttons) follows from that.
	 */
	import { onMount } from 'svelte';
	import { ChevronDown, ChevronUp } from 'lucide-svelte';
	import type { DeckCard } from '$lib/content';
	import { markSeen } from '$lib/stores/progress';
	import { bookmarks, toggleBookmark } from '$lib/stores/bookmarks';
	import { hydrated } from '$lib/stores/hydrate';
	import Post from '$lib/components/Post.svelte';

	export let cards: DeckCard[] = [];
	export let initialIndex = 0;
	export let examMode = false;
	export let onAsk: (() => void) | undefined = undefined;

	let scroller: HTMLDivElement;
	let active = 0;
	let io: IntersectionObserver | null = null;
	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;

	$: total = cards.length;
	$: current = cards[active];

	onMount(() => {
		window.addEventListener('keydown', onKey);
		io = new IntersectionObserver(
			(entries) => {
				for (const entry of entries) {
					if (entry.isIntersecting && entry.intersectionRatio >= 0.6) {
						const i = Number((entry.target as HTMLElement).dataset.i ?? 0);
						setActive(i);
					}
				}
			},
			{ root: scroller, threshold: [0.6] }
		);
		for (const el of Array.from(scroller.querySelectorAll('[data-i]'))) io.observe(el);

		if (initialIndex > 0) {
			// jump without animation so the first paint is already on the right card
			requestAnimationFrame(() => goTo(initialIndex, false));
		}
		return () => {
			io?.disconnect();
			window.removeEventListener('keydown', onKey);
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
		if (e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ') {
			e.preventDefault();
			step(1);
		} else if (e.key === 'ArrowUp' || e.key === 'PageUp') {
			e.preventDefault();
			step(-1);
		}
	}

	function onSave(id: string, next: boolean) {
		const added = toggleBookmark(id);
		notify(added ? 'Saved' : 'Removed');
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
					on:save={(e) => onSave(card.id, e.detail)}
					on:ask={() => (onAsk ? onAsk() : notify('Ask AI arrives in build step 6'))}
				/>
			{:else}
				<div class="stub"></div>
			{/if}
		</section>
	{/each}

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
</div>

{#if toast}<div class="toast" role="status">{toast}</div>{/if}

<style>
	.feed {
		position: relative;
		flex: 1;
		min-height: 0;
		overflow-y: auto;
		overscroll-behavior-y: contain;
		scroll-snap-type: y mandatory;
		-webkit-overflow-scrolling: touch;
		scrollbar-width: none;
		outline: none;
	}

	.feed::-webkit-scrollbar {
		display: none;
	}

	.bar {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
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
		transition: width 0.18s ease-out;
	}

	.snap {
		height: 100%;
		scroll-snap-align: start;
		scroll-snap-stop: always;
		display: flex;
		flex-direction: column;
		min-height: 0;
	}

	.snap + .snap {
		border-top: 1px solid var(--border);
	}

	.stub {
		flex: 1;
		margin: var(--sp-4);
		border-radius: var(--radius-lg);
		background: var(--fill);
	}

	.jump {
		position: absolute;
		right: var(--sp-3);
		bottom: var(--sp-4);
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
		z-index: 6;
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
		transition: transform 0.12s ease, opacity 0.12s ease;
	}

	.jump-btn:active {
		transform: scale(0.9);
	}

	.jump-btn[disabled] {
		opacity: 0.35;
		pointer-events: none;
	}
</style>
