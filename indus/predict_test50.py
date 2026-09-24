"""Fiftieth registered prediction set (PREDICTIONS.md, SC1-SC10): numbers on seals against numbers on tablets. Writes
results/predict_test50.md."""
import math
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(70)


def ent(xs):
    c = Counter(xs)
    n = len(xs)
    return -sum(v / n * math.log2(v / n) for v in c.values())


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Fiftieth registered predictions: numbers on seals against numbers on tablets', 'predict_test50')
    num = lambda t: any(g in R.NUMS for g in t)
    val = lambda t: sum(R.NUMS[g][0] for g in t if g in R.NUMS)
    S = [ln for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if nonname(ln) and num(ln)]
    Tb = [ln for r in F if r['type'].startswith('TAB') for ln in r['seq'] if nonname(ln) and num(ln)]
    rd.say('- seal numeral formulas %d, tablet numeral formulas %d; kinds %s.' % (len(S), len(Tb), sorted({R.kind(g) for g in R.NUMS})))
    rd.say()
    rd.rank('SC1', 'seals count higher', 'seal against tablet values', [val(t) for t in S], [val(t) for t in Tb])
    rd.gtl('SC2', 'seals use the tiered form', 'tiered, seal numerals', [R.kind(g) == 'tiered' for t in S for g in t if g in R.NUMS],
           [R.kind(g) == 'tiered' for t in Tb for g in t if g in R.NUMS])
    nx = [(0, y) for t in S for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS] + \
         [(1, y) for t in Tb for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS]
    rd.mi('SC3', 'seals count other things', 'numeral + sign pairs', [k for k, _ in nx], [y for _, y in nx])
    rd.rank('SC4', 'seal formulas are longer', 'seal against tablet formulas', [len(t) for t in S], [len(t) for t in Tb])
    sl = [(r['motif'].strip(), num(ln)) for r in rowsA if r['type'].startswith('SEAL') and r['motif'].strip() for ln in r['seq'] if ln]
    rd.mi('SC5', 'the motif goes with the count', 'seal lines with a motif', [m for m, _ in sl], [k for _, k in sl])
    sm = lambda site: [any(nonname(ln) and num(ln) for ln in r['seq']) for r in F if r['type'].startswith('SEAL') and r['site'].strip() == site]
    rd.gtl('SC6', 'Mohenjo-daro seals count', 'seals with a numeral formula, Mohenjo-daro', sm('Mohenjo-daro'), sm('Harappa'))
    v390 = []
    for r in F:
        for ln in r['seq']:
            for i in range(1, len(ln)):
                if ln[i] == '390' and ln[i - 1] in R.NUMS:
                    j = i - 1
                    while j > 0 and ln[j - 1] in R.NUMS:
                        j -= 1
                    v390.append(sum(R.NUMS[g][0] for g in ln[j:i]))
    rd.thr('SC7', '390 takes three or more', 'values before 390 (%s)' % dict(sorted(Counter(v390).items())), sum(v >= 3 for v in v390), len(v390), 0.9)
    hd = lambda t: t[0] in ('817', '820', '861')
    rd.gtl('SC8', 'seal counts are headed', 'heading first, seal numeral formulas', [hd(t) for t in S], [hd(t) for t in Tb])
    bodies = {b for b, _ in T.names(AB) if len(b) >= 2}
    emb = lambda t: any(tuple(t[i:j]) in bodies for i in range(len(t)) for j in range(i + 2, len(t) + 1))
    rd.gtl('SC9', 'seal counts cite a name', 'embedded body, seal numeral formulas', [emb(t) for t in S], [emb(t) for t in Tb])
    vs, vt = [val(t) for t in S], [val(t) for t in Tb]
    obs = ent(vs) - ent(vt)
    allv = vs + vt
    ge = 0
    for _ in range(R.N):
        random.shuffle(allv)
        ge += ent(allv[:len(vs)]) - ent(allv[len(vs):]) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('SC10', 'seal counts vary more', 'entropy seals %.2f, tablets %.2f bits; p = %.4f' % (ent(vs), ent(vt), p), obs > 0 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
