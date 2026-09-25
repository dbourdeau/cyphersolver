"""Three-hundred-and-thirty-ninth registered prediction set (PREDICTIONS.md, MA1-MA4): decipherment loop 164, the
true-duplicate pool of set 338 (mould copies and impressions collapsed) at stricter alphas (0.0001, 0.0005, 0.001,
0.002): the alpha with FDR <= 10% and the largest coverage is chosen; the Linear B control re-run with it.
Writes results/predict_test339.md."""
import predict_test334 as S
import rtools as R
from predict_test234 import lines
from predict_test235 import KEY
from predict_test304 import coverage
from predict_test325 import lb_q
from predict_test335 import fdr
from predict_test338 import collapse, objects_typed
from progress import data

ALPHAS = (0.0001, 0.0005, 0.001, 0.002)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirty-ninth registered predictions: decipherment loop 164, the true-duplicate pool at stricter alphas', 'predict_test339')
    DL, tr, te = data()
    clean, both = objects_typed(F, recs)
    cc, cb = collapse(clean), collapse(both)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    res = {}
    for a in ALPHAS:
        S.ALPHA = a
        u = S.units(cc, cb)
        n, f = fdr(cc, cb, 339)
        nb = {k: {g: m for g, m in v.items() if m != 'Bull1'} for k, v in u.items()}
        res[a] = (n, f, coverage(DL, P, u), coverage(DL, P, nb))
        rd.say('- alpha %.4f: %d units, FDR %.1f%%, coverage %.2f%% (without Bull1 units %.2f%%).' % (a, n, 100 * f, 100 * res[a][2], 100 * res[a][3]))
    good = [a for a in ALPHAS if res[a][1] <= 0.10]
    best = max(good, key=lambda a: (res[a][2], -a)) if good else None
    q = lb_q(lines(), best or 0.0001)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say('- Linear B with alpha %s: recovered %s; wrong %s.' % (best, ', '.join(rec) or 'none', ', '.join(wrong) or 'none'))
    rd.say()
    ok1 = best is not None and res[best][2] > 0.0109
    rd.rec('MA1', 'an alpha with FDR <= 10% gives coverage above 1.09%', 'alpha %s: %.2f%%' % (best, 100 * res[best][2] if best else 0), ok1)
    rd.rec('MA2', 'without Bull1 units above 0.99%', '%.2f%%' % (100 * res[best][3] if best else 0), best is not None and res[best][3] > 0.0099)
    rd.rec('MA3', 'Linear B with it: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('MA4', 'progress rule: MA1 and MA3 (the referent line uses the true-duplicate pool at that alpha)', 'MA1 %s, MA3 %s' % (ok1, len(rec) >= 2 and not wrong), ok1 and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
