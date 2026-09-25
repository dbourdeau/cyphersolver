"""Two-hundred-and-thirty-ninth registered prediction set (PREDICTIONS.md, F51-F54): decipherment loop 64, a family
5-gram context (famlm f5k). Writes results/predict_test239.md."""
import rtools as R
from famlm import score3
from prizebench import sign_task
from progress import data
from signs import load

OLD = ['trik', 'pos', 'end', 'f4k']
NEW = ['trik', 'pos', 'end', 'f5k']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirty-ninth registered predictions: decipherment loop 64, a longer family context', 'predict_test239')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, OLD)
    s1, w1 = score3(tr, te, NEW)
    rd.rec('F51', 'f5k beats f4k', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.003)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, OLD)
    b1, _ = score3(DA, DBx, NEW)
    rd.rec('F52', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_task(tr, te, OLD)[0]
    c1 = sign_task(tr, te, NEW)[0]
    rd.rec('F53', 'SIGN top-1 does not fall', 'before %.1f%%, after %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    rd.rec('F54', 'progress rule', 'F51 %s, F52 %s, F53 %s' % (s0 - s1 >= 0.003, b1 < b0, c1 >= a1), s0 - s1 >= 0.003 and b1 < b0 and c1 >= a1)
    rd.finish()


if __name__ == '__main__':
    main()
