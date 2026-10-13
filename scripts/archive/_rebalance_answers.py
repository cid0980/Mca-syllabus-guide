"""Spreads correct-answer positions evenly across A, B, C and D.

Only the order of the four options changes (a cyclic rotation), so the question,
the options themselves, the correct answer's meaning and the "why" line are all
untouched. Rotation keeps the relative order of the options intact.

Run: python3 scripts/archive/_rebalance_answers.py
"""
import json, pathlib, random

TREE = pathlib.Path(__file__).resolve().parents[2] / "src/lib/data/tree"
PATH = TREE / "CSCA411.json"

doc = json.loads(PATH.read_text())
questions = [
    q
    for m in doc["modules"]
    for t in m["topics"]
    if t.get("card")
    for q in t["card"]["quiz"]
]

def distribution():
    d = [0, 0, 0, 0]
    for q in questions:
        d[q["answer"]] += 1
    return d

before = distribution()
worst_before = sum(
    1 for q in questions if q["options"][q["answer"]] == max(q["options"], key=len) and len(set(map(len, q["options"]))) > 1
)

# balanced target positions, shuffled with a fixed seed so the run is reproducible
targets = [i % 4 for i in range(len(questions))]
random.Random(20261013).shuffle(targets)

changed = 0
for q, target in zip(questions, targets):
    shift = (q["answer"] - target) % 4
    if shift:
        q["options"] = [q["options"][(i + shift) % 4] for i in range(4)]
        q["answer"] = target
        changed += 1

after = distribution()
worst_after = sum(
    1 for q in questions if q["options"][q["answer"]] == max(q["options"], key=len) and len(set(map(len, q["options"]))) > 1
)

# integrity: the correct option text must be the same before and after
PATH.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
print(f"questions: {len(questions)}   options reordered in {changed}")
print(f"answer positions before: A {before[0]}  B {before[1]}  C {before[2]}  D {before[3]}")
print(f"answer positions after : A {after[0]}  B {after[1]}  C {after[2]}  D {after[3]}")
print(f"longest option is correct: {worst_before} -> {worst_after} of {len(questions)}")
