# StudyFeed

A personal, Instagram-style study app for the **Pondicherry University MCA (2020-21)** syllabus.
Every syllabus item is a node with its own definition, and every fully written topic becomes one
swipeable card: **definition -> explanation -> real-world example -> quiz -> exam tip**.

- SvelteKit + TypeScript, mobile-first, dark mode by default
- Installable PWA, works offline once installed
- No login, no database — progress lives in your browser
- One server route (`/api/ask`) keeps the Claude API key off the client

Repository: <https://github.com/cid0980/Mca-syllabus-guide> · Hosted on Vercel.

---

## Run it

```bash
npm install
npm run data:index   # rebuild src/lib/data/index.json (runs automatically before dev/build)
npm run dev          # http://localhost:5173
npm run check        # type check (svelte-check)
npm run build        # production build (adapter-node)
```

Install as an app: open the site on your phone -> browser menu -> **Add to Home screen**.

---

## Design system

The UI rules live in [`skills/`](skills/) and are the source of truth for every screen:

| File | Covers |
|---|---|
| `skills/TASTE.md` | The ban list: emojis, decorative gradients, glow, drop shadows on cards, backdrop blur, containers padded on all sides, centred paragraphs, competing primary buttons, dead-end empty screens |
| `skills/FRONTEND-DESIGN.md` | The token table (colour, type, spacing, radius) and the component state contract (default / hover / active / focus-visible / disabled / loading / error) |
| `skills/MOBILE-UX.md` | 48px touch targets, full-bleed rows, the scroll-snap feed, skeleton and error rules, performance budget |
| `skills/CONTENT-STYLE.md` | How a card is written (used by `scripts/generate-cards.ts`) |
| `skills/DATA.md` | Tree schema, `index.json` shape, storage keys |

The visual language is derived from Instagram's: a plain background, hairline dividers, one accent
blue (`#0095f6`), full-contrast text with a single muted grey for secondary lines, and solid icons
for the active tab. Light is the default and follows the system; dark is an override of the same
variables, so no component branches on theme.

What that means in code:

- **Tokens, never magic numbers.** `src/app.css` defines the palette and the 4/8/12/16/24/32/48/64
  spacing scale. Components never hardcode a colour.
- **The feed scrolls natively.** One card per screen with `scroll-snap-type: y mandatory`; an
  `IntersectionObserver` marks the current card. There is no JavaScript transform per frame —
  that is what made the first version stutter.
- **Real packages.** Icons are [Lucide](https://lucide.dev) components (`lucide-svelte`), the type
  is Inter Variable (`@fontsource-variable/inter`) shipped in the bundle so it works offline.
- **No emojis anywhere.** A scan of `src/`, `static/` and `scripts/` returns zero emoji characters.
- **One elevation.** Cards are separated by a 1px border and a background step, never by shadow.
  The only shadow in the app is on floating controls and toasts.
- **Every async view has three states:** loading (skeleton shaped like the content), error (what
  failed, why, retry) and done. Nothing renders an empty screen — `Saved`, `Progress`, an empty
  module feed and `Exam mode` all explain what is happening and offer the next tap.
- **Taps register.** Every button and row has a pressed state, and the bottom tab bar shows the
  active destination as a solid, full-contrast icon like Instagram's.

### Logo and icons

`static/logo.svg` is the app mark: two overlapping cards (the feed) with a solid accent face.
`static/favicon.svg`, `icon-192.png`, `icon-512.png`, `maskable-512.png` and `apple-touch-icon.png`
are generated from the same geometry by `scripts/make-icons.py`.

---

## What "complete" means here

The syllabus is stored as a **tree**, not a flat list, so nothing is skipped:

```
subject -> module -> topic -> subtopic -> type
```

Every node — including every subtopic and every "types of ..." entry — carries its **own one-line
definition**. Counts right now:

| Subject | Modules | Topics | Subtopics & types | Full cards |
|---|---|---|---|---|
| CSCA 411 Data Structures and Algorithms | 5 | 51 | 252 | **51** |
| CSCA 412 Object Oriented Programming | 5 | 26 | 116 | 0 |
| CSCA 413 Database Management Systems | 5 | 33 | 155 | 0 |
| CSCA 421 Computer Networks | 5 | 28 | 146 | 0 |
| CSCA 422 Operating Systems | 5 | 27 | 148 | 0 |
| CSCA 423 Communication Skills | 5 | 15 | 87 | 0 |
| CSCA 431 Mathematics for Computer Science | 5 | 21 | 120 | 0 |
| CSCA 432 Management Concepts and Strategies | 5 | 20 | 109 | 0 |
| CSCA 511 Software Engineering | 5 | 22 | 112 | 0 |
| CSCA 512 Internet and Web Technologies | 5 | 34 | 167 | 0 |
| **Total** | **50** | **277** | **1412** | **51** |

**1689 syllabus entries, each with a definition, and no subject or module left out.**

Data files: `src/lib/data/tree/<CODE>.json` (one per subject) plus `src/lib/data/index.json`, which
carries the totals, per-module counts and card ids so Home, Saved, Progress and Quiz can render
without touching a full tree.

### Why some cards exist and others do not

CSCA 411 is written out completely (51 cards, examples, 2 MCQs each with a *why*, exam tips).
The other nine subjects are fully **mapped** with definitions at every level, and their cards are
produced by `scripts/generate-cards.ts` (build step 5), which needs your `ANTHROPIC_API_KEY`.

---

## Screens

| Route | What it does |
|---|---|
| `/` | Subject story row (coloured ring = still to study), continue card, semester selector, subject rows, direct links into the syllabus tree and the first deck |
| `/explore` | Tile grid of subjects + **search** across every topic, subtopic and type |
| `/explore/[code]` | Full drill-down: modules -> topics -> subtopics -> types, expand all / collapse all, module rings |
| `/topic/[id]` | **Detail page**: definition, subtopics and types with definitions, full card, quiz, exam tip, prev/next, bookmark |
| `/subject/[code]` | Progress ring, module rows with counts, start studying / syllabus |
| `/feed/[code]/[module]` | Instagram-style vertical feed: one card per screen, native scroll-snap, **tap to flip to the quiz**, **double tap to save**, progress bar, next/previous buttons |
| `/saved` | Bookmarked topics and cards, resolved from the trees, with next-step links when empty |
| `/progress` | Cards seen, quiz accuracy, day streak, per-subject and per-module breakdowns |
| `/quiz` | Question-bank overview (step 4 adds the full quiz runner) |
| `/exam/[code]/[module]` | Exam mode: definitions and tips only, no quiz reveal |
| `/settings` | Theme (dark / light / system), data summary, reset progress and saved items |

Keyboard for desktop testing: `←` `->` move, `Space` flip, `B` bookmark.
A topic card links straight into the feed: `/feed/CSCA 411/II?card=CSCA411-M2-06`.

### How the screens get their data

- `index.json` is imported eagerly and is enough for Home, Saved, Progress and Quiz.
- Full trees are loaded with `+page.ts` **load functions**, so `/explore/[code]`, `/subject/[code]`,
  `/topic/[id]`, `/feed/...` and `/exam/...` are **server-rendered** with real content — no blank
  first paint. Card bodies are stripped for browse screens and kept for the feed.
- Browser-only data (progress, bookmarks, settings) starts empty on the server and is hydrated in
  `onMount` through `$lib/stores/hydrate.ts`. Views that change shape depending on stored data wait
  for `$hydrated`, which keeps hydration clean. The interactive deck only mounts in the browser.

---

## Build order status

| # | Step | State |
|---|------|-------|
| 1 | Scaffold SvelteKit + TypeScript + PWA + manifest | done |
| 2 | Sample cards + Home, Subject, Feed screens | done |
| 2b | Full syllabus tree for all 10 subjects + Explore / Topic pages | done |
| 2c | UI overhaul: skills, tokens, Lucide, Inter, logo, load-based SSR | done |
| 2d | Instagram-derived theme, native scroll-snap feed, solid active tab icons, tree rails, dev service worker removed | done |
| 2e | **Tab bar reactivity fixed at the compiler level, instant tap feedback + accent indicator, subject story row, Explore tile grid, store-read helpers inlined** | done |
| 3 | Saved screen, Progress screen, streak view | built — needs your test |
| 4 | Quiz mode and Exam mode | pending: exam mode done, quiz runner next |
| 5 | `generate-cards.ts`: card content for the other nine subjects | pending: needs API key |
| 6 | `/api/ask`, keyword search, Ask AI panel, answer cache | pending |
| 7 | Export / Import, offline check, polish | pending |

Search across the whole tree already works on `/explore`; the AI panel comes in step 6.

---

## Storage keys (browser only)

| Key | Contents |
|-----|----------|
| `sf:progress` | `nodeId -> { seen, lastSeen, quizCorrect, quizWrong }` |
| `sf:bookmarks` | array of node ids (topics and cards), newest first |
| `sf:streak` | `{ count, lastDay }` |
| `sf:settings` | `{ theme }` |
| `sf:lastOpened` | last subject + module for the continue card |

IndexedDB `aiAnswers` caches AI answers so the same question is never paid for twice.

---

## Layout

```
studyfeed/
  skills/                            # design + content rules (required reading before UI work)
  scripts/build-index.mjs            # tree -> index.json (counts, card ids) + validation
  scripts/make-icons.py              # regenerates the PWA PNG icons from the mark
  scripts/generate-cards.ts          # step 5 (fills `card` blocks into the tree files)
  scripts/archive/                   # one-off builders used to create the trees
  src/lib/data/mca_syllabus_topics.json
  src/lib/data/index.json            # totals, per-subject/module counts, card ids
  src/lib/data/tree/<CODE>.json      # the 10 subject trees - source of truth
  src/lib/content.ts                 # index + lazy tree access, node lookups, search
  src/lib/theme.ts                   # small presentation helpers
  src/lib/storage.ts                 # localStorage helpers + `sf:*` keys
  src/lib/types.ts                   # progress / streak / settings shapes
  src/lib/components/                # AppBar, ListRow, Card, SwipeFeed, ProgressRing,
                                     # Skeleton, ErrorState, Notice, BottomNav
  src/lib/stores/                    # progress, bookmarks, settings, hydrate
  src/routes/                        # +page, +layout, explore, topic/[id], subject/[code],
                                     # feed/[code]/[module], exam/[code]/[module], saved,
                                     # progress, quiz, settings, api/ask (step 6)
                                     # each deep route has a +page.ts load function
  static/                            # logo.svg, favicon.svg, PNG icons, manifest.webmanifest
  .env                               # ANTHROPIC_API_KEY (server only, never committed)
```

## Ground rules

API key never touches browser code. No database, no login, no analytics. No social features,
no native builds, no payments. No emojis in the UI. All content is written in original words; spell
every acronym out once and cross-check against the prescribed textbook before flipping a card to
`verified: true`.
