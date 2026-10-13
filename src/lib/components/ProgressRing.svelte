<script lang="ts">
	/**
	 * Progress ring. Single accent colour, neutral track, optional label or slot in the middle.
	 *
	 * `pending` is for a course that has cards but nothing marked read yet: the track is drawn as a
	 * dashed accent ring. A blue circle must never look finished when nothing has been read, so an
	 * empty ring is dashed (something is waiting) and only real progress draws a solid arc.
	 */
	export let percent = 0;
	export let size = 40;
	export let stroke = 3;
	export let label: string | null = null;
	export let labelSize = 0;
	export let pending = false;
	export let ariaLabel: string | null = null;

	const r = (size - stroke) / 2;
	const circ = 2 * Math.PI * r;

	$: pct = Math.max(0, Math.min(100, percent));
	$: offset = circ * (1 - pct / 100);
	$: fontSize = labelSize || Math.max(10, Math.round(size / 3.6));
	$: dashed = pending && pct === 0;
	$: trackColor = dashed ? 'var(--accent)' : 'var(--fill)';
	$: trackDash = dashed ? '2 4' : undefined;
</script>

<span
	class="ring"
	style={`width:${size}px;height:${size}px`}
	role="img"
	aria-label={ariaLabel ?? `${pct} percent complete`}
>
	<svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
		<circle
			cx={size / 2}
			cy={size / 2}
			{r}
			fill="none"
			stroke={trackColor}
			stroke-width={stroke}
			stroke-dasharray={trackDash}
		/>
		{#if pct > 0}
			<circle
				class="arc"
				cx={size / 2}
				cy={size / 2}
				{r}
				fill="none"
				stroke="var(--accent)"
				stroke-width={stroke}
				stroke-linecap="round"
				stroke-dasharray={circ}
				stroke-dashoffset={offset}
				transform={`rotate(-90 ${size / 2} ${size / 2})`}
			/>
		{/if}
	</svg>
	{#if label}
		<span class="label nums" style={`font-size:${fontSize}px`}>{label}</span>
	{:else if $$slots.default}
		<span class="label" style={`font-size:${fontSize}px`}><slot /></span>
	{:else}
		<span class="label nums" style={`font-size:${fontSize}px`}>{pct}%</span>
	{/if}
</span>

<style>
	.ring {
		position: relative;
		display: inline-grid;
		place-items: center;
		flex: 0 0 auto;
	}

	svg,
	.label {
		grid-area: 1 / 1;
	}

	.label {
		display: grid;
		place-items: center;
		font-weight: 600;
		letter-spacing: -0.02em;
	}

	/* the arc grows into place instead of jumping, and holds still for reduced motion */
	.arc {
		transition: stroke-dashoffset 0.3s cubic-bezier(0.2, 0, 0, 1);
	}

	@media (prefers-reduced-motion: reduce) {
		.arc {
			transition: none;
		}
	}
</style>
