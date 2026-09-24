"""Hundred-and-eleventh registered prediction set (PREDICTIONS.md, OG1-OG20): one sign, many genres. Writes
results/predict_test111.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test43 import sp_perm
from predict_test61 import units
from predict_test77 import jsd
from predict_test81 import classes_of
from predict_test103 import CL
from predict_test108 import genre
from signs import FISH

random.seed(131)


def relpos(lines, k=5):
    v = defaultdict(list)
    for t in lines:
        if len(t) >= 2:
            for i, g in enumerate(t):
                if g not in R.NUMS:
                    v[g].append(i / (len(t) - 1))
    return {g: sum(x) / len(x) for g, x in v.items() if len(x) >= k}


def company(lines, side):
    c = defaultdict(Counter)
    for t in lines:
        s = ['#'] + list(t) + ['#']
        for i in range(1, len(s) - 1):
            c[s[i]][s[i + 1] if side == 'R' else s[i - 1]] += 1
    return c


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-eleventh registered predictions: one sign, many genres', 'predict_test111')

    def by_genre(lines):
        d = defaultdict(list)
        for t in lines:
            d[genre(t)].append(t)
        return d
    DL = sorted({tuple(t) for t in AB})
    G = by_genre(DL)
    rd.say('- genres: %s.' % {k: len(v) for k, v in G.items()})
    rd.say()

    def corr(g1, g2, key, title, Gx, th=0.3):
        a, b = relpos(Gx[g1]), relpos(Gx[g2])
        s = sorted(set(a) & set(b))
        if len(s) < 5:
            rd.rec(key, title, 'signs %d; too few' % len(s), False)
            return
        o, p = sp_perm([a[g] for g in s], [b[g] for g in s])
        rd.rec(key, title, 'signs %d; Spearman %.3f; p = %.4f' % (len(s), o, p), o >= th and p < 0.05)
    corr('name', 'count', 'OG1', 'names and counts place signs alike', G)
    corr('name', 'closer', 'OG2', 'names and closers place signs alike', G)
    corr('name', 'bare', 'OG3', 'names and bare lines place signs alike', G)
    corr('count', 'bare', 'OG4', 'counts and bare lines place signs alike', G)
    nm = T.names(AB)
    pos = defaultdict(Counter)
    for b, e in nm:
        for i, g in enumerate(b):
            pos[g]['last' if i == len(b) - 1 else ('first' if i == 0 else 'mid')] += 1
    hd = {g for g, c in pos.items() if sum(c.values()) >= 5 and c['last'] / sum(c.values()) >= 0.5}
    op = {g for g, c in pos.items() if sum(c.values()) >= 5 and c['first'] / sum(c.values()) >= 0.5}
    bt = [(t, i) for t in G['bare'] for i in range(len(t))]
    rd.gtl('OG5', 'heads end bare lines', 'line-final, head tokens in bare lines', [i == len(t) - 1 for t, i in bt if t[i] in hd], [i == len(t) - 1 for t, i in bt if t[i] not in hd])
    ct = [(t, i) for t in G['count'] for i in range(len(t)) if t[i] not in R.NUMS]
    rd.gtl('OG6', 'openers open counts', 'line-first, opener tokens in counts', [i == 0 for t, i in ct if t[i] in op], [i == 0 for t, i in ct if t[i] not in op])

    def comp(Gx, side, key, title):
        cn, cc = company(Gx['name'], side), company(Gx['count'], side)
        sg = [g for g in cn if sum(cn[g].values()) >= 5 and sum(cc.get(g, Counter()).values()) >= 5]
        x = y = 0
        for g in sg:
            other = random.choice([h for h in sg if h != g])
            a, b = jsd(cn[g], cc[g]), jsd(cn[g], cc[other])
            x += a < b
            y += a > b
        p = R.binom_ge(x, x + y)
        rd.rec(key, title, 'signs %d; closer to itself %d, to another %d; p = %.4f' % (len(sg), x, y, p), x > y and p < 0.05)
    comp(G, 'R', 'OG7', 'a sign keeps its right company across genres')
    comp(G, 'L', 'OG8', 'a sign keeps its left company across genres')

    def og9(Gx, key, lab):
        pn = {p for t in Gx['name'] for p in zip(t, t[1:])}
        pc = Counter(p for t in Gx['count'] for p in zip(t, t[1:]))
        obs = sum(n for p, n in pc.items() if p in pn)
        ge = 0
        for _ in range(R.N // 10):
            sh = set()
            for t in Gx['name']:
                s = list(t)
                random.shuffle(s)
                sh.update(zip(s, s[1:]))
            ge += sum(n for p, n in pc.items() if p in sh) >= obs
        p = (ge + 1) / (R.N // 10 + 1)
        rd.rec(key, 'name pairs recur in counts%s' % lab, 'count pair tokens also name pairs %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    og9(G, 'OG9', '')
    U = units(sorted({b for b, e in nm if len(b) >= 2}))
    cpairs = [p for t in G['count'] for p in zip(t, t[1:])]
    nsig = sorted({g for b, e in nm for g in b})
    obs = sum(p in U for p in cpairs)
    ge = 0
    for _ in range(R.N):
        k = sum((random.choice(nsig), random.choice(nsig)) in U for _ in range(len(cpairs)))
        ge += k >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('OG10', 'units occur in counts', 'unit tokens in counts %d; p = %.4f' % (obs, p), p < 0.05)
    fw = sum(p in U for p in cpairs)
    bw = sum((b, a) in U and (a, b) not in U for a, b in cpairs)
    rd.thr('OG11', 'units keep their order in counts', 'unit occurrences in order', fw, fw + bw, 0.9)
    kinds = lambda lines: [(t[i], R.kind(t[i - 1])) for t in lines for i in range(1, len(t)) if t[i] not in R.NUMS and t[i - 1] in R.NUMS]
    kn, kc = defaultdict(Counter), defaultdict(Counter)
    for s, k in kinds(G['name']):
        kn[s][k] += 1
    for s, k in kinds(G['count']):
        kc[s][k] += 1
    both = [s for s in kn if s in kc]
    rd.thr('OG12', 'one notation across genres', 'signs with the same commonest kind', sum(kn[s].most_common(1)[0][0] == kc[s].most_common(1)[0][0] for s in both), len(both), 0.6)

    def vals(lines):
        v = defaultdict(list)
        for t in lines:
            for i in range(1, len(t)):
                if t[i] not in R.NUMS and t[i - 1] in R.NUMS:
                    j = i - 1
                    while j > 0 and t[j - 1] in R.NUMS:
                        j -= 1
                    v[t[i]].append(sum(R.NUMS[g][0] for g in t[j:i]))
        return {s: sum(x) / len(x) for s, x in v.items() if len(x) >= 3}
    vn, vc = vals(G['name']), vals(G['count'])
    s = sorted(set(vn) & set(vc))
    o, p = sp_perm([vn[g] for g in s], [vc[g] for g in s])
    rd.rec('OG13', 'a sign keeps its count across genres', 'signs %d; Spearman %.3f; p = %.4f' % (len(s), o, p), o >= 0.3 and p < 0.05)
    ft = [(t, i) for t in G['count'] for i in range(len(t)) if t[i] in FISH]
    rd.thr('OG14', 'fish are counted in counts too', 'fish tokens in counts after a numeral', sum(i > 0 and t[i - 1] in R.NUMS for t, i in ft), len(ft), 0.1)
    cl = classes_of(sorted({(b, e) for b, e in nm if b}))
    rd.gtl('OG15', 'the 520 class ends bare lines', 'ends a bare line, 520-class tokens', [i == len(t) - 1 for t, i in bt if cl.get(t[i]) == '520'],
           [i == len(t) - 1 for t, i in bt if cl.get(t[i]) == '740'])
    pc = [(t, i) for t in DL for i in range(1, len(t)) if cl.get(t[i - 1])]
    rd.gtl('OG16', 'closers follow the 740 class', 'closer next, 740-class tokens', [t[i] in CL for t, i in pc if cl[t[i - 1]] == '740'],
           [t[i] in CL for t, i in pc if cl[t[i - 1]] == '520'])
    GB = by_genre(sorted({tuple(t) for t in B}))
    corr('name', 'count', 'OG17', 'names and counts place signs alike (B)', GB)
    og9(GB, 'OG18', ' (B)')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    GF = by_genre(sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln}))
    corr('name', 'count', 'OG19', "names and counts place signs alike (F')", GF)
    comp(GF, 'R', 'OG20', "a sign keeps its right company across genres (F')")
    rd.finish()


if __name__ == '__main__':
    main()
