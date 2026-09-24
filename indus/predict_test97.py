"""Ninety-seventh registered prediction set (PREDICTIONS.md, XC1-XC20): the name findings without copper tablets.
Writes results/predict_test97.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test61 import units
from predict_test69 import perm
from predict_test82 import suffix_lines
from signs import FISH

random.seed(117)
CITY = ('Mohenjo-daro', 'Harappa')
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F0 = R.load_all()
    F = [r for r in F0 if r['type'] != 'TAB:C']
    AB = A + B
    rd = R.Round('Ninety-seventh registered predictions: the name findings without copper tablets', 'predict_test97')
    tok = [(r['site'].strip(), b, e, r) for r in F for b, e in R.names_in(r) if b]
    rd.say('- objects without copper %d (of %d); name tokens %d.' % (len(F), len(F0), len(tok)))
    rd.say()
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
    rd.rec('XC1', 'names are local', 'bodies at both cities %d; p = %.4f (lower tail)' % (obs, p), p < 0.05)
    objs = defaultdict(set)
    for s, b, e, r in tok:
        objs[(b, e)].add(r['sealid'])
    one = lambda k: len(objs[k]) == 1
    rd.thr('XC2', 'most names are unique', 'distinct names on one object', sum(map(one, objs)), len(objs), 0.7)
    rd.rank('XC3', 'common names are short', 'one-object against 3+-object bodies', [len(k[0]) for k in objs if one(k)], [len(k[0]) for k in objs if len(objs[k]) >= 3])
    rd.rank('XC4', 'Harappa names are shorter', 'MD against H bodies', [len(b) for s, b, e, r in tok if s == 'Mohenjo-daro'], [len(b) for s, b, e, r in tok if s == 'Harappa'])
    rd.gtl('XC5', 'Harappa prefers 520', '520, Harappa names', [e == '520' for s, b, e, r in tok if s == 'Harappa'], [e == '520' for s, b, e, r in tok if s == 'Mohenjo-daro'])
    hn = lambda b: any(g in R.NUMS for g in b)
    rd.gtl('XC6', 'Mohenjo-daro names count', 'numeral in body, MD', [hn(b) for s, b, e, r in tok if s == 'Mohenjo-daro'], [hn(b) for s, b, e, r in tok if s == 'Harappa'])
    fish = lambda b: any(g in FISH for g in b)
    rd.gtl('XC7', '520 names are fish names', 'fish, 520 names', [fish(b) for s, b, e, r in tok if e == '520'], [fish(b) for s, b, e, r in tok if e == '740'])
    on_s = {(b, e) for s, b, e, r in tok if r['type'].startswith('SEAL')}
    off_s = {(b, e) for s, b, e, r in tok if not r['type'].startswith('SEAL')}
    rd.gtl('XC8', 'seal names are unique', 'one-off, seal names', [one(k) for k in on_s], [one(k) for k in off_s])
    hnm = defaultdict(set)
    for k in objs:
        hnm[k[0][-1]].add(k)
    oo2 = [k for k in objs if one(k) and len(k[0]) >= 2]
    rd.thr('XC9', 'unique names end in common heads', 'one-off names whose head heads 5+ names', sum(len(hnm[k[0][-1]]) >= 5 for k in oo2), len(oo2), 0.7)
    ftc = Counter(g for r in F for ln in r['seq'] for g in ln)
    oo3 = [k[0] for k in objs if one(k) and len(k[0]) >= 3]
    rd.gtl('XC10', 'the rare part comes first', 'rare, first signs', [ftc[b[0]] <= 5 for b in oo3], [ftc[b[-1]] <= 5 for b in oo3])
    sn = lambda site: {(b, e) for s, b, e, r in tok if s == site}
    rd.gtl('XC11', 'Harappa repeats its names', 'repeated, Harappa', [not one(k) for k in sn('Harappa')], [not one(k) for k in sn('Mohenjo-daro')])
    U = units(sorted({b for b, e in T.names(AB) if len(b) >= 2}))
    oc = {}
    for s, b, e, r in tok:
        if s in CITY and one((b, e)) and len(b) >= 2:
            oc[(b, e)] = s
    ok_ = list(oc)
    us = [{p_ for p_ in zip(k[0], k[0][1:]) if p_ in U} for k in ok_]

    def share(labs):
        c = defaultdict(Counter)
        for u_, l_ in zip(us, labs):
            for x in u_:
                c[x][l_] += 1
        return sum(n * (n - 1) // 2 for v in c.values() for n in v.values())
    labs = [oc[k] for k in ok_]
    obs = share(labs)
    p = perm(obs, share, labs, n=R.N // 10)
    rd.rec('XC12', 'each city has its units', 'same-city unit-sharing pairs %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    fdn = {(s, b, e) for s, b, e, r in tok}
    hs, os_, oh, oo = defaultdict(set), defaultdict(set), defaultdict(set), defaultdict(set)
    for s, b, e in fdn:
        if s in CITY and len(b) >= 2:
            hs[b[-1]].add(s)
            os_[b[0]].add(s)
            if one((b, e)):
                oh[b[-1]].add(s)
                oo[b[0]].add(s)
    rd.gtl('XC13', 'heads are shared, openers local', 'at both cities, head types', [len(v) == 2 for v in hs.values()], [len(v) == 2 for v in os_.values()])
    rd.gtl('XC14', 'one-off names share heads, not openers', 'at both cities, one-off head types', [len(v) == 2 for v in oh.values()], [len(v) == 2 for v in oo.values()])
    N = {c: sorted({(b, e) for s, b, e in fdn if s == c}) for c in CITY}
    a = [len(b) for b, e in N['Mohenjo-daro']]
    c = [len(b) for b, e in N['Harappa']]
    o1, p1 = R.rank_perm(a, c)
    o2, p2 = R.rank_perm(c, a)
    rd.rec('XC15', 'Mohenjo-daro names are longer', 'means MD %.2f, H %.2f; two-sided p = %.4f' % (sum(a) / len(a), sum(c) / len(c), min(1, 2 * min(p1, p2))),
           2 * p1 < 0.05 and sum(a) / len(a) > sum(c) / len(c))
    L = {s: sorted({tuple(ln) for r in F if r['site'].strip() == s for ln in r['seq'] if ln}) for s in CITY}
    isn = lambda t: bool(R.name_of(list(t)) and R.name_of(list(t))[0])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    rd.gtl('XC16', 'Mohenjo-daro heads its names', 'heading unit, MD name lines', [hu(t) for t in L['Mohenjo-daro'] if isn(t)], [hu(t) for t in L['Harappa'] if isn(t)])
    sx = lambda s: [f != '#' for b, e, f in suffix_lines(L[s])]
    rd.gtl('XC17', 'Harappa suffixes its names', 'suffixed, Harappa name lines', sx('Harappa'), sx('Mohenjo-daro'))
    sd = {(r['type'].startswith('SEAL'), b, e) for s, b, e, r in tok}
    rd.gtl('XC18', '520 is a seal class', '520, seal names', [e == '520' for x, b, e in sd if x], [e == '520' for x, b, e in sd if not x])
    for key, c in (('XC19', 'Mohenjo-daro'), ('XC20', 'Harappa')):
        hc = defaultdict(Counter)
        for b, e in N[c]:
            hc[b[-1]][e] += 1
        h5 = [h for h in hc if sum(hc[h].values()) >= 5]
        rd.thr(key, 'fixed classes at %s' % c, 'heads with one ending in 90%+', sum(max(hc[h].values()) / sum(hc[h].values()) >= 0.9 for h in h5), len(h5), 0.8)
    rd.finish()


if __name__ == '__main__':
    main()
