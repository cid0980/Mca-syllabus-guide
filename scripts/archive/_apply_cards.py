#!/usr/bin/env python3
"""Merge authored cards into a subject tree file.

Usage:
    python3 scripts/archive/_apply_cards.py src/lib/data/tree/CSCA412.json \
        scripts/archive/_cards_412a.py scripts/archive/_cards_412b.py ...

Each card module defines CARDS = {node_id: {explanation, example, quiz, examTip}}.
The card is appended to the matching topic node as

    "card": {"explanation": ..., "example": ..., "quiz": [...], "examTip": ..., "verified": false}

so the file keeps its shape and the node keeps its id, title, definition and children
untouched. Everything is validated before a byte is written, and the script is safe to
re-run: an existing card is replaced, not duplicated.

Checks (the same rules scripts/build-index.mjs enforces, plus the authoring rules):
  * the node id exists in the tree
  * explanation, example and examTip are non-empty
  * at least 4 questions per card
  * every question has exactly 4 options, a non-empty q and why, and an answer in 0..3
  * no question is repeated inside one card
  * the correct option text does not appear twice in the same question
"""
import importlib.util
import json
import pathlib
import sys

MIN_QUESTIONS = 4


def load_cards(paths):
    cards = {}
    for path in paths:
        spec = importlib.util.spec_from_file_location(pathlib.Path(path).stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for node_id, card in module.CARDS.items():
            if node_id in cards:
                raise SystemExit(f"duplicate card id {node_id}")
            cards[node_id] = card
    return cards


def node_index(tree):
    found = {}

    def walk(nodes):
        for node in nodes:
            found[node["id"]] = node
            walk(node.get("children", []))

    for module in tree["modules"]:
        walk(module["topics"])
    return found


def validate(cards, nodes):
    problems = []
    for node_id, card in cards.items():
        if node_id not in nodes:
            problems.append(f"{node_id}: no such node in the tree")
            continue

        for field in ("explanation", "example", "examTip"):
            if not str(card.get(field, "")).strip():
                problems.append(f"{node_id}: empty {field}")

        quiz = card.get("quiz") or []
        if len(quiz) < MIN_QUESTIONS:
            problems.append(f"{node_id}: only {len(quiz)} question(s), need {MIN_QUESTIONS}")

        stems = set()
        for i, q in enumerate(quiz, start=1):
            where = f"{node_id} q{i}"
            stem = str(q.get("q", "")).strip()
            if not stem:
                problems.append(f"{where}: empty question text")
            elif stem.lower() in stems:
                problems.append(f"{where}: repeated question inside this card")
            stems.add(stem.lower())

            options = q.get("options") or []
            if len(options) != 4:
                problems.append(f"{where}: {len(options)} options, need exactly 4")
            if any(not str(o).strip() for o in options):
                problems.append(f"{where}: an empty option")
            if len(set(str(o) for o in options)) != len(options):
                problems.append(f"{where}: an option is repeated")

            answer = q.get("answer")
            if not isinstance(answer, int) or not 0 <= answer <= 3:
                problems.append(f"{where}: answer {answer!r} is not 0..3")
            elif len(options) == 4:
                correct = str(options[answer])
                if sum(1 for o in options if str(o) == correct) > 1:
                    problems.append(f"{where}: the correct option appears twice")

            if not str(q.get("why", "")).strip():
                problems.append(f"{where}: empty why")
    return problems


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)

    tree_path = pathlib.Path(sys.argv[1])
    patches = sys.argv[2:]

    tree = json.loads(tree_path.read_text())
    nodes = node_index(tree)
    cards = load_cards(patches)

    problems = validate(cards, nodes)
    if problems:
        print(f"{len(problems)} problem(s), nothing written:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)

    for node_id, card in cards.items():
        node = nodes[node_id]
        node["card"] = {
            "explanation": card["explanation"],
            "example": card["example"],
            "quiz": [
                {"q": q["q"], "options": q["options"], "answer": q["answer"], "why": q["why"]}
                for q in card["quiz"]
            ],
            "examTip": card["examTip"],
            "verified": False,
        }

    tree_path.write_text(json.dumps(tree, indent=2, ensure_ascii=False) + "\n")

    questions = sum(len(c["quiz"]) for c in cards.values())
    print(f"{tree_path.name}: {len(cards)} cards, {questions} questions written")
    for node_id in sorted(cards):
        node = nodes[node_id]
        print(f"  {node_id:20} {node['title'][:44]:46} {len(cards[node_id]['quiz'])} questions")


if __name__ == "__main__":
    main()
