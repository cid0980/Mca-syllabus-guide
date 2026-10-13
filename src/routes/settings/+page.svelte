<script lang="ts">
	import { Moon, Sun, Monitor, Eye, EyeOff, LoaderCircle, CircleCheck, CircleAlert, RefreshCw, Trash2, Sparkles } from 'lucide-svelte';
	import { settings, setTheme } from '$lib/stores/settings';
	import { streak, progress, clearProgress } from '$lib/stores/progress';
	import { bookmarks, clearBookmarks } from '$lib/stores/bookmarks';
	import {
		ai,
		setProvider,
		setKey,
		clearKey,
		setModel,
		activeProvider,
		configuredProviders
	} from '$lib/stores/ai';
	import { PROVIDERS, type ProviderId } from '$lib/ai/providers';
	import { listModels } from '$lib/ai/client';
	import { clearAnswers, countAnswers } from '$lib/ai/cache';
	import { totals, plural } from '$lib/content';
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	import AppBar from '$lib/components/AppBar.svelte';
	import ListRow from '$lib/components/ListRow.svelte';
	import { hydrated } from '$lib/stores/hydrate';

	const themes = [
		{ value: 'dark' as const, label: 'Dark', icon: Moon },
		{ value: 'light' as const, label: 'Light', icon: Sun },
		{ value: 'system' as const, label: 'System', icon: Monitor }
	];

	let draftKey: Partial<Record<ProviderId, string>> = {};
	let revealed: Partial<Record<ProviderId, boolean>> = {};
	let modelList: Partial<Record<ProviderId, string[]>> = {};
	let busy: Partial<Record<ProviderId, 'models' | 'test' | null>> = {};
	let status: Partial<Record<ProviderId, { ok: boolean; text: string } | null>> = {};
	let cachedCount = 0;
	let confirmClear = false;
	let toast = '';
	let toastTimer: ReturnType<typeof setTimeout>;

	$: active = activeProvider($ai);
	$: selected = PROVIDERS.find((p) => p.id === $ai.provider) ?? PROVIDERS[0];

	onMount(async () => {
		cachedCount = await countAnswers();
	});

	function notify(message: string) {
		toast = message;
		clearTimeout(toastTimer);
		toastTimer = setTimeout(() => (toast = ''), 2000);
	}

	function keyValue(id: ProviderId): string {
		return draftKey[id] ?? $ai.keys[id] ?? '';
	}

	function saveKey(id: ProviderId) {
		const value = (draftKey[id] ?? '').trim();
		if (!value) return;
		setKey(id, value);
		draftKey = { ...draftKey, [id]: '' };
		status = { ...status, [id]: { ok: true, text: 'Key saved in this browser.' } };
		notify('API key saved');
	}

	async function fetchModels(id: ProviderId) {
		busy = { ...busy, [id]: 'models' };
		status = { ...status, [id]: null };
		try {
			const models = await listModels(id, keyValue(id) || $ai.keys[id]);
			modelList = { ...modelList, [id]: models };
			status = {
				...status,
				[id]: { ok: true, text: models.length ? `${models.length} models available.` : 'No models came back.' }
			};
			if (!models.length) status = { ...status, [id]: { ok: false, text: 'No models came back for that key.' } };
		} catch (err) {
			status = { ...status, [id]: { ok: false, text: (err as Error).message } };
		} finally {
			busy = { ...busy, [id]: null };
		}
	}

	async function testKey(id: ProviderId) {
		busy = { ...busy, [id]: 'test' };
		status = { ...status, [id]: null };
		try {
			const res = await fetch('/api/ask', {
				method: 'POST',
				headers: { 'content-type': 'application/json' },
				body: JSON.stringify({
					provider: id,
					model: $ai.models[id] ?? PROVIDERS.find((p) => p.id === id)?.defaultModel ?? '',
					key: keyValue(id) || $ai.keys[id],
					question: 'Reply with the single word: ready',
					context: 'Test connection from the StudyFeed settings screen. This is not a study card, it is a connectivity check.'
				})
			});
			const data = (await res.json().catch(() => ({}))) as { answer?: string; error?: string };
			status = { ...status, [id]: res.ok && data.answer ? { ok: true, text: 'Connected. The model replied.' } : { ok: false, text: data.error ?? `Failed (${res.status}).` } };
		} catch (err) {
			status = { ...status, [id]: { ok: false, text: (err as Error).message } };
		} finally {
			busy = { ...busy, [id]: null };
		}
	}

	async function clearCache() {
		await clearAnswers();
		cachedCount = 0;
		notify('Cached answers cleared');
	}

	function resetProgress() {
		clearProgress();
		confirmClear = false;
		notify('Progress cleared');
	}

	$: seenCount = Object.values($progress).filter((p) => p.seen).length;
	$: answered = Object.values($progress).reduce((n, p) => n + p.quizCorrect + p.quizWrong, 0);
	$: isStandalone = browser && window.matchMedia('(display-mode: standalone)').matches;
</script>

<svelte:head><title>Settings — StudyFeed</title></svelte:head>

<AppBar title="Settings" back="/" />

<main class="page page-in">
	<p class="section-label">AI helper</p>
	{#if !$hydrated}
		<div class="group"><ListRow title="Loading your settings" lines={1} /></div>
	{:else}
		<div class="gutter ai-intro">
			<p class="ai-state">
				<Sparkles size={14} />
				<span>
					{#if active.ready}Using {active.def.label}{active.model ? ` · ${active.model}` : ''}{:else}{active.blockedReason ?? 'Not configured'}{/if}
				</span>
			</p>
			<p class="ai-help">
				Paste a key for any provider below. It is stored only in this browser and sent to the
				provider through this app's own server route, so the site never contains your key.
				{configuredProviders($ai).length ? `Configured: ${configuredProviders($ai).join(', ')}.` : ''}
			</p>
		</div>

		<div class="group">
			{#each PROVIDERS as p}
				<button class="provider-row pressable" on:click={() => setProvider(p.id)} aria-pressed={$ai.provider === p.id}>
					<span class="radio" class:on={$ai.provider === p.id} aria-hidden="true"></span>
					<span class="grow">
						<span class="p-name">{p.label}</span>
						<span class="p-meta">
							{#if p.needsKey}
								{$ai.keys[p.id] ? 'key saved' : 'no key yet'}{$ai.models[p.id] ? ` · ${$ai.models[p.id]}` : ''}
							{:else}
								uses the hosting environment variable
							{/if}
						</span>
					</span>
					{#if $ai.provider === p.id}<span class="badge">in use</span>{/if}
				</button>
			{/each}
		</div>

		{#if selected.needsKey}
			<div class="gutter panel">
				<p class="panel-label">{selected.label} API key</p>
				<div class="key-row">
					<label class="input no-margin">
						<input
							type={revealed[selected.id] ? 'text' : 'password'}
							placeholder={selected.keyHint}
							value={keyValue(selected.id)}
							on:input={(e) => (draftKey = { ...draftKey, [selected.id]: e.currentTarget.value })}
							autocomplete="off"
							spellcheck="false"
							aria-label={`${selected.label} API key`}
						/>
					</label>
					<button
						class="icon-btn"
						on:click={() => (revealed = { ...revealed, [selected.id]: !revealed[selected.id] })}
						aria-label={revealed[selected.id] ? 'Hide key' : 'Show key'}
					>
						{#if revealed[selected.id]}<EyeOff size={18} />{:else}<Eye size={18} />{/if}
					</button>
				</div>

				<div class="row-actions">
					<button class="btn btn--primary btn--sm" on:click={() => saveKey(selected.id)} disabled={!keyValue(selected.id).trim()}>
						Save key
					</button>
					<button class="btn btn--secondary btn--sm" on:click={() => fetchModels(selected.id)} disabled={!!busy[selected.id]}>
						{#if busy[selected.id] === 'models'}<LoaderCircle size={14} class="spin" />{/if}
						Fetch models
					</button>
					<button class="btn btn--secondary btn--sm" on:click={() => testKey(selected.id)} disabled={!!busy[selected.id]}>
						{#if busy[selected.id] === 'test'}<LoaderCircle size={14} class="spin" />{/if}
						Test
					</button>
				</div>

				{#if status[selected.id]}
					<p class="status" class:bad={!status[selected.id]?.ok}>
						{#if status[selected.id]?.ok}<CircleCheck size={14} />{:else}<CircleAlert size={14} />{/if}
						{status[selected.id]?.text}
					</p>
				{/if}

				<p class="panel-label">Model</p>
				{#if (modelList[selected.id] ?? []).length}
					<div class="models">
						{#each modelList[selected.id] ?? [] as m}
							<button class="model-chip" class:on={($ai.models[selected.id] ?? selected.defaultModel) === m} on:click={() => setModel(selected.id, m)}>
								{m}
							</button>
						{/each}
					</div>
				{/if}
				<label class="input">
					<input
						type="text"
						placeholder={selected.defaultModel ?? 'model id'}
						value={$ai.models[selected.id] ?? ''}
						on:input={(e) => setModel(selected.id, e.currentTarget.value)}
						autocomplete="off"
						spellcheck="false"
						aria-label={`${selected.label} model id`}
					/>
				</label>
				<p class="hint">
					Model ids change often, so this is editable. Tap “Fetch models” to list what your key can
					use, then pick one.
					{#if selected.console}
						Get a key at <span class="mono">{selected.console}</span>.
					{/if}
				</p>

				{#if $ai.keys[selected.id]}
					<button class="btn btn--danger btn--sm danger-gap" on:click={() => { clearKey(selected.id); notify('Key removed'); }}>
						<Trash2 size={14} /> Remove this key
					</button>
				{/if}
			</div>
		{:else}
			<div class="gutter panel">
				<p class="hint">
					The server option uses <span class="mono">STUDYFEED_AI_KEY</span> (and optionally
					<span class="mono"> STUDYFEED_AI_PROVIDER</span>, <span class="mono">STUDYFEED_AI_MODEL</span>)
					from the hosting environment. Set those on Vercel and nobody needs to paste a key into the
					browser. When you use it, no key is stored here at all.
				</p>
				<div class="row-actions">
					<button class="btn btn--secondary btn--sm" on:click={() => testKey(selected.id)} disabled={!!busy[selected.id]}>
						{#if busy[selected.id] === 'test'}<LoaderCircle size={14} class="spin" />{/if}
						Test connection
					</button>
				</div>
				{#if status[selected.id]}
					<p class="status" class:bad={!status[selected.id]?.ok}>
						{#if status[selected.id]?.ok}<CircleCheck size={14} />{:else}<CircleAlert size={14} />{/if}
						{status[selected.id]?.text}
					</p>
				{/if}
			</div>
		{/if}

		<p class="section-label">Answer cache</p>
		<div class="group">
			<ListRow title="Saved AI answers" value={String(cachedCount)} lines={1} />
		</div>
		<div class="gutter">
			<button class="btn btn--secondary btn--sm danger-gap" on:click={clearCache} disabled={cachedCount === 0}>
				<RefreshCw size={14} /> Clear cached answers
			</button>
		</div>
	{/if}

	<p class="section-label">Appearance</p>
	<div class="group">
		{#each themes as theme}
			{@const Icon = theme.icon}
			<button class="theme-row pressable" on:click={() => setTheme(theme.value)} aria-pressed={$hydrated && $settings.theme === theme.value}>
				<span class="theme-icon"><Icon size={18} /></span>
				<span class="grow">{theme.label}</span>
				{#if $hydrated && $settings.theme === theme.value}<span class="badge">current</span>{/if}
			</button>
		{/each}
	</div>

	<p class="section-label">Your data in this browser</p>
	<div class="group">
		<ListRow title="Cards seen" value={$hydrated ? `${seenCount} of ${totals.cards}` : '—'} lines={1} />
		<ListRow title="Quiz answers recorded" value={$hydrated ? String(answered) : '—'} lines={1} />
		<ListRow title="Saved items" value={$hydrated ? String($bookmarks.length) : '—'} lines={1} />
		<ListRow title="Day streak" value={$hydrated ? String($streak.count) : '—'} lines={1} />
	</div>

	<p class="section-label">Reset</p>
	<div class="group">
		{#if !confirmClear}
			<button class="danger-row pressable" on:click={() => (confirmClear = true)}>Clear progress and streak</button>
		{:else}
			<div class="confirm">
				<p class="confirm-text">This erases every card you have seen and all quiz results. There is no undo.</p>
				<div class="row-actions">
					<button class="btn btn--secondary btn--sm" on:click={() => (confirmClear = false)}>Keep my progress</button>
					<button class="btn btn--danger btn--sm" on:click={resetProgress}>Erase progress</button>
				</div>
			</div>
		{/if}
		<button class="danger-row pressable" on:click={() => { clearBookmarks(); notify('Saved items cleared'); }}>Clear saved items</button>
	</div>

	<p class="section-label">About</p>
	<div class="group">
		<ListRow
			title="StudyFeed"
			subtitle={`${plural(totals.cards, 'card')} and ${totals.topics} mapped topics`}
			meta={isStandalone ? 'Running as an installed app' : 'Add to home screen for offline use'}
		/>
		<ListRow
			title="Content state"
			subtitle="Draft cards are written in original words and need a textbook check before you mark them verified."
		/>
	</div>

	{#if toast}<div class="toast" role="status">{toast}</div>{/if}
</main>

<style>
	.ai-intro {
		padding-bottom: var(--sp-3);
	}

	.ai-state {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		font-weight: 600;
		color: var(--accent);
	}

	.ai-help {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		margin-top: var(--sp-2);
	}

	.provider-row {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		width: 100%;
		min-height: 56px;
		padding: var(--sp-3) var(--sp-4);
	}

	.radio {
		width: 18px;
		height: 18px;
		border-radius: var(--radius-full);
		border: 2px solid var(--border-strong);
		flex: 0 0 auto;
		transition: border-color var(--dur-quick) var(--ease-standard), box-shadow var(--dur-quick) var(--ease-standard);
	}

	.radio.on {
		border-color: var(--accent);
		box-shadow: inset 0 0 0 3px var(--bg), inset 0 0 0 9px var(--accent);
	}

	.p-name {
		display: block;
		font-size: var(--fs-body);
		font-weight: 600;
	}

	.p-meta {
		display: block;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.panel {
		padding-top: var(--sp-4);
	}

	.panel-label {
		font-size: var(--fs-caption);
		font-weight: 700;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--fg-subtle);
		margin: var(--sp-4) 0 var(--sp-2);
	}

	.panel-label:first-child {
		margin-top: 0;
	}

	.key-row {
		display: flex;
		align-items: center;
		gap: var(--sp-1);
	}

	.no-margin {
		margin: 0;
	}

	.row-actions {
		display: flex;
		flex-wrap: wrap;
		gap: var(--sp-2);
		margin-top: var(--sp-2);
	}

	.status {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		color: var(--success);
		margin-top: var(--sp-2);
	}

	.status.bad {
		color: var(--danger);
	}

	.models {
		display: flex;
		flex-wrap: wrap;
		gap: var(--sp-2);
		margin-bottom: var(--sp-3);
		max-height: 168px;
		overflow-y: auto;
	}

	.model-chip {
		padding: var(--sp-1) var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius-full);
		font-size: var(--fs-caption);
		max-width: 100%;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.model-chip.on {
		background: var(--accent);
		color: var(--accent-fg);
	}

	.hint {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		margin-top: var(--sp-2);
	}

	.mono {
		font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
		font-size: var(--fs-caption);
		color: var(--fg-muted);
	}

	.danger-gap {
		margin-top: var(--sp-3);
	}

	.theme-row {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		width: 100%;
		min-height: 52px;
		padding: var(--sp-3) var(--sp-4);
		font-size: var(--fs-body);
	}

	.theme-icon {
		display: inline-flex;
		color: var(--fg-muted);
	}

	.danger-row {
		width: 100%;
		min-height: 52px;
		padding: var(--sp-3) var(--sp-4);
		color: var(--danger);
		font-size: var(--fs-body);
	}

	.confirm {
		padding: var(--sp-3) var(--sp-4);
	}

	.confirm-text {
		font-size: var(--fs-small);
		line-height: 1.5;
		color: var(--fg-muted);
	}
</style>
