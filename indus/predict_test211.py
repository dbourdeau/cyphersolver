"""Two-hundred-and-eleventh registered prediction set (PREDICTIONS.md, TK1-TK4): decipherment loop 36, the discounted
sign trigram trik (famlm.py) against tri. Writes results/predict_test211.md."""
import rtools as R
from famlm import score3
from prizebench import sign_task
from progress import data
from signs import load

OLD = ['tri', 'pos', 'end', 'f4k']
NEW = ['trik', 'pos', 'end', 'f4k']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eleventh registered predictions: decipherment loop 36, a discounted sign trigram', 'predict_test211')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, OLD)
    s1, w1 = score3(tr, te, NEW)
    rd.rec('TK1', 'trik beats tri on the fixed test', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.01)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, OLD)
    b1, _ = score3(DA, DBx, NEW)
    rd.rec('TK2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_task(tr, te, OLD)[0]
    c1 = sign_task(tr, te, NEW)[0]
    rd.rec('TK3', 'SIGN top-1 does not fall', 'tri %.1f%%, trik %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    rd.rec('TK4', 'progress rule', 'TK1 %s, TK2 %s' % (s0 - s1 >= 0.01, b1 < b0), s0 - s1 >= 0.01 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
