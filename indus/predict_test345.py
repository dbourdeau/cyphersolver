"""Three-hundred-and-forty-fifth registered prediction set (PREDICTIONS.md, AB1-AB3): decipherment loop 170, an adaptive
alpha for the true-duplicate referent pool (set 339): bisection between 0.002 (FDR 6.8%) and 0.003 (FDR 10.1%), five
steps, each FDR from 100 within-stratum shuffles; the largest alpha with FDR <= 10% is taken; Linear B control.
Writes results/predict_test345.md."""
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
    rd = R.Round('Three-hundred-and-forty-fifth registered predictions: decipherment loop 170, an adaptive alpha for the true-duplicate referent pool', 'predict_test345')
    DL, tr, te = data()
    clean, both = objects_typed(F, recs)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    cc, cb = collapse(clean), collapse(both)
    lo, hi = 0.002, 0.003
    best = (0.002, None)
    for step in range(5):
        mid = (lo + hi) / 2
        S.ALPHA = mid
        n, f = fdr(cc, cb, 3450 + step)
        cov = coverage(DL, P, S.units(cc, cb))
        rd.say('- alpha %.5f: %d units, FDR %.1f%%, coverage %.2f%%.' % (mid, n, 100 * f, 100 * cov))
        if f <= 0.10:
            lo, best = mid, (mid, cov)
        else:
            hi = mid
    a = best[0]
    S.ALPHA = a
    cov = best[1] if best[1] is not None else coverage(DL, P, S.units(cc, cb))
    q = lb_q(lines(), a)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say('- chosen alpha %.5f, coverage %.2f%%; Linear B: recovered %s; wrong %s.' % (a, 100 * cov, ', '.join(rec) or 'none', ', '.join(wrong) or 'none'))
    rd.say()
    ok = cov > 0.0280
    rd.rec('AB1', 'the adaptive alpha covers more than 2.80% with FDR <= 10%', 'alpha %.5f: %.2f%%' % (a, 100 * cov), ok)
    rd.rec('AB2', 'Linear B with it: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('AB3', 'progress rule: AB1 and AB2 (the referent line uses the adaptive alpha)', 'AB1 %s, AB2 %s' % (ok, len(rec) >= 2 and not wrong), ok and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
