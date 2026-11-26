#!/usr/bin/env python3
import sys, json
sys.path.insert(0, sys.argv[1])
from solve import *
from run_controls import cipher, T1P, T2P

if __name__ == '__main__':
    lp, wl, n, wc = build_model()
    c1, c2 = cipher(T1P), cipher(T2P)
    print('T1', len(c1), c1); print('T2', len(c2), c2)
    print('diffs', [(i, a, b) for i, (a, b) in enumerate(zip(c1, c2)) if a != b])
    out = {}
    for tag, c, base in [('T1', c1, 1000), ('T2', c2, 2000), ('H170', c1[:170], 3000)]:
        rows = solve(c, lp, base, tag=tag)
        top = rows[:5]
        out[tag] = [dict(seed=r[0], score=round(r[1], 2), key=r[2], dec=r[3], cov=round(coverage(r[3], wl), 3)) for r in top]
        nsame = sum(1 for r in rows if r[3] == rows[0][3])
        out[tag + '_n_restarts_reaching_best'] = nsame
        print(tag, 'best', top[0][0], round(top[0][1], 2), 'restarts at best:', nsame)
        for r in top[:3]: print('  ', r[0], round(r[1], 2), r[2], r[3])
    json.dump(out, open(OUT + '/runs/real_summary.json', 'w'), indent=1)
