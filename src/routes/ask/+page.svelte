<script lang="ts">
	/**
	 * Ask about a card — a page, not a pop-up.
	 *
	 * Why a page: a sheet can be dismissed by accident and the question is gone. Here the thread is
	 * stored per card in IndexedDB, so closing the app and coming back shows the same conversation,
	 * and the URL (`/ask?card=<id>`) can be reloaded or shared. The header carries the way back to
	 * the exact card the question came from, and the context block under it opens the card too.
	 */
	import type { PageData } from './$types';
	import { onMount, tick } from 'svelte';
	import {
		Send,
		LoaderCircle,
		Copy,
		Check,
		CircleAlert,
		Sparkles,
		KeyRound,
		Trash2,
		RotateCcw,
		BookOpen,
		MessagesSquare
	} from 'lucide-svelte';
	import { ask } from '$lib/ai/client';
	import { ai, activeProvider } from '$lib/stores/ai';
	import { loadThread, saveThread, clearThread, type ChatMessage } from '$lib/ai/threads';
	import { shortName } from '$lib/labels';
	import AppBar from '$lib/components/AppBar.svelte';
	import Skeleton from '$lib/components/Skeleton.svelte';
	import ErrorState from '$lib/components/ErrorState.svelte';

	export let data: PageData;

	let messages: ChatMessage[] = [];
	let question = '';
	let loadingThread = true;
	let sending = false;
	let error: string | null = null;
	let copiedAt = -1;
	let confirmClear = false;
	let scroller: HTMLElement;
	let input: HTMLInputElement;
	let controller: AbortController | null = null;

	$: provider = activeProvider($ai);
	$: card = data.found ? data.card : null;
	$: context = card ? buildContext(card) : '';
	$: suggestions = [
		'Explain this more simply',
		'Give me another real-world example',
		'Why is the correct quiz option right?',
		'What is likely to be asked in the exam?'
	];

	function buildContext(c: NonNullable<typeof card>): string {
		return [
			`Subject: ${c.subjectCode} (semester ${c.semester}), Module ${c.module}`,
			`Topic: ${c.topic}`,
			`Definition: ${c.definition}`,
			`Explanation: ${c.explanation}`,
			`Example: ${c.example}`,
			c.quiz
				.map(
					(q, i) =>
						`Quiz ${i + 1}: ${q.q} | options: ${q.options.join(' / ')} | correct: ${q.options[q.answer]} | why: ${q.why}`
				)
				.join('\n'),
			`Exam tip: ${c.examTip}`
		].join('\n');
	}

	onMount(async () => {
		if (!card) {
			loadingThread = false;
			return;
		}
		const thread = await loadThread(card.id);
		messages = thread?.messages ?? [];
		loadingThread = false;
		await scrollToEnd(false);
	});

	async function scrollToEnd(smooth = true) {
		await tick();
		if (!scroller) return;
		scroller.scrollTo({ top: scroller.scrollHeight, behavior: smooth ? 'smooth' : 'auto' });
	}

	async function persist() {
		if (card) await saveThread(card.id, messages);
	}

	async function send(text: string) {
		const q = text.trim();
		if (!card || q.length < 2 || sending) return;
		question = '';
		error = null;
		sending = true;

		// the question is stored the moment it is asked, so a closed app cannot lose it
		messages = [...messages, { role: 'user', text: q, at: Date.now() }];
		await persist();
		await scrollToEnd();

		controller = new AbortController();
		try {
			const res = await ask(
				{
					provider: provider.def.id,
					model: provider.model,
					key: provider.key || undefined,
					question: q,
					cardId: card.id,
					context
				},
				controller.signal
			);
			messages = [...messages, { role: 'assistant', text: res.answer, at: Date.now(), cached: res.cached }];
		} catch (err) {
			if ((err as Error).name !== 'AbortError') {
				error = (err as Error).message;
				messages = [...messages, { role: 'assistant', text: (err as Error).message, at: Date.now(), failed: true }];
			}
		} finally {
			sending = false;
			controller = null;
			await persist();
			await scrollToEnd();
		}
	}

	/** Re-asks the question that failed, without making the student type it again. */
	async function retryLast() {
		const lastQuestion = [...messages].reverse().find((m) => m.role === 'user');
		if (!lastQuestion) return;
		messages = messages.filter((m) => !m.failed);
		await persist();
		await send(lastQuestion.text);
	}

	async function copy(text: string, at: number) {
		try {
			await navigator.clipboard.writeText(text);
			copiedAt = at;
			setTimeout(() => (copiedAt = -1), 1500);
		} catch {
			/* clipboard blocked - the text stays selectable */
		}
	}

	async function doClear() {
		if (!card) return;
		messages = [];
		confirmClear = false;
		await clearThread(card.id);
		await scrollToEnd(false);
		input?.focus();
	}
</script>

<svelte:head><title>{card ? `Ask · ${card.topic}` : 'Ask'} — StudyFeed</title></svelte:head>

<div class="ask-page">
	{#if !data.found}
		<AppBar title="Ask" back="/explore" />
		<main class="page">
			<ErrorState
				title="No card to ask about"
				message="This chat is opened from a card. Open a topic from the syllabus, then tap Ask on its card."
				retryLabel="Browse the syllabus"
				on:retry={() => (location.href = '/explore')}
			/>
		</main>
	{:else}
		<AppBar title="Ask" subtitle={card ? card.topic : ''} back={data.from} />

		<main class="thread" bind:this={scroller}>
			<a class="context pressable" href={data.from}>
				<span class="ctx-avatar nums" aria-hidden="true">{shortName(card?.subjectCode ?? "")}</span>
				<span class="grow">
					<span class="ctx-title truncate">{card?.topic}</span>
					<span class="ctx-sub truncate">
						{card?.subjectCode} · Module {card?.module}
						{#if data.cardCount}· card {data.cardIndex} of {data.cardCount}{/if}
					</span>
				</span>
				<span class="ctx-open"><BookOpen size={16} /> Card</span>
			</a>

			{#if !provider.ready}
				<div class="blocked">
					<span class="blocked-icon"><KeyRound size={18} /></span>
					<div class="grow">
						<p class="blocked-title">No AI key yet</p>
						<p class="blocked-text">{provider.blockedReason}</p>
					</div>
					<a class="btn btn--primary btn--sm" href="/settings">Open Settings</a>
				</div>
			{/if}

			<div class="meta">
				<span class="provider">
					<Sparkles size={13} />
					{provider.def.label}{provider.model ? ` · ${provider.model}` : ''}
				</span>
				{#if !loadingThread && messages.length}
					{#if confirmClear}
						<span class="confirm">
							<button class="link danger" on:click={doClear}>Clear this chat</button>
							<button class="link" on:click={() => (confirmClear = false)}>Keep</button>
						</span>
					{:else}
						<button class="link" on:click={() => (confirmClear = true)} aria-label="Clear this chat">
							<Trash2 size={13} /> Clear
						</button>
					{/if}
				{/if}
			</div>

			{#if loadingThread}
				<div class="loading-thread"><Skeleton variant="lines" /><Skeleton variant="lines" /></div>
			{:else if messages.length === 0}
				<div class="empty">
					<span class="empty-icon"><MessagesSquare size={20} /></span>
					<h2 class="empty-title">Ask about {card?.topic}</h2>
					<p class="empty-text">
						The answer comes only from this saved card. Nothing you type here leaves the browser except
						the question and the card text sent to {provider.def.label} through this app's own server
						route, and this chat is kept on this device so you can come back to it.
					</p>
					<div class="suggestions">
						{#each suggestions as s}
							<button class="chip" on:click={() => send(s)} disabled={!provider.ready || sending}>{s}</button>
						{/each}
					</div>
				</div>
			{:else}
				<div class="messages">
					{#each messages as m (m.at + m.role)}
						{#if m.role === 'user'}
							<article class="msg user">
								<p class="bubble">{m.text}</p>
							</article>
						{:else if m.failed}
							<article class="msg">
								<div class="failure" role="alert">
									<span class="failure-icon"><CircleAlert size={16} /></span>
									<p class="failure-text">{m.text}</p>
								</div>
								<button class="btn btn--secondary btn--sm" on:click={retryLast}>
									<RotateCcw size={13} /> Try that question again
								</button>
							</article>
						{:else}
							<article class="msg">
								<p class="answer">{m.text}</p>
								<div class="answer-foot">
									{#if m.cached}<span class="badge">saved answer</span>{/if}
									<button class="btn btn--ghost btn--sm" on:click={() => copy(m.text, m.at)}>
										{#if copiedAt === m.at}<Check size={13} /> Copied{:else}<Copy size={13} /> Copy{/if}
									</button>
								</div>
							</article>
						{/if}
					{/each}
					{#if sending}
						<article class="msg">
							<p class="thinking"><LoaderCircle size={15} class="spin" /> Reading the saved card…</p>
						</article>
					{/if}
					{#if error && !sending}
						<article class="msg">
							<button class="btn btn--secondary btn--sm" on:click={retryLast}>
								<RotateCcw size={13} /> Try again
							</button>
						</article>
					{/if}
				</div>
			{/if}
		</main>

		<form class="composer" on:submit|preventDefault={() => send(question)}>
			<label class="input no-margin">
				<input
					bind:this={input}
					type="text"
					placeholder={sending ? 'Waiting for an answer…' : 'Ask about this card'}
					bind:value={question}
					disabled={sending || !provider.ready}
					autocomplete="off"
					aria-label="Your question"
				/>
			</label>
			<button
				class="btn btn--primary send"
				type="submit"
				disabled={sending || !provider.ready || question.trim().length < 2}
			>
				{#if sending}<LoaderCircle size={16} class="spin" /><span>Asking</span>{:else}<Send size={16} /><span>Ask</span>{/if}
			</button>
		</form>
	{/if}
</div>

<style>
	.ask-page {
		display: flex;
		flex-direction: column;
		height: 100dvh;
		max-width: 600px;
		margin: 0 auto;
		padding-bottom: calc(var(--nav-h) + env(safe-area-inset-bottom));
		background: var(--bg);
	}

	.thread {
		flex: 1;
		min-height: 0;
		overflow-y: auto;
		-webkit-overflow-scrolling: touch;
		padding: var(--sp-3) var(--sp-4) var(--sp-4);
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
	}

	.context {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-2) var(--sp-3);
		border: 1px solid var(--border);
		border-radius: var(--radius-lg);
	}

	.ctx-avatar {
		display: grid;
		place-items: center;
		width: 32px;
		height: 32px;
		border-radius: var(--radius-full);
		background: var(--fill);
		font-size: var(--fs-caption);
		font-weight: 700;
		flex: 0 0 auto;
	}

	.ctx-title {
		display: block;
		font-size: var(--fs-small);
		font-weight: 600;
	}

	.ctx-sub {
		display: block;
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.ctx-open {
		display: inline-flex;
		align-items: center;
		gap: var(--sp-1);
		font-size: var(--fs-caption);
		font-weight: 600;
		color: var(--accent);
		flex: 0 0 auto;
	}

	.blocked {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius);
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

	.meta {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		font-size: var(--fs-caption);
		color: var(--fg-subtle);
	}

	.provider {
		display: inline-flex;
		align-items: center;
		gap: var(--sp-1);
		min-width: 0;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.confirm {
		display: inline-flex;
		gap: var(--sp-3);
		margin-left: auto;
	}

	.link {
		display: inline-flex;
		align-items: center;
		gap: var(--sp-1);
		color: var(--accent);
		font-size: var(--fs-caption);
		font-weight: 600;
		margin-left: auto;
	}

	.link.danger {
		color: var(--danger);
	}

	.confirm .link {
		margin-left: 0;
	}

	.loading-thread {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
	}

	.empty {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
		padding-top: var(--sp-3);
	}

	.empty-icon {
		display: inline-flex;
		color: var(--fg-subtle);
	}

	.empty-title {
		font-size: var(--fs-title);
		font-weight: 700;
	}

	.empty-text {
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
	}

	.suggestions {
		display: flex;
		flex-wrap: wrap;
		gap: var(--sp-2);
		margin-top: var(--sp-2);
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

	.chip:disabled {
		opacity: 0.5;
		pointer-events: none;
	}

	.messages {
		display: flex;
		flex-direction: column;
		gap: var(--sp-3);
	}

	.msg {
		display: flex;
		flex-direction: column;
		gap: var(--sp-2);
		max-width: 100%;
	}

	.msg.user {
		align-items: flex-end;
	}

	.bubble {
		padding: var(--sp-3);
		background: var(--accent);
		color: var(--accent-fg);
		border-radius: var(--radius-lg);
		font-size: var(--fs-body);
		line-height: 1.5;
		max-width: 85%;
		white-space: pre-wrap;
	}

	.answer {
		padding: var(--sp-3);
		background: var(--fill);
		border-radius: var(--radius-lg);
		font-size: var(--fs-body);
		line-height: 1.6;
		white-space: pre-wrap;
	}

	.answer-foot {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
	}

	.answer-foot .badge {
		margin-right: auto;
	}

	.failure {
		display: flex;
		gap: var(--sp-2);
		padding: var(--sp-3);
		background: var(--fill);
		border-left: 2px solid var(--danger);
		border-radius: var(--radius);
	}

	.failure-icon {
		display: inline-flex;
		color: var(--danger);
		flex: 0 0 auto;
	}

	.failure-text {
		font-size: var(--fs-small);
		line-height: 1.5;
	}

	.thinking {
		display: flex;
		align-items: center;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		color: var(--fg-muted);
	}

	.composer {
		display: flex;
		gap: var(--sp-2);
		padding: var(--sp-3) var(--sp-4);
		border-top: 1px solid var(--border);
		background: var(--bg);
	}

	.no-margin {
		margin: 0;
	}

	.send {
		flex: 0 0 auto;
		min-width: 92px;
	}
</style>
