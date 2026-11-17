"""Merge one proposal (JSON file arg 1, keyed by lead id) into proposals.json; fill date/by."""
import json, sys, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proposals.json')
cur = json.load(open(P, encoding='utf8')) if os.path.exists(P) else {}
new = json.load(open(sys.argv[1], encoding='utf8'))
for k, v in new.items():
    if 'vetting' in v:
        v['vetting'] = {'date': '2026-11-16', 'by': 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting', **v['vetting']}
    cur[k] = v
json.dump(cur, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('proposals:', sorted(cur, key=int))
