import { sveltekit } from '@sveltejs/kit/vite';
import { SvelteKitPWA } from '@vite-pwa/sveltekit';
import { defineConfig } from 'vite';

export default defineConfig({
	server: {
		host: '0.0.0.0',
		port: 5173,
		// allows the app to be opened through a proxy / tunnel host as well as localhost
		allowedHosts: true
	},
	preview: {
		host: '0.0.0.0',
		port: 4173,
		allowedHosts: true
	},
	// lucide ships raw .svelte files; Vite must compile them for SSR rather than
	// handing them to Node's ESM loader (which rejects the .svelte extension).
	ssr: {
		noExternal: ['lucide-svelte']
	},
	plugins: [
		sveltekit(),
		SvelteKitPWA({
			registerType: 'autoUpdate',
			manifest: false, // Using static/manifest.webmanifest directly
			workbox: {
				globPatterns: ['client/**/*.{js,css,ico,png,svg,webp,webmanifest,json}']
			},
			devOptions: {
				enabled: true,
				type: 'module'
			}
		})
	]
});
