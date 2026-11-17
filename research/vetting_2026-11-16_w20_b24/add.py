"""Merge one proposal (JSON file: {"id": ..., ...}) into proposals.json; fill vetting date/by."""
import json, sys, os
P = 'proposals.json'
d = json.load(open(P, encoding='utf8')) if os.path.exists(P) else {}
x = json.load(open(sys.argv[1], encoding='utf8'))
i = str(x.pop('id'))
v = x.get('vetting')
if v:
    v.setdefault('date', '2026-11-16'); v.setdefault('by', 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting')
    v = {'date': v.pop('date'), 'by': v.pop('by'), **v}; x['vetting'] = v
d[i] = x
json.dump(d, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('ok', i, x.get('verdict'), len(d))
