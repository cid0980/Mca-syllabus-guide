<script lang="ts">
	/**
	 * Swipe deck. Swipe or arrow keys to move, tap to flip to the quiz, double tap to save.
	 * Every gesture also has a visible control (skills/MOBILE-UX.md).
	 * At most three cards are mounted; motion is transform/opacity only.
	 */
	import { browser } from '$app/environment';
	import { onDestroy, onMount } from 'svelte';
	import { ArrowLeft, ArrowRight, Bookmark, MessageSquare, BookmarkCheck } from 'lucide-svelte';
	import type { DeckCard } from '$lib/content';
	import { markSeen, recordQuiz } from '$lib/stores/progress';
	import { bookmarks, isBookmarked, toggleBookmark } from '$lib/stores/bookmarks';
	import CardView from '$lib/components/Card.svelte';

	export let cards: DeckCard[] = [];
	export let initialIndex = 0;
	export let examMode = false;
	export let onAsk: (() => void) | undefined = undefined;

	const THRESHOLD = 88;

	let idx = Math.max(0, Math.min(initialIndex, Math.max(0, cards.length - 1)));
	let face: 'front' | 'back' = 'front';
	let dx = 0;
	let dragging = false;
	let locked: 'x' | null = null;
	let startX = 0;
	let startY = 0;
	let lastTapAt = 0;
	let outCard: DeckCard | null = null;
	let outFace: 'front' | 'back' = 'front';
	let flying = false;
	let entering: string | null = null;
	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;
	let flyTimer: ReturnType<typeof setTimeout>;

	$: total = cards.length;
	$: current = cards[idx];
	$: progressPct = total ? ((idx + 1) / total) * 100 : 0;
	$: saved = current ? isBookmarked(current.id, $bookmarks) : false;
	$: windowed = cards.slice(idx, idx + 3);
	$: deck = outCard ? [outCard, ...windowed] : windowed;
	$: if (browser && current) markSeen(current.id);

	onMount(() => {
		const onKey = (e: KeyboardEvent) => {
			if (e.key === 'ArrowRight') go(1);
			else if (e.key === 'ArrowLeft') go(-1);
			else if (e.key === ' ') {
				e.preventDefault();
				flip();
			} else if (e.key === 'b' || e.key === 'B') save();
		};
		globalThis.addEventListener('keydown', onKey);
		return () => globalThis.removeEventListener('keydown', onKey);
	});

	onDestroy(() => {
		clearTimeout(toastTimer);
		clearTimeout(flyTimer);
	});

	function notify(message: string) {
		toast = message;
		clearTimeout(toastTimer);
		toastTimer = setTimeout(() => (toast = ''), 1600);
	}

	function flip() {
		if (examMode) return;
		face = face === 'front' ? 'back' : 'front';
	}

	function save() {
		if (!current) return;
		const added = toggleBookmark(current.id);
		notify(added ? 'Saved' : 'Removed from saved');
		if (browser && 'vibrate' in navigator) navigator.vibrate(8);
	}

	function go(step: number) {
		const next = idx + step;
		clearTimeout(flyTimer);
		if (flying || next < 0 || next >= total) {
			dx = 0;
			return;
		}
		idx = next;
		dx = 0;
		if (step > 0) {
			outFace = face;
			outCard = cards[next - 1];
			flying = true;
			flyTimer = setTimeout(() => {
				outCard = null;
				flying = false;
			}, 220);
		} else {
			entering = cards[next].id;
			flyTimer = setTimeout(() => (entering = null), 280);
		}
		face = 'front';
	}

	function down(e: PointerEvent) {
		if (flying) return;
		dragging = true;
		locked = null;
		startX = e.clientX;
		startY = e.clientY;
		try {
			(e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
		} catch {
			/* ignore */
		}
	}

	function move(e: PointerEvent) {
		if (!dragging) return;
		const mx = e.clientX - startX;
		const my = e.clientY - startY;
		if (locked === null) {
			if (Math.abs(mx) > 10 && Math.abs(mx) > Math.abs(my)) locked = 'x';
			else if (Math.abs(my) > 10) {
				dragging = false;
				return;
			}
		}
		if (locked === 'x') {
			dx = (idx === 0 && mx > 0) || (idx === total - 1 && mx < 0) ? mx * 0.3 : mx;
		}
	}

	function up(e: PointerEvent) {
		if (!dragging) return;
		const moved = Math.abs(dx);
		dragging = false;
		locked = null;

		if (moved > THRESHOLD) {
			go(dx < 0 ? 1 : -1);
			return;
		}
		dx = 0;

		if (moved < 8) {
			const target = e.target as HTMLElement | null;
			if (target?.closest('button, a')) return;
			const now = Date.now();
			if (now - lastTapAt < 300) {
				lastTapAt = 0;
				save();
				return;
			}
			lastTapAt = now;
			setTimeout(() => {
				if (lastTapAt !== 0 && Date.now() - lastTapAt >= 290) {
					lastTapAt = 0;
					flip();
				}
			}, 300);
		}
	}

	function styleFor(card: DeckCard, i: number): string {
		if (outCard && card.id === outCard.id) {
			return 'z-index:40;transform:translate3d(-620px,0,0) rotate(-14deg);opacity:0;';
		}
		const depth = outCard ? i - 1 : i;
		const drag = Math.min(1, Math.abs(dx) / 140);
		if (depth === 0) return `z-index:30;transform:translate3d(${dx}px,0,0) rotate(${dx / 30}deg);`;
		const scale = 1 - depth * 0.04 + drag * 0.04;
		const y = depth * 10 - drag * 10;
		return `z-index:${30 - depth};transform:translate3d(0,${y}px,0) scale(${scale});`;
	}
</script>

<div class="wrap">
	<div class="topbar">
		<div class="track"><div class="fill" style={`width:${progressPct}%`}></div></div>
		<span class="count nums">{total ? idx + 1 : 0}/{total}</span>
		<button class="icon-btn" class:icon-btn--on={saved} on:click={save} aria-label={saved ? 'Remove from saved' : 'Save card'}>
			{#if saved}<BookmarkCheck size={18} />{:else}<Bookmark size={18} />{/if}
		</button>
	</div>

	<div class="deck" on:pointerdown={down} on:pointermove={move} on:pointerup={up} on:pointercancel={up}>
		{#if current}
			{#each deck as card, i (card.id)}
				<div
					class="layer"
					class:animating={!dragging}
					class:enter={entering === card.id}
					style={styleFor(card, i)}
				>
					<CardView
						{card}
						face={card.id === current.id ? face : outCard && card.id === outCard.id ? outFace : 'front'}
						{examMode}
						quizRecord={(correct) => recordQuiz(card.id, correct)}
					/>
				</div>
			{/each}
			{#if Math.abs(dx) > 26}
				<span class="hint">{dx < 0 ? 'Next' : 'Previous'}</span>
			{/if}
		{:else}
			<div class="placeholder">No cards in this deck.</div>
		{/if}
	</div>

	<div class="controls">
		<button class="icon-btn" disabled={idx === 0} on:click={() => go(-1)} aria-label="Previous card">
			<ArrowLeft size={18} />
		</button>
		<button class="btn btn--secondary flip" on:click={flip} disabled={examMode}>
			{examMode ? 'Definitions only' : face === 'front' ? 'Show quiz' : 'Back to card'}
		</button>
		<button class="icon-btn" disabled={idx >= total - 1} on:click={() => go(1)} aria-label="Next card">
			<ArrowRight size={18} />
		</button>
		<button
			class="btn btn--primary ask"
			on:click={() => (onAsk ? onAsk() : notify('Ask AI arrives in build step 6'))}
		>
			<MessageSquare size={16} />
			Ask
		</button>
	</div>

	{#if toast}<div class="toast" role="status">{toast}</div>{/if}
</div>

<style>
	.wrap {
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
		flex: 1;
		height: 100%;
		min-height: 0;
	}

	.topbar {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
	}

	.track {
		flex: 1;
		height: 2px;
		background: var(--bg-element);
		border-radius: var(--radius-full);
		overflow: hidden;
	}

	.fill {
		height: 100%;
		background: var(--accent);
		transition: width 0.2s ease-out;
	}

	.count {
		font-size: var(--fs-caption);
		font-weight: 500;
		color: var(--fg-subtle);
	}

	.deck {
		position: relative;
		flex: 1;
		min-height: 0;
		touch-action: pan-y;
		user-select: none;
		-webkit-user-select: none;
	}

	.layer {
		position: absolute;
		inset: 0;
		will-change: transform;
	}

	.layer.animating {
		transition: transform 0.22s ease-out, opacity 0.22s ease-out;
	}

	.layer.enter {
		animation: enter 0.26s ease-out;
	}

	@keyframes enter {
		from {
			transform: translate3d(-620px, 0, 0) rotate(-14deg);
			opacity: 0;
		}
	}

	.hint {
		position: absolute;
		top: var(--sp-4);
		left: var(--sp-4);
		z-index: 60;
		background: var(--bg-element);
		border: 1px solid var(--border-strong);
		border-radius: var(--radius-full);
		padding: 2px var(--sp-3);
		font-size: var(--fs-caption);
		font-weight: 500;
		text-transform: uppercase;
		letter-spacing: 0.06em;
		color: var(--fg-muted);
		pointer-events: none;
	}

	.placeholder {
		display: grid;
		place-items: center;
		height: 100%;
		color: var(--fg-subtle);
		font-size: var(--fs-small);
	}

	.controls {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
	}

	.flip {
		flex: 1;
	}

	.icon-btn:disabled {
		opacity: 0.4;
		pointer-events: none;
	}
</style>
