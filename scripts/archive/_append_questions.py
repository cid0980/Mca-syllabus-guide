"""Appends authored questions to existing cards in a syllabus tree.

Usage:  python3 scripts/archive/_append_questions.py <batch.py>
The batch file defines CODE (e.g. "CSCA411") and ADD = { cardId: [question, ...] }.

Keeps the stored format exactly as it is: { q, options[4], answer, why }.
Refuses to touch a card twice, so re-running is safe.
"""
import json, pathlib, sys, importlib.util

ROOT = pathlib.Path(__file__).resolve().parents[2]
TREE = ROOT / "src/lib/data/tree"

spec = importlib.util.spec_from_file_location("batch", sys.argv[1])
batch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch)

path = TREE / f"{batch.CODE}.json"
doc = json.loads(path.read_text())

existing = {}
for m in doc["modules"]:
    for t in m["topics"]:
        if t.get("card"):
            existing[t["id"]] = t["card"]

added = 0
for card_id, questions in batch.ADD.items():
    card = existing.get(card_id)
    assert card is not None, f"{card_id}: no card in {path.name}"
    stems = {q["q"] for q in card["quiz"]}
    for q in questions:
        assert set(q) == {"q", "options", "answer", "why"}, f"{card_id}: bad keys {set(q)}"
        assert len(q["options"]) == 4, f"{card_id}: needs 4 options"
        assert q["answer"] in (0, 1, 2, 3), f"{card_id}: bad answer index"
        assert q["q"] not in stems, f"{card_id}: duplicate question"
        card["quiz"].append(q)
        stems.add(q["q"])
        added += 1

path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
counts = {cid: len(c["quiz"]) for cid, c in existing.items()}
print(f"{batch.CODE}: +{added} questions; per-card now {sorted(set(counts.values()))}")
for m in doc["modules"]:
    n = sum(len(t["card"]["quiz"]) for t in m["topics"] if t.get("card"))
    cards = sum(1 for t in m["topics"] if t.get("card"))
    print(f"  module {m['module']}: {cards} cards, {n} questions")
