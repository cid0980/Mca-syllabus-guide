<script lang="ts">
	import '@fontsource-variable/inter';
	import '../app.css';

	import { onMount } from 'svelte';
	import { page, navigating } from '$app/stores';
	import { goto } from '$app/navigation';
	import BottomNav from '$lib/components/BottomNav.svelte';
	import { hydrateAll } from '$lib/stores/hydrate';

	onMount(async () => {
		hydrateAll();

		/**
		 * Offline shell fallback.
		 *
		 * Pages that are prerendered are served straight from the service worker cache. A page
		 * that is NOT prerendered (a topic definition, say) reaches the worker with no network,
		 * so the worker serves the prerendered home page instead. The address bar still shows
		 * the real URL, but the markup is the home page.
		 *
		 * SvelteKit keeps the route the server rendered in `$page.route.id`, so a home-page
		 * route under any other pathname means the fallback was served. Re-running the router in
		 * the browser fixes it: every load function is universal (+page.ts), so it runs here from
		 * the cached data chunks and the right page appears with no network at all.
		 */
		if ($page.route.id === '/' && $page.url.pathname !== '/') {
			goto($page.url.pathname + $page.url.search, { replaceState: true, noScroll: true }).catch(
				() => {
					/* route could not be resolved offline - the shell stays on screen */
				}
			);
		}

		if (import.meta.env.DEV) {
			// earlier builds registered a dev service worker; it caches stale assets and makes
			// everything feel slow, so clear it out in dev
			if ('serviceWorker' in navigator) {
				const regs = await navigator.serviceWorker.getRegistrations();
				await Promise.all(regs.map((r) => r.unregister()));
			}
			if ('caches' in window) {
				const keys = await caches.keys();
				await Promise.all(keys.map((k) => caches.delete(k)));
			}
			return;
		}

		try {
			const { registerSW } = await import('virtual:pwa-register');
			registerSW({ immediate: true });
		} catch {
			/* service worker unavailable (sandboxed preview) - app still works */
		}
	});
</script>

<div class="route-progress" class:active={!!$navigating} aria-hidden="true"></div>

<!--
	A keyed wrapper: the key changes on every navigation, so the entry animation replays.
	This is what makes moving between pages visible instead of instant. Pathname only, so
	query-only changes (?card=..., ?mode=...) do not re-animate the whole screen.
-->
{#key $page.url.pathname}
	<div class="route">
		<slot />
	</div>
{/key}

<BottomNav />

<style>
	.route-progress {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		height: 3px;
		background: var(--accent);
		transform: scaleX(0);
		transform-origin: left;
		transition: transform 0.4s var(--ease-standard), opacity 0.2s ease 0.25s;
		opacity: 0;
		z-index: 60;
		pointer-events: none;
	}

	.route-progress.active {
		transform: scaleX(0.75);
		opacity: 1;
		animation: creep 8s var(--ease-standard) forwards;
	}

	@keyframes creep {
		to {
			transform: scaleX(0.96);
		}
	}
</style>
