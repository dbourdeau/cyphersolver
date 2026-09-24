"""Hundred-and-thirteenth registered prediction set (PREDICTIONS.md, RO1-RO20): sets 111-112 on held-out data. Writes
results/predict_test113.md."""
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
from predict_test111 import company, relpos
from predict_test112 import runs

random.seed(133)
HEAD = ('817', '820', '861')
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-thirteenth registered predictions: sets 111-112 on held-out data', 'predict_test113')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FL = sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln})
    OL = sorted({tuple(ln) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if ln})
    BL = sorted({tuple(t) for t in B})
    bg = lambda lines: {g: [t for t in lines if genre(t) == g] for g in ('name', 'count', 'closer', 'bare')}
    GF, GO, GB = bg(FL), bg(OL), bg(BL)
    rd.say("- F' %s; OS %s; B %s." % ({k: len(v) for k, v in GF.items()}, {k: len(v) for k, v in GO.items()}, {k: len(v) for k, v in GB.items()}))
    rd.say()

    def corr(G, g1, g2, key, title, k=5):
        a, b = relpos(G[g1], k), relpos(G[g2], k)
        s = sorted(set(a) & set(b))
        if len(s) < 5:
            rd.rec(key, title, 'signs %d; too few' % len(s), False)
            return
        o, p = sp_perm([a[x] for x in s], [b[x] for x in s])
        rd.rec(key, title, 'signs %d; Spearman %.3f; p = %.4f' % (len(s), o, p), o >= 0.3 and p < 0.05)

    def comp(G, key, title, k=5):
        cn, cc = company(G['name'], 'R'), company(G['count'], 'R')
        sg = [g for g in cn if sum(cn[g].values()) >= k and sum(cc.get(g, Counter()).values()) >= k]
        x = y = 0
        for g in sg:
            other = random.choice([h for h in sg if h != g]) if len(sg) > 1 else g
            a, b = jsd(cn[g], cc[g]), jsd(cn[g], cc[other])
            x += a < b
            y += a > b
        p = R.binom_ge(x, x + y)
        rd.rec(key, title, 'signs %d; closer to itself %d, to another %d; p = %.4f' % (len(sg), x, y, p), x > y and p < 0.05)
    corr(GO, 'name', 'count', 'RO1', 'names and counts place signs alike (OS)', 3)
    comp(GO, 'RO2', 'a sign keeps its company (OS)', 3)
    corr(GF, 'name', 'closer', 'RO3', "names and closers place signs alike (F')")
    corr(GF, 'count', 'bare', 'RO4', "counts and bare lines place signs alike (F')")
    nm = [R.name_of(list(t)) for t in GF['name']]
    pos = defaultdict(Counter)
    for b, e in nm:
        for i, g in enumerate(b):
            pos[g]['last' if i == len(b) - 1 else 'x'] += 1
    hd = {g for g, c in pos.items() if sum(c.values()) >= 5 and c['last'] / sum(c.values()) >= 0.5}
    bt = [(t, i) for t in GF['bare'] for i in range(len(t))]
    rd.gtl('RO5', "heads end bare lines (F')", 'line-final, head tokens', [i == len(t) - 1 for t, i in bt if t[i] in hd], [i == len(t) - 1 for t, i in bt if t[i] not in hd])
    pn = {p for t in GF['name'] for p in zip(t, t[1:])}
    pc = Counter(p for t in GF['count'] for p in zip(t, t[1:]))
    obs = sum(n for p, n in pc.items() if p in pn)
    ge = 0
    for _ in range(R.N // 10):
        sh = set()
        for t in GF['name']:
            s = list(t)
            random.shuffle(s)
            sh.update(zip(s, s[1:]))
        ge += sum(n for p, n in pc.items() if p in sh) >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('RO6', "name pairs recur in counts (F')", 'count pair tokens also name pairs %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    U = units(sorted({b for b, e in T.names(AB) if len(b) >= 2}))
    cp = [p for t in GF['count'] for p in zip(t, t[1:])]
    nsig = sorted({g for b, e in nm for g in b})
    obs = sum(p in U for p in cp)
    ge = sum(sum((random.choice(nsig), random.choice(nsig)) in U for _ in cp) >= obs for _ in range(R.N))
    p = (ge + 1) / (R.N + 1)
    rd.rec('RO7', "units occur in counts (F')", 'unit tokens %d; p = %.4f' % (obs, p), p < 0.05)
    kd = lambda lines: [(t[i], R.kind(t[i - 1])) for t in lines for i in range(1, len(t)) if t[i] not in R.NUMS and t[i - 1] in R.NUMS]
    kn, kc = defaultdict(Counter), defaultdict(Counter)
    for s, k in kd(GF['name']):
        kn[s][k] += 1
    for s, k in kd(GF['count']):
        kc[s][k] += 1
    both = [s for s in kn if s in kc]
    rd.thr('RO8', "one notation across genres (F')", 'same commonest kind', sum(kn[s].most_common(1)[0][0] == kc[s].most_common(1)[0][0] for s in both), len(both), 0.6)

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

    def og13(G, key, lab):
        vn, vc = vals(G['name']), vals(G['count'])
        s = sorted(set(vn) & set(vc))
        o, p = sp_perm([vn[g] for g in s], [vc[g] for g in s])
        rd.rec(key, 'a sign keeps its count%s' % lab, 'signs %d; Spearman %.3f; p = %.4f' % (len(s), o, p), o >= 0.3 and p < 0.05)
    og13(GF, 'RO9', " (F')")
    cl = classes_of(sorted({(b, e) for b, e in nm}))
    pcl = [(t, i) for t in FL for i in range(1, len(t)) if cl.get(t[i - 1])]
    rd.gtl('RO10', "closers follow the 740 class (F')", 'closer next, 740 class', [t[i] in CL for t, i in pcl if cl[t[i - 1]] == '740'],
           [t[i] in CL for t, i in pcl if cl[t[i - 1]] == '520'])
    comp(GB, 'RO11', 'a sign keeps its company (B)')
    og13(GB, 'RO12', ' (B)')

    def tier(lines, key, lab):
        nt = [g for t in lines for g in t if g in R.NUMS]
        rd.gtl(key, 'tiered for large numbers%s' % lab, 'tiered, 5-8', [R.kind(g) == 'tiered' for g in nt if 5 <= R.NUMS[g][0] <= 8],
               [R.kind(g) == 'tiered' for g in nt if 1 <= R.NUMS[g][0] <= 4])
    tier(GF['name'], 'RO13', " in names (F')")
    tier(GF['count'], 'RO14', " in counts (F')")
    ng = defaultdict(set)
    nc = Counter()
    for t in FL:
        for g in t:
            if g in R.NUMS:
                nc[g] += 1
                if genre(t) in ('name', 'count', 'closer', 'bare'):
                    ng[g].add(genre(t))
    n10 = [g for g in nc if nc[g] >= 10]
    rd.thr('RO15', "one number set (F')", 'numeral signs in 2+ genres', sum(len(ng[g]) >= 2 for g in n10), len(n10), 1.0)
    gk = [(genre(t), R.kind(g)) for t in FL for g in t if g in R.NUMS and genre(t) in ('name', 'count', 'closer', 'bare')]
    o, p = R.mi_perm([a for a, _ in gk], [b for _, b in gk])
    rd.rec('RO16', "the notation is the same in every genre (F')", 'MI %.4f; p = %.4f' % (o, p), p >= 0.05)

    def order(lines, key, lab):
        r2 = [r for t in lines for i, j, r in runs(t) if len(r) == 2 and R.NUMS[r[0]][0] != R.NUMS[r[1]][0] and not (i > 0 and t[i - 1] in HEAD)]
        rd.thr(key, 'the larger part comes first%s' % lab, '2-sign runs (no heading before) with the larger value first', sum(R.NUMS[r[0]][0] > R.NUMS[r[1]][0] for r in r2), len(r2), 0.7)
    order(sorted({tuple(t) for t in AB}), 'RO17', '')
    order(FL, 'RO18', " (F')")
    nb = Counter(g for t in BL for g in t if g in R.NUMS)
    rd.rec('RO19', "'2' is the commonest numeral (B)", 'commonest: %s' % nb.most_common(3), nb.most_common(1)[0][0] == '2')
    vc = Counter(sum(R.NUMS[g][0] for g in r) for t in FL for i, j, r in runs(t))
    rd.rec('RO20', "twelve stands out (F')", 'runs worth 10: %d, 11: %d, 12: %d' % (vc[10], vc[11], vc[12]), vc[12] > vc[10] + vc[11])
    rd.finish()


if __name__ == '__main__':
    main()
