"""Seventy-sixth registered prediction set (PREDICTIONS.md, NP1-NP20): the name as a noun phrase. Writes
results/predict_test76.md. Counts over distinct names and lines."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test72 import cval
from signs import FISH

random.seed(96)


def fcounted(lines):
    """[(value, kind, sign)] for numeral runs followed by a sign in distinct formulas."""
    out = []
    for t in lines:
        if not nonname(list(t)):
            continue
        for i in range(1, len(t)):
            if t[i] not in R.NUMS and t[i - 1] in R.NUMS:
                j = i - 1
                while j > 0 and t[j - 1] in R.NUMS:
                    j -= 1
                out.append((sum(R.NUMS[g][0] for g in t[j:i]), R.kind(t[i - 1]), t[i]))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Seventy-sixth registered predictions: the name as a noun phrase', 'predict_test76')
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    DL = sorted({tuple(t) for t in AB})
    heads = {b[-1] for b, e in ns}
    mh = [(b[-2], cat[b[-1]]) for b, e in ns if len(b) >= 2 and b[-2] not in R.NUMS and b[-1] in cat]
    rd.mi('NP1', 'the head selects its modifier', 'names with a modifier before a categorised head', [m for m, _ in mh], [c for _, c in mh])

    def np2(names, key, lab):
        ch = [(b[-1], min(cval(b)[0], 5)) for b, e in names if b and cval(b)]
        rd.mi(key, 'the head selects its number%s' % lab, 'counted heads', [h for h, _ in ch], [v for _, v in ch])
    np2(ns, 'NP2', '')
    fc = fcounted(DL)
    nk, nv, fk, fv = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    for b, e in ns:
        if cval(b):
            v, k = cval(b)
            nk[b[-1]][k] += 1
            nv[b[-1]][v] += 1
    for v, k, s in fc:
        fk[s][k] += 1
        fv[s][v] += 1
    both = [s for s in nk if s in fk]
    top = lambda c: c.most_common(1)[0][0]
    rd.thr('NP3', 'one notation in names and formulas', 'signs counted in both with the same commonest kind', sum(top(nk[s]) == top(fk[s]) for s in both), len(both), 0.7)
    rd.thr('NP4', 'one typical count in names and formulas', 'signs counted in both with the same commonest value', sum(top(nv[s]) == top(fv[s]) for s in both), len(both), 0.5)
    rd.rank('NP5', 'names count small', 'formula against name values', [v for v, k, s in fc], [cval(b)[0] for b, e in ns if cval(b)])
    rd.gtl('NP6', 'fish heads are counted', 'counted, fish heads', [bool(cval(b)) for b, e in ns if b[-1] in FISH], [bool(cval(b)) for b, e in ns if b[-1] not in FISH])
    ones = {b[0] for b, e in ns if len(b) == 1}
    ch = {b[-1] for b, e in ns if cval(b)}
    rd.gtl('NP7', 'counted heads stand alone', '1-sign names, counted head types', [h in ones for h in ch], [h in ones for h in heads - ch])
    mp = {(x, y) for b, e in ns for x, y in zip(b[:-1], b[1:-1]) if x not in R.NUMS and y not in R.NUMS and x != y}
    rd.thr('NP8', 'modifiers keep their order', 'modifier pairs attested reversed', sum((y, x) in mp for x, y in mp), len(mp), 0.2, above=False)

    def np9(names, key, lab):
        a = sum(1 for b, e in names if len(b) >= 3 and b[-3] not in R.NUMS and b[-2] in R.NUMS and b[-1] not in R.NUMS)
        c = sum(1 for b, e in names if len(b) >= 3 and b[-3] in R.NUMS and b[-2] not in R.NUMS and b[-1] not in R.NUMS)
        p = R.binom_ge(a, a + c)
        rd.rec(key, 'the modifier stands before the number%s' % lab, "'mod N head' %d, 'N mod head' %d; p = %.4f" % (a, c, p), a > c and p < 0.05)
    np9(ns, 'NP9', '')
    b3 = [b for b, e in ns if len(b) == 3]
    sl = [(0, b[0]) for b in b3] + [(1, b[1]) for b in b3]
    rd.mi('NP10', 'openers and middles are different signs', 'slot tokens', [s for s, _ in sl], [g for _, g in sl])
    runs = lambda b: sum(1 for i, g in enumerate(b) if g in R.NUMS and (i == 0 or b[i - 1] not in R.NUMS))
    rd.thr('NP11', 'one number per name', 'bodies with two numeral runs', sum(runs(b) >= 2 for b, e in ns), len(ns), 0.05, above=False)
    mods = defaultdict(set)
    nn = Counter()
    for b, e in ns:
        nn[b[-1]] += 1
        for g in b[:-1]:
            if g not in R.NUMS:
                mods[b[-1]].add(g)
    h3 = [h for h in nn if nn[h] >= 3]
    rd.rank('NP12', 'counted heads take more modifiers', 'counted against uncounted heads', [len(mods[h]) / nn[h] for h in h3 if h in ch],
            [len(mods[h]) / nn[h] for h in h3 if h not in ch])

    def np13(lines, names, key, lab):
        hd = {b[-1] for b, e in names if b}
        f = fcounted(lines)
        tok = [g for t in lines if nonname(list(t)) for g in t if g not in R.NUMS]
        rd.gtl(key, 'formulas count name heads%s' % lab, 'name heads, signs after a numeral', [s in hd for v, k, s in f], [g in hd for g in tok])
    np13(DL, ns, 'NP13', '')
    res2 = [tuple(g for g in t if g not in R.NUMS) for t in DL if nonname(list(t))]
    res2 = [r_ for r_ in res2 if len(r_) == 2]
    x = sum(r_[1] in heads and r_[0] not in heads for r_ in res2)
    y = sum(r_[0] in heads and r_[1] not in heads for r_ in res2)
    p = R.binom_ge(x, x + y)
    rd.rec('NP14', 'formula residues end in a head', 'head last only %d, first only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    fcs = {s for v, k, s in fc}
    rd.gtl('NP15', 'number-first names name counted things', 'formula-counted head, numeral-first names',
           [b[-1] in fcs for b, e in ns if len(b) >= 2 and b[0] in R.NUMS], [b[-1] in fcs for b, e in ns if len(b) >= 2 and b[0] not in R.NUMS])
    nsB = sorted({(b, e) for b, e in T.names(B) if b})
    np2(nsB, 'NP16', ' (B)')
    np13(sorted({tuple(t) for t in B}), nsB, 'NP17', ' (B)')
    fs = lambda site: sorted({(b, e) for r in F if r['site'].strip() == site for b, e in R.names_in(r) if b})
    np2(fs('Harappa'), 'NP18', ' (Harappa)')
    np2(fs('Mohenjo-daro'), 'NP19', ' (Mohenjo-daro)')
    np9(nsB, 'NP20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
