# UX audit — every discomfort we know about

A living list. Anything found by the user or by testing goes here with the fix, so the same
complaint can never come back. Status: `fixed`, `planned`, `wontfix`.

## Navigation and orientation

| # | Where a person gets stuck | Fix | Status |
|---|---|---|---|
| 1 | Tab bar doesn't follow the page (bar frozen on Home) | Active tab derived in a `$:` statement, compared in the template; tapped tab lights up before the route changes | fixed |
| 2 | Can't tell if a tap registered | 110ms pressed state on tabs, rows and buttons; haptic tick on Android | fixed |
| 3 | Deep in a topic, no sense of place | Breadcrumb row in the app bar (`subject / module`) plus prev/next topic buttons | fixed |
| 4 | Back goes somewhere unexpected | App bar back button names its destination (compares subject vs syllabus) | fixed |
| 5 | Settings has no obvious way back | App bar back button on every non-tab screen | fixed |

## The feed and cards

| # | Where a person gets stuck | Fix | Status |
|---|---|---|---|
| 6 | A card's content overlapped the next card | Cards are natural height inside one scroll container; the card body no longer has its own scroll area | fixed |
| 7 | Scrolling got trapped between cards | `scroll-snap-type: y proximity` instead of `mandatory`, and no `scroll-snap-stop: always` | fixed |
| 8 | Accidental flip while scrolling | Tap only flips if the finger moved less than 8px and no scroll happened in the last 120ms | fixed |
| 9 | After opening the quiz there was no way back | A labelled "Back to card" control sits under the quiz **and** in the action row; the last answer reveals a "Back to card" primary button | fixed |
| 10 | Quiz felt like a dead end after answering | Each answer reveals the explanation immediately, and a completion line counts the score with the next action offered | fixed |
| 11 | Couldn't tell which subject/module a card belongs to | Post header shows the course avatar, subject code and module | fixed |
| 12 | Progress through a deck was invisible | Sticky progress bar at the top of the feed plus an "n/total" counter in the action row | fixed |
| 13 | Asking something about the card did nothing | Ask opens the AI panel with the card already as context | fixed |

## Trust, data and errors

| # | Where a person gets stuck | Fix | Status |
|---|---|---|---|
| 14 | Empty screens with no way forward | Every empty state names what is missing and offers a next tap | fixed |
| 15 | A failed load left a blank page | `ErrorState` with what failed, why, and a retry that shows its own spinner | fixed |
| 16 | No idea whether study progress is safe | Settings lists exactly what is stored in this browser; reset asks twice | fixed |
| 17 | AI answers would be lost on reload | Answers cached in IndexedDB (`aiAnswers`) keyed by provider + model + question + card | fixed |
| 18 | A pasted API key is scary | Keys stay in this browser, are never bundled into the site, and can be cleared with one tap; the panel says which provider receives the request | fixed |
| 19 | No AI key configured and the Ask button did nothing | The panel detects the missing key and links straight to Settings | fixed |

## Reading and comfort

| # | Where a person gets stuck | Fix | Status |
|---|---|---|---|
| 20 | Long definitions hard to scan | Definition is the lead line in 17px semibold; explanation is muted body text; example and exam tip are labelled blocks | fixed |
| 21 | Small tap targets | 44px minimum on every control, 48–56px rows, 40px icon buttons with a 4px ring | fixed |
| 22 | White flash or theme flicker on load | Theme applied pre-paint from `sf:settings`; dark is `#000` and light is `#fff`, following the system by default | fixed |
| 23 | Content pops in and looks broken for a moment | Skeletons are shaped like the real content and cross-fade in 150ms | fixed |
| 24 | Typography feels cramped on a phone | One Inter variable stack, 4/8/12/16/24/32/48 spacing scale, 1.3–1.6 line heights | fixed |
| 25 | Panels appear with no explanation | Sheets slide from the bottom edge, menus grow from their trigger, per `skills/MOTION.md` | fixed |

## Quiz mode (built)

| # | Where a person gets stuck | Fix | Status |
|---|---|---|---|
| 31 | Not knowing what a quiz will cover | The picker shows the question count and the card count per module, plus what the last run scored | fixed |
| 32 | Answering with no idea why | Every answer immediately shows the verdict and the card's written reason for the correct option | fixed |
| 33 | Finishing with no next step | Results screen: score ring, a plain-language verdict, the missed questions with both your pick and the right one, then retry-missed / run-again / back | fixed |
| 34 | Questions repeating in the same order | Order is shuffled once the page is live (never during hydration, which would break the server-rendered first question) | fixed |
| 35 | No keyboard path on desktop | Keys 1-4 or A-D answer, Enter or Space advances, Escape leaves the sheet | fixed |
| 36 | Recording a wrong answer twice | Each question records once; the option buttons lock after answering | fixed |
| 37 | The same card asked twice inside one 10 or 20 question run | `pickQuestions` hands out one question per card per round (0 repeats in 300 trials at 5, 10 and 20) | fixed |
| 38 | A quiz that ignores which cards I keep failing | Bands from the existing `sf:progress` signals - wrong first, then never opened, then revision - with a "Picked for you" line so the reason is visible | fixed |
| 39 | Refusing to say why these questions were chosen | The first question of a prioritised run names the counts ("4 cards you answered wrongly, 12 not opened yet") | fixed |
| 40 | "Retry what I missed" jumping back to question one after each answer | The pool keeps a stable identity; it was rebuilt on every progress write, which restarted the run | fixed |
| 41 | A card answered twice always opening with the same question | The starting question rotates with the card's existing answer counters | fixed |
| 42 | Guessing by position worked (B held 73 of 102 correct answers) | Answers are spread across A, B, C and D (63/63/62/62 of 250) and every new question's distractors are written to the answer's length | fixed |
| 43 | Home printed the course number twice: inside the circle and again below it | The circle keeps the number, the label below it is the short name from `$lib/labels` (DSA, OOP, DBMS, Maths) | fixed |
| 44 | The "1d" pill never said what it counted | Flame icon inside the pill plus a `title` and an `aria-label` spelling out "N day study streak"; it counts `sf:streak` consecutive study days | fixed |
| 45 | A subject with no cards looked the same as a written one | A "Syllabus only" tag on the row, shown only while `counts.cards === 0`, so it disappears by itself once cards are added | fixed |
| 46 | No way to see how a module went before starting it again | "Best 38/47" on each module row, read from the existing `sf:quiz` run log at the deck's current question count; nothing shown when there is no matching run | fixed |

## Truthful progress and reading (2026-10-13)

| # | Where a person gets stuck | Fix | Status |
|---|---|---|---|
| 47 | Scrolling a deck marked every card as read, so the completion numbers meant nothing | Reading is a decision: the card carries a Mark-as-read toggle, and the feed header counts marked cards out of the total | fixed |
| 48 | "Continue" appeared for a deck that was only opened to check | The Continue point is written by two actions only - marking a card read, or answering a question - and it points at that exact card | fixed |
| 49 | Clearing progress still showed the old numbers after a fast reload | Clearing also removes the quiz run log and the Continue point, and writes immediately, so nothing can come back from a debounce window | fixed |
| 50 | Ask AI closed on an accidental tap and lost the whole conversation | Ask is a page (`/ask?card=…`) with one thread per card in IndexedDB; Back, reload and app close all restore it | fixed |
| 51 | A question lost because the request failed | The question is saved before the request is sent, and a failed answer offers Retry with the same text | fixed |
| 52 | Counting was called "seen" while the mark was manual | Every label now says "marked read" (Home, Syllabus, Progress, Saved, Settings, backup copy) | fixed |
| 53 | A blue circle around 411 read as "finished" while nothing had been read (reported 2026-10-13) | The course ring is now the progress itself: dashed accent = cards waiting, solid accent arc = the share marked read, grey = nothing to track yet. Same treatment on Home and Syllabus | fixed |
| 54 | OpenRouter answered with its own billing text: "you requested up to 700 tokens, but can only afford 615 - upgrade to a paid account" (reported 2026-10-13) | The request now asks for 400 tokens, which is still twice what a 120-word answer needs; a refusal of that kind is translated into plain words with the three ways out (add credit, use a `:free` model, switch provider); OpenRouter's free models are listed first and tagged in Settings | fixed |

## Still planned

| # | Item | Why |
|---|---|---|
| 26 | Export / import of progress and bookmarks | Settings exports one JSON file and imports it back, with validation and a blocked-storage warning (build step 7) | fixed |
| 27 | Streak calendar view | The streak number alone doesn't show gaps |
| 28 | Offline indicator | The PWA works offline, but nothing tells the user they are offline |
| 29 | ~~Full quiz runner with ordered question banks and a wrong-answer review list~~ | Done: `/quiz` picker (mixed 10/20, retry-missed, per-module decks), `/quiz/mixed` and `/quiz/[code]/[module]` runners with immediate feedback, score, review list and retry-missed | fixed |
| 30 | Verified-card review flow | Draft cards are marked; there is no screen yet to tick them off in bulk |
