"""Three-hundred-and-thirty-fifth registered prediction set (PREDICTIONS.md, SL1-SL4): decipherment loop 160, the
site-and-class stratified referent pool (set 334) at looser alphas (0.005, 0.01, 0.02): the alpha with FDR <= 10% (100
within-stratum shuffles) and the largest coverage is chosen; the Linear B control re-run with it.
Writes results/predict_test335.md."""
import random
from collections import defaultdict

import predict_test334 as S
import rtools as R
import referents as X
from predict_test234 import lines
from predict_test235 import KEY
from predict_test304 import coverage
from predict_test325 import lb_q
from progress import data

ALPHAS = (0.005, 0.01, 0.02)


def fdr(clean, both, seed):
    rnd = random.Random(seed)
    real = X.count(S.units(clean, both))
    tot = 0
    for _ in range(100):
        bys = defaultdict(list)
        for i, (t, m, s) in enumerate(both):
            bys[s].append(i)
        pics = [m for t, m, s in both]
        for s, idx in bys.items():
            vals = [pics[i] for i in idx]
            rnd.shuffle(vals)
            for i, v in zip(idx, vals):
                pics[i] = v
        sb = [(t, p, s) for (t, m, s), p in zip(both, pics)]
        cl = defaultdict(list)
        for t, m, s in clean:
            cl[s].append(m)
        for s in cl:
            rnd.shuffle(cl[s])
        it = {s: iter(v) for s, v in cl.items()}
        sc = [(t, next(it[s]), s) for t, m, s in clean]
        tot += X.count(S.units(sc, sb))
    return real, tot / 100 / max(1, real)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirty-fifth registered predictions: decipherment loop 160, the stratified referent pool at looser alphas', 'predict_test335')
    DL, tr, te = data()
    clean, both = S.site_objects(F, recs)
    P = {'made': ([(t, m) for t, m, s in clean], [(t, m) for t, m, s in both])}
    res = {}
    for a in ALPHAS:
        S.ALPHA = a
        u = S.units(clean, both)
        n, f = fdr(clean, both, 335)
        nb = {k: {g: m for g, m in v.items() if m != 'Bull1'} for k, v in u.items()}
        res[a] = (n, f, coverage(DL, P, u), coverage(DL, P, nb))
        rd.say('- alpha %.3f: %d units, FDR %.1f%%, coverage %.2f%% (without Bull1 units %.2f%%).' % (a, n, 100 * f, 100 * res[a][2], 100 * res[a][3]))
    good = [a for a in ALPHAS if res[a][1] <= 0.10]
    best = max(good, key=lambda a: (res[a][2], -a)) if good else None
    q = lb_q(lines(), best or 0.005)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say('- Linear B with alpha %s: recovered %s; wrong %s.' % (best, ', '.join(rec) or 'none', ', '.join(wrong) or 'none'))
    rd.say()
    ok1 = best is not None and res[best][2] > 0.1269
    rd.rec('SL1', 'an alpha with FDR <= 10% gives coverage above 12.69%', 'alpha %s: %.2f%%' % (best, 100 * res[best][2] if best else 0), ok1)
    rd.rec('SL2', 'without Bull1 units it covers more than 5.75%', '%.2f%%' % (100 * res[best][3] if best else 0), best is not None and res[best][3] > 0.0575)
    rd.rec('SL3', 'Linear B with it: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('SL4', 'progress rule: SL1 and SL3 (the stratified referent line uses that alpha)', 'SL1 %s, SL3 %s' % (ok1, len(rec) >= 2 and not wrong), ok1 and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
