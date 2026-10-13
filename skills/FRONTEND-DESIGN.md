# FRONTEND-DESIGN — tokens and components

Single source of truth is `src/app.css`. Components never hardcode a colour, a radius or a font
size; they use the tokens below.

## Colour

12-step scale per Radix convention, but only the steps we actually need are exposed as semantic
tokens. Dark is the default; light overrides the same names, so components never branch on theme.

| Token | Dark | Light | Used for |
|---|---|---|---|
| `--bg` | `#0e0e10` | `#ffffff` | app background |
| `--bg-subtle` | `#141416` | `#f7f7f9` | grouped surfaces, inputs, sheets |
| `--bg-element` | `#1a1a1d` | `#f1f1f4` | rows, chips, skeletons |
| `--bg-hover` | `#222226` | `#e9e9ee` | hover / press feedback |
| `--bg-active` | `#2b2b31` | `#e0e0e6` | selected row, pressed segment |
| `--border` | `#26262b` | `#e2e2e7` | hairlines, dividers, card stroke |
| `--border-strong` | `#34343c` | `#cfcfd7` | inputs, focusable outlines |
| `--fg` | `#ededf0` | `#16161a` | primary text |
| `--fg-muted` | `#a0a0ab` | `#5f5f6b` | secondary text, labels, icons |
| `--fg-subtle` | `#6e6e7a` | `#8a8a94` | tertiary text, chevrons, placeholders |
| `--accent` | `#6e56cf` | `#6e56cf` | primary action, progress, focus |
| `--accent-hover` | `#7c66dc` | `#5f49bd` | hovered primary action |
| `--accent-fg` | `#ffffff` | `#ffffff` | text on accent |
| `--danger` | `#e5484d` | `#dc3d43` | destructive, error icon |
| `--success` | `#30a46c` | `#218358` | correct answer |

Never grey text on a coloured background. Never use `--accent` for decoration.

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
