"""Seventy-fourth registered prediction set (PREDICTIONS.md, HR1-HR20): heads as roles, openers as persons. Writes
results/predict_test74.md. All counts are over distinct names."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test72 import cmi
from signs import FISH

random.seed(94)
CITY = ('Mohenjo-daro', 'Harappa')
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Seventy-fourth registered predictions: heads as roles, openers as persons', 'predict_test74')
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    n2 = [(b, e) for b, e in ns if len(b) >= 2]
    fd = {(r['site'].strip(), r['type'][:3], b, e, r['sealid']) for r in F for b, e in R.names_in(r) if b}
    fdn = {(s, ty, b, e) for s, ty, b, e, _ in fd}
    rd.say('- distinct names %d (2+ signs %d); F distinct (site, type, name) %d.' % (len(ns), len(n2), len(fdn)))
    rd.say()
    hs, os_ = defaultdict(set), defaultdict(set)
    for s, ty, b, e in fdn:
        if s in CITY and len(b) >= 2:
            hs[b[-1]].add(s)
            os_[b[0]].add(s)
    rd.gtl('HR1', 'heads are shared, openers local', 'at both cities, head types', [len(v) == 2 for v in hs.values()], [len(v) == 2 for v in os_.values()])
    hp, op = defaultdict(list), defaultdict(list)
    for b, e in n2:
        hp[b[-1]].append(b[0])
        op[b[0]].append(b[-1])
    ratio = lambda d: [len(set(v)) / len(v) for v in d.values() if len(v) >= 5]
    rd.rank('HR2', 'a head takes many persons', 'heads against openers, distinct partners per name', ratio(hp), ratio(op))
    top = lambda d: sum(len(v) for _, v in sorted(d.items(), key=lambda kv: -len(kv[1]))[:10])
    th, to = top(hp), top(op)
    p = R.hyper_ge(th, len(n2) - th, to, len(n2) - to)
    rd.rec('HR3', 'few heads, many openers', 'top-10 coverage heads %d, openers %d of %d; p = %.4f' % (th, to, len(n2), p), th > to and p < 0.05)
    nB = {(b, e) for b, e in T.names(B) if len(b) >= 2}
    hB, oB = defaultdict(list), defaultdict(list)
    for b, e in nB:
        hB[b[-1]].append(b)
        oB[b[0]].append(b)
    th, to = top(hB), top(oB)
    p = R.hyper_ge(th, len(nB) - th, to, len(nB) - to)
    rd.rec('HR4', 'few heads in B too', 'top-10 coverage heads %d, openers %d of %d; p = %.4f' % (th, to, len(nB), p), th > to and p < 0.05)
    sh = {b[-1] for s, ty, b, e in fdn if ty == 'SEA'}
    so = {b[0] for s, ty, b, e in fdn if ty == 'SEA' and len(b) >= 2}
    th_ = {b[-1] for s, ty, b, e in fdn if ty == 'TAB'}
    to_ = {b[0] for s, ty, b, e in fdn if ty == 'TAB' and len(b) >= 2}
    a = [h in sh for h in th_]
    c = [o in so for o in to_]
    p = R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))
    rd.rec('HR5', 'tablets name the same roles', 'tablet heads on seals %s' % R.fl(sum(a), len(a), sum(c), len(c), p),
           sum(a) / max(1, len(a)) >= 0.8 and p < 0.05)
    objn = defaultdict(set)
    for s, ty, b, e, sid in fd:
        objn[(b, e)].add(sid)
    oh, oo = defaultdict(set), defaultdict(set)
    for s, ty, b, e in fdn:
        if s in CITY and len(b) >= 2 and len(objn[(b, e)]) == 1:
            oh[b[-1]].add(s)
            oo[b[0]].add(s)
    rd.gtl('HR6', 'one-off names share heads, not openers', 'at both cities, one-off head types', [len(v) == 2 for v in oh.values()], [len(v) == 2 for v in oo.values()])
    ocount = Counter(b[0] for b, e in n2)
    cnt = Counter(T.names(AB))
    one = [b for b, e in n2 if cnt[(b, e)] == 1]
    rd.thr('HR7', 'personal openers', 'one-off name openers found in one name only', sum(ocount[b[0]] == 1 for b in one), len(one), 0.2)
    b2 = [b for b, e in ns if len(b) == 2]
    o_, p = R.mi_perm([b[0] for b in b2], [b[1] for b in b2])
    rd.rec('HR8', 'opener and head combine freely', '2-sign bodies %d; MI %.3f; p = %.4f' % (len(b2), o_, p), p >= 0.05)
    b3 = [b for b, e in ns if len(b) >= 3]
    o_, p = R.mi_perm([b[0] for b in b3], [b[-1] for b in b3])
    rd.rec('HR9', 'first and last combine freely', 'bodies of 3+ %d; MI %.3f; p = %.4f' % (len(b3), o_, p), p >= 0.05)
    hh = [b[-1] for b, e in n2]
    pp = [b[0] for b, e in n2]
    ee = [e for b, e in n2]
    obs = cmi(hh, pp, ee)
    grp = defaultdict(list)
    for i, h in enumerate(hh):
        grp[h].append(i)
    ge = 0
    for _ in range(R.N):
        q = pp[:]
        for ii in grp.values():
            v = [pp[i] for i in ii]
            random.shuffle(v)
            for i, x in zip(ii, v):
                q[i] = x
        ge += cmi(hh, q, ee) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('HR10', 'the opener does not touch the ending', 'conditional MI %.3f bits; p = %.4f' % (obs, p), p >= 0.05)
    bods2 = [b for b, e in ns if len(b) == 2]
    h2, o2 = {b[1] for b in bods2}, {b[0] for b in bods2}
    x = y = 0
    for b, e in ns:
        if len(b) >= 4:
            a_, c_ = b[-1] in h2, b[0] in o2
            x += a_ and not c_
            y += c_ and not a_
    p = R.binom_ge(x, x + y)
    rd.rec('HR11', 'long names keep the head', 'head shared only %d, opener shared only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    role = defaultdict(Counter)
    for b, e in n2:
        role[b[-1]]['h'] += 1
        role[b[0]]['o'] += 1
    ht = {g for g, c in role.items() if sum(c.values()) >= 3 and c['h'] / sum(c.values()) >= 0.7}
    ot = {g for g, c in role.items() if sum(c.values()) >= 3 and c['o'] / sum(c.values()) >= 0.7}
    counted = {y_ for t in {tuple(t) for t in AB} if nonname(list(t)) for x_, y_ in zip(t, t[1:]) if x_ in R.NUMS}
    rd.gtl('HR12', 'heads are counted things', 'counted in formulas, head types', [g in counted for g in ht], [g in counted for g in ot])
    tc = [(g, 'h') for g in ht if g in cat] + [(g, 'o') for g in ot if g in cat]
    rd.mi('HR13', 'the role goes with the category', 'typed signs', [cat[g] for g, _ in tc], [r_ for _, r_ in tc])
    he = [(cat[b[-1]], e) for b, e in ns if b[-1] in cat]
    rd.mi('HR14', 'the ending goes with the head category', 'names with a categorised head', [c_ for c_, _ in he], [e for _, e in he])
    d5 = [b for b, e in ns if e == '520']
    rd.thr('HR15', '520 names are fish-headed', 'distinct 520 names with a fish head', sum(b[-1] in FISH for b in d5), len(d5), 0.4)
    hc = defaultdict(Counter)
    for b, e in ns:
        hc[b[-1]][e] += 1
    nf = [h for h in hc if h not in FISH and sum(hc[h].values()) >= 5]
    rd.thr('HR16', '520 is rare outside fish', 'non-fish heads with a 520 majority', sum(hc[h]['520'] > hc[h]['740'] for h in nf), len(nf), 0.1, above=False)
    rd.gtl('HR17', 'fish open names', 'fish, opener tokens', [b[0] in FISH for b, e in n2], [b[-1] in FISH for b, e in n2])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    hn = {(R.name_of(t), hu(t)) for t in AB if R.name_of(t) and R.name_of(t)[0]}
    rd.mi('HR18', 'titled names have their own heads', 'distinct (name, headed)', [h for _, h in hn], [nm[0][-1] for nm, _ in hn])
    rd.rank('HR19', '740 names are longer', '740 against 520', [len(b) for b, e in ns if e == '740'], [len(b) for b, e in ns if e == '520'])
    th10 = [h for h, _ in sorted(hp.items(), key=lambda kv: -len(kv[1]))[:10]]
    fh = defaultdict(set)
    for s, ty, b, e in fdn:
        if s in CITY:
            fh[b[-1]].add(s)
    rd.thr('HR20', 'the common heads are everywhere', 'top-10 heads at both cities (%s)' % ', '.join(th10), sum(len(fh[h]) == 2 for h in th10), 10, 1.0)
    rd.finish()


if __name__ == '__main__':
    main()
