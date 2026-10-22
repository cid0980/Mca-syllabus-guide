"""Prints the topics a card still has to be written for.

Usage:  python3 scripts/archive/_dump_topics.py CSCA413 [--all]
Shows id, title, definition and every child, which is the context a card is written from.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
TREE = ROOT / "src/lib/data/tree"

code = sys.argv[1]
show_all = "--all" in sys.argv
doc = json.loads((TREE / f"{code}.json").read_text())

print(f"# {doc['code']} {doc['subject']} (semester {doc['semester']})")
for m in doc["modules"]:
    print(f"\n## MODULE {m['module']} - {m['title']}")
    for t in m["topics"]:
        if t.get("card") and not show_all:
            continue
        mark = "[has card] " if t.get("card") else ""
        print(f"\n{mark}{t['id']}  {t['title']}")
        print(f"   def: {t['definition']}")
        for c in t.get("children", []):
            print(f"   ({c['kind'][:4]}) {c['title']}: {c['definition']}")
