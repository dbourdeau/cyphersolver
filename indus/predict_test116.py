"""Hundred-and-sixteenth registered prediction set (PREDICTIONS.md, HX1-HX20): sets 114-115 on held-out data. Writes
results/predict_test116.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test112 import runs
from predict_test114 import rows
from predict_test115 import cond_ent, ent
from signs import FISH

random.seed(136)
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixteenth registered predictions: sets 114-115 on held-out data', 'predict_test116')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FL = sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln})
    OL = sorted({tuple(ln) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if ln})
    OT = sorted({(r['type'][:3], tuple(ln)) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if ln})
    BL = sorted({tuple(t) for t in B})
    rd.say("- F' %d, OS %d, B %d distinct lines." % (len(FL), len(OL), len(BL)))
    rd.say()
    V = lambda g: R.NUMS[g][0]
    is2N = lambda r: len(r) == 2 and r[0] == '2'

    def sr13(lines, key, lab):
        rr = rows(lines)
        single = defaultdict(Counter)
        for t, i, j, r in rr:
            if len(r) == 1 and j < len(t) and t[j] not in R.NUMS:
                single[t[j]][V(r[0])] += 1
        a = b = 0
        for t, i, j, r in rr:
            if is2N(r) and j < len(t) and t[j] not in R.NUMS and single[t[j]]:
                c = single[t[j]].most_common(1)[0][0]
                a += c == V(r[1])
                b += c == V(r[1]) + 2
        rd.rec(key, "the '2' is not added%s" % lab, 'equals N %d, equals N + 2 %d' % (a, b), a > b)

    def sr4(lines, key, lab):
        rr = rows(lines)
        cases = [(t, i, j) for t, i, j, r in rr if is2N(r) and j < len(t)]
        ok = sum(any(u[k:k + 2] == (t[i + 1], t[j]) and not (k > 0 and u[k - 1] == '2') for u in lines for k in range(len(u) - 1) if u is not t) for t, i, j in cases)
        rd.thr(key, "the '2' is an added prefix%s" % lab, "'N X' attested without the '2'", ok, len(cases), 0.5)
    sr13(FL, 'HX1', " (F')")
    sr4(BL, 'HX2', ' (B)')
    sr13(BL, 'HX3', ' (B)')
    x = [ty for ty, t in OT if any(is2N(r) for tt, i, j, r in rows([t]))]
    rd.thr('HX4', "'2 N' lines are seal lines (OS)", "'2 N' lines on seals", sum(ty == 'SEA' for ty in x), len(x), 0.7)

    def sr15(lines, key, lab):
        rr = rows(lines)
        rd.thr(key, 'numbers are short%s' % lab, 'runs of 3+ signs', sum(len(r) >= 3 for t, i, j, r in rr), len(rr), 0.03, above=False)
    sr15(FL, 'HX5', " (F')")
    sr15(BL, 'HX6', ' (B)')
    nx = Counter(t[j] for t, i, j, r in rows(FL) if is2N(r) and j < len(t))
    rd.thr('HX7', "'2 N' counts few things (F')", 'five commonest followers (%s)' % ', '.join('%s x%d' % kv for kv in nx.most_common(5)),
           sum(n for _, n in nx.most_common(5)), sum(nx.values()), 0.5)

    def minimal(lines):
        bodies = sorted({R.name_of(list(t))[0] for t in lines if R.name_of(list(t)) and R.name_of(list(t))[0]})
        ks = defaultdict(set)
        for b in bodies:
            for i, g in enumerate(b):
                if g in FISH:
                    ks[b[:i] + ('*',) + b[i + 1:]].add(g)
        return sum(len(v) * (len(v) - 1) // 2 for v in ks.values())
    m = minimal(FL)
    rd.rec('HX8', "fish variants are different words (F')", 'minimal pairs %d; threshold 10' % m, m >= 10)
    m = minimal(BL)
    rd.rec('HX9', 'fish variants are different words (B)', 'minimal pairs %d; threshold 5' % m, m >= 5)

    def pr6(lines, key, lab):
        t7 = [(t, i) for t in lines for i in range(len(t)) if t[i] == '740']
        rd.thr(key, '740 is a suffix%s' % lab, '740 line-initial', sum(i == 0 for t, i in t7), len(t7), 0.02, above=False)

    def pr7(lines, key, lab):
        b = sum(1 for t in lines for x, y in zip(t, t[1:]) if x in ('400', '90', '151') and y == '740')
        a = sum(1 for t in lines for x, y in zip(t, t[1:]) if x == '740' and y in ('400', '90', '151'))
        rd.thr(key, 'suffixes stack after the ending%s' % lab, "'suffix 740'", b, a + b, 0.05, above=False)
    pr6(FL, 'HX10', " (F')")
    pr6(BL, 'HX11', ' (B)')
    pr7(FL, 'HX12', " (F')")
    pr7(BL, 'HX13', ' (B)')

    def pr10(lines, key, lab):
        rep = lambda t: any(t[i] == t[j] for i in range(len(t)) for j in range(i + 2, len(t)))
        obs = sum(map(rep, lines))
        le = 0
        for _ in range(R.N // 10):
            k = 0
            for t in lines:
                s = list(t)
                random.shuffle(s)
                k += rep(s)
            le += k <= obs
        p = (le + 1) / (R.N // 10 + 1)
        rd.rec(key, 'little repetition%s' % lab, 'lines with a repeat %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    pr10(BL, 'HX14', ' (B)')
    pr10(OL, 'HX15', ' (OS)')

    def pr13(lines, key, lab):
        fc = sorted(Counter(g for t in lines for g in t).values(), reverse=True)[:100]
        xs = [math.log(i + 1) for i in range(len(fc))]
        ys = [math.log(v) for v in fc]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        rd.rec(key, 'a Zipf-like curve%s' % lab, 'slope %.2f; range -1.3 to -0.7' % sl, -1.3 <= sl <= -0.7)
    pr13(FL, 'HX16', " (F')")
    pr13(BL, 'HX17', ' (B)')
    big = Counter(p for t in FL for p in zip(t, t[1:]))
    rd.thr('HX18', "open combination (F')", 'pair types occurring once', sum(n == 1 for n in big.values()), len(big), 0.5)
    h1 = ent(Counter(g for t in BL for g in t))
    hc = cond_ent(BL)
    rd.rec('HX19', 'the next sign is predictable (B)', 'ratio %.2f; threshold 0.80' % (hc / h1), hc / h1 < 0.8)
    objs = defaultdict(set)
    for r in Fn:
        if r['site'].strip() not in CITY:
            for b, e in R.names_in(r):
                objs[(b, e)].add(r['sealid'])
    nf = lambda b: any(x in R.NUMS and y in FISH for x, y in zip(b, b[1:]))
    k = [k_ for k_ in objs if nf(k_[0])]
    rd.thr('HX20', 'star names are personal (OS)', 'numeral + fish names on one object', sum(len(objs[k_]) == 1 for k_ in k), len(k), 0.7)
    rd.finish()


if __name__ == '__main__':
    main()
