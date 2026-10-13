<script lang="ts">
	/** Four primary destinations + Progress. Settings lives behind an icon in the Home app bar. */
	import { page } from '$app/stores';
	import { House, BookOpen, Bookmark, ListChecks, ChartNoAxesColumn } from 'lucide-svelte';

	const items = [
		{ href: '/', label: 'Home', icon: House },
		{ href: '/explore', label: 'Syllabus', icon: BookOpen },
		{ href: '/saved', label: 'Saved', icon: Bookmark },
		{ href: '/quiz', label: 'Quiz', icon: ListChecks },
		{ href: '/progress', label: 'Progress', icon: ChartNoAxesColumn }
	];

	$: path = $page.url.pathname;

	function active(href: string): boolean {
		if (href === '/') return path === '/' || path.startsWith('/subject');
		if (href === '/explore')
			return (
				path.startsWith('/explore') ||
				path.startsWith('/topic') ||
				path.startsWith('/feed') ||
				path.startsWith('/exam')
			);
		return path.startsWith(href);
	}
</script>

<nav aria-label="Main">
	<div class="inner">
		{#each items as item}
			{@const Icon = item.icon}
			<a href={item.href} class:active={active(item.href)} aria-current={active(item.href) ? 'page' : undefined}>
				<Icon size={22} strokeWidth={active(item.href) ? 2.1 : 1.8} />
				<span>{item.label}</span>
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
		min-height: var(--nav-h);
	}

	a {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 2px;
		color: var(--fg-subtle);
		font-size: var(--fs-caption);
		font-weight: 500;
		letter-spacing: 0.01em;
		transition: color 0.14s ease;
	}

	a.active {
		color: var(--accent);
	}

	a:active {
		color: var(--fg);
	}
</style>
