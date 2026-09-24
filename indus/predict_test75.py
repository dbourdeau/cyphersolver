"""Seventy-fifth registered prediction set (PREDICTIONS.md, QS1-QS20): how the name is put together. Writes
results/predict_test75.md. Counts over distinct names."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from signs import FISH

random.seed(95)
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventy-fifth registered predictions: how the name is put together', 'predict_test75')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    ns = sorted({(b, e) for b, e in T.names(AB) if b})

    def constituents(names, k1, k2):
        b3 = [b for b, e in names if len(b) == 3]
        o1, p1 = R.mi_perm([b[1] for b in b3], [b[2] for b in b3])
        o2, p2 = R.mi_perm([b[1] for b in b3], [b[0] for b in b3])
        rd.rec(k1, 'the middle leans on the head', '3-sign bodies %d; MI middle-head %.3f (p = %.4f), middle-opener %.3f (p = %.4f)' % (
            len(b3), o1, p1, o2, p2), o1 > o2 and p1 < 0.05)
        two = {b for b, e in names if len(b) == 2}
        x = y = 0
        for b, e in names:
            if len(b) == 4:
                a_, c_ = b[2:] in two, b[:2] in two
                x += a_ and not c_
                y += c_ and not a_
        p = R.binom_ge(x, x + y)
        rd.rec(k2, 'the last two form a name', '4-sign bodies: last two only %d, first two only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
        return b3, two
    b3, two = constituents(ns, 'QS1', 'QS3')
    x = sum(b[1:] in two and b[:2] not in two for b in b3)
    y = sum(b[:2] in two and b[1:] not in two for b in b3)
    p = R.binom_ge(x, x + y)
    rd.rec('QS2', 'middle + head is a name', '(middle, head) only %d, (opener, middle) only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    rd.thr('QS4', 'the middle qualifies', 'middles that are numerals or fish', sum(b[1] in R.NUMS or b[1] in FISH for b in b3), len(b3), 0.4)
    x = y = 0
    for b, e in ns:
        if len(b) >= 3:
            a_, c_ = b[-2] in R.NUMS, b[0] in R.NUMS
            x += a_ and not c_
            y += c_ and not a_
    p = R.binom_ge(x, x + y)
    rd.rec('QS5', 'the number stands before the head', 'before the head only %d, first only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    constituents(sorted({(b, e) for b, e in T.names(B) if b}), 'QS6', 'QS7')
    fdn = {(r['site'].strip(), r['type'][:3], full(r).split(':')[0].strip(), b, e) for r in F for b, e in R.names_in(r) if b}
    md = [(m, b) for s, ty, m, b, e in fdn if s == 'Mohenjo-daro' and ty == 'SEA' and m and len(b) >= 2]
    rd.mi('QS8', 'the picture goes with the head at Mohenjo-daro', 'distinct seal names', [m for m, _ in md], [b[-1] for _, b in md])
    rd.mi('QS9', 'the picture goes with the opener at Mohenjo-daro', 'distinct seal names', [m for m, _ in md], [b[0] for _, b in md])
    hr = [(ty, b[-1]) for s, ty, m, b, e in fdn if s == 'Harappa' and ty in ('SEA', 'TAB')]
    rd.mi('QS10', 'Harappa seals and tablets name different heads', 'distinct Harappa names', [t for t, _ in hr], [h for _, h in hr])
    ch = {b[-1] for s, ty, m, b, e in fdn if s in CITY}
    co = {b[0] for s, ty, m, b, e in fdn if s in CITY and len(b) >= 2}
    oh = {b[-1] for s, ty, m, b, e in fdn if s not in CITY and len(b) >= 2}
    oo = {b[0] for s, ty, m, b, e in fdn if s not in CITY and len(b) >= 2}
    rd.ltl('QS11', 'small-site openers are their own', 'also in the cities, small-site openers', [o in co for o in oo], [h in ch for h in oh])
    lvn = defaultdict(set)
    for r in F:
        if r['site'].strip() == 'Harappa':
            l_ = R.level('Harappa', recs[r['sealid']])
            if l_ in ('E', 'L'):
                for b, e in R.names_in(r):
                    if len(b) >= 2:
                        lvn[('h', b[-1])].add(l_)
                        lvn[('o', b[0])].add(l_)
    rd.gtl('QS12', 'heads last, openers change', 'in both periods, head types', [len(v) == 2 for k, v in lvn.items() if k[0] == 'h'],
           [len(v) == 2 for k, v in lvn.items() if k[0] == 'o'])
    cn = sorted({(s, b) for s, ty, m, b, e in fdn if s in CITY and len(b) >= 2})
    bl = [b for _, b in cn]

    def samepairs(sites, key):
        g, g2 = defaultdict(Counter), defaultdict(Counter)
        for s, b in zip(sites, bl):
            g[key(b)][s] += 1
            g2[(b[0], b[-1])][s] += 1
        a = sum(n * (n - 1) // 2 for c in g.values() for n in c.values())
        d = sum(n * (n - 1) // 2 for c in g2.values() for n in c.values())
        return a - d
    ss = [s for s, _ in cn]
    for k, title, key, want in (('QS13', 'a shared opener means one place', lambda b: b[0], True),
                                ('QS14', 'a shared head does not', lambda b: b[-1], False)):
        obs = samepairs(ss, key)
        sh = ss[:]
        ge = 0
        for _ in range(R.N):
            random.shuffle(sh)
            ge += samepairs(sh, key) >= obs
        p = (ge + 1) / (R.N + 1)
        rd.rec(k, title, 'same-site pairs %d; p = %.4f' % (obs, p), (p < 0.05) if want else (p >= 0.05))
    DL = {tuple(t) for t in AB}
    counted = {y_ for t in DL if nonname(list(t)) for x_, y_ in zip(t, t[1:]) if x_ in R.NUMS}
    hn = Counter(b[-1] for b, e in ns)
    rd.rank('QS15', 'counted heads are common', 'counted against uncounted heads', [hn[h] for h in hn if h in counted], [hn[h] for h in hn if h not in counted])
    top = [h for h, _ in hn.most_common(10)]
    ones = {b[0] for b, e in ns if len(b) == 1}
    rd.thr('QS16', 'common heads stand alone', 'top-10 heads also 1-sign names (%s)' % ', '.join(top), sum(h in ones for h in top), 10, 0.5)
    lastc = defaultdict(Counter)
    for b, e in ns:
        if len(b) >= 2:
            for i, g in enumerate(b):
                lastc[g][i == len(b) - 1] += 1
    oq = [g for g in ones if sum(lastc[g].values()) >= 3]
    rd.thr('QS17', 'single-sign names are heads', '1-sign names standing last in most longer names', sum(lastc[g][True] > lastc[g][False] for g in oq), len(oq), 0.8)
    rec_ = lambda t: any(x_ in R.END and y_ == '400' for x_, y_ in zip(t, t[1:]))
    nl = [t for t in DL if R.name_of(list(t)) and R.name_of(list(t))[0]]
    rd.gtl('QS18', 'receipts name the common roles', 'top-10 head, receipt names', [R.name_of(list(t))[0][-1] in top for t in nl if rec_(t)],
           [R.name_of(list(t))[0][-1] in top for t in nl if not rec_(t)])
    bset = {b for b, e in ns if len(b) >= 2}
    mx = max(len(b) for b in bset)
    emb = []
    for t in DL:
        if nonname(list(t)):
            for k_ in range(min(mx, len(t)), 1, -1):
                hit = [tuple(t[i:i + k_]) for i in range(len(t) - k_ + 1) if tuple(t[i:i + k_]) in bset]
                if hit:
                    emb.append(hit[-1])
                    break
    rd.gtl('QS19', 'formulas cite the common roles', 'top-10 head, cited names', [b[-1] in top for b in emb], [b[-1] in top for b, e in ns if len(b) >= 2])
    fp = Counter(i for b in b3 for i, g in enumerate(b) if g in FISH)
    rd.rec('QS20', 'fish sit in the middle', 'fish in 3-sign bodies by position: first %d, middle %d, last %d' % (fp[0], fp[1], fp[2]),
           fp[1] > fp[0] and fp[1] > fp[2])
    rd.finish()


if __name__ == '__main__':
    main()
