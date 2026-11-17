"""Merge proposal snippets (a JSON file of {id: proposal}) into proposals.json."""
import json, sys, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proposals.json')
d = json.load(open(P, encoding='utf8')) if os.path.exists(P) else {}
for f in sys.argv[1:]:
    d.update(json.load(open(f, encoding='utf8')))
json.dump(d, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(d), 'proposals:', ', '.join(d))
