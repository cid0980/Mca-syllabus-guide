# CONTENT-STYLE — how study text is written

Applies to every definition, explanation, example, quiz and exam tip in `src/lib/data/tree/*.json`,
and to `scripts/generate-cards.ts` when it fills in new cards.

## Voice

- Simple Indian-English classroom English. Short sentences. No filler.
- Explain the thing; do not describe that the thing is being explained.
- Never copy textbook wording. Original phrasing only.
- Spell out every acronym the first time it appears in a card, with a tiny example:
  "TLB (translation lookaside buffer) is a small cache of recent page translations."
- Prefer the Indian exam register: students write "state the formula", "draw the diagram",
  "give an example". Tips should sound like a senior's advice.

## Per-field rules

| Field | Length | Rule |
|---|---|---|
| `definition` | 1 line, ≤ 20 words | Answers "what is it?" with no example. Atomic: one idea only. |
| `explanation` | 3–5 short sentences | Mechanism and why it matters. May mention one contrast or comparison. |
| `example` | 1–2 sentences | Real, everyday, local where possible (college, canteen, exam week). No code unless the topic is code. |
| `quiz[].q` | 1 line | Tests one fact, application or comparison. Never "which of the following is false" unless the distractor matters. |
| `quiz[].options` | 4 options, similar length | Distractors must be plausible and about the same length as the answer. |
| `quiz[].why` | 1 sentence | Explains the correct option, and where useful why the tempting one is wrong. |
| `examTip` | 1 line | What to write/draw in the exam to pick up marks: a formula, a table, a diagram, a definition order. |

## Structure rules

- Subtopic and type nodes carry only `title` + `definition` (one line). No explanation on leaves.
- A topic node's children must cover everything named in the syllabus line for that topic, including
  the "types of X" items, which are `kind: "type"`.
- Every numbered technique or classification in the syllabus becomes a child node, never inline prose.
- Acronyms in titles are expanded in the definition, not in the title.

## Banned in content

- Emoji anywhere in the data.
- "Simply", "just", "obviously", "as we all know".
- Marketing adjectives: powerful, robust, seamless, cutting-edge.
- Sentences longer than 25 words.

## Verified flag

New content is written with `"verified": false` and shows a `draft — verify` chip in the UI. Flip it
to `true` only after checking the card against the prescribed textbook. This is the review gate.
