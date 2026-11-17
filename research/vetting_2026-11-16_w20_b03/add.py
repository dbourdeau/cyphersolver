"""Merge one proposal (JSON file: {"<id>": {...}}) into proposals.json."""
import json, sys, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proposals.json')
d = json.load(open(P, encoding='utf8')) if os.path.exists(P) else {}
new = json.load(open(sys.argv[1], encoding='utf8'))
d.update(new)
json.dump(d, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('proposals:', sorted(d, key=int))
