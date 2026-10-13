/** App settings. key `sf:settings` -> { theme }. Theme is applied pre-paint by src/app.html. */
import { browser } from '$app/environment';
import { writable } from 'svelte/store';
import type { Settings } from '$lib/types';
import { KEYS, readJSON, writeJSON } from '$lib/storage';

const DEFAULTS: Settings = { theme: 'system' };

export const settings = writable<Settings>(DEFAULTS);

let ready = false;

export function initSettings(): void {
	if (!browser || ready) return;
	ready = true;
	const stored = readJSON<Settings>(KEYS.settings, DEFAULTS);
	settings.set(stored);
	applyTheme(stored.theme);
	settings.subscribe((v) => {
		writeJSON(KEYS.settings, v);
		applyTheme(v.theme);
	});
}

export function applyTheme(theme: Settings['theme']): void {
	if (!browser) return;
	const dark =
		theme === 'dark' ||
		(theme === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
	document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
}

export function setTheme(theme: Settings['theme']): void {
	settings.update((s) => ({ ...s, theme }));
}

/** Resolved theme actually on screen right now. */
export function resolvedTheme(): 'dark' | 'light' {
	if (!browser) return 'light';
	return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
}
