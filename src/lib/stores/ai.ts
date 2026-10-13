/**
 * AI configuration, stored in this browser only (key `sf:ai`).
 *
 * The key never ships with the site: it lives in localStorage, is sent to this app's own
 * /api/ask route, and is forwarded from there to the provider the user picked.
 */
import { browser } from '$app/environment';
import { get, writable } from 'svelte/store';
import { KEYS, readJSON, writeJSON } from '$lib/storage';
import { PROVIDERS, providerById, type ProviderId } from '$lib/ai/providers';

export interface AiConfig {
	provider: ProviderId;
	keys: Partial<Record<ProviderId, string>>;
	models: Partial<Record<ProviderId, string>>;
}

const DEFAULTS: AiConfig = { provider: 'gemini', keys: {}, models: {} };

export const ai = writable<AiConfig>(DEFAULTS);

let ready = false;

export function initAi(): void {
	if (!browser || ready) return;
	ready = true;
	const stored = { ...DEFAULTS, ...readJSON<Partial<AiConfig>>(KEYS.ai, {}) };
	ai.set({ provider: stored.provider, keys: { ...stored.keys }, models: { ...stored.models } });
	let t: ReturnType<typeof setTimeout> | undefined;
	ai.subscribe((v) => {
		clearTimeout(t);
		t = setTimeout(() => writeJSON(KEYS.ai, v), 250);
	});
}

export function setProvider(id: ProviderId): void {
	ai.update((c) => ({ ...c, provider: id }));
}

export function setKey(id: ProviderId, key: string): void {
	ai.update((c) => ({ ...c, keys: { ...c.keys, [id]: key.trim() } }));
}

export function clearKey(id: ProviderId): void {
	ai.update((c) => {
		const keys = { ...c.keys };
		delete keys[id];
		return { ...c, keys };
	});
}

export function setModel(id: ProviderId, model: string): void {
	ai.update((c) => ({ ...c, models: { ...c.models, [id]: model.trim() } }));
}

export interface ActiveProvider {
	def: ReturnType<typeof providerById>;
	model: string;
	key: string;
	ready: boolean;
	blockedReason: string | null;
}

/** The provider Ask will actually use, and whether it is usable right now. */
export function activeProvider(config: AiConfig = get(ai)): ActiveProvider {
	const def = providerById(config.provider);
	const key = config.keys[def.id] ?? '';
	const model = config.models[def.id] ?? def.defaultModel ?? '';

	if (def.needsKey && !key) {
		return { def, model, key, ready: false, blockedReason: `Add your ${def.label} API key in Settings.` };
	}
	if (!model && def.needsKey) {
		return { def, model, key, ready: false, blockedReason: `Pick a model for ${def.label} in Settings.` };
	}
	return { def, model, key, ready: true, blockedReason: null };
}

export function configuredProviders(config: AiConfig = get(ai)): string[] {
	return PROVIDERS.filter((p) => p.needsKey && config.keys[p.id]).map((p) => p.label);
}
