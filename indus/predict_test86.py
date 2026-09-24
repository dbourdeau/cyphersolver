"""Eighty-sixth registered prediction set (PREDICTIONS.md, HO1-HO20): recent findings on held-out data. Writes
results/predict_test86.md. Distinct lines and names."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test53 import lab_perm, rate
from predict_test78 import parse
from predict_test81 import classes_of
from predict_test82 import jperm, suffix_lines
from signs import FISH

random.seed(106)
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Eighty-sixth registered predictions: recent findings on held-out data', 'predict_test86')
    nsAB = sorted({(b, e) for b, e in T.names(AB) if b})
    bodiesAB = {b for b, e in nsAB}
    clAB = classes_of(nsAB)
    OL = sorted({tuple(ln) for r in F if r['site'].strip() not in CITY for ln in r['seq'] if ln})
    ON = sorted({(b, e) for r in F if r['site'].strip() not in CITY for b, e in R.names_in(r) if b})
    FL = sorted({tuple(ln) for r in F for ln in r['seq'] if ln})
    FN = sorted({(b, e) for r in F for b, e in R.names_in(r) if b})
    rd.say('- smaller sites: distinct lines %d, names %d; F: lines %d, names %d.' % (len(OL), len(ON), len(FL), len(FN)))
    rd.say()
    b3 = [b for b, e in ON if len(b) == 3]
    x = sum(b[1:] in bodiesAB and b[:2] not in bodiesAB for b in b3)
    y = sum(b[:2] in bodiesAB and b[1:] not in bodiesAB for b in b3)
    p = R.binom_ge(x, x + y)
    rd.rec('HO1', 'right-branching at the small sites', '(middle, head) only %d, (opener, middle) only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    f = lambda b: any(g in FISH for g in b)
    rd.gtl('HO2', 'fish-520 at the small sites', 'fish, 520 names', [f(b) for b, e in ON if e == '520'], [f(b) for b, e in ON if e == '740'])
    hc = defaultdict(Counter)
    for b, e in ON:
        hc[b[-1]][e] += 1
    h3 = [h for h in hc if sum(hc[h].values()) >= 3]
    rd.thr('HO3', 'classes at the small sites', 'heads with one ending in 90%+', sum(max(hc[h].values()) / sum(hc[h].values()) >= 0.9 for h in h3), len(h3), 0.8)
    h2 = [h for h in hc if sum(hc[h].values()) >= 2 and h in clAB and hc[h]['740'] != hc[h]['520']]
    rd.thr('HO4', 'the small sites use the same classes', 'same majority as A + B', sum(hc[h].most_common(1)[0][0] == clAB[h] for h in h2), len(h2), 0.9)
    nt = [g for t in OL for g in t if g in R.NUMS]
    rd.gtl('HO5', 'tiered for large numbers at the small sites', 'tiered, 5-8', [R.kind(g) == 'tiered' for g in nt if 5 <= R.NUMS[g][0] <= 8],
           [R.kind(g) == 'tiered' for g in nt if 1 <= R.NUMS[g][0] <= 4])
    pr = [(R.kind(a), b) for t in OL for a, b in zip(t, t[1:]) if a in R.NUMS and b not in R.NUMS]
    rd.mi('HO6', 'the sign sets the kind at the small sites', 'numeral + sign pairs', [k for k, _ in pr], [y_ for _, y_ in pr])

    def hdr(lines):
        return [(parse(t)[0][-1], parse(t)[1][0][1]) for t in lines if nonname(list(t)) and parse(t) and parse(t)[0] and parse(t)[1]]
    hi = hdr(OL)
    rd.mi('HO7', 'the header selects the item at the small sites', 'headed formulas', [a for a, _ in hi], [b for _, b in hi])
    top = {h for h, _ in Counter(b[-1] for b, e in nsAB).most_common(10)}
    rd.thr('HO8', 'the small sites use the common heads', 'names ending in an A + B top-10 head', sum(b[-1] in top for b, e in ON), len(ON), 0.5)
    nsB = sorted({(b, e) for b, e in T.names(B) if b})
    DB = sorted({tuple(t) for t in B})
    mh = [(b[-2], cat[b[-1]]) for b, e in nsB if len(b) >= 2 and b[-2] not in R.NUMS and b[-1] in cat]
    rd.mi('HO9', 'the head selects its modifier (B)', 'names', [m for m, _ in mh], [c for _, c in mh])
    be = defaultdict(set)
    for b, e in nsB:
        be[b].add(e)
    rd.thr('HO10', 'a body keeps its ending (B)', 'bodies with both endings', sum(len(v) == 2 for v in be.values()), len(be), 0.02, above=False)
    hs = defaultdict(set)
    for b, e, f_ in suffix_lines(DB):
        if f_ in ('90', '400'):
            hs[b[-1]].add(f_)
    rd.thr('HO11', 'a head takes one suffix (B)', 'heads with only one of 90 and 400', sum(len(v) == 1 for v in hs.values()), len(hs), 0.8)
    vi = [(it, min(v, 8)) for t in DB if nonname(list(t)) and parse(t) for v, it, i in parse(t)[1]]
    rd.mi('HO12', 'the item sets the count (B)', 'counted items', [a for a, _ in vi], [b for _, b in vi])
    NLB = [t for t in DB if R.name_of(list(t))]
    FLB = [t for t in DB if nonname(list(t))]
    lines = NLB + FLB
    labs = [0] * len(NLB) + [1] * len(FLB)

    def shared(lb):
        a, c = set(), set()
        for t, l_ in zip(lines, lb):
            (a if l_ == 0 else c).update((x_, y_) for x_, y_ in zip(t, t[1:]) if x_ in R.NUMS and y_ not in R.NUMS)
        return len(a & c)
    obs = shared(labs)
    lb = labs[:]
    le = 0
    for _ in range(R.N // 10):
        random.shuffle(lb)
        le += shared(lb) <= obs
    p = (le + 1) / (R.N // 10 + 1)
    rd.rec('HO13', 'names and formulas count differently (B)', 'shared (numeral, sign) types %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    o, p = lab_perm([list(t) for t in NLB], [list(t) for t in FLB], lambda a, b: rate(a) - rate(b), R.N // 10)
    rd.rec('HO14', 'names are the repetitive genre (B)', 'repeat rate names %.3f, formulas %.3f; p = %.4f (1,000 shuffles)' % (
        rate([list(t) for t in NLB]), rate([list(t) for t in FLB]), p), o > 0 and p < 0.05)
    a = sum(1 for b, e in FN if len(b) >= 3 and b[-3] in R.NUMS and b[-2] not in R.NUMS and b[-1] not in R.NUMS)
    c = sum(1 for b, e in FN if len(b) >= 3 and b[-3] not in R.NUMS and b[-2] in R.NUMS and b[-1] not in R.NUMS)
    p = R.binom_ge(a, a + c)
    rd.rec('HO15', 'the number stands before the modifier (F)', "'N mod head' %d, 'mod N head' %d; p = %.4f" % (a, c, p), a > c and p < 0.05)
    hi = hdr(FL)
    rd.mi('HO16', 'the header selects the item (F)', 'headed formulas', [a_ for a_, _ in hi], [b_ for _, b_ in hi])
    rows = [(b[-1], f_) for b, e, f_ in suffix_lines(FL) if e == '740' and f_ in ('90', '400')]
    o, p = jperm(rows, '90', '400')
    rd.rec('HO17', '90 and 400 take different heads (F)', 'lines %d; Jaccard %.3f; p = %.4f' % (len(rows), o, p), p < 0.05)
    b3 = [b for b, e in FN if len(b) == 3]
    o1, p1 = R.mi_perm([b[1] for b in b3], [b[2] for b in b3])
    o2, p2 = R.mi_perm([b[1] for b in b3], [b[0] for b in b3])
    rd.rec('HO18', 'the middle leans on the head (F)', 'bodies %d; MI middle-head %.3f (p = %.4f), middle-opener %.3f (p = %.4f)' % (len(b3), o1, p1, o2, p2), o1 > o2 and p1 < 0.05)
    n5 = [t for t in FL if any(t[i] == '520' and t[i - 1] in R.NUMS for i in range(1, len(t)))]
    ph = [any(t[i] == '520' and t[i - 1] == '33' and i >= 2 and t[i - 2] in ('705', '706') for i in range(2, len(t))) for t in n5]
    rd.thr('HO19', "'N 520' is one phrase (F)", "distinct 'N 520' lines that are '705/706 33 520'", sum(ph), len(ph), 0.8)
    hc = defaultdict(Counter)
    for b, e in FN:
        hc[b[-1]][e] += 1
    h5 = [h for h in hc if sum(hc[h].values()) >= 5]
    rd.thr('HO20', 'classes in F', 'heads with one ending in 90%+', sum(max(hc[h].values()) / sum(hc[h].values()) >= 0.9 for h in h5), len(h5), 0.8)
    rd.finish()


if __name__ == '__main__':
    main()
