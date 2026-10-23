<script lang="ts">
	/**
	 * Today's goal, on the home screen.
	 *
	 * Deliberately its own card rather than a line inside the progress card: the number and the
	 * action belong together, and both come straight from the reminder's own store, so the card
	 * and the notification can never disagree about how many are left.
	 */
	import { BookOpen, ChevronRight, CircleCheck } from 'lucide-svelte';
	import { percent } from '$lib/content';
	import { hydrated } from '$lib/stores/hydrate';
	import { lastOpened } from '$lib/stores/lastOpened';
	import { today } from '$lib/reminders';

	const FIRST_DECK = { code: 'CSCA 411', module: 'I' };

	/** Where the action goes: back to the deck you were last in, else the first deck. */
	$: deck = $lastOpened
		? { code: $lastOpened.code, module: $lastOpened.module, cardId: $lastOpened.cardId }
		: { code: FIRST_DECK.code, module: FIRST_DECK.module, cardId: '' };

	$: href = deck.cardId
		? `/feed/${encodeURIComponent(deck.code)}/${deck.module}?card=${encodeURIComponent(deck.cardId)}`
		: `/feed/${encodeURIComponent(deck.code)}/${deck.module}`;

	$: done = $hydrated ? $today.done : 0;
	$: goal = $today.goal;
	$: met = $hydrated && done >= goal;
	$: pct = percent(done, goal);
</script>

{#if !$hydrated}
	<div class="gutter">
		<div class="goal skeleton">
			<span class="ring-sk" aria-hidden="true"></span>
			<span class="grow">
				<span class="sk-line w40"></span>
				<span class="sk-line w70"></span>
			</span>
		</div>
	</div>
{:else}
	<div class="gutter">
		<a class="goal pressable" class:met href={met ? '/progress' : href} aria-label="Today's goal">
			<span class="ring" aria-hidden="true">
				<svg viewBox="0 0 40 40" width="44" height="44">
					<circle cx="20" cy="20" r="17" fill="none" stroke="var(--fill-strong)" stroke-width="3.5" />
					<circle
						cx="20"
						cy="20"
						r="17"
						fill="none"
						stroke={met ? 'var(--success)' : 'var(--accent)'}
						stroke-width="3.5"
						stroke-linecap="round"
						stroke-dasharray={2 * Math.PI * 17}
						stroke-dashoffset={2 * Math.PI * 17 * (1 - pct / 100)}
						transform="rotate(-90 20 20)"
					/>
				</svg>
				<span class="ring-num nums">{done}<span class="ring-of">/{goal}</span></span>
			</span>

			<span class="grow">
				<span class="goal-label">Today</span>
				{#if met}
					<span class="goal-title done">
						<CircleCheck size={14} /> Daily goal met
					</span>
					<span class="goal-sub">{done} of {goal} cards read. See your streak.</span>
				{:else}
					<span class="goal-title">
						{goal - done} {goal - done === 1 ? 'card' : 'cards'} to go today
					</span>
					<span class="goal-sub">
						{done} of {goal} read. Two minutes and the day is done.
					</span>
				{/if}
			</span>

			<span class="chev">
				{#if met}
					<ChevronRight size={18} />
				{:else}
					<BookOpen size={18} />
				{/if}
			</span>
		</a>
	</div>
{/if}

<style>
	.goal {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		width: 100%;
		min-height: 72px;
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		text-align: left;
	}

	.grow {
		flex: 1 1 auto;
		min-width: 0;
	}

	.ring {
		position: relative;
		display: inline-flex;
		align-items: center;
		justify-content: center;
		flex: 0 0 auto;
		width: 44px;
		height: 44px;
	}

	.ring svg {
		position: absolute;
		inset: 0;
	}

	.ring-num {
		font-size: 13px;
		font-weight: 700;
		line-height: 1;
	}

	.ring-of {
		color: var(--fg-subtle);
		font-weight: 500;
	}

	.goal-label {
		display: block;
		font-size: var(--fs-caption);
		font-weight: 700;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--fg-subtle);
	}

	.goal-title {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
		font-size: var(--fs-body);
		font-weight: 600;
		margin-top: 2px;
	}

	.goal-title.done {
		color: var(--success);
	}

	.goal-sub {
		display: block;
		font-size: var(--fs-caption);
		line-height: 1.5;
		color: var(--fg-subtle);
		margin-top: 2px;
	}

	.chev {
		flex: 0 0 auto;
		color: var(--fg-subtle);
	}

	/* loading state keeps the card's height so nothing jumps when it fills in */
	.skeleton {
		align-items: center;
	}

	.ring-sk {
		flex: 0 0 auto;
		width: 44px;
		height: 44px;
		border-radius: var(--radius-full);
		background: var(--fill);
	}

	.sk-line {
		display: block;
		height: 10px;
		border-radius: var(--radius-full);
		background: var(--fill);
		margin-bottom: 6px;
	}

	.w40 {
		width: 40%;
	}

	.w70 {
		width: 70%;
	}
</style>
