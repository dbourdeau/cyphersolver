"""Two-hundred-and-twelfth registered prediction set (PREDICTIONS.md, SM1-SM4): decipherment loop 37, add-0.3 in place of
add-one smoothing in the count components (famlm.M3.K). Writes results/predict_test212.md."""
import rtools as R
from famlm import M3, score3, with_k
from prizebench import sign_task
from progress import data
from signs import load

KEYS = ['trik', 'pos', 'end', 'f4k']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twelfth registered predictions: decipherment loop 37, lighter smoothing', 'predict_test212')
    DL, tr, te = data()
    K3 = with_k(0.3)
    s0, _ = score3(tr, te, KEYS)
    s1, w1 = score3(tr, te, KEYS, cls=K3)
    rd.rec('SM1', 'add-0.3 improves S on the fixed test', 'S %.4f -> %.4f (gain %.4f; weights %s)' % (s0, s1, s0 - s1, {k: round(v, 3) for k, v in w1.items()}), s0 - s1 >= 0.005)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, KEYS)
    b1, _ = score3(DA, DBx, KEYS, cls=K3)
    rd.rec('SM2', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    import prizebench
    a1 = sign_task(tr, te, KEYS)[0]
    prizebench.M3 = K3
    c1 = sign_task(tr, te, KEYS)[0]
    prizebench.M3 = M3
    rd.rec('SM3', 'SIGN top-1 does not fall', 'add-one %.1f%%, add-0.3 %.1f%%' % (100 * a1, 100 * c1), c1 >= a1)
    rd.rec('SM4', 'progress rule', 'SM1 %s, SM2 %s' % (s0 - s1 >= 0.005, b1 < b0), s0 - s1 >= 0.005 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
