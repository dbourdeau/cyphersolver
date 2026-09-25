"""Three-hundred-and-forty-fourth registered prediction set (PREDICTIONS.md, SO1-SO4): decipherment loop 169, the
true-duplicate referent pool (set 339) with sign units only (no description-family units, which are coarser and may
carry most chance matches), at alpha 0.003 and 0.005; the alpha with FDR <= 10% and the larger coverage is chosen;
Linear B control. Writes results/predict_test344.md."""
import predict_test334 as S
import rtools as R
from predict_test234 import lines
from predict_test235 import KEY
from predict_test304 import coverage
from predict_test325 import lb_q
from predict_test335 import fdr
from predict_test338 import collapse, objects_typed
from progress import data


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-forty-fourth registered predictions: decipherment loop 169, sign units only in the true-duplicate pool', 'predict_test344')
    DL, tr, te = data()
    clean, both = objects_typed(F, recs)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    cc, cb = collapse(clean), collapse(both)
    S.FAMILIES = False
    res = {}
    for a in (0.003, 0.005):
        S.ALPHA = a
        u = S.units(cc, cb)
        n, f = fdr(cc, cb, 344)
        res[a] = (n, f, coverage(DL, P, u))
        rd.say('- sign units only, alpha %.3f: %d units, FDR %.1f%%, coverage %.2f%%.' % (a, n, 100 * f, 100 * res[a][2]))
    S.FAMILIES = True
    good = [a for a in res if res[a][1] <= 0.10]
    best = max(good, key=lambda a: (res[a][2], -a)) if good else None
    q = lb_q(lines(), best or 0.003)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say('- chosen alpha %s; Linear B: recovered %s; wrong %s.' % (best, ', '.join(rec) or 'none', ', '.join(wrong) or 'none'))
    rd.say()
    ok1 = best is not None and res[best][2] > 0.0280
    rd.rec('SO1', 'sign units only, an alpha with FDR <= 10% covers more than 2.80%', 'alpha %s: %.2f%%' % (best, 100 * res[best][2] if best else 0), ok1)
    rd.rec('SO2', 'Linear B with it: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('SO3', 'alpha 0.005 keeps FDR <= 10% without the family units', 'FDR %.1f%%' % (100 * res[0.005][1]), res[0.005][1] <= 0.10)
    rd.rec('SO4', 'progress rule: SO1 and SO2 (the referent line uses sign units only at that alpha)', 'SO1 %s, SO2 %s' % (ok1, len(rec) >= 2 and not wrong), ok1 and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
