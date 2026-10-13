# Motion

Derived from Material 3's easing/duration system and Apple's guidance, plus the community rule of
thumb that an exit should be 20–30% faster than its entrance. Every number here is a token in
`src/app.css`; components must not invent their own timings.

## The rule people notice first

**Nothing appears out of thin air.** An element must come from somewhere the user can follow:

| Element | Where it comes from |
|---|---|
| Bottom sheet / Ask panel | Slides up from the bottom edge, 24px of travel, `transform-origin: bottom` |
| Menu or popover | Grows from the control that opened it — `transform-origin` at the trigger, scale 0.96 -> 1 |
| Inline expansion (quiz, tree branch) | Height and opacity of the content itself, from the row above it |
| Toast | Slides up 8px, fades in, holds, then fades out — it never just blinks |
| Card content under a skeleton | Skeletons cross-fade to content in 150ms, no jump |
| **Route change** | The whole page rises 14px and settles in 260ms, keyed on pathname in `+layout.svelte`, so every navigation replays it. The current tab's icon settles from 0.86 to 1 at the same time. |

A 6px move over 240ms is invisible in practice — that was the first attempt and it read as "nothing
happened". Route transitions need to be at least a 12px travel to be noticed, and the tab the user
landed on has to acknowledge the tap.

## Durations and curves

| Token | Value | Used for |
|---|---|---|
| `--dur-press` | 110ms | button and row press feedback (must be under 150ms to feel instant) |
| `--dur-quick` | 150ms | hover, colour changes, icon swaps, skeleton cross-fade |
| `--dur-enter` | 240ms | content entering: sheet, panel, expanded section |
| `--dur-exit` | 180ms | content leaving — always shorter than the entrance |
| `--dur-page` | 240ms | route content fade/slide |
| `--dur-slow` | 320ms | the save confirmation burst only (the one deliberately expressive moment) |
| `--ease-standard` | `cubic-bezier(0.2, 0, 0, 1)` | begins and ends on screen |
| `--ease-enter` | `cubic-bezier(0.05, 0.7, 0.1, 1)` | entering the screen (decelerate to rest) |
| `--ease-exit` | `cubic-bezier(0.3, 0, 0.8, 0.15)` | leaving the screen (accelerate away) |

Rules that come with those numbers:

- Animate **transform and opacity only**. Never `width`, `height`, `top`, `left` — they cause layout
  per frame, which is the stutter users describe as "lagging".
- No bounce on tap-to-open. Bounce is for things that land (a save, a like), never for a panel the
  user asked for.
- Motion is interruptible: if the user scrolls or taps mid-animation, the end state must still be
  correct. Drive panels with a boolean class, not a queue of animations.
- `prefers-reduced-motion: reduce` collapses every duration to ~0 and keeps the end state.

## Interaction honesty

- Every tap shows *something* within 110ms: a background fill, a 0.97 scale, or the tab lighting up.
- A control that starts work shows a spinner **inside itself** and disables — never a bare page spinner.
- Destructive actions ask once, in place, and the confirm button states the consequence.
- Scrolling must never be "trapped": no mandatory snap on tall cards, no nested scroll areas, no
  fixed overlays that cover the tab bar.
