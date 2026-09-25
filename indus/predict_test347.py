"""Three-hundred-and-forty-seventh registered prediction set (PREDICTIONS.md, WF1-WF3): decipherment loop 172, family
wide skip-pairs and 5-sign runs added to set 346's referent units (true-duplicate pool, alpha 0.002); FDR against 100
within-stratum shuffles; Linear B control. Writes results/predict_test347.md."""
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
    rd = R.Round('Three-hundred-and-forty-seventh registered predictions: decipherment loop 172, family wide skip-pairs and 5-sign runs', 'predict_test347')
    DL, tr, te = data()
    clean, both = objects_typed(F, recs)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    cc, cb = collapse(clean), collapse(both)
    S.ALPHA = 0.002
    S.SIGN = tuple(S.SIGN) + (-3, 5)
    S.FAM = tuple(S.FAM) + (-3,)
    u = S.units(cc, cb)
    n, f = fdr(cc, cb, 347)
    c = coverage(DL, P, u)
    rd.say('- %d units (%d 5-sign runs, %d family wide skip-pairs), FDR %.1f%%, coverage %.2f%% (set 346: 2.86%%).' % (n, len(u.get(('made', 5), {})), len(u.get(('Fmade', -3), {})), 100 * f, 100 * c))
    q = lb_q(lines(), 0.002)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say()
    ok = f <= 0.10 and c > 0.0286
    rd.rec('WF1', 'FDR <= 10% and coverage above 2.86%', 'FDR %.1f%%, %.2f%%' % (100 * f, 100 * c), ok)
    rd.rec('WF2', 'Linear B at alpha 0.002: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('WF3', 'progress rule: WF1 and WF2 (family wide skip-pairs and 5-sign runs join)', 'WF1 %s, WF2 %s' % (ok, len(rec) >= 2 and not wrong), ok and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
