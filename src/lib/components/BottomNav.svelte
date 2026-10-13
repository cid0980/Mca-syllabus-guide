<script lang="ts">
	/**
	 * Instagram-style tab bar.
	 *
	 * Reactivity note (this was a real bug): Svelte only re-runs a template expression when it
	 * textually references the variable that changed. Calling `active(item.href)` hid the URL read
	 * inside the function, so the bar never updated after the first render. Everything here
	 * compares against `current`, which is derived in a `$:` statement, so it always re-renders.
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

	function tabFor(pathname: string): string {
		if (
			pathname === '/' ||
			pathname.startsWith('/subject') ||
			pathname.startsWith('/feed') ||
			pathname.startsWith('/exam')
		)
			return '/';
		if (pathname.startsWith('/explore') || pathname.startsWith('/topic')) return '/explore';
		for (const item of items) if (item.href !== '/' && pathname.startsWith(item.href)) return item.href;
		return '/';
	}

	/** instant feedback: the tapped tab lights up before the route has even changed */
	let tapped: string | null = null;

	$: path = $page.url.pathname;
	$: current = tapped ?? tabFor(path);
	$: if (path) tapped = null;
</script>

<nav aria-label="Main">
	<div class="inner">
		{#each items as item}
			{@const Icon = item.icon}
			<a
				href={item.href}
				class="tab"
				class:on={current === item.href}
				aria-current={current === item.href ? 'page' : undefined}
				data-sveltekit-preload-data="tap"
				on:click={() => {
					tapped = item.href;
					if ('vibrate' in navigator) navigator.vibrate(6);
				}}
			>
				<span class="glyph"><Icon size={24} strokeWidth={current === item.href ? 2.3 : 1.9} /></span>
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
		position: relative;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 3px;
		color: var(--fg-subtle);
		transition: color 0.12s ease, transform 0.12s ease, background-color 0.12s ease;
	}

	.tab:active {
		background: var(--fill);
		transform: scale(0.96);
	}

	/* solid glyph + full contrast = unmistakably the current tab */
	.tab.on {
		color: var(--fg);
	}

	.tab.on .glyph :global(svg) {
		fill: currentColor;
	}

	.glyph {
		display: inline-flex;
		line-height: 0;
	}

	/* the tab you land on settles in, so a navigation is visibly acknowledged */
	.tab.on .glyph {
		animation: tab-settle var(--dur-page) var(--ease-standard) both;
	}

	@keyframes tab-settle {
		from {
			transform: scale(0.86);
		}
		to {
			transform: scale(1);
		}
	}

	.label {
		font-size: 10px;
		font-weight: 500;
		letter-spacing: 0.01em;
	}

	.tab.on .label {
		font-weight: 700;
	}

	/* the current tab also carries a 2px accent bar, so the state is readable at a glance */
	.tab.on::before {
		content: '';
		position: absolute;
		top: 0;
		left: 50%;
		transform: translateX(-50%);
		width: 28px;
		height: 2px;
		border-radius: var(--radius-full);
		background: var(--accent);
	}
</style>
