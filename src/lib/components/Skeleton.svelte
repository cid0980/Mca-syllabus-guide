<script lang="ts">
	/** Loading placeholder. Shape must match the content it replaces (skills/FRONTEND-DESIGN.md). */
	export let variant: 'rows' | 'card' | 'list' | 'lines' = 'rows';
	export let count = 6;
</script>

{#if variant === 'lines'}
	<div class="lines">
		{#each Array(count) as _, i}
			<span class="skeleton" style={`width:${i % 3 === 2 ? 62 : 100}%`}></span>
		{/each}
	</div>
{:else if variant === 'card'}
	<div class="card">
		<span class="skeleton head"></span>
		<span class="skeleton title"></span>
		<span class="skeleton def"></span>
		<div class="lines">
			{#each Array(3) as _}<span class="skeleton" style="width:100%"></span>{/each}
			<span class="skeleton" style="width:64%"></span>
		</div>
	</div>
{:else}
	<div class="rows" class:list={variant === 'list'}>
		{#each Array(count) as _}
			<div class="row">
				<span class="skeleton avatar"></span>
				<span class="col">
					<span class="skeleton" style="width:56%;height:14px"></span>
					<span class="skeleton" style="width:78%;height:12px"></span>
				</span>
			</div>
		{/each}
	</div>
{/if}

<style>
	.rows {
		display: flex;
		flex-direction: column;
	}

	.rows.list .row {
		background: var(--bg-subtle);
	}

	.rows.list .row + .row {
		border-top: 1px solid var(--border);
	}

	.row {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3) var(--sp-4);
	}

	.avatar {
		width: 36px;
		height: 36px;
		border-radius: var(--radius-full);
		flex: 0 0 auto;
	}

	.col {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.card {
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
		padding: var(--sp-4);
		margin: 0 var(--sp-4);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
	}

	.head {
		width: 120px;
		height: 12px;
	}

	.title {
		width: 70%;
		height: 20px;
	}

	.def {
		width: 100%;
		height: 16px;
	}

	.lines {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.lines span {
		height: 12px;
		display: block;
	}
</style>
