"""Three-hundred-and-thirtieth registered prediction set (PREDICTIONS.md, SA1-SA4): decipherment loop 155, the combined
pool of set 329 (tablets, seals, tags) at stricter alphas (0.0001, 0.0005, 0.001, 0.002, 0.005): the alpha with FDR <=
10% (100 picture shuffles) and the largest coverage is chosen, the Linear B control re-run with it; coverage without
units labelled Bull1 (the default seal animal, possibly a seal type rather than a word) is reported beside it.
Writes results/predict_test330.md."""
import rtools as R
import referents as X
from predict_test200 import objects
from predict_test235 import KEY
from predict_test237 import merged
from predict_test234 import lines
from predict_test254 import frag_objects
from predict_test304 import coverage, fdr
from predict_test325 import build, lb_q
from progress import data

TYPES = ('SEAL:S', 'SEAL:R', 'SEAL', 'SEAL:C', 'SEAL:CY', 'TAG')
ALPHAS = (0.0001, 0.0005, 0.001, 0.002, 0.005)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirtieth registered predictions: decipherment loop 155, the combined pool at stricter alphas', 'predict_test330')
    DL, tr, te = data()
    P = X.pools(F, recs)
    sc = objects(F, recs, TYPES)
    P2 = {'made': (P['made'][0] + P['moulded'][0] + sc, merged(P['made'][1] + P['moulded'][1] + sc + frag_objects(TYPES)))}
    res = {}
    for a in ALPHAS:
        f = build(a)
        u = f(P2)
        nb = {k: ({g: m for g, m in v.items() if m != 'Bull1'}) for k, v in u.items()}
        res[a] = (X.count(u), fdr(P2, f, 330), coverage(DL, P2, u), coverage(DL, P2, nb))
        rd.say('- alpha %.4f: %d units, FDR %.1f%%, coverage %.2f%% (without Bull1 units %.2f%%).' % (a, res[a][0], 100 * res[a][1], 100 * res[a][2], 100 * res[a][3]))
    good = [a for a in ALPHAS if res[a][1] <= 0.10]
    best = max(good, key=lambda a: (res[a][2], -a)) if good else None
    q = lb_q(lines(), best or 0.0001)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say('- Linear B with alpha %s: recovered %s; wrong %s.' % (best, ', '.join(rec) or 'none', ', '.join(wrong) or 'none'))
    rd.say()
    ok1 = best is not None and res[best][2] > 0.0543
    rd.rec('SA1', 'an alpha with FDR <= 10% gives coverage above 5.43%', 'alpha %s: %.2f%%' % (best, 100 * res[best][2] if best else 0), ok1)
    rd.rec('SA2', 'without Bull1 units that alpha still covers more than 5.43%', '%.2f%%' % (100 * res[best][3] if best else 0), best is not None and res[best][3] > 0.0543)
    rd.rec('SA3', 'Linear B with that alpha: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('SA4', 'progress rule: SA1 and SA3 (the referent line uses the combined pool at that alpha)', 'SA1 %s, SA3 %s' % (ok1, len(rec) >= 2 and not wrong), ok1 and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
