"""Three-hundred-and-thirty-first registered prediction set (PREDICTIONS.md, CV1-CV4): decipherment loop 156, split-half
check of the combined referent pool (set 330: tablets, seals, tags; alpha 0.002): five random half-splits of the
distinct texts, both directions, real held-out matches against 200 joint shuffles, for all units and for the units not
labelled Bull1; held-out precision of each. Validation only. Writes results/predict_test331.md."""
import random

import rtools as R
import referents as X
from predict_test200 import objects
from predict_test237 import merged
from predict_test254 import frag_objects
from predict_test308 import matches, split
from predict_test325 import build

TYPES = ('SEAL:S', 'SEAL:R', 'SEAL', 'SEAL:C', 'SEAL:CY', 'TAG')


def test(allm, rnd):
    real = sum(a == b for ms in allm for a, b, t in ms)
    tot = sum(len(ms) for ms in allm)
    ge = 0
    null = []
    for _ in range(200):
        s = 0
        for ms in allm:
            objs = sorted({(t, b) for a, b, t in ms})
            pics = [b for t, b in objs]
            rnd.shuffle(pics)
            idx = {t: i for i, (t, b) in enumerate(objs)}
            s += sum(a == pics[idx[t]] for a, b, t in ms)
        null.append(s)
        ge += s >= real
    return real, tot, sorted(null)[100], (ge + 1) / 201


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirty-first registered predictions: decipherment loop 156, split-half check of the combined referent pool', 'predict_test331')
    P = X.pools(F, recs)
    sc = objects(F, recs, TYPES)
    P2 = {'made': (P['made'][0] + P['moulded'][0] + sc, merged(P['made'][1] + P['moulded'][1] + sc + frag_objects(TYPES)))}
    f = build(0.002)
    allm, nobull = [], []
    for seed in range(3091, 3096):
        H1, H2 = split(P2, seed)
        for learn, tst in ((H1, H2), (H2, H1)):
            ms = matches(f(learn), tst)
            allm.append(ms)
            nobull.append([x for x in ms if x[0] != 'Bull1'])
    rnd = random.Random(331)
    ra = test(allm, rnd)
    rb = test(nobull, rnd)
    for lab, r in (('all units', ra), ('units not labelled Bull1', rb)):
        rd.say('- %s: %d of %d held-out matches right (%.0f%%); shuffles median %d; p = %.3f.' % (lab, r[0], r[1], 100 * r[0] / max(1, r[1]), r[2], r[3]))
    rd.say()
    rd.rec('CV1', 'all units confirmed on five split-halves (p < 0.05)', 'p = %.3f' % ra[3], ra[3] < 0.05)
    rd.rec('CV2', 'units not labelled Bull1 confirmed (p < 0.05)', 'p = %.3f' % rb[3], rb[3] < 0.05)
    rd.rec('CV3', 'held-out precision of the non-Bull1 units at least 14% (set 326)', '%.0f%%' % (100 * rb[0] / max(1, rb[1])), rb[0] >= 0.14 * rb[1])
    rd.rec('CV4', 'progress rule: none (validation; a failure of CV1 or CV2 downgrades the line)', 'CV1 %s, CV2 %s' % (ra[3] < 0.05, rb[3] < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
