/**
 * Server-rendered shell so the first paint already has the real layout and text,
 * then browser-only data (progress, bookmarks, settings) is hydrated in onMount.
 * See $lib/stores/hydrate.ts - nothing reads localStorage during the first render.
 */
export const ssr = true;
export const prerender = false;
