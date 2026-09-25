"""Two-hundred-and-forty-fifth registered prediction set (PREDICTIONS.md, FS1-FS2): decipherment loop 70, fish pairs and
seal animals. Writes results/predict_test245.md."""
import rtools as R
from predict_test17 import rank_perm
from predict_test200 import objects
from predict_test244 import split


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-fifth registered predictions: decipherment loop 70, fish names and seal animals', 'predict_test245')
    f, o = split(objects(F, recs, ('SEAL:S', 'SEAL:R')))
    d, p = rank_perm(f, o)
    ok = d > 0 and p < 0.05
    rd.rec('FS1', 'fish pairs more animal-diverse on seals', '%d against %d pairs; means %.2f and %.2f; rank difference %+.1f; p = %.4f' % (len(f), len(o), sum(f) / len(f), sum(o) / len(o), d, p), ok)
    rd.rec('FS2', 'progress rule', 'FS1 %s' % ok, ok)
    rd.finish()


if __name__ == '__main__':
    main()
