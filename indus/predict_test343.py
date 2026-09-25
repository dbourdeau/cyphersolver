"""Three-hundred-and-forty-third registered prediction set (PREDICTIONS.md, VS1-VS4): decipherment loop 168, two variants of
the true-duplicate referent pool (set 339, site-and-class strata, alpha 0.002): (a) alpha 0.003; (b) site-only strata
at alpha 0.002 (class strata were for the seal-bull phrases, now mostly gone with mould copies counted once). Each
with FDR against 100 within-stratum shuffles; the variant with FDR <= 10% and the larger coverage is chosen; Linear B
control with its alpha. Writes results/predict_test343.md."""
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
    rd = R.Round('Three-hundred-and-forty-third registered predictions: decipherment loop 168, two variants of the true-duplicate referent pool', 'predict_test343')
    DL, tr, te = data()
    clean, both = objects_typed(F, recs)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    cc, cb = collapse(clean), collapse(both)
    res = {}
    S.ALPHA = 0.003
    ua = S.units(cc, cb)
    na, fa = fdr(cc, cb, 3431)
    res['a alpha 0.003'] = (na, fa, coverage(DL, P, ua), 0.003)
    site_only = lambda obs: [(t, m, (s[0],)) for t, m, s in obs]
    S.ALPHA = 0.002
    sc, sb = site_only(cc), site_only(cb)
    ub = S.units(sc, sb)
    nb, fb = fdr(sc, sb, 3432)
    res['b site-only strata'] = (nb, fb, coverage(DL, P, ub), 0.002)
    for k, v in res.items():
        rd.say('- %s: %d units, FDR %.1f%%, coverage %.2f%%.' % (k, v[0], 100 * v[1], 100 * v[2]))
    good = [k for k in res if res[k][1] <= 0.10]
    best = max(good, key=lambda k: res[k][2]) if good else None
    q = lb_q(lines(), res[best][3] if best else 0.002)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say('- chosen %s; Linear B: recovered %s; wrong %s.' % (best, ', '.join(rec) or 'none', ', '.join(wrong) or 'none'))
    rd.say()
    ok1 = best is not None and res[best][2] > 0.0280
    rd.rec('VS1', 'a variant with FDR <= 10% covers more than 2.80%', '%s: %.2f%%' % (best, 100 * res[best][2] if best else 0), ok1)
    rd.rec('VS2', 'Linear B with its alpha: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('VS3', 'both variants keep FDR <= 10%', ', '.join('%s %.1f%%' % (k, 100 * v[1]) for k, v in res.items()), all(v[1] <= 0.10 for v in res.values()))
    rd.rec('VS4', 'progress rule: VS1 and VS2 (the referent line uses the chosen variant)', 'VS1 %s, VS2 %s' % (ok1, len(rec) >= 2 and not wrong), ok1 and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
