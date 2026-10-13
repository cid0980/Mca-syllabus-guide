# DATA — content storage and the index

## Files

```
src/lib/data/mca_syllabus_topics.json   raw syllabus lines per subject (source, read-only)
src/lib/data/tree/<CODE>.json           the syllabus tree, one file per subject
src/lib/data/index.json                 generated summary, tiny, loaded on every screen
```

`<CODE>` is the course code with the space removed: `CSCA411.json`, `CSCA512.json`.

## Tree schema

```jsonc
{
  "code": "CSCA 411",
  "subject": "Data Structures and Algorithms",
  "semester": 1,
  "modules": [
    {
      "module": "II",
      "title": "Linear Structures: Stacks, Queues and Linked Lists",
      "topics": [
        {
          "id": "CSCA411-M2-06",          // stable, used as the card id everywhere
          "title": "Circular Queue and Its Need",
          "kind": "topic",                 // topic | subtopic | type
          "definition": "one line",
          "children": [
            { "id": "CSCA411-M2-06-s2", "title": "Circular increment formula", "kind": "subtopic", "definition": "..." }
          ],
          "card": {                        // optional: only fully written topics have this
            "explanation": "...",
            "example": "...",
            "quiz": [{ "q": "...", "options": ["a","b","c","d"], "answer": 0, "why": "..." }],
            "examTip": "...",
            "verified": false
          }
        }
      ]
    }
  ]
}
```

Rules:

- Ids are `<CODE><-Mmodule-Tnn>` for topics and `-sN` for children. Never renumber existing ids:
  progress, bookmarks and quiz history are stored against them.
- `kind: "type"` is used for the "types of X" entries so the UI can group them separately.
- A topic without a `card` is still valid content: it has a definition and children.

## Index

`npm run data:index` runs `scripts/build-index.mjs` and rewrites `src/lib/data/index.json`:

```jsonc
{
  "generatedAt": "2026-10-13T...",
  "totals": { "subjects": 10, "modules": 50, "topics": 277, "subtopics": 1412, "cards": 51 },
  "subjects": [
    {
      "code": "CSCA 411", "subject": "Data Structures and Algorithms", "semester": 1,
      "counts": { "modules": 5, "topics": 51, "subtopics": 252, "cards": 51 },
      "cardIds": ["CSCA411-M1-01", "..."],
      "modules": [
        { "module": "II", "title": "...", "topics": 12, "subtopics": 57, "types": 0, "cards": 12,
          "cardIds": ["..."] }
      ]
    }
  ]
}
```

Why: home, progress and saved can render counts, rings and accuracy without downloading any tree.
The index must always be regenerated after content changes (the build script does it too).

## Loading model

- `index.json` — eager, a few KB.
- `tree/<CODE>.json` — lazy `import()`, cached in memory per subject after first use.
- Search — needs every tree, so it loads them once on first query and caches.

Any screen that touches a tree shows a skeleton while loading and an `ErrorState` with retry if the
import fails (offline first load, corrupted file).

## Quiz questions

Questions live on the card, inside `card.quiz`, and nowhere else. The stored shape never changed:

```jsonc
{ "q": "question text", "options": ["a", "b", "c", "d"], "answer": 0, "why": "one line of reasoning" }
```

- `options` is always exactly four and `answer` is the index 0-3 of the correct option.
- There is no question id. A question is identified by its card plus its position in the array.
- Every written card carries **four or five** questions: recall, a "which is NOT" (three true
  statements from that card plus one false statement that belongs to a sibling topic), a short
  scenario, and - where the topic has a real count, capacity, cost or complexity - a numeric one.
- Distractors are written at about the same length as the correct option, and correct answers are
  spread evenly across A, B, C and D. `scripts/archive/_rebalance_answers.py` rotates the options of
  every question to keep that spread even; it never changes the wording, only the order.
- A batch is authored as `{ cardId: [question, ...] }` and appended with
  `python3 scripts/archive/_append_questions.py scripts/archive/_batch_mX.py`, which refuses duplicate
  question text, wrong option counts and out-of-range answer indexes. `verified` stays `false` until
  the card has been checked against the textbook.

### How a run is built (`src/lib/quiz.ts`)

`pickQuestions(items, limit, progress)` orders the pool before the first question appears:

| Band | Cards | Why |
|---|---|---|
| 0 | `quizWrong > 0` | mistakes are the point of a quiz |
| 1 | never seen | new material |
| 2 | seen and not wrong | revision |

Inside a band the card seen longest ago comes first. Questions are then handed out **one per card per
round**, so a 10 or 20 question mixed run cannot ask the same card twice while cards remain, and a
module run using every question spreads a card's four or five questions apart instead of sitting them
in a row. A card's opening question rotates with its existing `quizCorrect + quizWrong` counters, so
the priority and rotation features store nothing new. `scripts/build-index.mjs` warns (does not fail)
when a card has fewer than four questions, so the subjects still being written can be filled in
gradually; duplicate question or option text is treated as a hard error.

## Progress keys

| Key | Shape | Written by |
|---|---|---|
| `sf:progress` | `{ [nodeId]: { seen, lastSeen, quizCorrect, quizWrong } }` | feed, exam, quizzes |
| `sf:bookmarks` | `string[]` of node ids, newest first | swipe double-tap, topic page, card |
| `sf:streak` | `{ count, lastDay }` (local `YYYY-MM-DD`) | any study action |
| `sf:settings` | `{ theme: 'dark' \| 'light' \| 'system' }` | settings |
| `sf:lastOpened` | `{ code, module, at }` | opening a feed |

Export/import (step 7) must round-trip all of them plus the IndexedDB `aiAnswers` cache.
