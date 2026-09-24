"""Eighty-fifth registered prediction set (PREDICTIONS.md, CS1-CS20): one grammar, two cities? Writes
results/predict_test85.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test41 import dbl
from predict_test42 import dom, pairs
from predict_test44 import nonname
from predict_test78 import parse
from predict_test82 import jperm, suffix_lines
from signs import FISH

random.seed(105)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Eighty-fifth registered predictions: one grammar, two cities?', 'predict_test85')
    L = {s: sorted({tuple(ln) for r in F if r['site'].strip() == s for ln in r['seq'] if ln}) for s in ('Mohenjo-daro', 'Harappa')}
    N = {s: sorted({(b, e) for r in F if r['site'].strip() == s for b, e in R.names_in(r) if b}) for s in L}
    MD, H = 'Mohenjo-daro', 'Harappa'
    rd.say('- distinct lines MD %d, H %d; distinct names MD %d, H %d.' % (len(L[MD]), len(L[H]), len(N[MD]), len(N[H])))
    rd.say()

    def two(key, title, lab, a, c):
        p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
        rd.rec(key, title, '%s, Harappa %s' % (lab, R.fl(sum(a), len(a), sum(c), len(c), p)), p < 0.05)

    def cls(ns):
        hc = defaultdict(Counter)
        for b, e in ns:
            hc[b[-1]][e] += 1
        return {h: c.most_common(1)[0][0] for h, c in hc.items() if sum(c.values()) >= 3}
    cm, ch = cls(N[MD]), cls(N[H])
    bh = [h for h in cm if h in ch]
    rd.thr('CS1', 'the classes are shared', 'heads with the same class', sum(cm[h] == ch[h] for h in bh), len(bh), 0.9)
    for key, s in (('CS2', MD), ('CS3', H)):
        two_ = {b for b, e in N[s] if len(b) == 2}
        x = sum(b[2:] in two_ and b[:2] not in two_ for b, e in N[s] if len(b) == 4)
        y = sum(b[:2] in two_ and b[2:] not in two_ for b, e in N[s] if len(b) == 4)
        p = R.binom_ge(x, x + y)
        rd.rec(key, 'right-branching at %s' % s, 'last two only %d, first two only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    nt = lambda s: [g for t in L[s] for g in t if g in R.NUMS]
    for key, s in (('CS4', MD), ('CS5', H)):
        rd.gtl(key, 'tiered for large numbers at %s' % s, 'tiered, values 5-8', [R.kind(g) == 'tiered' for g in nt(s) if 5 <= R.NUMS[g][0] <= 8],
               [R.kind(g) == 'tiered' for g in nt(s) if 1 <= R.NUMS[g][0] <= 4])
    for key, s in (('CS6', MD), ('CS7', H)):
        pr = [(R.kind(x), y) for t in L[s] for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS]
        rd.mi(key, 'the sign sets the kind at %s' % s, 'numeral + sign pairs', [k for k, _ in pr], [y for _, y in pr])
    for key, s in (('CS8', MD), ('CS9', H)):
        f = lambda b: any(g in FISH for g in b)
        rd.gtl(key, 'fish go with 520 at %s' % s, 'fish, 520 names', [f(b) for b, e in N[s] if e == '520'], [f(b) for b, e in N[s] if e == '740'])
    rows = [(b[-1], f) for b, e, f in suffix_lines(L[MD]) if e == '740' and f in ('90', '400')]
    o, p = jperm(rows, '90', '400')
    rd.rec('CS10', '90 and 400 take different heads at Mohenjo-daro', 'lines %d; Jaccard %.3f; p = %.4f' % (len(rows), o, p), p < 0.05)
    dm = dom(pairs(set(N[MD]), 3))
    dh = dom(pairs(set(N[H]), 3))
    bp = [p_ for p_ in dm if p_ in dh]
    rd.thr('CS11', 'the order is shared', 'pairs with the same order', sum(dm[p_] == dh[p_] for p_ in bp), len(bp), 0.85)
    two('CS12', 'the 520 share differs', '520 names', [e == '520' for b, e in N[H]], [e == '520' for b, e in N[MD]])
    lb = lambda s: [len(b) for b, e in N[s]]
    a, c = lb(MD), lb(H)
    o1, p1 = R.rank_perm(a, c)
    o2, p2 = R.rank_perm(c, a)
    rd.rec('CS13', 'name length differs', 'means MD %.2f, H %.2f; two-sided p = %.4f' % (sum(a) / len(a), sum(c) / len(c), min(1, 2 * min(p1, p2))), min(p1, p2) * 2 < 0.05)
    isn = lambda t: bool(R.name_of(list(t)) and R.name_of(list(t))[0])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    two('CS14', 'headings differ', 'heading unit, name lines', [hu(t) for t in L[H] if isn(t)], [hu(t) for t in L[MD] if isn(t)])
    sx = lambda s: [f != '#' for b, e, f in suffix_lines(L[s])]
    two('CS15', 'suffixing differs', 'suffixed name lines', sx(H), sx(MD))
    two('CS16', 'the formula share differs', 'formulas', [nonname(list(t)) for t in L[H]], [nonname(list(t)) for t in L[MD]])
    two('CS17', 'the tiered share differs', 'tiered numerals', [R.kind(g) == 'tiered' for g in nt(H)], [R.kind(g) == 'tiered' for g in nt(MD)])
    two('CS18', 'doubling differs', 'lines with a double', [bool(dbl(list(t))) for t in L[H]], [bool(dbl(list(t))) for t in L[MD]])
    si = [(s, v[1]) for s in (MD, H) for t in L[s] if nonname(list(t)) and parse(t) for v in parse(t)[1]]
    rd.mi('CS19', 'each city counts its own things', 'counted items', [s for s, _ in si], [i for _, i in si])
    t5 = lambda s: {h for h, _ in Counter(b[-1] for b, e in N[s]).most_common(5)}
    rd.rec('CS20', 'each city has its common heads', 'top five MD %s, H %s; shared %d; threshold at most 3' % (
        ', '.join(sorted(t5(MD))), ', '.join(sorted(t5(H))), len(t5(MD) & t5(H))), len(t5(MD) & t5(H)) <= 3)
    rd.finish()


if __name__ == '__main__':
    main()
