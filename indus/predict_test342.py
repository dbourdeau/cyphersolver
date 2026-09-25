"""Three-hundred-and-forty-second registered prediction set (PREDICTIONS.md, VB1-VB2): decipherment loop 167, the
corrected picture vault (set 341: mould copies counted once) with base-rate votes: a unit votes for its commonest
picture m among the other observations carrying it only if a binomial test against m's share in the pool gives
P < 0.01 (set 325's criterion); otherwise as set 341 (all unit kinds, 2+ observations in 2+ texts, cross-pool fallback).
Excess of correct predictions over the shuffle median (set 341: +41). Writes results/predict_test342.md."""
import random
from collections import Counter

from scipy.stats import binom

import predict_test298 as V
import rtools as R
import referents as X
from predict_test294 import grams
from predict_test341 import once

BASE = {}


def votes_for(t, occ):
    v = Counter()
    for g in grams(t):
        rest = [(u, x) for u, x in occ.get(g, []) if u != t]
        if len(rest) < 2 or len({u for u, x in rest}) < 2:
            continue
        m, k = Counter(x for u, x in rest).most_common(1)[0]
        if binom.sf(k - 1, len(rest), BASE[id(occ)].get(m, 1.0)) < 0.01:
            v[m] += 1
    return v


def vault(pools):
    occ = {lab: V.index(objs) for lab, objs in pools.items()}
    for lab, objs in pools.items():
        c = Counter(m for t, m in objs)
        BASE[id(occ[lab])] = {m: c[m] / len(objs) for m in c}
    h = n = 0
    for lab, objs in pools.items():
        other = [o for o in pools if o != lab][0]
        for t, m in objs:
            vv = votes_for(t, occ[lab]) or votes_for(t, occ[other])
            if vv:
                n += 1
                h += sorted(vv.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return h, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-forty-second registered predictions: decipherment loop 167, the corrected vault with base-rate votes', 'predict_test342')
    P = X.pools(F, recs)
    pools = {'made': P['made'][1], 'moulded': once(P['moulded'][1])}
    h, n = vault(pools)
    rnd = random.Random(342)
    null = []
    for _ in range(200):
        Q = {}
        for lab, objs in pools.items():
            pics = [m for t, m in objs]
            rnd.shuffle(pics)
            Q[lab] = list(zip([t for t, m in objs], pics))
        null.append(vault(Q)[0])
    med = sorted(null)[100]
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f; excess %+d (set 341: +41).' % (h, n, 100 * h / max(1, n), med, sorted(null)[189], p, h - med))
    rd.say()
    rd.rec('VB1', 'excess over the shuffle median above +41, p < 0.05', 'excess %+d, p = %.3f' % (h - med, p), h - med > 41 and p < 0.05)
    rd.rec('VB2', 'progress rule: VB1 (the tier 3 vault line rises)', 'VB1 %s' % (h - med > 41 and p < 0.05), h - med > 41 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
