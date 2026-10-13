# MOBILE-UX — patterns and budget

Assume a 360–430px wide phone, one thumb, patchy network, and an older mid-range Android.
Nothing here is optional.

## Touch

- Minimum target: **48x48 CSS px** for any interactive element (Apple asks 44pt, Material 48dp;
  we take the larger). Icon buttons are 40x40 visually with 4px padding all round to reach 48.
- Hit areas never overlap. A row is a single target; if it has a trailing action, that action gets
  its own 48px area (`stopPropagation` so the row does not also fire).
- No hover-only affordances. Anything important is visible without hover.
- Swipe gestures are additive, never the only way: every swipe action also has a visible button.

## Layout

- One column. Max content width `600px`, centred only to avoid absurd line lengths on desktop.
- Full-bleed list groups: the group touches both screen edges; text starts at the 16px gutter;
  dividers are inset to the text start (iOS convention).
- Sticky app bar with a solid background and a hairline bottom border. No blur.
- Bottom tab bar with the safe-area inset respected (`env(safe-area-inset-bottom)`).
- Content scrolls under the bars; add matching bottom padding so nothing is trapped behind the nav.
- Text is left aligned. Values and counts sit right, tabular.

## Navigation

- Five bottom tabs maximum: Home, Syllabus, Saved, Quiz, Progress. Settings lives behind an icon in
  the home app bar.
- A 2px accent progress line appears at the very top during route transitions (`$navigating`).
- Every deep page has a back control in the app bar, and breadcrumbs for the 4-level syllabus tree.
- Deep links must work: a card in the feed is reachable by URL (`?card=<id>`) and from its topic page.

## States (must all exist)

- **Loading**: skeletons shaped like the final content. For a module: skeleton rows. For a card:
  skeleton lines in the card frame. Never a full-screen spinner.
- **Error**: what failed, why (short), and a `Retry`. Keep the app bar so the user can leave.
- **Empty**: no dead ends. Offer the next useful thing (open the syllabus, start the feed at card 1).
- **Offline**: content is local, so only the AI call can fail; that failure is a normal error state.

## Performance budget

- No `backdrop-filter`, no animated blur, no filter animations.
- Animate only `transform` and `opacity`, 120–180ms, `ease-out`. Respect `prefers-reduced-motion`.
- Long lists (syllabus, search results) use `content-visibility: auto` with `contain-intrinsic-size`.
- Heavy data is lazy: the subject index (a few KB) loads on home; full syllabus trees load only
  when a subject, topic or feed is opened, and are cached after that.
- Icons are imported by name from `lucide-svelte` so only used icons ship.
- No layout thrash while scrolling: fixed-height rows, no measuring in scroll handlers.
- Swipe deck keeps at most three cards mounted and uses `transform: translate3d` only.
