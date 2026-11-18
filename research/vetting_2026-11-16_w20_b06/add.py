"""Merge p/<id>.json into proposals.json (in lead order) and check each vetting block with the gate.
python -I -X utf8 add.py"""
import json, os, glob, sys
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(H))
sys.path.insert(0, os.path.join(ROOT, 'docs'))
import _check_catalogue as C
ORDER = '2730 2749 2727 2728 2725 2729 2736 2743 2748 2737 2740 2738 2739 2741 2915 2745 2747 2751'.split()
BY = 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting'
out = {}
for i in ORDER:
    f = os.path.join(H, 'p', i + '.json')
    if not os.path.exists(f): continue
    d = json.load(open(f, encoding='utf8'))
    v = d.get('vetting')
    if v:
        v.setdefault('date', '2026-11-16'); v.setdefault('by', BY)
        v['verdict'] = d['verdict']
        e = {'access': d['access'], 'vetting': v}
        probs = [p for p in C.vetting_problems(e) if 'only "open" leads' not in p]
        print(i, d['verdict'], 'OK' if not probs else probs)
    else:
        print(i, d.get('verdict'), '(no vetting)')
    out[i] = d
json.dump(out, open(os.path.join(H, 'proposals.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'proposals written')
