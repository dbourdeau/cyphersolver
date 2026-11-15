#!/usr/bin/env python3
"""True leave-one-out calibration: rebuild the alignment without one crib despatch (6 jittered runs, best kept, same firm
rule as build_table.py without the stability condition), then score the left-out despatch with lcs_test."""
import sys, os, random
from collections import Counter
from align import build
from align2 import prep, table
import build_table, lcs_test
Dall = build()
for name in sys.argv[1:]:
    D = [d for d in Dall if name not in d['file']]; held = [d for d in Dall if name in d['file']][0]
    P = prep(D); rng = random.Random(1778)
    runs = []
    for r in range(6):
        A = build_table.one_run(D, P, rng); runs.append((build_table.objective(D, A, P), A))
    runs.sort(key=lambda x: -x[0]); T = table(D, runs[0][1])
    tab = {g: t.most_common(1)[0][0] for g, t in T.items() if t.most_common(1)[0][1] >= 2 and t.most_common(1)[0][1]/sum(t.values()) >= 2/3}
    cov, real, sh = lcs_test.run([g for g, _, _ in held['G']], [w for w, _ in held['W']], tab, 200)
    print('%-40s groups %3d covered %3d matched %3d (%.0f%%) shuffled mean %.1f max %d ; firm entries %d' % (name, len(held['G']), cov, real, 100*real/max(cov,1), sum(sh)/len(sh), max(sh), len(tab)))
