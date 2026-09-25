"""Three-hundred-and-fortieth registered prediction set (PREDICTIONS.md, TV1-TV3): decipherment loop 165, split-half check
of the true-duplicate referent configuration (set 339: mould copies and impressions once, site-and-class strata, alpha
0.002): five random half-splits of the distinct texts (seeds 3091-3095), both directions, real held-out matches against
200 joint shuffles; held-out precision. Validation only. Writes results/predict_test340.md."""
import random

import predict_test334 as S
import rtools as R
from predict_test308 import matches
from predict_test338 import collapse, objects_typed


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-fortieth registered predictions: decipherment loop 165, split-half check of the true-duplicate configuration', 'predict_test340')
    clean, both = objects_typed(F, recs)
    cc, cb = collapse(clean), collapse(both)
    S.ALPHA = 0.002
    allm = []
    for seed in range(3091, 3096):
        rnd = random.Random(seed)
        texts = sorted({t for t, m, s in cb})
        rnd.shuffle(texts)
        a = set(texts[:len(texts) // 2])
        halves = []
        for keep in (lambda t: t in a, lambda t: t not in a):
            halves.append(([o for o in cc if keep(o[0])], [o for o in cb if keep(o[0])]))
        for (lc, lb), (tc, tb) in ((halves[0], halves[1]), (halves[1], halves[0])):
            u = S.units(lc, lb)
            allm.append(matches(u, {'made': ([(t, m) for t, m, s in tc], [(t, m) for t, m, s in tb])}))
    real = sum(x == y for ms in allm for x, y, t in ms)
    tot = sum(len(ms) for ms in allm)
    rnd = random.Random(340)
    ge = 0
    null = []
    for _ in range(200):
        s = 0
        for ms in allm:
            objs = sorted({(t, y) for x, y, t in ms})
            pics = [y for t, y in objs]
            rnd.shuffle(pics)
            idx = {t: i for i, (t, y) in enumerate(objs)}
            s += sum(x == pics[idx[t]] for x, y, t in ms)
        null.append(s)
        ge += s >= real
    p = (ge + 1) / 201
    rd.say('- %d of %d held-out matches right (%.0f%%); shuffles median %d; p = %.3f.' % (real, tot, 100 * real / max(1, tot), sorted(null)[100], p))
    rd.say()
    rd.rec('TV1', 'confirmed on five split-halves (p < 0.05)', 'p = %.3f' % p, p < 0.05)
    rd.rec('TV2', 'held-out precision at least 14% (set 326)', '%.0f%%' % (100 * real / max(1, tot)), real >= 0.14 * tot)
    rd.rec('TV3', 'progress rule: none (validation; a failure of TV1 downgrades the line)', 'TV1 %s' % (p < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
