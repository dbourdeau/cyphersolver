"""Merge one lead's proposal (a JSON file {"<id>": {...}}) into proposals.json and fill the common fields.
python -I -X utf8 add.py p_<id>.json"""
import sys, json, os
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, 'proposals.json')
cur = json.load(open(P, encoding='utf8')) if os.path.exists(P) else {}
new = json.load(open(sys.argv[1], encoding='utf8'))
for k, v in new.items():
    vt = v.get('vetting')
    if vt:
        vt.setdefault('date', '2026-11-16')
        vt.setdefault('by', 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting')
        vt.setdefault('verdict', v.get('verdict'))
        # key order like the gate
        order = ['date', 'by', 'seen', 'prior_art', 'key_check', 'key_in_volume', 'key_held', 'duplicates', 'verdict', 'closed']
        v['vetting'] = {x: vt[x] for x in order if x in vt} | {x: vt[x] for x in vt if x not in order}
    cur[k] = v
json.dump(cur, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('proposals:', sorted(cur, key=int))
