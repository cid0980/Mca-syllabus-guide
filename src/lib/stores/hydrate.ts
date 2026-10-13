/**
 * One switch for "browser data is ready".
 *
 * The first render (server, and the client's first hydration pass) must be identical,
 * so every store starts from its empty value and is filled in onMount. Screens that
 * change shape depending on stored data wait for `$hydrated`.
 */
import { browser } from '$app/environment';
import { writable } from 'svelte/store';
import { initProgress } from '$lib/stores/progress';
import { initBookmarks } from '$lib/stores/bookmarks';
import { initSettings } from '$lib/stores/settings';

export const hydrated = writable(false);

let done = false;

export function hydrateAll(): void {
	if (done || !browser) return;
	done = true;
	initProgress();
	initBookmarks();
	initSettings();
	hydrated.set(true);
}
