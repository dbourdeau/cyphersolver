#!/usr/bin/env python3
import sys, random, re, json
sys.path.insert(0, sys.argv[1])
from solve import *

T1P = HC + "/output/ill_photo_leads_2026-11-23/work/test/T1_telegram.txt"
T2P = HC + "/output/ill_photo_leads_2026-11-23/work/blind/T2_telegram.txt"

def cipher(path):
    t = open(path).read().split('\n')
    s = ' '.join(l for l in t if l.startswith(('CLAVE T', 'YEYPS', 'UYPCE', 'VTZSC', 'VTCXG')))
    s = s.replace('CLAVE TREINTAIUNO', '')
    s = re.sub(r'\[(\w)/\w\]', r'\1', s)
    return re.sub('[^A-Z]', '', s)

def held_out_text():
    t = open(REPO + "/carranza1915/decryption.txt").read().split('\n')[1:]
    t = [l for l in t if not re.match(r'^t\d+\s*$', l) and not l.startswith('head:')]
    return letters('\n'.join(t))

if __name__ == '__main__':
    lp, wl, n, wc = build_model()
    out = {'corpus_letters': n}
    c1 = cipher(T1P); assert len(c1) == 246, len(c1)
    res = {}
    for i, sd in enumerate([11, 12, 13]):
        l = list(c1); random.Random(sd).shuffle(l); s = ''.join(l)
        rows = solve(s, lp, 100 * (i + 1), tag=f"S{i+1}")
        b = rows[0]; res[f"S{i+1}"] = dict(seed=sd, best_seed=b[0], score=round(b[1], 2), dec=b[3], cov=round(coverage(b[3], wl), 3))
    H = held_out_text()
    for i, sd in enumerate([21, 22, 23]):
        p = H[246 * i:246 * (i + 1)]; assert len(p) == 246
        perm = list(A); random.Random(sd).shuffle(perm); enc = dict(zip(A, perm))
        c = ''.join(enc[x] for x in p)
        rows = solve(c, lp, 100 * (i + 4), tag=f"E{i+1}")
        b = rows[0]; acc = sum(x == y for x, y in zip(b[3], p)) / 246
        res[f"E{i+1}"] = dict(seed=sd, best_seed=b[0], score=round(b[1], 2), acc=round(acc, 3), dec=b[3], plain=p, cov=round(coverage(b[3], wl), 3), true_score=round(score_int(to_int(p), lp), 2))
    out['controls'] = res
    json.dump(out, open(OUT + "/runs/controls_summary.json", 'w'), indent=1)
    for k, v in res.items(): print(k, {a: b for a, b in v.items() if a not in ('plain',)})
