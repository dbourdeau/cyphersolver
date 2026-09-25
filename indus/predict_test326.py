"""Three-hundred-and-twenty-sixth registered prediction set (PREDICTIONS.md, BV1-BV3): decipherment loop 151, split-half
check of the base-rate configuration (set 325, alpha 0.01), as set 309: five random half-splits (seeds 3091-3095), both
directions, real held-out matches against 200 joint shuffles; held-out precision compared with set 309's C7 (23%).
Validation only. Writes results/predict_test326.md."""
import random

import rtools as R
import referents as X
from predict_test308 import matches, split
from predict_test325 import build


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-sixth registered predictions: decipherment loop 151, split-half check of the base-rate configuration', 'predict_test326')
    P = X.pools(F, recs)
    f = build(0.01)
    allm = []
    for seed in range(3091, 3096):
        H1, H2 = split(P, seed)
        for learn, test in ((H1, H2), (H2, H1)):
            allm.append(matches(f(learn), test))
    real = sum(a == b for ms in allm for a, b, t in ms)
    tot = sum(len(ms) for ms in allm)
    rnd = random.Random(326)
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
    p = (ge + 1) / 201
    prec = real / max(1, tot)
    rd.say('- %d of %d held-out matches right (%.0f%%); shuffles median %d; p = %.3f (set 309 C7: 23%%).' % (real, tot, 100 * prec, sorted(null)[100], p))
    rd.say()
    rd.rec('BV1', 'the base-rate configuration is confirmed on five split-halves (p < 0.05)', 'p = %.3f' % p, p < 0.05)
    rd.rec('BV2', 'its held-out precision is at least C7\'s 23%', '%.0f%%' % (100 * prec), prec >= 0.23)
    rd.rec('BV3', 'progress rule: none (validation; a failure of BV1 downgrades the line)', 'BV1 %s' % (p < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
