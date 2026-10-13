# FRONTEND-DESIGN — tokens and components

Single source of truth is `src/app.css`. Components never hardcode a colour, a radius or a font
size; they use the tokens below.

## Colour

The palette is derived from Instagram's: a plain background, hairline dividers, one accent blue,
and text that is either full-contrast or a muted grey. No gradients, no glow, no tinted panels.

Light is the default; dark is an override of the same variables, so no component branches on theme.

| Token | Light | Dark | Used for |
|---|---|---|---|
| `--bg` | `#ffffff` | `#000000` | page and card background |
| `--bg-subtle` | `#fafafa` | `#090909` | pressed / secondary surfaces |
| `--fill` | `#efefef` | `#262626` | secondary buttons, chips, avatars, skeletons |
| `--fill-strong` | `#dbdbdb` | `#363636` | stronger fills |
| `--border` | `#dbdbdb` | `#262626` | hairline dividers, 1px only |
| `--border-strong` | `#c7c7c7` | `#363636` | inputs, outlined controls |
| `--fg` | `#262626` | `#f5f5f5` | primary text and icons |
| `--fg-muted` | `#737373` | `#a8a8a8` | body copy, secondary lines |
| `--fg-subtle` | `#8e8e8e` | `#737373` | captions, counts, idle tab icons |
| `--accent` | `#0095f6` | `#0095f6` | primary buttons, links, active tab icon, progress |
| `--accent-hover` | `#1877f2` | `#4db5f9` | hover on the accent |
| `--danger` | `#ed4956` | `#ff5c6c` | destructive + wrong quiz answer |
| `--success` | `#1a7f37` | `#4ade80` | correct quiz answer |
| `--warning` | `#b26a00` | `#f5a623` | the "draft" badge |
| `--shadow-pop` | `0 4px 16px rgba(0,0,0,.12)` | `0 4px 16px rgba(0,0,0,.7)` | floating controls and toasts only |

Contrast rule: body text is `--fg-muted` on `--bg`, never `--fg-subtle`. `--fg-subtle` is for
captions and counts only. Never put grey text on the accent colour.


## Type

Family: Inter variable, self-hosted through `@fontsource-variable/inter` (works offline, no CDN).

| Token | Size / line-height | Weight | Use |
|---|---|---|---|
| `--fs-caption` | 11 / 16 | 500 | uppercase section labels, tab labels |
| `--fs-small` | 13 / 18 | 400 | secondary text, metadata |
| `--fs-body` | 15 / 22 | 400 | body copy, list row titles |
| `--fs-body-strong` | 15 / 22 | 500 | emphasised body, row titles |
| `--fs-title` | 17 / 24 | 600 | page titles |
| `--fs-title-lg` | 22 / 28 | 600 | large screen titles (rare) |
| `--fs-def` | 18 / 26 | 500 | card definition (the one thing to read first) |

Numbers that change (`67%`, `12/51`, streak) use `font-variant-numeric: tabular-nums`.

## Space and size

Scale: `4, 8, 12, 16, 24, 32, 48, 64`. No other values.

- Gutter: `16px` (text and lists).
- Spacing inside a group: `4`–`12px`. Between groups: `24px`+. Section label sits `24px` above its group.
- Row: minimum height `48px` (56px with two lines), vertical padding `12px`.
- App bar: `52px` content height + safe-area top.
- Bottom nav: `56px` + safe-area bottom.
- Icon sizes: `16` inline, `18` in rows, `20` in actions, `22` in nav.

## Radius

`--radius-sm: 6px`, `--radius: 8px` (buttons, inputs, rows), `--radius-lg: 12px` (sheets, cards),
`--radius-full: 999px` (pills, avatars, rings). One value, derived scale.

## Depth

Exactly one elevation in the whole app: overlays (bottom sheet, toast, menu) get
`--shadow-overlay: 0 8px 28px rgba(0,0,0,.45)` plus a border. Everything else separates by
background step and 1px hairline. Pressed states use `--bg-hover`, not a shadow.

## Component contract

Every interactive component must implement these states. Missing one is a defect.

| State | Implementation |
|---|---|
| default | token background/border |
| hover (pointer devices only) | `--bg-hover` |
| active/pressed | `--bg-active` + `transform: scale(.985)` |
| focus-visible | `outline: 2px solid var(--accent); outline-offset: 2px` |
| disabled | `opacity: .5; pointer-events: none` |
| loading | `Loader2` icon spinning + label change ("Saving…") + `aria-busy="true"` |
| error | `ErrorState` with a retry action, never a raw browser alert |

Buttons: `primary` (accent, one per screen), `secondary` (border, transparent), `ghost` (text only),
`danger`. Heights: `sm 32`, `md 40`, `lg 44`. Labels are verbs ("Start quiz", "Save"), never "OK".

## Async views

Three possible render states, always:

1. **loading** — `Skeleton` rows that match the shape of the real content (never a spinner page).
2. **error** — `ErrorState` with the message and a `Retry` button that re-runs the loader.
3. **content** — the real thing.

If a list is legitimately empty, replace it with useful content and one next step. Example: a module
with no cards yet shows its full topic list with definitions and a link to the syllabus.

## Svelte reactivity rules (learned the hard way)

1. A template expression only re-runs when it **textually references** a variable that changed.
   `class:on={active(item.href)}` never updates if `active()` reads a store internally, because
   Svelte cannot see the dependency. Derive first, then compare:
   `$: current = tabFor($page.url.pathname);` … `class:on={current === item.href}`.
   The same bug hid in `pct()`-style helpers — inline `percentSeenByIds(ids, $progress)` instead.
2. Never read `localStorage` during the first render: start from the empty value, then hydrate in
   `onMount` and gate anything that changes shape on `$hydrated`.
3. Never write to `localStorage` on every scroll or view; debounce (300ms) — it was visible jank.
4. Do not animate with per-frame JavaScript. Use native scroll-snap and let the compositor work.
