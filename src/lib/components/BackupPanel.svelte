<script lang="ts">
	/**
	 * Export / import of everything StudyFeed stores in this browser.
	 *
	 * Why: progress, saved cards and quiz accuracy live in localStorage only. Clearing browser data
	 * (or a private window) wipes them, and iOS may evict storage after long periods. A file is the
	 * only real backup, and it needs no account, no backend and no paid service.
	 *
	 * All reads and writes go through $lib/storage.ts, which wraps localStorage in try/catch, so a
	 * blocked or full storage can never crash the screen.
	 */
	import {
		Download,
		Upload,
		LoaderCircle,
		CircleAlert,
		CircleCheck,
		FileJson,
		X
	} from 'lucide-svelte';
	import { browser } from '$app/environment';
	import { KEYS, readJSON, writeJSON } from '$lib/storage';
	import { progress, streak } from '$lib/stores/progress';
	import { bookmarks } from '$lib/stores/bookmarks';
	import { settings } from '$lib/stores/settings';
	import { hydrated } from '$lib/stores/hydrate';
	import { readSessions } from '$lib/quiz';
	import {
		buildBackup,
		sanitiseBackup,
		countsOf,
		backupFileName,
		type BackupCounts,
		type BackupQuizRun
	} from '$lib/backup';

	let exporting = false;
	let importing = false;
	let fileInput: HTMLInputElement;
	let message: { tone: 'ok' | 'bad'; text: string } | null = null;
	let pending: { name: string; counts: BackupCounts; data: Extract<ReturnType<typeof sanitiseBackup>, { ok: true }> } | null =
		null;

	/** what this browser holds right now */
	$: mine = countsOf({
		progress: $progress,
		bookmarks: $bookmarks,
		quizzes: $hydrated ? readSessions() : []
	});

	async function exportBackup() {
		if (!browser) return;
		exporting = true;
		message = null;
		try {
			const quizzes: BackupQuizRun[] = readSessions();
			const file = buildBackup({
				progress: $progress,
				bookmarks: $bookmarks,
				streak: $streak,
				settings: $settings,
				quizzes
			});
			const counts = countsOf(file);
			if (counts.cards === 0 && counts.bookmarks === 0 && counts.quizRuns === 0) {
				message = { tone: 'bad', text: 'Nothing to export yet: swipe a card or save one first.' };
				return;
			}
			const blob = new Blob([JSON.stringify(file, null, 2)], { type: 'application/json' });
			const url = URL.createObjectURL(blob);
			const link = document.createElement('a');
			link.href = url;
			link.download = backupFileName();
			document.body.appendChild(link);
			link.click();
			link.remove();
			setTimeout(() => URL.revokeObjectURL(url), 2000);
			message = {
				tone: 'ok',
				text: `Exported ${counts.cards} tracked cards, ${counts.bookmarks} saved items and ${counts.quizRuns} quiz runs.`
			};
		} catch (err) {
			message = { tone: 'bad', text: `Export failed: ${(err as Error).message}` };
		} finally {
			exporting = false;
		}
	}

	async function pickFile(event: Event) {
		const input = event.currentTarget as HTMLInputElement;
		const file = input.files?.[0];
		if (!file) return;
		message = null;
		importing = true;
		try {
			if (file.size > 5_000_000) throw new Error('that file is larger than 5 MB, so it is not a StudyFeed progress file');
			const text = await file.text();
			const parsed = sanitiseBackup(JSON.parse(text));
			if (!parsed.ok) {
				message = { tone: 'bad', text: parsed.error };
				return;
			}
			pending = { name: file.name, counts: countsOf(parsed), data: parsed };
		} catch (err) {
			const reason = err instanceof SyntaxError ? 'that file is not valid JSON' : (err as Error).message;
			message = { tone: 'bad', text: `Could not read the file: ${reason}.` };
		} finally {
			importing = false;
			input.value = '';
		}
	}

	async function applyImport() {
		if (!pending) return;
		importing = true;
		try {
			writeJSON(KEYS.progress, pending.data.progress);
			writeJSON(KEYS.bookmarks, pending.data.bookmarks);
			writeJSON(KEYS.streak, pending.data.streak);
			writeJSON(KEYS.settings, pending.data.settings);
			writeJSON(KEYS.quiz, pending.data.quizzes);

			// quota or a blocked store fails silently, so read it back before claiming success
			const landed = readJSON<Record<string, unknown>>(KEYS.progress, {});
			if (Object.keys(landed).length !== pending.counts.cards) {
				throw new Error('this browser refused to store the file (storage may be full or blocked)');
			}
			const { cards, bookmarks: saved, quizRuns } = pending.counts;
			message = { tone: 'ok', text: `Restored ${cards} tracked cards, ${saved} saved items and ${quizRuns} quiz runs. Reloading…` };
			pending = null;
			setTimeout(() => location.reload(), 800);
		} catch (err) {
			message = { tone: 'bad', text: `Import failed: ${(err as Error).message}` };
			importing = false;
		}
	}
</script>

<div class="panel">
	<p class="summary">
		This browser holds <strong class="nums">{mine.cards}</strong> tracked cards,
		<strong class="nums">{mine.bookmarks}</strong> saved items and
		<strong class="nums">{mine.quizRuns}</strong> quiz runs.
	</p>

	<div class="buttons">
		<button class="btn btn--primary" on:click={exportBackup} disabled={exporting || importing}>
			{#if exporting}<LoaderCircle size={16} class="spin" /><span>Preparing</span>{:else}<Download size={16} /><span>Export progress</span>{/if}
		</button>
		<button class="btn btn--secondary" on:click={() => fileInput?.click()} disabled={exporting || importing}>
			{#if importing}<LoaderCircle size={16} class="spin" /><span>Reading</span>{:else}<Upload size={16} /><span>Import progress</span>{/if}
		</button>
		<input
			bind:this={fileInput}
			class="hidden-input"
			type="file"
			accept="application/json,.json"
			on:change={pickFile}
			aria-label="Choose a StudyFeed progress file"
		/>
	</div>

	{#if message}
		<p class="status" class:bad={message.tone === 'bad'} role="status">
			<span class="status-icon">
				{#if message.tone === 'ok'}<CircleCheck size={15} />{:else}<CircleAlert size={15} />{/if}
			</span>
			{message.text}
		</p>
	{/if}

	{#if pending}
		<div class="confirm" role="alertdialog" aria-label="Confirm import">
			<p class="confirm-head">
				<span class="confirm-icon"><FileJson size={15} /></span>
				<span class="grow"><strong>{pending.name}</strong></span>
				<button class="icon-btn small" on:click={() => (pending = null)} aria-label="Cancel the import">
					<X size={16} />
				</button>
			</p>
			<p class="confirm-text">
				{pending.counts.cards} tracked cards, {pending.counts.bookmarks} saved items and
				{pending.counts.quizRuns} quiz runs. Importing <strong>replaces</strong> what is in this browser
				now ({mine.cards} tracked cards).
			</p>
			<div class="confirm-actions">
				<button class="btn btn--secondary btn--sm" on:click={() => (pending = null)}>Cancel</button>
				<button class="btn btn--primary btn--sm" on:click={applyImport} disabled={importing}>
					{#if importing}<LoaderCircle size={14} class="spin" />{/if}
					Replace and import
				</button>
			</div>
		</div>
	{/if}

	<p class="note">
		The file is plain JSON: your cards marked read, saved cards, quiz accuracy, streak and theme. Your AI API
		keys are never included. Keep it in Drive, or email it to yourself, then import it on a new
		phone or after clearing browser data. No account and no server are involved.
	</p>
</div>

<style>
	.panel {
		margin: var(--sp-3) var(--sp-4) 0;
		padding: var(--sp-3);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
	}

	.summary {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.summary strong {
		color: var(--fg);
		font-weight: 600;
	}

	.buttons {
		display: flex;
		gap: var(--sp-2);
		margin-top: var(--sp-3);
		flex-wrap: wrap;
	}

	.buttons .btn {
		flex: 1;
		min-width: 150px;
	}

	.hidden-input {
		display: none;
	}

	.status {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-2);
		margin-top: var(--sp-3);
		font-size: var(--fs-small);
		line-height: 1.5;
		color: var(--success);
	}

	.status.bad {
		color: var(--danger);
	}

	.status-icon {
		display: inline-flex;
		flex: 0 0 auto;
		margin-top: 1px;
	}

	.confirm {
		margin-top: var(--sp-3);
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
	}

	.confirm-head {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-small);
	}

	.confirm-icon {
		display: inline-flex;
		color: var(--fg-muted);
	}

	.icon-btn.small {
		width: 28px;
		height: 28px;
	}

	.confirm-text {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-muted);
		margin-top: var(--sp-2);
	}

	.confirm-actions {
		display: flex;
		gap: var(--sp-2);
		margin-top: var(--sp-3);
	}

	.note {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		margin-top: var(--sp-3);
	}
</style>
