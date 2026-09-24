"""Seventy-seventh registered prediction set (PREDICTIONS.md, LX1-LX20): numbers that are part of names, and two
systems. Writes results/predict_test77.md. Counts over distinct names and lines."""
import math
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test72 import cval
from predict_test76 import fcounted
from signs import FISH

random.seed(97)


def jsd(a, b):
    ta, tb = sum(a.values()), sum(b.values())
    out = 0.0
    for k in set(a) | set(b):
        p, q = a[k] / ta, b[k] / tb
        m = (p + q) / 2
        if p:
            out += p / 2 * math.log2(p / m)
        if q:
            out += q / 2 * math.log2(q / m)
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventy-seventh registered predictions: numbers that are part of names, and two systems', 'predict_test77')
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    DL = sorted({tuple(t) for t in AB})
    NL = [t for t in DL if R.name_of(list(t))]
    FL = [t for t in DL if nonname(list(t))]
    cn = [(cval(b)[0], b[-1], b, e) for b, e in ns if cval(b)]

    def lx1(cnames, key, lab):
        hv = defaultdict(Counter)
        for v, h, b, e in cnames:
            hv[h][v] += 1
        sh = [c.most_common(1)[0][1] / sum(c.values()) for c in hv.values() if sum(c.values()) >= 3]
        m = sum(sh) / max(1, len(sh))
        rd.rec(key, 'each head has its number%s' % lab, 'heads %d; mean commonest-value share %.2f; threshold 0.70' % (len(sh), m), bool(sh) and m >= 0.7)
        return hv
    hv = lx1(cn, 'LX1', '')
    fv = defaultdict(Counter)
    for v, k, s in fcounted(FL):
        fv[s][v] += 1
    x = y = 0
    for s in hv:
        if sum(hv[s].values()) >= 3 and sum(fv[s].values()) >= 3:
            a = hv[s].most_common(1)[0][1] / sum(hv[s].values())
            c = fv[s].most_common(1)[0][1] / sum(fv[s].values())
            x += a > c
            y += c > a
    p = R.binom_ge(x, x + y)
    rd.rec('LX2', 'names fix the number, formulas vary it', 'signs more fixed in names %d, in formulas %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    vals = [v for v, h, b, e in cn]
    hb = [(h, b) for v, h, b, e in cn]

    def rec_(vs):
        g = defaultdict(set)
        for v, (h, b) in zip(vs, hb):
            g[(v, h)].add(b)
        return sum(len(s) >= 2 for s in g.values())
    obs = rec_(vals)
    vv = vals[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(vv)
        ge += rec_(vv) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('LX3', 'number + head is a unit', '(value, head) pairs in 2+ bodies %d; p = %.4f' % (obs, p), p < 0.05)
    vc = Counter(vals)
    rd.thr('LX4', 'names use few numbers', 'two commonest values (%s)' % dict(vc.most_common(4)), sum(n for _, n in vc.most_common(2)), len(vals), 0.7)
    fvals = [v for v, k, s in fcounted(FL)]
    lab = [0] * len(vals) + [1] * len(fvals)
    rd.mi('LX5', 'names and formulas count differently', 'numeral runs', lab, [min(v, 8) for v in vals + fvals])
    nmh = [b for v, h, b, e in cn if len(b) >= 3 and b[-3] in R.NUMS]
    nmh = [b for b, e in ns if len(b) >= 3 and b[-3] in R.NUMS and b[-2] not in R.NUMS and b[-1] not in R.NUMS]
    val3 = lambda b: R.NUMS[b[-3]][0]
    o1, p1 = R.mi_perm([val3(b) for b in nmh], [b[-1] for b in nmh])
    o2, p2 = R.mi_perm([val3(b) for b in nmh], [b[-2] for b in nmh])
    rd.rec('LX6', 'the number belongs to the head', "'N mod head' %d; MI value-head %.3f (p = %.4f), value-mod %.3f (p = %.4f)" % (len(nmh), o1, p1, o2, p2),
           o1 > o2 and p1 < 0.05)
    two = {b for b, e in ns if len(b) == 2}
    pairs = {(v, h) for v, h, b, e in cn}
    alone = {(R.NUMS[b[0]][0], b[1]) for b in two if b[0] in R.NUMS}
    rd.thr('LX7', 'number + head stands alone', '(value, head) pairs also 2-sign bodies', len(pairs & alone), len(pairs), 0.3)
    nruns = [v for v in vals]
    rd.gtl('LX8', 'names count two and three', 'value 2-3, name runs', [v in (2, 3) for v in nruns], [v in (2, 3) for v in fvals])
    ntok = Counter(g for t in NL for g in t)
    ftok = Counter(g for t in FL for g in t)
    n3 = [g for g in ntok if ntok[g] >= 3 and g not in R.NUMS]
    rd.thr('LX9', 'names have their own signs', 'name sign types never in formulas', sum(ftok[g] == 0 for g in n3), len(n3), 0.2)
    lines = NL + FL
    labs = [0] * len(NL) + [1] * len(FL)

    def shared(lb, f):
        a, c = set(), set()
        for t, l_ in zip(lines, lb):
            (a if l_ == 0 else c).update(f(t))
        return len(a & c)
    for key, title, f in (('LX10', 'names and formulas share few pairs', lambda t: set(zip(t, t[1:]))),
                          ('LX11', 'names and formulas share few counts', lambda t: {(x_, y_) for x_, y_ in zip(t, t[1:]) if x_ in R.NUMS and y_ not in R.NUMS})):
        obs = shared(labs, f)
        lb = labs[:]
        le = 0
        for _ in range(R.N // 10):
            random.shuffle(lb)
            le += shared(lb, f) <= obs
        p = (le + 1) / (R.N // 10 + 1)
        rd.rec(key, title, 'shared types %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)

    def mjsd(lb):
        L = [defaultdict(Counter), defaultdict(Counter)]
        for t, l_ in zip(lines, lb):
            s = ['#'] + list(t)
            for i in range(1, len(s)):
                L[l_][s[i]][s[i - 1]] += 1
        gs = [g for g in L[0] if sum(L[0][g].values()) >= 10 and sum(L[1][g].values()) >= 10]
        return sum(jsd(L[0][g], L[1][g]) for g in gs) / max(1, len(gs)), len(gs)
    obs, ng = mjsd(labs)
    lb = labs[:]
    ge = 0
    for _ in range(R.N // 10):
        random.shuffle(lb)
        ge += mjsd(lb)[0] >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('LX12', 'the same sign keeps different company', 'signs %d; mean JSD %.3f; p = %.4f (1,000 shuffles)' % (ng, obs, p), p < 0.05)
    fin = lambda L: [i + 1 == len(t) - 1 for t in L for i in range(len(t) - 1) if t[i] in R.NUMS and t[i + 1] not in R.NUMS]
    rd.gtl('LX13', 'the counted item closes the formula', 'line-final, formula counted signs', fin(FL), fin(NL))
    nmh2 = nmh
    rd.thr('LX14', "in 'N mod head' the rest is a name", '(mod, head) attested 2-sign bodies', sum(b[-2:] in two for b in nmh2), len(nmh2), 0.3)
    mnh = [b for b, e in ns if len(b) >= 3 and b[-3] not in R.NUMS and b[-2] in R.NUMS and b[-1] not in R.NUMS]
    rd.thr('LX15', "in 'mod N head' the rest is a name", '(N, head) attested 2-sign bodies', sum(b[-2:] in two for b in mnh), len(mnh), 0.3)
    rd.gtl('LX16', 'the fish goes inside the number', "fish modifier, 'N mod head'", [b[-2] in FISH for b in nmh2], [b[-3] in FISH for b in mnh])
    e_of = {b: e for b, e in ns}
    nm5 = [(b, e) for b, e in ns if b in set(nmh2)]
    mn5 = [(b, e) for b, e in ns if b in set(mnh)]
    rd.gtl('LX17', "'N mod head' takes 520", "520, 'N mod head'", [e == '520' for b, e in nm5], [e == '520' for b, e in mn5])
    shape = lambda b: 'nmh' if (len(b) >= 3 and b[-3] in R.NUMS and b[-2] not in R.NUMS) else ('mnh' if (len(b) >= 3 and b[-3] not in R.NUMS and b[-2] in R.NUMS) else None)
    fs = {(r['site'].strip(), b) for r in F if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for b, e in R.names_in(r) if b and shape(b)}
    fs = [(site, shape(b)) for site, b in sorted(fs)]
    a = [s_ == 'nmh' for site, s_ in fs if site == 'Harappa']
    c = [s_ == 'nmh' for site, s_ in fs if site == 'Mohenjo-daro']
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('LX18', 'the cities order the number differently', "'N mod head' share, Harappa %s" % R.fl(sum(a), len(a), sum(c), len(c), p), p < 0.05)
    nsB = sorted({(b, e) for b, e in T.names(B) if b})
    lx1([(cval(b)[0], b[-1], b, e) for b, e in nsB if cval(b)], 'LX19', ' (B)')
    DB = sorted({tuple(t) for t in B})
    NB = [t for t in DB if R.name_of(list(t))]
    FB = [t for t in DB if nonname(list(t))]
    lines, labs = NB + FB, [0] * len(NB) + [1] * len(FB)
    obs = shared(labs, lambda t: set(zip(t, t[1:])))
    lb = labs[:]
    le = 0
    for _ in range(R.N // 10):
        random.shuffle(lb)
        le += shared(lb, lambda t: set(zip(t, t[1:]))) <= obs
    p = (le + 1) / (R.N // 10 + 1)
    rd.rec('LX20', 'names and formulas share few pairs (B)', 'shared types %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
