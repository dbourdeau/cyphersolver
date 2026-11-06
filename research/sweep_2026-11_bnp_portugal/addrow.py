"""Append (or replace by shelfmark) one row in candidates.json from a JSON file: python addrow.py row.json"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, 'candidates.json')
rows = json.load(open(P, encoding='utf-8')) if os.path.exists(P) else []
new = json.load(open(sys.argv[1], encoding='utf-8'))
for n in (new if isinstance(new, list) else [new]):
    rows = [r for r in rows if r['shelfmark'] != n['shelfmark']] + [n]
json.dump(rows, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
