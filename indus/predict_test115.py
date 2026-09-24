"""Hundred-and-fifteenth registered prediction set (PREDICTIONS.md, PR1-PR20): structural predictions of published
proposals. Writes results/predict_test115.md."""
import math
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test112 import runs
from signs import FISH

random.seed(135)
CITY = ('Mohenjo-daro', 'Harappa')


def ent(c):
    n = sum(c.values())
    return -sum(v / n * math.log2(v / n) for v in c.values())


def cond_ent(lines):
    big = Counter(p for t in lines for p in zip(t, t[1:]))
    first = Counter(a for a, b in big.elements())
    n = sum(big.values())
    return -sum(v / n * math.log2(v / first[a]) for (a, b), v in big.items())


def adj_mi(lines):
    big = Counter(p for t in lines for p in zip(t, t[1:]))
    n = sum(big.values())
    L = Counter(a for (a, b), v in big.items() for _ in range(v))
    Rr = Counter(b for (a, b), v in big.items() for _ in range(v))
    return sum(v / n * math.log2(v * n / (L[a] * Rr[b])) for (a, b), v in big.items())


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-fifteenth registered predictions: structural predictions of published proposals', 'predict_test115')
    DL = sorted({tuple(t) for t in AB})
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FL = sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln})
    rd.say("- distinct lines: A + B %d, F' %d." % (len(DL), len(FL)))
    rd.say()

    def pr1(lines, key, lab):
        v = [(sum(R.NUMS[g][0] for g in r), t[j] in FISH) for t in lines for i, j, r in runs(t) if j < len(t) and t[j] not in R.NUMS]
        rd.gtl(key, 'six and seven fish%s' % lab, 'value 6 or 7, before a fish', [x in (6, 7) for x, f in v if f], [x in (6, 7) for x, f in v if not f])
    pr1(DL, 'PR1', '')
    objs = defaultdict(set)
    site = defaultdict(set)
    typ = {}
    for r in Fn:
        for b, e in R.names_in(r):
            objs[(b, e)].add(r['sealid'])
            site[b].add(r['site'].strip())
            typ.setdefault((b, e), []).append(r['type'][:3])
    nf = lambda b: any(x in R.NUMS and y in FISH for x, y in zip(b, b[1:]))
    k = [k_ for k_ in objs if nf(k_[0])]
    rd.thr('PR2', 'star names are personal', 'numeral + fish names on one object', sum(len(objs[k_]) == 1 for k_ in k), len(k), 0.7)
    bodies = sorted({b for b, e in T.names(AB) if b})
    keyset = defaultdict(set)
    for b in bodies:
        for i, g in enumerate(b):
            if g in FISH:
                keyset[b[:i] + ('*',) + b[i + 1:]].add(g)
    mp = sum(len(v) * (len(v) - 1) // 2 for v in keyset.values())
    rd.rec('PR3', 'fish variants are different words', 'minimal pairs differing by one fish sign: %d; threshold 10' % mp, mp >= 10)
    tk = [x for k_ in k for x in typ[k_]]
    rd.thr('PR4', 'star names are seal names', 'numeral + fish name tokens on seals', sum(x == 'SEA' for x in tk), len(tk), 0.8)
    both = lambda b: len(site[b] & set(CITY)) == 2
    cb = [b for b in site if site[b] & set(CITY)]
    a = [both(b) for b in cb if b[-1] in FISH]
    c = [both(b) for b in cb if b[-1] not in FISH]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('PR5', 'fish names are as local as others', 'at both cities, fish-final bodies %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    t740 = [(t, i) for t in DL for i in range(len(t)) if t[i] == '740']
    rd.thr('PR6', '740 is a suffix', '740 tokens line-initial', sum(i == 0 for t, i in t740), len(t740), 0.02, above=False)
    before = sum(1 for t in DL for x, y in zip(t, t[1:]) if x in ('400', '90', '151') and y == '740')
    after = sum(1 for t in DL for x, y in zip(t, t[1:]) if x == '740' and y in ('400', '90', '151'))
    rd.thr('PR7', 'suffixes stack after the ending', "'suffix 740' among suffix-740 adjacencies", before, before + after, 0.05, above=False)
    allF = Counter(g for r in F for ln in r['seq'] for g in ln)
    rd.thr('PR8', 'many singletons', 'F sign types occurring once', sum(n == 1 for n in allF.values()), len(allF), 0.2)
    m = sum(len(t) for t in FL) / len(FL)
    rd.rec('PR9', 'texts are short', "mean F' line length %.2f; threshold under 5" % m, m < 5)
    rep = lambda t: any(t[i] == t[j] for i in range(len(t)) for j in range(i + 2, len(t)))
    obs = sum(map(rep, DL))
    le = 0
    for _ in range(R.N // 10):
        k2 = 0
        for t in DL:
            s = list(t)
            random.shuffle(s)
            k2 += rep(s)
        le += k2 <= obs
    p = (le + 1) / (R.N // 10 + 1)
    rd.rec('PR10', 'little repetition', 'lines with a non-adjacent repeat %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)

    def pr11(lines, key, lab):
        obs = adj_mi(lines)
        sh = []
        for _ in range(100):
            ss = []
            for t in lines:
                s = list(t)
                random.shuffle(s)
                ss.append(s)
            sh.append(adj_mi(ss))
        mean = sum(sh) / len(sh)
        rd.rec(key, 'order carries information%s' % lab, 'adjacent MI %.3f; shuffled mean %.3f; ratio %.2f; threshold 2' % (obs, mean, obs / mean), obs >= 2 * mean)
    pr11(DL, 'PR11', '')

    def pr12(lines, key, lab):
        h1 = ent(Counter(g for t in lines for g in t))
        hc = cond_ent(lines)
        rd.rec(key, 'the next sign is predictable%s' % lab, 'H(next|prev) %.2f, H %.2f bits; ratio %.2f; threshold 0.80' % (hc, h1, hc / h1), hc / h1 < 0.8)
    pr12(DL, 'PR12', '')
    fc = sorted(Counter(g for t in DL for g in t).values(), reverse=True)[:100]
    xs = [math.log(i + 1) for i in range(len(fc))]
    ys = [math.log(v) for v in fc]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    rd.rec('PR13', 'a Zipf-like curve', 'slope %.2f; range -1.3 to -0.7' % sl, -1.3 <= sl <= -0.7)
    big = Counter(p for t in DL for p in zip(t, t[1:]))
    rd.thr('PR14', 'frequent pairs cover the text', 'top-50 pair tokens', sum(n for _, n in big.most_common(50)), sum(big.values()), 0.3)
    rd.thr('PR15', 'open combination', 'pair types occurring once', sum(n == 1 for n in big.values()), len(big), 0.5)
    nx = sum(1 for t in DL for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS)
    xn = sum(1 for t in DL for x, y in zip(t, t[1:]) if x not in R.NUMS and y in R.NUMS)
    rd.rec('PR16', 'the number precedes the noun', "'N X' %d, 'X N' %d; ratio %.2f; threshold 1.5" % (nx, xn, nx / max(1, xn)), nx >= 1.5 * xn)
    BL = sorted({tuple(t) for t in B})
    pr11(BL, 'PR17', ' (B)')
    pr12(FL, 'PR18', " (F')")
    bc = Counter(g for t in B for g in t)
    rd.thr('PR19', 'many singletons (B)', 'B sign types occurring once', sum(n == 1 for n in bc.values()), len(bc), 0.2)
    pr1(FL, 'PR20', " (F')")
    rd.finish()


if __name__ == '__main__':
    main()
