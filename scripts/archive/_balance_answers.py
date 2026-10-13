#!/usr/bin/env python3
"""Spread the correct answers of one subject tree across positions A, B, C and D.

Usage:
    python3 scripts/archive/_balance_answers.py src/lib/data/tree/CSCA412.json

Only the order of the options changes. The question text, the `why`, the number of
options and the text of the correct option all stay exactly as written, and the
`answer` index follows the correct option to its new place. The target position for
each question is chosen as the position that is currently least used, with the
question's own position breaking the tie, so the script moves as few as possible and
is safe to re-run: a balanced file comes back unchanged.
"""
import collections
import json
import sys


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    path = sys.argv[1]
    tree = json.loads(open(path).read())

    questions = [q for m in tree["modules"] for n in m["topics"] for q in n["card"]["quiz"]]
    before = collections.Counter(q["answer"] for q in questions)

    counts = collections.Counter(before)
    moved = 0
    for q in questions:
        options = q["options"]
        current = q["answer"]
        correct = options[current]

        target = min(range(4), key=lambda i: (counts[i], i != current))
        if target != current:
            rest = [o for i, o in enumerate(options) if i != current]
            rest.insert(target, correct)
            q["options"] = rest
            q["answer"] = target
            counts[current] -= 1
            counts[target] += 1
            moved += 1

    open(path, "w").write(json.dumps(tree, indent=2, ensure_ascii=False) + "\n")

    after = collections.Counter(q["answer"] for q in questions)
    print(f"{path}: {len(questions)} questions, {moved} reordered")
    print("  before:", " ".join(f"{chr(65+i)} {before[i]}" for i in range(4)))
    print("  after: ", " ".join(f"{chr(65+i)} {after[i]}" for i in range(4)))


if __name__ == "__main__":
    main()
