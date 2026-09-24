"""Seventieth registered prediction set (PREDICTIONS.md, PN1-PN20): twenty hypotheses on the local name stocks.
Writes results/predict_test70.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test50 import ent
from predict_test53 import lab_perm
from predict_test61 import units
from predict_test67 import same_pairs
from predict_test69 import perm
from signs import FISH

random.seed(90)
CITY = ('Mohenjo-daro', 'Harappa')
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventieth registered predictions: twenty hypotheses on the local name stocks', 'predict_test70')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    tok = [(r['site'].strip(), b, e, r) for r in F for b, e in R.names_in(r)]
    objs = defaultdict(set)
    for s, b, e, r in tok:
        objs[(b, e)].add(r['sealid'])
    oneoff = lambda k: len(objs[k]) == 1
    # PN1
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    ht = [((b, e), lv(r)) for s, b, e, r in tok if s == 'Harappa' and lv(r) in ('E', 'L')]
    dc = Counter(k for k, _ in ht)
    ht = [(k, l_) for k, l_ in ht if dc[k] >= 2]
    keys = [k for k, _ in ht]

    def onep(ls):
        g = defaultdict(set)
        for k, l_ in zip(keys, ls):
            g[k].add(l_)
        return sum(len(v) == 1 for v in g.values())
    ls = [l_ for _, l_ in ht]
    obs = onep(ls)
    p = perm(obs, onep, ls)
    rd.rec('PN1', 'a name keeps to its period', 'names on 2+ dated objects %d; one period %d; p = %.4f' % (len(set(keys)), obs, p), p < 0.05)
    # PN2
    op = defaultdict(set)
    cl = defaultdict(set)
    for s, b, e, r in tok:
        if s in CITY and len(b) >= 2:
            op[b[:2]].add(s)
            cl[b[-2:]].add(s)
    rd.gtl('PN2', 'openers travel, closers stay', 'opening pairs at both cities', [len(v) == 2 for v in op.values()], [len(v) == 2 for v in cl.values()])
    # PN3
    seals = [r for r in F if r['type'].startswith('SEAL') and full(r)]
    key3 = [(r['site'].strip(), tuple(tuple(ln) for ln in r['seq'] if ln)) for r in seals]
    mo = [full(r) for r in seals]
    obs = same_pairs(key3, mo)
    bysite = defaultdict(list)
    for i, (s, _) in enumerate(key3):
        bysite[s].append(i)
    ge = 0
    for _ in range(R.N):
        mm = mo[:]
        for ii in bysite.values():
            v = [mo[i] for i in ii]
            random.shuffle(v)
            for i, x in zip(ii, v):
                mm[i] = x
        ge += same_pairs(key3, mm) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('PN3', 'within a site the same text has the same picture', 'same-text same-site pairs sharing a motif %d; p = %.4f' % (obs, p), p < 0.05)
    # PN4
    top = sorted(objs, key=lambda k: -len(objs[k]))[:10]
    tt = [s for s, b, e, r in tok if (b, e) in set(top)]
    rd.thr('PN4', 'the common names are Harappan', 'tokens of the ten commonest names at Harappa (%s)' % ', '.join(
        '%s %s x%d' % (' '.join(k[0]), k[1], len(objs[k])) for k in top[:5]), sum(s == 'Harappa' for s in tt), len(tt), 0.6)
    # PN5
    U = units(sorted({b for b, _ in T.names(AB) if len(b) >= 2}))
    oo = {}
    for s, b, e, r in tok:
        if s in CITY and oneoff((b, e)) and len(b) >= 2:
            oo[(b, e)] = s
    ok_ = list(oo)
    us = [{p_ for p_ in zip(k[0], k[0][1:]) if p_ in U} for k in ok_]

    def share(labs):
        c = defaultdict(Counter)
        for u_, l_ in zip(us, labs):
            for x in u_:
                c[x][l_] += 1
        return sum(n * (n - 1) // 2 for v in c.values() for n in v.values())
    labs = [oo[k] for k in ok_]
    obs = share(labs)
    p = perm(obs, share, labs, n=R.N // 10)
    rd.rec('PN5', 'each city has its units', 'one-off city names %d; same-city unit-sharing pairs %d; p = %.4f (1,000 shuffles)' % (len(ok_), obs, p), p < 0.05)
    # PN6-PN11
    num = lambda b: any(g in R.NUMS for g in b)
    fish = lambda b: any(g in FISH for g in b)
    rd.rank('PN6', 'counted names are longer', 'with against without a numeral', [len(b) for s, b, e, r in tok if num(b)], [len(b) for s, b, e, r in tok if not num(b)])
    rd.rank('PN7', 'fish names are longer', 'with against without a fish', [len(b) for s, b, e, r in tok if fish(b)], [len(b) for s, b, e, r in tok if not fish(b)])
    nf = lambda b: any(x in R.NUMS and y in FISH for x, y in zip(b, b[1:]))
    rd.gtl('PN8', 'counted fish are Mohenjo-daran', 'numeral + fish, Mohenjo-daro', [nf(b) for s, b, e, r in tok if s == 'Mohenjo-daro'],
           [nf(b) for s, b, e, r in tok if s == 'Harappa'])
    rd.rank('PN9', 'Harappa 520 names are short', '740 against 520 at Harappa', [len(b) for s, b, e, r in tok if s == 'Harappa' and e == '740'],
            [len(b) for s, b, e, r in tok if s == 'Harappa' and e == '520'])
    dbl = lambda b: any(x == y and x not in R.NUMS for x, y in zip(b, b[1:]))
    rd.gtl('PN10', 'Mohenjo-daro doubles', 'double in body, Mohenjo-daro', [dbl(b) for s, b, e, r in tok if s == 'Mohenjo-daro'],
           [dbl(b) for s, b, e, r in tok if s == 'Harappa'])
    rd.gtl('PN11', '520 names have fish', 'fish, 520 names', [fish(b) for s, b, e, r in tok if e == '520'], [fish(b) for s, b, e, r in tok if e == '740'])
    # PN12-PN16
    seal = lambda r: r['type'].startswith('SEAL')
    rd.rank('PN12', 'names off seals are short', 'seal against off-seal names', [len(b) for s, b, e, r in tok if seal(r)], [len(b) for s, b, e, r in tok if not seal(r)])
    on_s = {(b, e) for s, b, e, r in tok if seal(r)}
    off_s = {(b, e) for s, b, e, r in tok if not seal(r)}
    rd.gtl('PN13', 'seal names are unique', 'one-off, names on seals', [oneoff(k) for k in on_s], [oneoff(k) for k in off_s])
    tabn = {(b, e) for s, b, e, r in tok if r['type'].startswith('TAB')}
    potn = {(b, e) for s, b, e, r in tok if r['type'].startswith('POT')}
    rd.gtl('PN14', 'tablets name seal owners', 'also on a seal, tablet names', [k in on_s for k in tabn], [k in potn and k in on_s for k in potn])
    rd.rank('PN15', 'Harappa tablet names are short', 'seal against tablet names at Harappa', [len(b) for s, b, e, r in tok if s == 'Harappa' and seal(r)],
            [len(b) for s, b, e, r in tok if s == 'Harappa' and r['type'].startswith('TAB')])
    nc = Counter(R.name_of(t) for t in AB if R.name_of(t))
    hd = lambda t: t[0] in HEAD
    rd.gtl('PN16', 'titled names are unique', 'one-off, headed names', [nc[R.name_of(t)] == 1 for t in AB if R.name_of(t) and hd(t)],
           [nc[R.name_of(t)] == 1 for t in AB if R.name_of(t) and not hd(t)])
    # PN17-PN20
    hn = defaultdict(set)
    for (b, e) in objs:
        if b:
            hn[b[-1]].add((b, e))
    oo2 = [k for k in objs if oneoff(k) and len(k[0]) >= 2]
    rd.thr('PN17', 'unique names end in common heads', 'one-off names whose head heads 5+ names', sum(len(hn[k[0][-1]]) >= 5 for k in oo2), len(oo2), 0.7)
    ftc = Counter(g for r in F for ln in r['seq'] for g in ln)
    oo3 = [k[0] for k in objs if oneoff(k) and len(k[0]) >= 3]
    rd.gtl('PN18', 'the rare part comes first', 'rare, first signs of one-off names', [ftc[b[0]] <= 5 for b in oo3], [ftc[b[-1]] <= 5 for b in oo3])
    hh = [b[-1] for s, b, e, r in tok if s == 'Harappa' and b]
    hm = [b[-1] for s, b, e, r in tok if s == 'Mohenjo-daro' and b]
    o, p = lab_perm(hm, hh, lambda a, b: ent(a) - ent(b), R.N)
    rd.rec('PN19', 'Harappa has fewer heads', 'head entropy Mohenjo-daro %.2f, Harappa %.2f; p = %.4f' % (ent(hm), ent(hh), p), o > 0 and p < 0.05)
    sn = lambda site: {(b, e) for s, b, e, r in tok if s == site}
    rd.gtl('PN20', 'Harappa repeats its names', 'repeated, Harappa names', [not oneoff(k) for k in sn('Harappa')], [not oneoff(k) for k in sn('Mohenjo-daro')])
    rd.finish()


if __name__ == '__main__':
    main()
