<script lang="ts">
	import '@fontsource-variable/inter';
	import '../app.css';

	import { onMount } from 'svelte';
	import { navigating } from '$app/stores';
	import BottomNav from '$lib/components/BottomNav.svelte';
	import { hydrateAll } from '$lib/stores/hydrate';

	onMount(async () => {
		hydrateAll();

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
			/* service worker unavailable (sandboxed preview) — app still works */
		}
	});
</script>

<div class="route-progress" class:active={!!$navigating} aria-hidden="true"></div>
<slot />
<BottomNav />

<style>
	.route-progress {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		height: 2px;
		background: var(--accent);
		transform: scaleX(0);
		transform-origin: left;
		transition: transform 0.3s ease-out, opacity 0.2s ease 0.2s;
		opacity: 0;
		z-index: 60;
		pointer-events: none;
	}

	.route-progress.active {
		transform: scaleX(0.7);
		opacity: 1;
		animation: creep 6s ease-out forwards;
	}

	@keyframes creep {
		to {
			transform: scaleX(0.95);
		}
	}
</style>
