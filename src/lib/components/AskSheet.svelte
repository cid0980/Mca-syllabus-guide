<script lang="ts">
	/**
	 * Ask AI about the card on screen.
	 *
	 * The answer may only come from saved cards: the card text is sent as CONTEXT and the server
	 * route holds the "answer only from context" instruction. Answers are cached in IndexedDB, so
	 * asking the same thing twice costs nothing.
	 */
	import { createEventDispatcher } from 'svelte';
	import { Send, LoaderCircle, Copy, Check, CircleAlert, Sparkles, KeyRound } from 'lucide-svelte';
	import type { DeckCard } from '$lib/content';
	import { ask } from '$lib/ai/client';
	import { ai, activeProvider } from '$lib/stores/ai';
	import Sheet from '$lib/components/Sheet.svelte';

	export let open = false;
	export let card: DeckCard | null = null;

	const dispatch = createEventDispatcher<{ close: void }>();

	let question = '';
	let answer = '';
	let cached = false;
	let loading = false;
	let error: string | null = null;
	let copied = false;
	let controller: AbortController | null = null;

	$: provider = activeProvider($ai);
	$: context = card ? buildContext(card) : '';
	$: suggestions = card
		? [
				'Explain this more simply',
				'Give me another real-world example',
				'Why is the correct quiz option right?',
				'What is likely to be asked in the exam?'
		  ]
		: [];

	function buildContext(c: DeckCard): string {
		return [
			`Subject: ${c.subjectCode} (semester ${c.semester}), Module ${c.module}`,
			`Topic: ${c.topic}`,
			`Definition: ${c.definition}`,
			`Explanation: ${c.explanation}`,
			`Example: ${c.example}`,
			c.quiz.map((q, i) => `Quiz ${i + 1}: ${q.q} | options: ${q.options.join(' / ')} | correct: ${q.options[q.answer]} | why: ${q.why}`).join('\n'),
			`Exam tip: ${c.examTip}`
		].join('\n');
	}

	function reset() {
		question = '';
		answer = '';
		error = null;
		cached = false;
		loading = false;
		controller?.abort();
		controller = null;
	}

	function close() {
		reset();
		dispatch('close');
	}

	async function send(text: string) {
		const q = text.trim();
		if (q.length < 2 || loading) return;
		question = q;
		loading = true;
		error = null;
		answer = '';
		controller = new AbortController();
		try {
			const res = await ask(
				{
					provider: provider.def.id,
					model: provider.model,
					key: provider.key || undefined,
					question: q,
					cardId: card?.id,
					context
				},
				controller.signal
			);
			answer = res.answer;
			cached = res.cached;
		} catch (err) {
			if ((err as Error).name !== 'AbortError') error = (err as Error).message;
		} finally {
			loading = false;
		}
	}

	async function copy() {
		try {
			await navigator.clipboard.writeText(answer);
			copied = true;
			setTimeout(() => (copied = false), 1500);
		} catch {
			/* clipboard blocked - the text is selectable anyway */
		}
	}
</script>

<Sheet {open} title="Ask about this card" subtitle={card ? `${card.subjectCode} · ${card.topic}` : ''} on:close={close}>
	{#if !provider.ready}
		<div class="blocked">
			<span class="blocked-icon"><KeyRound size={18} /></span>
			<div class="grow">
				<p class="blocked-title">No AI key yet</p>
				<p class="blocked-text">{provider.blockedReason}</p>
			</div>
			<a class="btn btn--primary btn--sm" href="/settings" on:click={close}>Open Settings</a>
		</div>
	{:else}
		<div class="provider">
			<Sparkles size={14} />
			<span>{provider.def.label}{provider.model ? ` · ${provider.model}` : ''}</span>
			<a class="change" href="/settings" on:click={close}>change</a>
		</div>
	{/if}

	{#if !answer && !loading && !error && card}
		<div class="suggestions">
			{#each suggestions as s}
				<button class="chip" on:click={() => send(s)}>{s}</button>
			{/each}
		</div>
	{/if}

	{#if loading}
		<div class="loading">
			<LoaderCircle size={16} class="spin" />
			<span>Reading the saved card…</span>
		</div>
	{/if}

	{#if error}
		<div class="error" role="alert">
			<span class="error-icon"><CircleAlert size={18} /></span>
			<div class="grow">
				<p class="error-text">{error}</p>
				<button class="btn btn--secondary btn--sm" on:click={() => send(question)}>Try again</button>
			</div>
		</div>
	{/if}

	{#if answer}
		<article class="answer fade-in">
			<p class="answer-text">{answer}</p>
			<div class="answer-foot">
				{#if cached}<span class="badge">saved answer</span>{/if}
				<button class="btn btn--ghost btn--sm" on:click={copy}>
					{#if copied}<Check size={14} /> Copied{:else}<Copy size={14} /> Copy{/if}
				</button>
				<button class="btn btn--ghost btn--sm" on:click={reset}>Ask another</button>
			</div>
		</article>
	{/if}

	<form class="ask-form" on:submit|preventDefault={() => send(question)}>
		<label class="input">
			<input
				data-autofocus
				type="text"
				placeholder="Ask about this card"
				bind:value={question}
				disabled={loading || !provider.ready}
				aria-label="Your question"
			/>
		</label>
		<button class="btn btn--primary send" type="submit" disabled={loading || !provider.ready || question.trim().length < 2}>
			{#if loading}<LoaderCircle size={16} class="spin" /><span>Asking</span>{:else}<Send size={16} /><span>Ask</span>{/if}
		</button>
	</form>

	<p class="fineprint">
		Answers come only from the saved cards. Your key is stored in this browser and sent to
		{provider.def.label} through this app's own server route.
	</p>
</Sheet>

<style>
	.blocked {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
		margin-bottom: var(--sp-4);
	}

	.blocked-icon {
		display: inline-flex;
		color: var(--warning);
	}

	.blocked-title {
		font-size: var(--fs-body);
		font-weight: 600;
	}

	.blocked-text {
		font-size: var(--fs-small);
		color: var(--fg-muted);
	}

	.provider {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
		margin-bottom: var(--sp-3);
	}

	.change {
		color: var(--accent);
		margin-left: auto;
	}

	.suggestions {
		display: flex;
		flex-wrap: wrap;
		gap: var(--sp-2);
		margin-bottom: var(--sp-4);
	}

	.chip {
		padding: var(--sp-2) var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius-full);
		font-size: var(--fs-small);
		transition: transform var(--dur-press) var(--ease-standard), background-color var(--dur-press) var(--ease-standard);
	}

	.chip:active {
		transform: scale(0.96);
		background: var(--fill-strong);
	}

	.loading {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		color: var(--fg-muted);
		padding: var(--sp-3) 0;
	}

	.error {
		display: flex;
		gap: var(--sp-3);
		padding: var(--sp-3);
		background: var(--fill);
		border-left: 2px solid var(--danger);
		border-radius: var(--radius);
		margin-bottom: var(--sp-3);
	}

	.error-icon {
		display: inline-flex;
		color: var(--danger);
	}

	.error-text {
		font-size: var(--fs-small);
		margin-bottom: var(--sp-2);
	}

	.answer {
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
		margin-bottom: var(--sp-3);
	}

	.answer-text {
		font-size: var(--fs-body);
		line-height: 1.6;
		white-space: pre-wrap;
	}

	.answer-foot {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		margin-top: var(--sp-3);
	}

	.answer-foot .badge {
		margin-right: auto;
	}

	.ask-form {
		display: flex;
		gap: var(--sp-2);
		margin-top: var(--sp-2);
	}

	.send {
		flex: 0 0 auto;
		min-width: 92px;
	}

	.fineprint {
		font-size: var(--fs-caption);
		line-height: 1.5;
		color: var(--fg-subtle);
		margin-top: var(--sp-3);
	}
</style>
