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

## Progress keys

| Key | Shape | Written by |
|---|---|---|
| `sf:progress` | `{ [nodeId]: { seen, lastSeen, quizCorrect, quizWrong } }` | feed, exam, quizzes |
| `sf:bookmarks` | `string[]` of node ids, newest first | swipe double-tap, topic page, card |
| `sf:streak` | `{ count, lastDay }` (local `YYYY-MM-DD`) | any study action |
| `sf:settings` | `{ theme: 'dark' \| 'light' \| 'system' }` | settings |
| `sf:lastOpened` | `{ code, module, at }` | opening a feed |

Export/import (step 7) must round-trip all of them plus the IndexedDB `aiAnswers` cache.
