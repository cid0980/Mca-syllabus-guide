"""Helper used by the one-off syllabus tree builders in this folder.

A module is written as:
    ('I', 'Module title', [ (topic, definition, [ (subtopic, definition), ... ]), ... ])
Each entry may also carry a 'card' dict, which is what the feed and quizzes use.
"""
import json
import pathlib
import re

OUT = pathlib.Path('/home/user/studyfeed/src/lib/data/tree')


def _slug_id(code, module, index, child=None):
    base = f"{code.replace(' ', '')}-M{module}-T{index:02d}"
    return base if child is None else f"{base}-s{child}"


def write_tree(code, subject, semester, modules):
    doc = {
        'code': code,
        'subject': subject,
        'semester': semester,
        'modules': [],
    }
    for module, title, topics in modules:
        m = {'module': module, 'title': title, 'topics': []}
        for i, entry in enumerate(topics, start=1):
            topic, definition, children = entry[0], entry[1], entry[2]
            node = {
                'id': _slug_id(code, module, i),
                'title': topic,
                'kind': 'topic',
                'definition': definition,
                'children': [
                    {
                        'id': _slug_id(code, module, i, j),
                        'title': c[0],
                        'kind': c[2] if len(c) > 2 else 'subtopic',
                        'definition': c[1],
                    }
                    for j, c in enumerate(children, start=1)
                ],
            }
            if len(entry) > 3 and entry[3]:
                node['card'] = entry[3]
            m['topics'].append(node)
        doc['modules'].append(m)

    fname = re.sub(r'[^A-Za-z0-9]', '', code) + '.json'
    path = OUT / fname
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
    topics = sum(len(m['topics']) for m in doc['modules'])
    nodes = sum(len(t['children']) + 1 for m in doc['modules'] for t in m['topics'])
    print(f"{code}: {len(doc['modules'])} modules, {topics} topics, {nodes} nodes -> {path.name}")
    return path
