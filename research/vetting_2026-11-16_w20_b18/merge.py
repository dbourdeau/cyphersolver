"""Merge p/<id>.json into proposals.json (fills vetting.date / vetting.by)."""
import json, glob, os
H = os.path.dirname(os.path.abspath(__file__))
out = {}
order = '2833 2837 2836 2109 2650 2087 2893 2517 1915 2799 2889 2718 1964 1965 1966 2938 2397 2519'.split()
for i in order:
    f = os.path.join(H, 'p', i + '.json')
    if not os.path.exists(f):
        continue
    d = json.load(open(f, encoding='utf8'))
    v = d.get('vetting')
    if v:
        v2 = {'date': '2026-11-16', 'by': 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting'}
        v2.update(v)
        d['vetting'] = v2
    out[i] = d
json.dump(out, open(os.path.join(H, 'proposals.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'proposals:', ', '.join(f'{k}={v.get("verdict")}' for k, v in out.items()))
