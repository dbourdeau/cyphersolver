"""Two-hundred-and-thirteenth registered prediction set (PREDICTIONS.md, FS1-FS4): decipherment loop 38, the opening
sign as context (the set-125 first component). Writes results/predict_test213.md."""
import rtools as R
from famlm import score3
from prizebench import sign_task
from progress import data
from signs import load

OLD = ['trik', 'pos', 'end', 'f4k']
NEW = ['trik', 'pos', 'end', 'f4k', 'first']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirteenth registered predictions: decipherment loop 38, the opening sign as context', 'predict_test213')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, OLD)
    s1, w1 = score3(tr, te, NEW)
    rd.rec('FS1', '+ first beats the model without it', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.005)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, OLD)
    b1, _ = score3(DA, DBx, NEW)
    rd.rec('FS2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    a1 = sign_task(tr, te, OLD)[0]
    c1 = sign_task(tr, te, NEW)[0]
    rd.rec('FS3', 'SIGN top-1 does not fall', 'without %.1f%%, with first %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    rd.rec('FS4', 'progress rule', 'FS1 %s, FS2 %s' % (s0 - s1 >= 0.005, b1 < b0), s0 - s1 >= 0.005 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
