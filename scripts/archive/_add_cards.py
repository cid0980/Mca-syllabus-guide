"""Writes full cards into a syllabus tree.

Usage:  python3 scripts/archive/_add_cards.py <batch.py> [--force]
The batch file defines CODE (e.g. "CSCA413") and
CARDS = { cardId: { explanation, example, quiz: [...], examTip } }.

Rules enforced here, matching scripts/build-index.mjs and skills/CONTENT-STYLE.md:
  - every card gets explanation, example, examTip, verified: false and 4-5 questions
  - each question is { q, options[4], answer, why }
  - no duplicate question text inside a card, no duplicate option text inside a question
  - a card that already has content is left alone unless --force is passed
  - no emoji anywhere in the written content

Keeps the stored format exactly as it is: json indent=2, ensure_ascii=False, trailing newline.
"""

import json
import pathlib
import re
import sys
import importlib.util

ROOT = pathlib.Path(__file__).resolve().parents[2]
TREE = ROOT / "src/lib/data/tree"

EMOJI = re.compile(
    "[\U0001f000-\U0001faff"
    "\U00002190-\U000021ff"
    "\U00002300-\U000023ff"
    "\U00002460-\U000027bf"
    "\U0001f1e6-\U0001f1ff"
    "☀-➿]"
)
BANNED = ("simply", "just ", "obviously", "as we all know", "robust", "seamless", "cutting-edge", "powerful")


def validate(card_id, card):
    errs = []
    for field in ("explanation", "example", "examTip"):
        if not card.get(field):
            errs.append(f"{card_id}: missing {field}")
    quiz = card.get("quiz")
    if not isinstance(quiz, list) or not (4 <= len(quiz) <= 5):
        errs.append(f"{card_id}: needs 4 or 5 questions, got {len(quiz) if isinstance(quiz, list) else 'none'}")

    stems = set()
    for i, q in enumerate(quiz or []):
        tag = f"{card_id} q{i}"
        if set(q) != {"q", "options", "answer", "why"}:
            errs.append(f"{tag}: bad keys {set(q)}")
            continue
        if len(q["options"]) != 4:
            errs.append(f"{tag}: needs 4 options")
        if q["answer"] not in (0, 1, 2, 3):
            errs.append(f"{tag}: answer index out of range")
        if q["q"] in stems:
            errs.append(f"{tag}: duplicate question text")
        stems.add(q["q"])
        low = [str(o).strip().lower() for o in q["options"]]
        if len(set(low)) != len(low):
            errs.append(f"{tag}: duplicate option text")
        if not q["why"]:
            errs.append(f"{tag}: missing why")

    blob = json.dumps(card, ensure_ascii=False)
    if EMOJI.search(blob):
        errs.append(f"{card_id}: emoji in content")
    for word in BANNED:
        if word in blob.lower():
            errs.append(f"{card_id}: banned word {word!r}")
    for field in ("explanation", "example", "examTip"):
        text = card.get(field) or ""
        for sentence in re.split(r"(?<=[.!?]) +", text):
            if len(sentence.split()) > 25:
                errs.append(f"{card_id}.{field}: sentence over 25 words: {sentence[:60]}...")
    return errs


def rotate(q, k):
    """Move the correct option to (answer + k) mod 4. Wording is never touched."""
    k %= 4
    if k == 0:
        return q
    n = len(q["options"])
    return {**q, "options": [q["options"][(i - k) % n] for i in range(n)],
            "answer": (q["answer"] + k) % 4}


def balance(doc):
    """Spread correct answers evenly over A/B/C/D without changing any wording."""
    counters = [0, 0, 0, 0]
    moved = 0
    for m in doc["modules"]:
        for t in m["topics"]:
            card = t.get("card")
            if not card:
                continue
            for i, q in enumerate(card["quiz"]):
                target = min(range(4), key=lambda p: (counters[p], p))
                k = (target - q["answer"]) % 4
                if k:
                    card["quiz"][i] = rotate(q, k)
                    moved += 1
                counters[card["quiz"][i]["answer"]] += 1
    return counters, moved


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    spec = importlib.util.spec_from_file_location("batch", args[0])
    batch = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(batch)

    path = TREE / f"{batch.CODE}.json"
    doc = json.loads(path.read_text())

    topics = {t["id"]: t for m in doc["modules"] for t in m["topics"]}
    problems = []
    written = 0
    skipped = 0

    for card_id, card in batch.CARDS.items():
        topic = topics.get(card_id)
        if topic is None:
            problems.append(f"{card_id}: no such topic in {path.name}")
            continue
        if topic.get("card") and not force:
            skipped += 1
            continue
        problems += validate(card_id, card)
        topic["card"] = {
            "explanation": card["explanation"],
            "example": card["example"],
            "quiz": card["quiz"],
            "examTip": card["examTip"],
            "verified": False,
        }
        written += 1

    if problems:
        print(f"{batch.CODE}: {len(problems)} problem(s) - nothing written")
        for p in problems[:40]:
            print("  -", p)
        sys.exit(1)

    counters, moved = balance(doc)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")

    cards = {t["id"]: t["card"] for m in doc["modules"] for t in m["topics"] if t.get("card")}
    answers = [q["answer"] for c in cards.values() for q in c["quiz"]]
    spread = {i: answers.count(i) for i in range(4)}
    print(f"{batch.CODE}: +{written} cards ({skipped} already had one) -> {len(cards)} cards, "
          f"{len(answers)} questions, answer spread A/B/C/D = {spread} ({moved} rotated)")
    for m in doc["modules"]:
        n = sum(1 for t in m["topics"] if t.get("card"))
        q = sum(len(t["card"]["quiz"]) for t in m["topics"] if t.get("card"))
        print(f"  module {m['module']:3s}: {n:2d}/{len(m['topics']):2d} cards, {q:3d} questions")


main()
