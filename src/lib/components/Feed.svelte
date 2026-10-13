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
	import { ChevronDown, ChevronLeft, ChevronRight, ChevronUp } from 'lucide-svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { plural } from '$lib/content';
	import type { DeckCard, ModuleRef } from '$lib/content';
	import { shortName } from '$lib/labels';
	import { progress } from '$lib/stores/progress';
	import { bookmarks, toggleBookmark } from '$lib/stores/bookmarks';
	import { hydrated } from '$lib/stores/hydrate';
	import Post from '$lib/components/Post.svelte';

	export let cards: DeckCard[] = [];
	export let initialIndex = 0;
	export let examMode = false;
	/** the module this deck belongs to, and the written modules before and after it */
	export let current: ModuleRef | null = null;
	export let prev: ModuleRef | null = null;
	export let next: ModuleRef | null = null;

	let scroller: HTMLDivElement;
	let active = 0;
	let io: IntersectionObserver | null = null;
	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;
	/** true while the deck is scrolled to the very bottom, where the end block lives */
	let atEnd = false;

	$: total = cards.length;
	/** the jump arrows move between cards; the end footer is at the bottom of the scroll */
	$: lastStop = Math.max(0, total - 1);
	/** the bar shows how much of this deck the student has actually marked, not scroll position */
	$: readCount = $hydrated ? cards.filter((c) => $progress[c.id]?.seen).length : 0;

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

	/**
	 * Only tracks which card is on screen, for the jump buttons and the keyboard. Marking a card as
	 * read is the student's tap on the card itself.
	 */
	function setActive(i: number) {
		active = i;
	}

	/** The ask page needs the card and the way back to it, and both go in the URL. */
	function openAsk(cardId: string) {
		const from = `${$page.url.pathname}?card=${encodeURIComponent(cardId)}`;
		goto(`/ask?card=${encodeURIComponent(cardId)}&from=${encodeURIComponent(from)}`);
	}

	function notify(message: string) {
		toast = message;
		clearTimeout(toastTimer);
		toastTimer = setTimeout(() => (toast = ''), 1400);
	}

	function onScroll() {
		if (!scroller) return;
		atEnd = scroller.scrollTop + scroller.clientHeight >= scroller.scrollHeight - 24;
	}

	function goTo(i: number, smooth = true) {
		const el = scroller?.querySelector<HTMLElement>(`[data-i="${i}"]`);
		if (!el) return;
		el.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', block: 'start' });
		if (!smooth) setActive(i);
	}

	function step(by: number) {
		const target = Math.min(lastStop, Math.max(0, active + by));
		if (target !== active) goTo(target);
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

<div class="feed" bind:this={scroller} on:scroll={onScroll} aria-label="Study cards">
	<div class="bar">
		<div class="track"><div class="fill" style={`width:${total ? (readCount / total) * 100 : 0}%`}></div></div>
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
					read={$progress[card.id]?.seen ?? false}
					on:save={() => onSave(card.id)}
					on:read={(e) => notify(e.detail ? 'Marked as read' : 'Mark removed')}
					on:ask={() => openAsk(card.id)}
				/>
			{:else}
				<div class="stub"></div>
			{/if}
		</section>
	{/each}

<!--
	The end of a deck used to be a dead end: the student had to go back to the subject page and hunt
	for the next module. This block names where the next tap goes, and shows what was read.
-->
{#if current}
	<section class="end" aria-label={`End of Module ${current.module}: ${current.title}`}>
		<p class="end-line">
			<span class="end-label">End of Module {current.module}</span>
			<span class="end-count nums">{readCount}/{total} read</span>
		</p>

		<div class="end-actions">
			{#if prev}
				<a
					class="end-btn"
					href={`/feed/${encodeURIComponent(prev.code)}/${prev.module}`}
					aria-label={`Previous module: ${prev.title} for ${prev.subject}`}
				>
					<ChevronLeft size={16} />
					<span class="end-btn-text">
						<span class="end-btn-title">Previous</span>
						<span class="end-btn-sub">
							{prev.code !== current.code ? `${shortName(prev.code)} · ` : ''}Module {prev.module}
						</span>
					</span>
				</a>
			{/if}

			{#if next}
				<a
					class="end-btn end-btn--primary"
					href={`/feed/${encodeURIComponent(next.code)}/${next.module}`}
					aria-label={`Next module: ${next.title} for ${next.subject}`}
				>
					<span class="end-btn-text">
						<span class="end-btn-title">
							{next.code === current.code ? 'Next' : 'Next subject'}
						</span>
						<span class="end-btn-sub">
							{next.code !== current.code ? `${shortName(next.code)} · ` : ''}Module {next.module}
						</span>
					</span>
					<ChevronRight size={16} />
				</a>
			{:else}
				<a
					class="end-btn"
					href={`/subject/${encodeURIComponent(current.code)}`}
					aria-label={`All modules of ${current.subject}`}
				>
					<span class="end-btn-text">
						<span class="end-btn-title">All modules</span>
						<span class="end-btn-sub">nothing follows yet</span>
					</span>
					<ChevronRight size={16} />
				</a>
			{/if}
		</div>
	</section>
{/if}

</div>

{#if total > 1 && !atEnd}
	<div class="jump">
		<button class="jump-btn" disabled={active === 0} on:click={() => step(-1)} aria-label="Previous card">
			<ChevronUp size={18} />
		</button>
		<button class="jump-btn" disabled={active >= lastStop} on:click={() => step(1)} aria-label="Next card">
			<ChevronDown size={18} />
		</button>
	</div>
{/if}

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

	/* ---------- end of module ---------- */

	/* a small footer at the end of the cards, not a full screen: it must not eat the reading area */
	.end {
		display: grid;
		gap: var(--sp-2);
		padding: var(--sp-4) var(--sp-4) var(--sp-6);
		border-top: 1px solid var(--border);
		background: var(--bg);
	}

	.end-line {
		display: flex;
		align-items: baseline;
		justify-content: space-between;
		gap: var(--sp-2);
	}

	.end-label {
		font-size: var(--fs-caption);
		font-weight: 600;
		letter-spacing: 0.04em;
		text-transform: uppercase;
		color: var(--fg-subtle);
	}

	.end-count {
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.end-actions {
		display: flex;
		gap: var(--sp-2);
	}

	.end-btn {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
		flex: 1 1 0;
		min-width: 0;
		min-height: 46px;
		padding: var(--sp-2) var(--sp-3);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		color: var(--fg);
		font-size: var(--fs-small);
		transition: transform var(--dur-press) var(--ease-standard), background-color var(--dur-press) var(--ease-standard);
	}

	.end-btn:active {
		transform: scale(0.99);
		background: var(--fill);
	}

	.end-btn--primary {
		background: var(--accent);
		border-color: var(--accent);
		color: var(--accent-fg);
	}

	.end-btn--primary:active {
		background: var(--accent);
		opacity: 0.9;
	}

	.end-btn-text {
		display: block;
		flex: 1;
		min-width: 0;
	}

	.end-btn-title {
		display: block;
		font-weight: 600;
		line-height: 1.2;
	}

	.end-btn-sub {
		display: block;
		font-size: var(--fs-caption);
		line-height: 1.2;
		color: var(--fg-subtle);
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.end-btn--primary .end-btn-sub {
		color: var(--accent-fg);
		opacity: 0.85;
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
