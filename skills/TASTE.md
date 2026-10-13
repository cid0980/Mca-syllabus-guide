# TASTE — the ban list

The fastest way to make this app look designed by a machine is to add decoration. This file lists
what is banned and what replaces it.

## Banned outright

| Banned | Why | Do this instead |
|---|---|---|
| Emoji in UI | Renders differently per platform, reads as a placeholder. | A Lucide icon component, or nothing. |
| Decorative gradients (purple→pink→orange) | Says nothing about the content. | One flat accent colour, used only for actions and progress. |
| Glow / drop-shadow on cards, buttons, icons | Fake depth, costs paint, hides weak hierarchy. | Depth from background steps and 1px borders. |
| Everything in a floating rounded card | Uniform elevation means nothing is elevated. | One full-bleed list group with inset dividers. |
| Container with 16px padding on every side around every element | Wastes the narrow screen, creates nested boxes. | Full-bleed rows on mobile, one gutter (16px) for text. |
| Centred everything | Reads like a landing page, not a tool. | Left-aligned text, right-aligned numbers and values. |
| Two or three competing primary buttons | User cannot tell the main action. | One primary action per screen; the rest are secondary/ghost. |
| Blur (`backdrop-filter`) on sticky headers/nav | GPU-heavy on mobile, causes scroll jank. | Solid header background + 1px bottom border. |
| Blank screen with "No data" | A dead end. | Content that is useful now (e.g. the topic list) plus one clear next step. |
| Arbitrary pixel values (13px, 17px, 23px) | Every value must come from the scales. | Use the spacing/type scales in FRONTEND-DESIGN.md. |
| Coloured text on a coloured background | Washed out and low contrast. | Foreground token on that surface's token. |
| Animation on scroll or on mount for decoration | Distracting, janky. | Motion only to explain a state change (press, swipe, save). |

## Required taste rules

1. **Grayscale first.** If hierarchy does not read in grayscale, colour will not fix it. Check by
   squinting: primary, secondary and tertiary must be clearly separated by size, weight or value.
2. **Emphasise by de-emphasising.** Rather than shouting with the important element, quieten the
   rest: muted labels, muted inactive tabs, dim icons.
3. **Two weights.** 400 for body, 500 for emphasis, 600 for titles. Nothing else.
4. **Spacing defines grouping.** Spacing between groups must be visibly larger than spacing inside
   a group (24 vs 8/12). If it is ambiguous, it is a bug.
5. **One accent.** Accent is state, not decoration: primary button, focus ring, progress fill,
   active tab indicator, selected row. If it is not state, it is grey.
6. **Numbers are tabular.** Counts, streaks, percentages, scores must not shift when they change.
7. **Text width.** Body text maxes out near 65 characters; on a phone the gutter does that for us.
8. **Every screen has a 1-line purpose.** The header says where you are, the content says what is
   inside, and the bottom nav says where you can go.
