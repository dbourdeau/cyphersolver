"""Two-hundred-and-tenth registered prediction set (PREDICTIONS.md, DK1-DK4): decipherment loop 35, the discounted family
context f4k (famlm.py) against f4. Writes results/predict_test210.md."""
import rtools as R
from famlm import score3
from prizebench import sign_task
from progress import data
from signs import load

OLD = ['tri', 'pos', 'end', 'f4']
NEW = ['tri', 'pos', 'end', 'f4k']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-tenth registered predictions: decipherment loop 35, discounted family context', 'predict_test210')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, OLD)
    s1, w1 = score3(tr, te, NEW)
    rd.rec('DK1', 'f4k beats f4 on the fixed test', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.003)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, OLD)
    b1, _ = score3(DA, DBx, NEW)
    rd.rec('DK2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_task(tr, te, OLD)[0]
    c1 = sign_task(tr, te, NEW)[0]
    rd.rec('DK3', 'SIGN top-1 does not fall', 'f4 %.1f%%, f4k %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    rd.rec('DK4', 'progress rule', 'DK1 %s, DK2 %s' % (s0 - s1 >= 0.003, b1 < b0), s0 - s1 >= 0.003 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
