"""Three-hundred-and-first registered prediction set (PREDICTIONS.md, VF1-VF3): decipherment loop 126, the picture vault
of set 298 (all unit kinds, cross-pool fallback) with sign-family units added to the votes: every unit kind is also
formed over Parpola's description families (descfam), tagged apart from the sign units. Scored by the excess of correct
predictions over the shuffle median (set 298: +64). Writes results/predict_test301.md."""
import random

import predict_test294 as V
import predict_test298 as C
import rtools as R
import referents as X
from descfam import families

FM = families()
_sign_grams = V.grams


def grams(t):
    ft = tuple(g if g == '|' else FM.get(g, g) for g in t)
    return _sign_grams(t) | {('F',) + g for g in _sign_grams(ft)}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-first registered predictions: decipherment loop 126, the picture vault with sign-family units', 'predict_test301')
    C.grams = grams
    P = {lab: both for lab, (clean, both) in X.pools(F, recs).items()}
    h, n = C.vault2(P)
    rnd = random.Random(301)
    null = []
    for _ in range(200):
        Q = {}
        for lab, objs in P.items():
            pics = [m for t, m in objs]
            rnd.shuffle(pics)
            Q[lab] = list(zip([t for t, m in objs], pics))
        null.append(C.vault2(Q)[0])
    med = sorted(null)[100]
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f (set 298: 70 of 295, excess +64).' % (h, n, 100 * h / max(1, n), med, sorted(null)[189], p))
    rd.say()
    ex = h - med
    rd.rec('VF1', 'excess over the shuffle median above +64 (set 298), p < 0.05', 'excess %+d, p = %.3f' % (ex, p), ex > 64 and p < 0.05)
    rd.rec('VF2', 'accuracy on predicted objects 23.7%+ (set 298)', '%.1f%%' % (100 * h / max(1, n)), h / max(1, n) >= 0.237)
    rd.rec('VF3', 'progress rule: VF1 (the tier 3 vault line rises)', 'VF1 %s' % (ex > 64 and p < 0.05), ex > 64 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
