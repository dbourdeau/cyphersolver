"""Hundred-and-eighty-seventh registered prediction set (PREDICTIONS.md, DB1-DB7): decipherment loop 12, doubling and
brackets. Writes results/predict_test187.md."""
import math
import random
from collections import Counter

import rtools as R
from predict_test103 import CL
from signs import load

random.seed(266)
M = set(R.END) | set(CL) | {'400', '90'}


def jsd(a, b):
    ta, tb = sum(a.values()), sum(b.values())
    out = 0.0
    for k in set(a) | set(b):
        p, q = a[k] / ta, b[k] / tb
        m = (p + q) / 2
        if p:
            out += 0.5 * p * math.log2(p / m)
        if q:
            out += 0.5 * q * math.log2(q / m)
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-seventh registered predictions: decipherment loop 12, doubling and brackets', 'predict_test187')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    lex = lambda g: g not in R.NUMS and g not in M
    fin = lambda t, j: all(g in ('400', '90') for g in t[j + 1:])

    def split(D):
        dbl = Counter(t[i] for t in D for i in range(len(t) - 1) if t[i] == t[i + 1] and lex(t[i]))
        signs = {g for g, n in dbl.items() if n >= 3}
        dd, ss = [], []
        for t in D:
            i = 0
            while i < len(t):
                g = t[i]
                if g in signs and i + 1 < len(t) and t[i + 1] == g:
                    dd.append((t, i, i + 1))
                    i += 2
                    continue
                if g in signs:
                    ss.append((t, i, i))
                i += 1
        return signs, dd, ss
    sa, da, ssa = split(DA)
    sb, db, ssb = split(DB)
    rd.say('- doubled signs A %s; doubled tokens A %d, single %d; B %d / %d.' % (sorted(sa), len(da), len(ssa), len(db), len(ssb)))
    rd.say()
    rd.ltl('DB1', 'doubled signs end lines less often (A)', 'final, doubled', [fin(t, j) for t, i, j in da], [fin(t, j) for t, i, j in ssa])
    rd.ltl('DB2', 'on B', 'final, doubled (B)', [fin(t, j) for t, i, j in db], [fin(t, j) for t, i, j in ssb])
    nx = lambda t, j: j + 1 < len(t) and t[j + 1] in R.END
    rd.ltl('DB3', 'doubled pairs take the ending less often', 'followed by 740 / 520, doubled', [nx(t, j) for t, i, j in da + db], [nx(t, j) for t, i, j in ssa + ssb])
    rd.gtl('DB4', 'doubling marks the opening element', 'line-initial, doubled', [i == 0 for t, i, j in da + db], [i == 0 for t, i, j in ssa + ssb])
    f_d = Counter(t[j + 1] if j + 1 < len(t) else '#' for t, i, j in da + db if t[i] == '615')
    f_s = Counter(t[j + 1] if j + 1 < len(t) else '#' for t, i, j in ssa + ssb if t[i] == '615')
    obs = jsd(f_d, f_s) if f_d and f_s else 0
    allt = [t[j + 1] if j + 1 < len(t) else '#' for t, i, j in da + db + ssa + ssb if t[i] == '615']
    nd = sum(f_d.values())
    rnd = []
    for _ in range(1000):
        random.shuffle(allt)
        rnd.append(jsd(Counter(allt[:nd]), Counter(allt[nd:])))
    q95 = sorted(rnd)[949]
    rd.rec('DB5', 'doubled 615 is followed differently', 'JSD %.3f (doubled %d, single %d); 95th percentile of random splits %.3f' % (obs, nd, sum(f_s.values()), q95), obs > q95)
    DAB = DA + DB
    br = [fin(t, i) for t in DAB for i, g in enumerate(t) if g in ('101', '103', '905')]
    bs = [fin(t, i) for t in DAB for i, g in enumerate(t) if g in ('100', '904', '927')]
    rd.gtl('DB6', 'bracketed signs end lines', 'final, bracketed', br, bs)
    rate = lambda xs: sum(xs) / max(1, len(xs))
    checks = [
        (rate([fin(t, j) for t, i, j in da]) < rate([fin(t, j) for t, i, j in ssa]), rate([fin(t, j) for t, i, j in db]) < rate([fin(t, j) for t, i, j in ssb])),
        (rate([nx(t, j) for t, i, j in da]) < rate([nx(t, j) for t, i, j in ssa]), rate([nx(t, j) for t, i, j in db]) < rate([nx(t, j) for t, i, j in ssb])),
        (rate([i == 0 for t, i, j in da]) > rate([i == 0 for t, i, j in ssa]), rate([i == 0 for t, i, j in db]) > rate([i == 0 for t, i, j in ssb]))]
    rd.rec('DB7', 'the progress rule', 'direction in A and B for DB1, DB3, DB4: %s' % checks, any(a and b for a, b in checks))
    rd.finish()


if __name__ == '__main__':
    main()
