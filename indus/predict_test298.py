"""Two-hundred-and-ninety-eighth registered prediction set (PREDICTIONS.md, VC1-VC3): decipherment loop 123, the picture
vault of set 294 with a cross-pool fallback: a held-out tablet whose own pool gives no vote takes the votes of the other
pool's units (learned from all of that pool's objects without copies of the text). Scored by the excess of correct
predictions over the shuffle median (set 294: +60). Writes results/predict_test298.md."""
import random
from collections import Counter, defaultdict

import rtools as R
import referents as X
from predict_test294 import K, S, grams


def index(objs):
    occ = defaultdict(list)
    for t, m in objs:
        for g in grams(t):
            occ[g].append((t, m))
    return occ


def votes_for(t, occ):
    v = Counter()
    for g in grams(t):
        rest = [(u, x) for u, x in occ.get(g, []) if u != t]
        if len(rest) < K or len({u for u, x in rest}) < 2:
            continue
        lab = X.ok([x for u, x in rest], K, S)
        if lab:
            v[lab] += 1
    return v


def vault2(pools):
    occ = {lab: index(objs) for lab, objs in pools.items()}
    hits = n = 0
    for lab, objs in pools.items():
        other = [o for o in pools if o != lab][0]
        for t, m in objs:
            v = votes_for(t, occ[lab]) or votes_for(t, occ[other])
            if v:
                n += 1
                hits += sorted(v.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return hits, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-eighth registered predictions: decipherment loop 123, the picture vault with a cross-pool fallback', 'predict_test298')
    P = {lab: both for lab, (clean, both) in X.pools(F, recs).items()}
    h, n = vault2(P)
    rnd = random.Random(298)
    null = []
    for _ in range(200):
        Q = {}
        for lab, objs in P.items():
            pics = [m for t, m in objs]
            rnd.shuffle(pics)
            Q[lab] = list(zip([t for t, m in objs], pics))
        null.append(vault2(Q)[0])
    med = sorted(null)[100]
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f (set 294: 64 of 191, excess +60).' % (h, n, 100 * h / max(1, n), med, sorted(null)[189], p))
    rd.say()
    ex = h - med
    rd.rec('VC1', 'excess over the shuffle median above +60 (set 294), p < 0.05', 'excess %+d, p = %.3f' % (ex, p), ex > 60 and p < 0.05)
    rd.rec('VC2', 'more held-out tablets predicted than 191', '%d' % n, n > 191)
    rd.rec('VC3', 'progress rule: VC1 (the tier 3 vault line rises)', 'VC1 %s' % (ex > 60 and p < 0.05), ex > 60 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
