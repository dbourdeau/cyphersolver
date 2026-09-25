"""Three-hundred-and-second registered prediction set (PREDICTIONS.md, VG1-VG3): decipherment loop 127, the picture vault
of set 298 without catch-all votes: a unit whose qualifying picture is a catch-all code (Mult, Scene, Comp: several
pictures, a scene, a composite) does not vote, so the vote goes to units naming one thing. All tablets stay targets.
Scored by the excess of correct predictions over the shuffle median (set 298: +64). Writes results/predict_test302.md."""
import random
from collections import Counter

import predict_test298 as C
import rtools as R
import referents as X
from predict_test294 import K, S, grams

CATCH = {'Mult', 'Scene', 'Comp'}


def votes_for(t, occ):
    v = Counter()
    for g in grams(t):
        rest = [(u, x) for u, x in occ.get(g, []) if u != t]
        if len(rest) < K or len({u for u, x in rest}) < 2:
            continue
        lab = X.ok([x for u, x in rest], K, S)
        if lab and lab not in CATCH:
            v[lab] += 1
    return v


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-second registered predictions: decipherment loop 127, the picture vault without catch-all votes', 'predict_test302')
    C.votes_for = votes_for
    P = {lab: both for lab, (clean, both) in X.pools(F, recs).items()}
    h, n = C.vault2(P)
    rnd = random.Random(302)
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
    rd.rec('VG1', 'excess over the shuffle median above +64 (set 298), p < 0.05', 'excess %+d, p = %.3f' % (ex, p), ex > 64 and p < 0.05)
    rd.rec('VG2', 'accuracy on predicted objects 23.7%+ (set 298)', '%.1f%%' % (100 * h / max(1, n)), h / max(1, n) >= 0.237)
    rd.rec('VG3', 'progress rule: VG1 (the tier 3 vault line rises)', 'VG1 %s' % (ex > 64 and p < 0.05), ex > 64 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
