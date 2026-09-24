"""Hundredth registered prediction set (PREDICTIONS.md, AL1-AL20): variant forms of one sign. Writes
results/predict_test100.md."""
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from predict_test50 import ent
from predict_test62 import sims

random.seed(120)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Hundredth registered predictions: variant forms of one sign', 'predict_test100')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    site = defaultdict(Counter)
    per = defaultdict(Counter)
    for r in Fn:
        s = r['site'].strip()
        lv = R.level('Harappa', recs[r['sealid']]) if s == 'Harappa' else None
        for ln in r['seq']:
            for g in ln:
                site[g][s] += 1
                if lv in ('E', 'L'):
                    per[g][lv] += 1
    mds = lambda g: site[g]['Mohenjo-daro'] / max(1, site[g]['Mohenjo-daro'] + site[g]['Harappa'])
    es = lambda g: per[g]['E'] / max(1, per[g]['E'] + per[g]['L'])
    tc, S, C = sims(AB, 10)
    S = [s for s in S if s not in R.NUMS]
    pairs = sorted(combinations(S, 2), key=lambda p: -C[p])
    top = pairs[:30]
    q = T.quintiles(tc, S)
    byq = defaultdict(list)
    for s in S:
        byq[q[s]].append(s)
    rd.say('- signs %d; top context pairs: %s.' % (len(S), ', '.join('%s/%s %.2f' % (a, b, C[(a, b)]) for a, b in top[:10])))
    rd.say()
    DL = sorted({tuple(t) for t in AB})
    lines_of = defaultdict(set)
    for i, t in enumerate(DL):
        for g in set(t):
            lines_of[g].add(i)
    co = lambda a, b: len(lines_of[a] & lines_of[b])

    def rand_pair(p):
        a, b = p
        while True:
            x, y = random.choice(byq[q[a]]), random.choice(byq[q[b]])
            if x != y:
                return x, y

    def vs_random(key, title, stat, ps, higher=True, n=R.N):
        obs = sum(stat(*p) for p in ps) / len(ps)
        c = 0
        for _ in range(n):
            r_ = [rand_pair(p) for p in ps]
            v = sum(stat(*p) for p in r_) / len(r_)
            c += (v >= obs) if higher else (v <= obs)
        p = (c + 1) / (n + 1)
        rd.rec(key, title, 'pairs %d; mean %.3f; p = %.4f' % (len(ps), obs, p), p < 0.05)
    vs_random('AL1', 'twins split by city', lambda a, b: abs(mds(a) - mds(b)), top, n=R.N // 10)
    vs_random('AL2', 'twins avoid each other', co, top, higher=False, n=R.N // 10)
    sc = lambda a, b: 1.0 if a in cat and b in cat and cat[a] == cat[b] else 0.0
    vs_random('AL3', 'twins look alike', sc, top, n=R.N // 10)
    vs_random('AL4', 'twins split by period', lambda a, b: abs(es(a) - es(b)), top, n=R.N // 10)
    sp = [(a, b) for a, b in top if (mds(a) >= 0.8 and mds(b) <= 0.2) or (mds(b) >= 0.8 and mds(a) <= 0.2)]
    rd.rec('AL5', 'twins in different cities', 'pairs split 80/80 by city %d (%s); threshold 5' % (len(sp), ', '.join('%s/%s' % p for p in sp)), len(sp) >= 5)

    def two(key, title, a, b, cnt, k1, k2):
        x = [cnt[a][k1], cnt[a][k2]]
        y = [cnt[b][k1], cnt[b][k2]]
        p = min(1, 2 * min(R.hyper_ge(x[0], x[1], y[0], y[1]), R.fisher_less(x[0], x[1], y[0], y[1])))
        rd.rec(key, title, '%s %s %d/%d, %s %d/%d; two-sided p = %.4f' % (k1, a, x[0], sum(x), b, y[0], sum(y), p), p < 0.05)
    two('AL6', '705 and 706 by city', '705', '706', site, 'Mohenjo-daro', 'Harappa')
    two('AL7', '705 and 706 by period', '705', '706', per, 'E', 'L')
    two('AL8', '220 and 240 by city', '220', '240', site, 'Mohenjo-daro', 'Harappa')
    two('AL9', '220 and 233 by city', '220', '233', site, 'Mohenjo-daro', 'Harappa')
    hp = [(h, R.level('Harappa', recs[r['sealid']])) for r in Fn if r['site'].strip() == 'Harappa' for ln in r['seq'] if ln and ln[0] in ('817', '820', '861')
          for h in [ln[0]] if R.level('Harappa', recs[r['sealid']]) in ('E', 'L')]
    rd.mi('AL10', 'headings by period', 'Harappa headed lines', [h for h, _ in hp], [l_ for _, l_ in hp])
    mdo = [g for g in site if site[g]['Mohenjo-daro'] >= 5 and site[g]['Harappa'] == 0 and g not in R.NUMS]
    rd.rec('AL11', 'Mohenjo-daro has its own signs', 'Mohenjo-daro-only signs %d (%s); threshold 10' % (len(mdo), ', '.join(sorted(mdo)[:15])), len(mdo) >= 10)
    tc5, S5, C5 = sims(AB, 5)
    near = lambda g: max((x for x in S5 if x != g), key=lambda x: C5[(g, x)]) if g in S5 else None
    mn = [(g, near(g)) for g in mdo if near(g)]
    rd.thr('AL12', 'city-only signs have twins elsewhere', 'Mohenjo-daro-only signs whose nearest neighbour is Harappan', sum(mds(n) <= 0.5 for g, n in mn), len(mn), 0.3)
    ta = Counter(g for t in A for g in t)
    tb = Counter(g for t in B for g in t)
    ao = [g for g in ta if ta[g] >= 5 and tb[g] == 0]
    rd.rec('AL13', 'transcription-only signs', 'signs in A only %d (%s); threshold 5' % (len(ao), ', '.join(sorted(ao)[:15])), len(ao) >= 5)
    num = lambda g: int(g) if g.isdigit() else None
    close = lambda a, b: num(a) is not None and num(b) is not None and abs(num(a) - num(b)) <= 5
    vs_random('AL14', 'twins have near numbers', lambda a, b: 1.0 if close(a, b) else 0.0, top, n=R.N // 10)

    def adj_pairs(Sx):
        ss = set(Sx)
        return [(a, str(num(a) + 1)) for a in Sx if num(a) is not None and str(num(a) + 1) in ss]

    def al15(Sx, Cx, key, lab):
        ap = adj_pairs(Sx)
        allp = list(combinations(Sx, 2))
        rnd = [Cx[p] for p in random.sample(allp, min(len(allp), 2000))]
        rd.rank(key, 'number neighbours share contexts%s' % lab, 'adjacent-number against random pairs', [Cx[p] for p in ap], rnd)
        return ap
    ap = al15(S, C, 'AL15', '')
    vs_random('AL16', 'number neighbours avoid each other', co, ap, higher=False, n=R.N // 10)
    vs_random('AL17', 'number neighbours split by city', lambda a, b: abs(mds(a) - mds(b)), ap, n=R.N // 10)
    hi = [(a, b) for a, b in ap if C[(a, b)] >= 0.3]
    rd.rec('AL18', 'candidate variant list', 'number-adjacent pairs with cosine 0.3+: %d (%s); threshold 10' % (len(hi), ', '.join('%s/%s' % p for p in hi)), len(hi) >= 10)
    tcB, SB, CB = sims(B, 5)
    al15([s for s in SB if s not in R.NUMS], CB, 'AL19', ' (B)')
    FL = [list(ln) for r in Fn for ln in r['seq'] if ln]
    tcF, SF, CF = sims(FL, 10)
    al15([s for s in SF if s not in R.NUMS], CF, 'AL20', ' (F)')
    rd.finish()


if __name__ == '__main__':
    main()
