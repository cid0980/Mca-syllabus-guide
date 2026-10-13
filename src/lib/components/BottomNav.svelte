<script lang="ts">
	/**
	 * Instagram-style tab bar: outline + grey when idle, solid + full-contrast when active,
	 * with a press state so a tap registers before the page changes.
	 */
	import { page } from '$app/stores';
	import { House, BookOpen, Bookmark, GraduationCap, ChartNoAxesColumn } from 'lucide-svelte';

	const items = [
		{ href: '/', label: 'Home', icon: House },
		{ href: '/explore', label: 'Syllabus', icon: BookOpen },
		{ href: '/saved', label: 'Saved', icon: Bookmark },
		{ href: '/quiz', label: 'Quiz', icon: GraduationCap },
		{ href: '/progress', label: 'Progress', icon: ChartNoAxesColumn }
	];

	$: path = $page.url.pathname;

	function active(href: string): boolean {
		if (href === '/')
			return (
				path === '/' ||
				path.startsWith('/subject') ||
				path.startsWith('/feed') ||
				path.startsWith('/exam')
			);
		if (href === '/explore') return path.startsWith('/explore') || path.startsWith('/topic');
		return path.startsWith(href);
	}
</script>

<nav aria-label="Main">
	<div class="inner">
		{#each items as item}
			{@const Icon = item.icon}
			{@const on = active(item.href)}
			<a
				href={item.href}
				class="tab pressable"
				class:on
				aria-current={on ? 'page' : undefined}
				data-sveltekit-preload-data="tap"
			>
				<span class="glyph"><Icon size={24} strokeWidth={on ? 2.4 : 1.8} /></span>
				<span class="label">{item.label}</span>
			</a>
		{/each}
	</div>
</nav>

<style>
	nav {
		position: fixed;
		left: 0;
		right: 0;
		bottom: 0;
		z-index: 40;
		background: var(--bg);
		border-top: 1px solid var(--border);
		padding-bottom: env(safe-area-inset-bottom);
	}

	.inner {
		max-width: 600px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		height: var(--nav-h);
	}

	.tab {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 2px;
		color: var(--fg-subtle);
	}

	.glyph {
		display: inline-flex;
		line-height: 0;
	}

	/* solid glyph + full contrast = unmistakably selected */
	.tab.on {
		color: var(--fg);
	}

	.tab.on .glyph :global(svg) {
		fill: currentColor;
	}

	.label {
		font-size: 10px;
		font-weight: 500;
		letter-spacing: 0.01em;
	}

	.tab.on .label {
		font-weight: 700;
	}
</style>
