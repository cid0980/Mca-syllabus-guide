<script lang="ts">
	/** Progress ring. Single accent colour, neutral track, optional label in the middle. */
	export let percent = 0;
	export let size = 40;
	export let stroke = 3;
	export let label: string | null = null;
	export let labelSize = 0;

	const r = (size - stroke) / 2;
	const circ = 2 * Math.PI * r;

	$: pct = Math.max(0, Math.min(100, percent));
	$: offset = circ * (1 - pct / 100);
	$: fontSize = labelSize || Math.max(10, Math.round(size / 3.6));
</script>

<span class="ring" style={`width:${size}px;height:${size}px`} role="img" aria-label={`${pct} percent complete`}>
	<svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
		<circle cx={size / 2} cy={size / 2} {r} fill="none" stroke="var(--bg-element)" stroke-width={stroke} />
		{#if pct > 0}
			<circle
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
		font-weight: 600;
		letter-spacing: -0.02em;
	}
</style>
