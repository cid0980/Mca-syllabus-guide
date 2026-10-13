/**
 * Where the student actually stopped studying.
 *
 * This used to be written whenever a feed screen opened, which made Home say "Continue" for a deck
 * that had only been glanced at. It is now written only by a real study action:
 *
 *   - marking a card as read
 *   - answering a quiz question that belongs to that deck
 *
 * A store (not a raw localStorage read) so "Clear progress" can drop the continue point and every
 * screen updates immediately, without a reload.
 */
import { browser } from '$app/environment';
import { get, writable } from 'svelte/store';
import { KEYS, readJSON, removeKey, writeJSON } from '$lib/storage';

export interface LastOpened {
	code: string;
	module: string;
	cardId: string;
	at: number;
}

export const lastOpened = writable<LastOpened | null>(null);

let ready = false;

export function initLastOpened(): void {
	if (!browser || ready) return;
	ready = true;
	const stored = readJSON<LastOpened | null>(KEYS.lastOpened, null);
	lastOpened.set(stored && stored.code && stored.module ? stored : null);
	lastOpened.subscribe((value) => {
		if (value) writeJSON(KEYS.lastOpened, value);
	});
}

/** Records the card a study action happened on. */
export function rememberCard(code: string, module: string, cardId: string): void {
	if (!browser || !code || !module || !cardId) return;
	lastOpened.set({ code, module, cardId, at: Date.now() });
}

export function forgetLastOpened(): void {
	lastOpened.set(null);
	removeKey(KEYS.lastOpened);
}

export function currentLastOpened(): LastOpened | null {
	return get(lastOpened);
}
