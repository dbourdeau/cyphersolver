"""Hundred-and-twentieth registered prediction set (PREDICTIONS.md, SK1-SK15): two kinds of closer. Writes
results/predict_test120.md."""
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test81 import classes_of
from predict_test103 import CL
from predict_test118 import strip

ST = ('151', '161', '527', '565', '621', '679')
PL = ('154', '156', '226', '241', '426')
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twentieth registered predictions: two kinds of closer', 'predict_test120')
    DL = sorted({tuple(t) for t in AB})
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    FL = sorted({t for s, ty, t in FD})
    BL = sorted({tuple(t) for t in B})

    def bodies(lines, kind):
        out = []
        for t in lines:
            s = strip(t)
            for i in range(1, len(s)):
                if s[i] in kind and s[i - 1] not in R.END:
                    out.append(s[:i])
        return out

    def b740(lines):
        return {strip(t)[:i] for t in lines for i in range(1, len(strip(t))) if strip(t)[i] == '740'}

    def sk1(lines, key, lab):
        b7 = b740(lines)
        rd.gtl(key, 'plain closers replace 740%s' % lab, 'body also before 740, plain', [b in b7 for b in bodies(lines, PL)], [b in b7 for b in bodies(lines, ST)])
    sk1(DL, 'SK1', '')

    def sk2(lines, key, lab):
        x = [(t, i) for t in lines for i in range(len(t)) if t[i] in ST]
        rd.thr(key, 'stacking closers follow 740%s' % lab, 'stacking tokens after 740', sum(i > 0 and t[i - 1] == '740' for t, i in x), len(x), 0.25)
    sk2(DL, 'SK2', '')
    n = sum(1 for t in FL if any(x == '740' and y in PL for x, y in zip(t, t[1:])))
    rd.rec('SK3', "plain closers never follow 740 (F')", 'distinct lines %d; threshold 1' % n, n <= 1)
    cl = classes_of(sorted({(b, e) for b, e in T.names(AB) if b}))
    bp, bs = bodies(DL, PL), bodies(DL, ST)
    rd.gtl('SK4', 'plain closers follow the 520 class', '520-class head, plain', [cl.get(b[-1]) == '520' for b in bp if b], [cl.get(b[-1]) == '520' for b in bs if b])
    kind = lambda t: 'S' if any(g in ST for g in t) else ('P' if any(g in PL for g in t) else None)
    rd.gtl('SK5', 'stacking closers are tablet forms', 'tablet, stacking lines', [ty == 'TAB' for s, ty, t in FD if kind(t) == 'S'], [ty == 'TAB' for s, ty, t in FD if kind(t) == 'P'])
    f4 = lambda t, K: any(t[i] in K and t[i + 1] == '400' for i in range(len(t) - 1))
    rd.gtl('SK6', 'plain closers take 400', '400 after, plain lines', [f4(t, PL) for t in DL if kind(t) == 'P'], [f4(t, ST) for t in DL if kind(t) == 'S'])
    a = [s == 'Mohenjo-daro' for s, ty, t in FD if kind(t) == 'P' and s in CITY]
    c = [s == 'Mohenjo-daro' for s, ty, t in FD if kind(t) == 'S' and s in CITY]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('SK7', 'the kinds differ by city', 'Mohenjo-daro, plain %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p < 0.05)
    hs = [cl[b[-1]] for b in bs if b and b[-1] in cl]
    hp = [cl[b[-1]] for b in bp if b and b[-1] in cl]
    rd.thr('SK8', 'stacking closers follow 740-class heads', '740-class heads before stacking closers', sum(x == '740' for x in hs), len(hs), 0.9)
    rd.thr('SK9', 'plain closers follow other heads too', '740-class heads before plain closers', sum(x == '740' for x in hp), len(hp), 0.8, above=False)
    cnt = lambda b: len(b) >= 2 and b[-2] in R.NUMS
    rd.gtl('SK10', 'plain closers are counted', 'counted head, plain', [cnt(b) for b in bp], [cnt(b) for b in bs])

    def sk11(lines, key, lab):
        b7 = b740(lines)
        rd.gtl(key, 'stacking bodies are names%s' % lab, 'body also before 740, stacking', [b in b7 for b in bodies(lines, ST)], [b in b7 for b in bodies(lines, PL)])
    sk11(DL, 'SK11', '')
    sk1(BL, 'SK12', ' (B)')
    sk2(FL, 'SK13', " (F')")
    sk11(FL, 'SK14', " (F')")
    tails = []
    for t in DL:
        for i in range(len(t) - 1):
            if t[i] in R.END and t[i + 1] not in ('400', '90'):
                tails.append(t[i + 1])
    ns, np_ = sum(g in ST for g in tails), sum(g in PL for g in tails)
    rd.rec('SK15', 'name tails are stacking closers', 'stacking %d, plain %d' % (ns, np_), ns >= 3 * max(1, np_))
    rd.finish()


if __name__ == '__main__':
    main()
