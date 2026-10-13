<script lang="ts">
	import { Moon, Monitor, Sun } from 'lucide-svelte';
	import { settings, setTheme } from '$lib/stores/settings';
	import { hydrated } from '$lib/stores/hydrate';
	import { streak, progress, clearProgress } from '$lib/stores/progress';
	import { bookmarks, clearBookmarks } from '$lib/stores/bookmarks';
	import { totals } from '$lib/content';
	import { plural } from '$lib/content';
	import { browser } from '$app/environment';
	import AppBar from '$lib/components/AppBar.svelte';
	import ListRow from '$lib/components/ListRow.svelte';

	const themes = [
		{ value: 'dark' as const, label: 'Dark', icon: Moon },
		{ value: 'light' as const, label: 'Light', icon: Sun },
		{ value: 'system' as const, label: 'System', icon: Monitor }
	];

	let confirmClear = false;
	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;

	$: seenCount = Object.values($progress).filter((p) => p.seen).length;
	$: answered = Object.values($progress).reduce((n, p) => n + p.quizCorrect + p.quizWrong, 0);

	function notify(message: string) {
		toast = message;
		clearTimeout(toastTimer);
		toastTimer = setTimeout(() => (toast = ''), 1800);
	}

	function resetProgress() {
		clearProgress();
		confirmClear = false;
		notify('Progress cleared');
	}

	function resetBookmarks() {
		clearBookmarks();
		notify('Saved items cleared');
	}

	$: isStandalone = browser && window.matchMedia('(display-mode: standalone)').matches;
</script>

<svelte:head><title>Settings — StudyFeed</title></svelte:head>

<AppBar title="Settings" back="/" />

<main class="page">
	<p class="section-label">Appearance</p>
	<div class="group">
		{#each themes as theme}
			{@const Icon = theme.icon}
			<button class="theme-row" on:click={() => setTheme(theme.value)} aria-pressed={$hydrated && $settings.theme === theme.value}>
				<span class="theme-icon"><Icon size={18} /></span>
				<span class="grow">{theme.label}</span>
				{#if $hydrated && $settings.theme === theme.value}<span class="check" aria-hidden="true">Selected</span>{/if}
			</button>
		{/each}
	</div>

	<p class="section-label">Your data in this browser</p>
	<div class="group">
		<ListRow title="Cards seen" value={`${seenCount} of ${totals.cards}`} lines={1} />
		<ListRow title="Quiz answers recorded" value={String(answered)} lines={1} />
		<ListRow title="Saved items" value={String($bookmarks.length)} lines={1} />
		<ListRow title="Day streak" value={String($streak.count)} lines={1} />
	</div>

	<p class="section-label">Reset</p>
	<div class="group">
		<button class="danger-row" on:click={() => (confirmClear = !confirmClear)}>
			{confirmClear ? 'Tap again to clear all progress' : 'Clear progress and streak'}
		</button>
		{#if confirmClear}
			<button class="danger-row solid" on:click={resetProgress}>Yes, clear progress</button>
		{/if}
		<button class="danger-row" on:click={resetBookmarks}>Clear saved items</button>
	</div>

	<p class="section-label">About</p>
	<div class="group">
		<ListRow
			title="StudyFeed"
			subtitle={`Personal study companion · ${plural(totals.cards, 'card')} and ${totals.topics} mapped topics`}
			meta={isStandalone ? 'Running as an installed app' : 'Add to home screen for offline use'}
			lines={2}
		/>
		<ListRow
			title="Content state"
			subtitle="Draft cards are written in original words and need a textbook check before you mark them verified."
			lines={2}
		/>
	</div>

	<p class="footnote">
		No account, no server database, no analytics. Export and import of this data arrives in build step 7.
	</p>

	{#if toast}<div class="toast" role="status">{toast}</div>{/if}
</main>

<style>
	.theme-row {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		width: 100%;
		min-height: 52px;
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		font-size: var(--fs-body);
	}

	.theme-row:hover {
		background: var(--fill);
	}

	.theme-icon {
		color: var(--fg-muted);
	}

	.check {
		font-size: var(--fs-caption);
		color: var(--accent);
	}

	.danger-row {
		width: 100%;
		min-height: 52px;
		padding: var(--sp-3) var(--sp-4);
		background: var(--bg-subtle);
		color: var(--danger);
		font-size: var(--fs-body);
	}

	.danger-row.solid {
		background: var(--danger);
		color: #fff;
		font-weight: 500;
	}

	.danger-row:hover {
		background: var(--fill);
	}

	.danger-row.solid:hover {
		background: var(--danger);
	}

	.footnote {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		padding: var(--sp-6) var(--sp-4) 0;
	}
</style>
