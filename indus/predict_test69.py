"""Sixty-ninth registered prediction set (PREDICTIONS.md, AM1-AM20): twenty hypotheses on names as names. Writes
results/predict_test69.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test61 import units
from signs import FISH

random.seed(89)
CITY = ('Mohenjo-daro', 'Harappa')


def perm(obs, stat, labels, lower=False, n=R.N):
    lab = labels[:]
    c = 0
    for _ in range(n):
        random.shuffle(lab)
        k = stat(lab)
        c += (k <= obs) if lower else (k >= obs)
    return (c + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Sixty-ninth registered predictions: twenty hypotheses on names as names', 'predict_test69')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    tok = [(r['site'].strip(), b, e, r) for r in F for b, e in R.names_in(r)]
    rd.say('- F name tokens %d; A + B names %d.' % (len(tok), len(T.names(AB))))
    rd.say()
    # AM1
    ct = [(s, b) for s, b, e, r in tok if s in CITY and len(b) >= 2]
    bl = [b for _, b in ct]

    def both(ss):
        g = defaultdict(set)
        for s, b in zip(ss, bl):
            g[b].add(s)
        return sum(len(v) == 2 for v in g.values())
    ss = [s for s, _ in ct]
    obs = both(ss)
    p = perm(obs, both, ss, lower=True)
    rd.rec('AM1', 'names are local', 'bodies at both cities %d; p = %.4f (lower tail)' % (obs, p), p < 0.05)
    # AM2
    seals = [r for r in F if r['type'].startswith('SEAL')]
    txt = lambda r: tuple(tuple(ln) for ln in r['seq'] if ln)
    tc = Counter(txt(r) for r in seals)
    gs = [r for r in seals if tc[txt(r)] >= 2]
    gt = [txt(r) for r in gs]

    def one(ss_):
        g = defaultdict(set)
        for s, t in zip(ss_, gt):
            g[t].add(s)
        return sum(len(v) == 1 for v in g.values())
    s2 = [r['site'].strip() for r in gs]
    obs = one(s2)
    p = perm(obs, one, s2)
    rd.rec('AM2', 'a seal text belongs to a place', 'repeated seal texts %d; at one site %d; p = %.4f' % (len(set(gt)), obs, p), p < 0.05)
    # AM3
    allb = {b for _, b, _, _ in tok}
    sites3 = [s for s, _, _, _ in tok]
    bods = [b for _, b, _, _ in tok]
    longs = [(i, next((b[k:] for k in range(1, len(b) - 1) if b[k:] in allb), None)) for i, b in enumerate(bods) if len(b) >= 4]
    longs = [(i, x) for i, x in longs if x]

    def fam(ss_):
        g = defaultdict(set)
        for s, b in zip(ss_, bods):
            g[b].add(s)
        return sum(ss_[i] in g[x] for i, x in longs)
    obs = fam(sites3)
    p = perm(obs, fam, sites3, n=R.N // 10)
    rd.rec('AM3', 'a name and its tail live together', 'long bodies ending in a body %d; same site %d; p = %.4f (1,000 shuffles)' % (
        len(longs), obs, p), p < 0.05)
    # AM4
    bset = {b for b, _ in T.names(AB) if len(b) >= 2}
    mx = max(len(b) for b in bset)

    def emb(t):
        for k in range(min(mx, len(t)), 1, -1):
            for i in range(len(t) - k, -1, -1):
                if tuple(t[i:i + k]) in bset:
                    return tuple(t[i:i + k])
    fe = [(r['site'].strip(), emb(ln)) for r in F for ln in r['seq'] if nonname(ln) and emb(ln)]
    bs_sites = defaultdict(set)
    for s, b, _, _ in tok:
        bs_sites[b].add(s)
    fe = [(s, b) for s, b in fe if b in bs_sites]
    fl = [b for _, b in fe]
    st4 = lambda ss_: sum(s in bs_sites[b] for s, b in zip(ss_, fl))
    s4 = [s for s, _ in fe]
    obs = st4(s4)
    p = perm(obs, st4, s4)
    rd.rec('AM4', 'formulas cite local names', 'embedded bodies attested as F names %d; at the same site %d; p = %.4f' % (len(fe), obs, p), p < 0.05)
    # AM5
    rd.rank('AM5', 'Harappa names are shorter', 'Mohenjo-daro against Harappa bodies', [len(b) for s, b, _, _ in tok if s == 'Mohenjo-daro'],
            [len(b) for s, b, _, _ in tok if s == 'Harappa'])
    # AM6
    ch = {b[-1] for s, b, _, _ in tok if s in CITY and b}
    oh = {b[-1] for s, b, _, _ in tok if s not in CITY and b}
    rd.thr('AM6', 'one stock of heads', 'other-site heads also city heads', len(oh & ch), len(oh), 0.8)
    # AM7
    be = defaultdict(set)
    for s, b, e, _ in tok:
        be[b].add(e)
    dual = {b for b, v in be.items() if len(v) == 2}
    dt = [(s, b, e) for s, b, e, _ in tok if b in dual]
    dl = [(b, e) for _, b, e in dt]

    def co(ss_):
        g = defaultdict(set)
        for s, (b, e) in zip(ss_, dl):
            g[(b, s)].add(e)
        return len({b for (b, s), v in g.items() if len(v) == 2})
    s7 = [s for s, _, _ in dt]
    obs = co(s7)
    p = perm(obs, co, s7)
    rd.rec('AM7', 'the endings alternate in one place', 'bodies with both endings %d; both at one site %d; p = %.4f' % (len(dual), obs, p), p < 0.05)
    # AM8
    off = lambda r: not r['type'].startswith('SEAL')
    rd.gtl('AM8', '520 names are off the seals', 'off seals, 520 names', [off(r) for s, b, e, r in tok if e == '520'],
           [off(r) for s, b, e, r in tok if e == '740'])
    # AM9
    hi5 = hi7 = 0
    for b in dual:
        o5 = [off(r) for s, bb, e, r in tok if bb == b and e == '520']
        o7 = [off(r) for s, bb, e, r in tok if bb == b and e == '740']
        d = sum(o5) / len(o5) - sum(o7) / len(o7)
        hi5 += d > 0
        hi7 += d < 0
    p = R.binom_ge(hi5, hi5 + hi7)
    rd.rec('AM9', 'the 520 form is the off-seal form', 'bodies where 520 is more off-seal %d, 740 %d; p = %.4f' % (hi5, hi7, p), hi5 > hi7 and p < 0.05)
    # AM10
    rd.gtl('AM10', 'Harappa prefers 520', '520, Harappa names', [e == '520' for s, b, e, r in tok if s == 'Harappa'],
           [e == '520' for s, b, e, r in tok if s == 'Mohenjo-daro'])
    # AM11-12
    nm = T.names(AB)
    fv = []
    for b, _ in nm:
        for i in range(1, len(b)):
            if b[i] in FISH and b[i - 1] in R.NUMS:
                j = i - 1
                while j > 0 and b[j - 1] in R.NUMS:
                    j -= 1
                fv.append((sum(R.NUMS[g][0] for g in b[j:i]), b[i]))
    rd.thr('AM11', 'few fish are counted', 'values 1-3 before a fish (%s)' % dict(sorted(Counter(v for v, _ in fv).items())),
           sum(1 <= v <= 3 for v, _ in fv), len(fv), 0.8)
    rd.mi('AM12', 'each fish has its count', 'counted fish', [f for _, f in fv], [v for v, _ in fv])
    # AM13
    hn = lambda b: any(g in R.NUMS for g in b)
    rd.gtl('AM13', 'Mohenjo-daro names count', 'numeral in body, Mohenjo-daro', [hn(b) for s, b, e, r in tok if s == 'Mohenjo-daro'],
           [hn(b) for s, b, e, r in tok if s == 'Harappa'])
    # AM14-16
    objc = defaultdict(set)
    for s, b, e, r in tok:
        objc[(b, e)].add(r['sealid'])
    rd.thr('AM14', 'most names are unique', 'distinct names on one object', sum(len(v) == 1 for v in objc.values()), len(objc), 0.7)
    rd.rank('AM15', 'common names are short', 'one-object against 3+-object bodies', [len(k[0]) for k, v in objc.items() if len(v) == 1],
            [len(k[0]) for k, v in objc.items() if len(v) >= 3])
    U = units(sorted({b for b, _ in nm if len(b) >= 2}))
    oo = [k[0] for k, v in objc.items() if len(v) == 1 and len(k[0]) >= 3]
    rd.thr('AM16', 'unique names are built of stock units', 'one-off bodies of 3+ with a unit', sum(any(p_ in U for p_ in zip(b, b[1:])) for b in oo), len(oo), 0.7)
    # AM17
    b3 = [b for b, _ in set(nm) if len(b) >= 3]
    firstc = Counter(b[0] for b in b3)
    top = [g for g, _ in firstc.most_common(20)]
    pf, pm = defaultdict(set), defaultdict(set)
    for b in b3:
        pf[b[0]].add(b[-1])
        for g in b[1:-1]:
            pm[g].add(b[-1])
    tk = Counter(g for b, _ in nm for g in b)
    S = [g for g in tk if tk[g] >= 5]
    q = T.quintiles(tk, S)
    byq = defaultdict(list)
    for s in S:
        byq[q[s]].append(s)
    obs = sum(len(pf[g]) for g in top)
    ge = 0
    for _ in range(R.N):
        ge += sum(len(pm[random.choice(byq[q[g]])]) for g in top if g in q) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('AM17', 'openers are productive', 'distinct heads after the 20 commonest openers %d; p = %.4f' % (obs, p), p < 0.05)
    # AM18
    sm = [(full(r).split(':')[0].strip() == 'Bull1', all(R.name_of(ln) for ln in r['seq'] if ln)) for r in seals if full(r) and r['seq']]
    rd.gtl('AM18', 'unicorn seals carry pure names', 'whole-name text, unicorn seals', [w for u, w in sm if u], [w for u, w in sm if not u])
    # AM19
    b2 = [(b, e) for b, e in nm if len(b) >= 2]
    o1, p1 = R.mi_perm([b[-1] for b, _ in b2], [e for _, e in b2])
    o2, p2 = R.mi_perm([b[0] for b, _ in b2], [e for _, e in b2])
    rd.rec('AM19', 'the head sets the ending', 'MI head %.3f (p = %.4f), first sign %.3f (p = %.4f)' % (o1, p1, o2, p2), o1 > o2 and p1 < 0.05)
    # AM20
    rd.rank('AM20', 'small-site names are short', 'city against other-site bodies', [len(b) for s, b, e, r in tok if s in CITY],
            [len(b) for s, b, e, r in tok if s not in CITY])
    rd.finish()


if __name__ == '__main__':
    main()
