"""Hundred-and-forty-eighth registered prediction set (PREDICTIONS.md, PV1-PV7): productivity of the endings.
Writes results/predict_test148.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test103 import CL

random.seed(168)
N = 10000


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-forty-eighth registered predictions: productivity of the endings', 'predict_test148')
    DL = sorted({tuple(t) for t in AB})
    names = sorted({(b, e) for b, e in T.names(AB) if b})
    cn = set()
    for t in DL:
        u = t[:-1] if t and t[-1] == '400' else t
        if len(u) >= 2 and u[-1] in CL and not any(g in R.END for g in u):
            cn.add((u[:-1], 'CL'))
    pool = names + sorted(cn)
    hc = Counter(b[-1] for b, e in pool)
    hapax = lambda b: hc[b[-1]] == 1
    rd.say('- names: 740 %d, 520 %d, closer %d; hapax heads (one distinct name in the pool) %d.' % (
        sum(e == '740' for b, e in pool), sum(e == '520' for b, e in pool), sum(e == 'CL' for b, e in pool), sum(v == 1 for v in hc.values())))
    rd.say()

    def P(items, lab):
        x = [h for h, e in items if e == lab]
        return sum(x) / max(1, len(x))

    def pdiff(key, title, hi, lo):
        items = [(hapax(b), e) for b, e in pool if e in (hi, lo)]
        obs = P(items, hi) - P(items, lo)
        labs = [e for h, e in items]
        ge = 0
        for _ in range(N):
            random.shuffle(labs)
            it = [(h, l) for (h, _), l in zip(items, labs)]
            ge += P(it, hi) - P(it, lo) >= obs
        p = (ge + 1) / (N + 1)
        rd.rec(key, title, 'P(%s) %.3f, P(%s) %.3f; difference %+.3f; p = %.4f' % (hi, P(items, hi), lo, P(items, lo), obs, p), obs > 0 and p < 0.05)
    pdiff('PV1', '740 is more productive than 520', '740', '520')
    a = [e == '740' for b, e in names if hapax(b)]
    c = [e == '740' for b, e in names if not hapax(b)]
    rd.gtl('PV2', 'hapax heads take 740', '740, names with a hapax head', a, c)
    n5 = [b[-1] for b, e in names if e == '520']
    n7 = [b[-1] for b, e in names if e == '740']
    k = len(n5)
    win = sum(len(set(random.sample(n7, k))) > len(set(n5)) for _ in range(1000))
    rd.thr('PV3', 'more heads at equal size', '740 draws of %d names with more distinct heads than 520 (%d)' % (k, len(set(n5))), win, 1000, 0.95)
    items = [(hapax(b), e) for b, e in pool if e in ('740', 'CL')]
    obs = P(items, '740') - P(items, 'CL')
    labs = [e for h, e in items]
    ge = 0
    for _ in range(N):
        random.shuffle(labs)
        it = [(h, l) for (h, _), l in zip(items, labs)]
        ge += P(it, '740') - P(it, 'CL') >= obs
    p = (ge + 1) / (N + 1)
    rd.rec('PV4', 'closers are less productive than 740', 'P(740) %.3f, P(closer) %.3f; p = %.4f' % (P(items, '740'), P(items, 'CL'), p), obs > 0 and p < 0.05)
    rd.rank('PV5', '740 bodies are longer', '740 against 520 bodies', [len(b) for b, e in names if e == '740'], [len(b) for b, e in names if e == '520'])
    sites = defaultdict(set)
    for r in F:
        for b, e in R.names_in(r):
            if b:
                sites[b[-1]].add(r['site'].strip())
    a = [e == '740' for b, e in names if len(sites.get(b[-1], ())) == 1]
    c = [e == '740' for b, e in names if len(sites.get(b[-1], ())) >= 2]
    rd.gtl('PV6', 'one-site heads take 740', '740, names with a one-site head', a, c)
    tc = Counter(g for t in AB for g in t)
    h7 = sorted({b[-1] for b, e in names if e == '740' and hapax(b)})
    rd.thr('PV7', 'new heads are rare signs', 'hapax heads of 740 names with under 10 tokens', sum(tc[h] < 10 for h in h7), len(h7), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
