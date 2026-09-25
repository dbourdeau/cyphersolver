"""Three-hundred-and-twenty-first registered prediction set (PREDICTIONS.md, PC1-PC2): decipherment loop 146, referent
units over picture classes. ICIT picture codes merged into classes fixed here (bovine: Bult Bull1 Bull Bull2 Zebu Gaur
Buff; goat: Goat; plant: Phyt Pipal; others unchanged); set 312's configuration re-run with the classes as pictures;
combined FDR against 100 shuffles of the classes. Writes results/predict_test321.md."""
import rtools as R
import referents as X
from predict_test304 import coverage, fdr
from predict_test312 import plus4
from progress import data

CLASS = {'Bult': 'bovine', 'Bull1': 'bovine', 'Bull': 'bovine', 'Bull2': 'bovine', 'Zebu': 'bovine', 'Gaur': 'bovine',
         'Buff': 'bovine', 'Phyt': 'plant', 'Pipal': 'plant'}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-first registered predictions: decipherment loop 146, referent units over picture classes', 'predict_test321')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, plus4(P))
    PC = {lab: ([(t, CLASS.get(m, m)) for t, m in clean], [(t, CLASS.get(m, m)) for t, m in both]) for lab, (clean, both) in P.items()}
    u = plus4(PC)
    f = fdr(PC, plus4, 321)
    c1 = coverage(DL, PC, u)
    rd.say('- %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (X.count(u), 100 * f, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('PC1', 'combined FDR <= 10% and coverage rises above 2.29%', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * f, 100 * c0, 100 * c1), f <= 0.10 and c1 > c0)
    rd.rec('PC2', 'progress rule: PC1 (the referent line uses picture classes)', 'PC1 %s' % (f <= 0.10 and c1 > c0), f <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
