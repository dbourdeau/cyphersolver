"""Two-hundred-and-seventeenth registered prediction set (PREDICTIONS.md, F21-F24): decipherment loop 42, the first two
signs as context (famlm first2). Writes results/predict_test217.md."""
import rtools as R
from famlm import score3
from prizebench import sign_task
from progress import data
from signs import load

OLD = ['trik', 'pos', 'end', 'f4k', 'first']
NEW = ['trik', 'pos', 'end', 'f4k', 'first2']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-seventeenth registered predictions: decipherment loop 42, the first two signs as context', 'predict_test217')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, OLD)
    s1, w1 = score3(tr, te, NEW)
    rd.rec('F21', 'first2 beats first', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.01)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, OLD)
    b1, _ = score3(DA, DBx, NEW)
    rd.rec('F22', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_task(tr, te, OLD)[0]
    c1 = sign_task(tr, te, NEW)[0]
    rd.rec('F23', 'SIGN top-1 does not fall', 'first %.1f%%, first2 %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    rd.rec('F24', 'progress rule', 'F21 %s, F22 %s, F23 %s' % (s0 - s1 >= 0.01, b1 < b0, c1 >= a1), s0 - s1 >= 0.01 and b1 < b0 and c1 >= a1)
    rd.finish()


if __name__ == '__main__':
    main()
