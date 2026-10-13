# Skills

Working rules for this repo. Any agent or human changing UI or content must read these first and
follow them. They are short on purpose: if a rule is not in here, it is not a rule.

| File | Covers |
|---|---|
| [TASTE.md](./TASTE.md) | What this UI must never look like. The ban list. |
| [FRONTEND-DESIGN.md](./FRONTEND-DESIGN.md) | Tokens, type scale, spacing, radius, component contract, states. |
| [MOBILE-UX.md](./MOBILE-UX.md) | Mobile patterns, touch targets, navigation, performance budget. |
| [CONTENT-STYLE.md](./CONTENT-STYLE.md) | How study text is written (also used by `scripts/generate-cards.ts`). |
| [DATA.md](./DATA.md) | Where content lives, the tree schema, how the index is built. |

## Enforcement

- `npm run check` must pass with 0 errors and 0 warnings before a change is considered done.
- A UI change that adds an emoji, a decorative gradient, a glow, or a shadowed card has failed
  review. See TASTE.md.
- Every asynchronous view must render one of: skeleton, error, or content. No blank states.

## Sources these rules come from

- Refactoring UI principles (Wathan & Schoger): constrained scales, grayscale-first hierarchy,
  spacing between groups > spacing within groups, depth via borders/background instead of shadows.
  <https://www.ui-skills.com/skills/s0xdk/refactoring-ui>
- Radix Colors 12-step scale and its documented use cases per step.
  <https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale>
- Apple Human Interface Guidelines: 44x44pt minimum touch target, content fills the viewport,
  one primary action per screen. <https://www.dequeuniversity.com/rules/attest-ios/1.0/touch-target-size>
- Android/Material list conventions: 48dp targets, edge-to-edge dividers.
  <https://www.designyourway.net/blog/the-simple-yet-complicated-mobile-ui-list-design-43-examples/>
- `content-visibility: auto` + `contain-intrinsic-size` for long lists; backdrop-filter is a
  GPU-budget decision, not a default.
  <https://www.debugbear.com/blog/content-visibility-api>
  <https://www.f22labs.com/blogs/how-css-properties-affect-website-performance/>
- shadcn semantic token convention (`background/foreground` pairs, `--radius` base scale).
  <https://ui.shadcn.com/docs/theming>
- Lucide icon set, named imports only for tree-shaking.
  <https://iconsguild.vercel.app/guide/packages/lucide-svelte>
