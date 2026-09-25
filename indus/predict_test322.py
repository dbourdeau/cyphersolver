"""Three-hundred-and-twenty-second registered prediction set (PREDICTIONS.md, PX1-PX2): decipherment loop 147, the
referent pools without catch-all objects: tablets whose picture code is Mult, Scene or Comp (several pictures, a scene,
a composite) are removed from both pools before set 312's configuration is run; combined FDR against 100 picture
shuffles; coverage on the real tokens (texts of the remaining pictured tablets). Writes results/predict_test322.md."""
import rtools as R
import referents as X
from predict_test304 import coverage, fdr
from predict_test312 import plus4
from progress import data

CATCH = {'Mult', 'Scene', 'Comp'}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-second registered predictions: decipherment loop 147, the referent pools without catch-all objects', 'predict_test322')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, plus4(P))
    PQ = {lab: ([o for o in clean if o[1] not in CATCH], [o for o in both if o[1] not in CATCH]) for lab, (clean, both) in P.items()}
    u = plus4(PQ)
    f = fdr(PQ, plus4, 322)
    c1 = coverage(DL, PQ, u)
    rd.say('- objects %d -> %d; %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (sum(len(b) for c, b in P.values()), sum(len(b) for c, b in PQ.values()), X.count(u), 100 * f, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('PX1', 'combined FDR <= 10% and coverage rises above 2.29%', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * f, 100 * c0, 100 * c1), f <= 0.10 and c1 > c0)
    rd.rec('PX2', 'progress rule: PX1 (the referent pools drop the catch-all objects)', 'PX1 %s' % (f <= 0.10 and c1 > c0), f <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
