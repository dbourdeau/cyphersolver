"""Two-hundred-and-fourteenth registered prediction set (PREDICTIONS.md, FP1-FP4): decipherment loop 39, the opening
sign by position (famlm firstpos). Writes results/predict_test214.md."""
import rtools as R
from famlm import score3
from prizebench import sign_task
from progress import data
from signs import load

OLD = ['trik', 'pos', 'end', 'f4k', 'first']
NEW = ['trik', 'pos', 'end', 'f4k', 'firstpos']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fourteenth registered predictions: decipherment loop 39, opening sign by position', 'predict_test214')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, OLD)
    s1, w1 = score3(tr, te, NEW)
    rd.rec('FP1', 'firstpos beats first', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.005)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, OLD)
    b1, _ = score3(DA, DBx, NEW)
    rd.rec('FP2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_task(tr, te, OLD)[0]
    c1 = sign_task(tr, te, NEW)[0]
    rd.rec('FP3', 'SIGN top-1 does not fall', 'first %.1f%%, firstpos %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    rd.rec('FP4', 'progress rule', 'FP1 %s, FP2 %s' % (s0 - s1 >= 0.005, b1 < b0), s0 - s1 >= 0.005 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
