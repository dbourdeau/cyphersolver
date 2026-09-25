"""Three-hundred-and-twenty-third registered prediction set (PREDICTIONS.md, VT1-VT2): decipherment loop 148, the picture
vault voting with the tier 1 configuration (set 312: pairs and 3-sign runs at 2+ / 67%+; single signs, skip-pairs,
4-sign runs and the family kinds at 3+ / 67%+). Held out one text at a time within its pool (copies excluded), with the
cross-pool fallback of set 298; excess of correct predictions over the shuffle median (set 298: +64).
Writes results/predict_test323.md."""
import random
from collections import Counter, defaultdict

import rtools as R
import referents as X
from predict_test304 import fam

KINDS = [(2, 2, 0.67, False), (3, 2, 0.67, False), (1, 3, 0.67, False), (-2, 3, 0.67, False), (4, 3, 0.67, False),
         (1, 3, 0.67, True), (2, 3, 0.67, True), (3, 3, 0.67, True), (-2, 3, 0.67, True)]


def keyed(t):
    out = []
    ftt = fam(t)
    for n, k, s, isf in KINDS:
        src = ftt if isf else t
        for g in X.grams_of(src, n):
            if '|' not in g:
                out.append(((n, isf, g), k, s))
    return out


def index(objs):
    occ = defaultdict(list)
    for t, m in objs:
        for key, k, s in keyed(t):
            occ[key].append((t, m))
    return occ


def votes(t, occ):
    v = Counter()
    for key, k, s in keyed(t):
        rest = [(u, x) for u, x in occ.get(key, []) if u != t]
        if len(rest) < k or len({u for u, x in rest}) < 2:
            continue
        lab = X.ok([x for u, x in rest], k, s)
        if lab:
            v[lab] += 1
    return v


def vault(pools):
    occ = {lab: index(objs) for lab, objs in pools.items()}
    h = n = 0
    for lab, objs in pools.items():
        other = [o for o in pools if o != lab][0]
        for t, m in objs:
            v = votes(t, occ[lab]) or votes(t, occ[other])
            if v:
                n += 1
                h += sorted(v.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return h, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-third registered predictions: decipherment loop 148, the picture vault with the tier 1 configuration', 'predict_test323')
    P = {lab: both for lab, (clean, both) in X.pools(F, recs).items()}
    h, n = vault(P)
    rnd = random.Random(323)
    null = []
    for _ in range(200):
        Q = {}
        for lab, objs in P.items():
            pics = [m for t, m in objs]
            rnd.shuffle(pics)
            Q[lab] = list(zip([t for t, m in objs], pics))
        null.append(vault(Q)[0])
    med = sorted(null)[100]
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f (set 298: 70 of 295, excess +64).' % (h, n, 100 * h / max(1, n), med, sorted(null)[189], p))
    rd.say()
    ex = h - med
    rd.rec('VT1', 'excess over the shuffle median above +64, p < 0.05', 'excess %+d, p = %.3f' % (ex, p), ex > 64 and p < 0.05)
    rd.rec('VT2', 'progress rule: VT1 (the tier 3 vault line rises)', 'VT1 %s' % (ex > 64 and p < 0.05), ex > 64 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
