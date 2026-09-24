"""Forty-first registered prediction set (PREDICTIONS.md, DB1-DB10): repeated and doubled signs. Writes
results/predict_test41.md.

DB4 is implemented as a paired comparison within bodies that contain a double: removing one sign of the double gives an
attested body (same ending) more often than removing a random other sign of the same body (exact sign test)."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test16 import m_break
from signs import load

random.seed(61)


def dbl(t):
    return [i for i in range(len(t) - 1) if t[i] == t[i + 1] and t[i] not in R.NUMS]


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Forty-first registered predictions: repeated and doubled signs', 'predict_test41')
    out, ok = [], True
    for lab, L in (('A', A), ('B', B)):
        obs = sum(len(dbl(t)) for t in L)
        ge = 0
        for _ in range(R.N // 10):
            k = 0
            for t in L:
                s = list(t)
                random.shuffle(s)
                k += len(dbl(s))
            ge += k >= obs
        p = (ge + 1) / (R.N // 10 + 1)
        out.append('%s: doubles %d; p = %.4f (1,000 shuffles)' % (lab, obs, p))
        ok = ok and p < 0.05
    rd.rec('DB1', 'doubling is deliberate', out, ok)
    nm = T.names(AB)
    dsigns = {b[i] for b, _ in nm for i in dbl(b)}
    a = [i < len(b) - 2 for b, _ in nm for i in dbl(b)]
    c = [i < len(b) - 1 for b, _ in nm for i, g in enumerate(b) if g in dsigns and not (
        (i + 1 < len(b) and b[i + 1] == g) or (i > 0 and b[i - 1] == g))]
    rd.gtl('DB2', 'doubles are attributes', 'inside the name, doubled tokens', a, c)
    ed, es = defaultdict(Counter), defaultdict(Counter)
    for b, e in nm:
        if len(b) >= 2 and b[-1] == b[-2] and b[-1] not in R.NUMS:
            ed[b[-1]][e] += 1
        elif b[-1] not in R.NUMS:
            es[b[-1]][e] += 1
    sg = [g for g in ed if sum(ed[g].values()) >= 3 and sum(es[g].values()) >= 3]
    ag = sum(ed[g].most_common(1)[0][0] == es[g].most_common(1)[0][0] for g in sg)
    rd.rec('DB3', 'a double keeps the ending', 'signs %d (%s); same majority ending %d; threshold 80%%' % (
        len(sg), ', '.join(sg), ag), bool(sg) and ag / len(sg) >= 0.8)
    ns = set(nm)
    b10 = b01 = 0
    for b, e in ns:
        d = dbl(b)
        if not d:
            continue
        i = d[0]
        x = (b[:i] + b[i + 1:], e) in ns
        others = [j for j in range(len(b)) if j not in (i, i + 1)]
        if not others:
            continue
        j = random.choice(others)
        y = (b[:j] + b[j + 1:], e) in ns
        b10 += x and not y
        b01 += y and not x
    p = R.binom_ge(b10, b10 + b01)
    rd.rec('DB4', 'a double alternates with the single sign', 'discordant %d / %d; p = %.4f' % (b10, b01, p), b10 > b01 and p < 0.05)
    items = [(r['type'].startswith('TAB'), R.lstrat(len(ln)), 1 if dbl(ln) else 0) for r in F
             if r['type'].startswith(('TAB', 'SEAL')) for ln in r['seq'] if len(ln) >= 2]
    rd.strat('DB5', 'tablets double more', 'tablets minus seals', items)
    out, ok = [], True
    for lab, L in (('A', A), ('B', B)):
        bs = [b for b, _ in T.names(L) if len(b) >= 3]
        rep = lambda b: any(b[i] == b[j] and b[i] not in R.NUMS for i in range(len(b)) for j in range(i + 2, len(b)))
        obs = sum(map(rep, bs))
        le = 0
        for _ in range(R.N // 10):
            k = 0
            for b in bs:
                s = list(b)
                random.shuffle(s)
                k += rep(s)
            le += k <= obs
        p = (le + 1) / (R.N // 10 + 1)
        out.append('%s: bodies %d; non-adjacent repeats %d; p = %.4f (1,000 shuffles)' % (lab, len(bs), obs, p))
        ok = ok and p < 0.05
    rd.rec('DB6', 'names do not repeat a sign', out, ok)
    rd.rank('DB7', 'lines with a double are shorter', 'lines without against with a double',
            [len(t) for t in AB if R.name_of(t) and not dbl(t)], [len(t) for t in AB if R.name_of(t) and dbl(t)])
    m77 = [r['seq'] for r in load(only_m77=True) if len(r['seq']) >= 2 and not any('?' in ln for ln in r['seq'])]
    out, ok = [], True
    for lab, texts in (('as listed', m77), ('reversed', [t[::-1] for t in m77])):
        a_, na, c_, nc = m_break(texts, lambda t: {g for g in range(1, len(t)) if t[g - 1] == t[g] and t[g] not in R.NUMS})
        p = R.fisher_less(a_, na - a_, c_, nc - c_)
        out.append('lines %s: %s' % (lab, R.fl(a_, na, c_, nc, p)))
        ok = ok and p < 0.05 and a_ / max(1, na) < c_ / nc and na >= 20
    rd.rec('DB8', 'a double is not split', out, ok)
    items = [(r['site'].strip() == 'Harappa', R.lstrat(len(ln)), 1 if dbl(ln) else 0) for r in F
             if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for ln in r['seq'] if len(ln) >= 2]
    rd.strat('DB9', 'Harappa doubles more', 'Harappa minus Mohenjo-daro', items)
    dc = Counter(t[i] for t in AB for i in dbl(t))
    top = sum(n for _, n in dc.most_common(3))
    rd.thr('DB10', 'a few signs are doubled', 'the three commonest doubled signs (%s)' % ', '.join(
        '%s x%d' % kv for kv in dc.most_common(5)), top, sum(dc.values()), 0.6)
    rd.finish()


if __name__ == '__main__':
    main()
