"""Hundred-and-thirty-fourth registered prediction set (PREDICTIONS.md, IC1-IC10): our genres against ICIT's text
codes. Writes results/predict_test134.md."""
import math
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test108 import genre


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round("Hundred-and-thirty-fourth registered predictions: our genres against ICIT's text codes", 'predict_test134')
    code = lambda r: recs[r['sealid']][25].strip()
    rows = [(code(r), tuple(ln), r) for r in F for ln in r['seq'] if ln]
    gc = [(c, genre(t)) for c, t, r in rows]
    Hg = -sum(v / len(gc) * math.log2(v / len(gc)) for v in Counter(g for c, g in gc).values())
    mi = T.mi([c for c, g in gc], [g for c, g in gc])
    rd.rec('IC1', 'our genres agree with ICIT', 'MI %.3f / H(genre) %.3f = %.2f; threshold 0.3' % (mi, Hg, mi / Hg), mi / Hg >= 0.3)
    sub = lambda codes: [(t, genre(t)) for c, t, r in rows if c in codes]
    x = sub(('VN',))
    rd.thr('IC2', 'VN = counts', 'VN lines that are counts', sum(g == 'count' for t, g in x), len(x), 0.9)
    x = sub(('LP', 'IT', 'SP', 'MT'))
    rd.thr('IC3', 'LP/IT/SP/MT = names', 'lines that are names', sum(g == 'name' for t, g in x), len(x), 0.7)
    x = sub(('NU',))
    rd.thr('IC4', 'NU = numerals only', 'NU lines of numerals only', sum(all(s in R.NUMS for s in t) for t, g in x), len(x), 0.8)
    x = sub(('TS',))
    rd.thr('IC5', 'TS = single signs', 'TS lines of one sign', sum(len(t) == 1 for t, g in x), len(x), 0.8)
    x = sub(('LC',))
    rd.thr('IC6', 'LC = counts', 'LC lines that are counts', sum(g == 'count' for t, g in x), len(x), 0.6)
    o2 = {r['sealid']: len([ln for ln in r['seq'] if ln]) for r in F if code(r) == '2L'}
    rd.thr('IC7', '2L = two lines', '2L objects with 2+ lines', sum(n >= 2 for n in o2.values()), len(o2), 0.9)
    cc = Counter(c for c, t, r in rows if genre(t) == 'closer')
    rd.rec('IC8', 'closer inscriptions are our own category', 'commonest ICIT code among closer lines: %s of %d' % (cc.most_common(3), sum(cc.values())),
           cc.most_common(1)[0][1] / sum(cc.values()) < 0.5)
    bc = Counter(c for c, t, r in rows if genre(t) == 'bare')
    rd.thr('IC9', 'bare lines are SC', 'bare lines coded SC (%s)' % bc.most_common(3), bc['SC'], sum(bc.values()), 0.5)
    ss = Counter(genre(t) for c, t, r in rows if c == 'SS')
    rd.rec('IC10', 'SS is mixed', 'SS genres %s' % dict(ss), ss.most_common(1)[0][1] / sum(ss.values()) < 0.7)
    rd.finish()


if __name__ == '__main__':
    main()
