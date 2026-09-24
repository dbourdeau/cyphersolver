"""Sixty-sixth registered prediction set (PREDICTIONS.md, RX1-RX10): replicating loop 3 on held-out data. Writes
results/predict_test66.md."""
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from predict_test62 import sims
from signs import FISH

random.seed(86)
HEAD = ('817', '820', '861')


def units(bodies, k):
    c = Counter()
    for b in bodies:
        c.update(set(zip(b, b[1:])))
    return {p for p, n in c.items() if n >= k}


def coverage(bodies, k):
    u = units(bodies, k)
    cov = tot = 0
    for b in bodies:
        tot += len(b)
        m = [False] * len(b)
        for i in range(len(b) - 1):
            if (b[i], b[i + 1]) in u:
                m[i] = m[i + 1] = True
        cov += sum(m)
    return cov / max(1, tot)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Sixty-sixth registered predictions: replicating loop 3 on held-out data', 'predict_test66')
    nmB = T.names(B)
    bs = [b for b, _ in nmB if len(b) >= 2]
    ff = lambda b: sum(x in FISH and y in FISH and x != y for x, y in zip(b, b[1:]))
    obs = sum(map(ff, bs))
    ge = 0
    for _ in range(R.N // 10):
        k = 0
        for b in bs:
            s = list(b)
            random.shuffle(s)
            k += ff(s)
        ge += k >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('RX1', 'fish cluster (FS1)', 'B: adjacent different-fish pairs %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    pre = lambda b, i: i > 0 and b[i - 1] in R.NUMS
    rd.gtl('RX2', 'fish are counted (FS5)', 'B: after a numeral, fish body tokens', [pre(b, i) for b, _ in nmB for i, g in enumerate(b) if g in FISH],
           [pre(b, i) for b, _ in nmB for i, g in enumerate(b) if g not in FISH])
    pv = [(b[i - 1], g) for b, _ in nmB for i, g in enumerate(b) if g in FISH and i > 0]
    rd.mi('RX3', 'the neighbour picks the fish (FS6)', 'B fish tokens with a preceding sign', [a for a, _ in pv], [g for _, g in pv])
    bodies = sorted({b for b, _ in nmB if len(b) >= 2})
    obs = coverage(bodies, 3)
    ge = 0
    for _ in range(R.N // 10):
        sh = []
        for b in bodies:
            s = list(b)
            random.shuffle(s)
            sh.append(tuple(s))
        ge += coverage(sh, 3) >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('RX4', 'names are built of units (SG1)', 'B: coverage %.3f; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    U = units(bodies, 3)
    rd.thr('RX5', 'units stand alone (SG10)', 'B units attested as whole 2-sign bodies', sum(u in set(bodies) for u in U), len(U), 0.3)
    tc, S, C = sims(B, 10)
    q = T.quintiles(tc, S)
    byq = defaultdict(list)
    for s in S:
        byq[q[s]].append(s)
    mean = lambda xs: sum(C[p_] for p_ in combinations(xs, 2)) / max(1, len(xs) * (len(xs) - 1) // 2)
    m = [g for g in S if g in FISH]
    obs = mean(m)
    ge = 0
    for _ in range(R.N):
        pick = set()
        for g in m:
            x = random.choice(byq[q[g]])
            while x in pick:
                x = random.choice(byq[q[g]])
            pick.add(x)
        ge += mean(sorted(pick)) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('RX6', 'fish keep company (DC1)', 'B: fish signs %d; mean cosine %.3f; p = %.4f' % (len(m), obs, p), p < 0.05)
    hd = lambda t: len(t) >= 2 and t[0] in HEAD
    nl = [t for t in B if R.name_of(t)]
    hb = {R.name_of(t)[0] for t in nl if hd(t)}
    ub = {R.name_of(t)[0] for t in nl if not hd(t)}
    rd.thr('RX7', 'the heading is optional (HD7)', 'B headed bodies also unheaded', len(hb & ub), len(hb), 0.3)
    oth = [r for r in F if r['site'].strip() not in ('Mohenjo-daro', 'Harappa')]
    items = [(r['type'].startswith('SEAL'), R.lstrat(len(ln)), 1 if hd(ln) else 0) for r in oth for ln in r['seq'] if len(ln) >= 2]
    rd.strat('RX8', 'seals are headed (HD5)', 'other sites, seals minus others', items)
    mot = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    ti = [r for r in F if r['type'] == 'TAB:I' and mot(r)]
    texts = [tuple(tuple(ln) for ln in r['seq'] if ln) for r in ti]
    mots = [mot(r) for r in ti]

    def same(ms):
        g = defaultdict(Counter)
        for t, m_ in zip(texts, ms):
            g[t][m_] += 1
        return sum(n * (n - 1) // 2 for c in g.values() for n in c.values())
    obs = same(mots)
    mm = mots[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(mm)
        ge += same(mm) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('RX9', 'same text, same picture (MT7)', 'TAB:I with a motif %d; same-text pairs sharing a motif %d; p = %.4f' % (len(ti), obs, p), p < 0.05)
    nct = lambda ln: len(ln) >= 2 and ln[-1] == '700' and all(g in R.NUMS for g in ln[:-1])
    rct = lambda ln: len(ln) >= 2 and ln[0] == '700' and all(g in R.NUMS for g in ln[1:])
    ca = [(r['type'], rct(ln)) for r in rowsA for ln in r['seq'] if nct(ln) or rct(ln)]
    rd.gtl('RX10', 'moulds reverse (DR1)', 'A: reversed, TAB:B count tokens', [x for ty, x in ca if ty == 'TAB:B'], [x for ty, x in ca if ty == 'TAB:I'])
    rd.finish()


if __name__ == '__main__':
    main()
