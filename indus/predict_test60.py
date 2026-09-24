"""Sixtieth registered prediction set (PREDICTIONS.md, VR1-VR10): are rare signs variants? Writes
results/predict_test60.md."""
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname


def frames(lines):
    fr = defaultdict(Counter)
    for t in lines:
        p = ['#'] + list(t) + ['#']
        for i in range(1, len(p) - 1):
            fr[p[i]][(p[i - 1], p[i + 1])] += 1
    return fr


def setup(lines):
    tc = Counter(g for t in lines for g in t)
    rare = {g for g in tc if 2 <= tc[g] <= 5 and g not in R.NUMS}
    common = {g for g in tc if tc[g] >= 20}
    fr = frames(lines)
    byf = defaultdict(set)
    for g in common:
        for f in fr[g]:
            byf[f].add(g)
    best = {}
    for g in rare:
        c = Counter(x for f in fr[g] for x in byf[f] if x != g)
        if c:
            best[g] = max(c, key=lambda x: (c[x], tc[x]))
    return tc, rare, common, fr, byf, best


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Sixtieth registered predictions: are rare signs variants?', 'predict_test60')
    tc, rare, common, fr, byf, best = setup(AB)
    rd.say('- rare signs %d, common signs %d, rare signs with a best match %d.' % (len(rare), len(common), len(best)))
    rd.say()
    toks = [(f, g) for g in rare for f, n in fr[g].items() for _ in range(n)]
    rd.thr('VR1', 'rare signs fill common frames', 'rare tokens in a frame shared with a common sign',
           sum(bool(byf[f] - {g}) for f, g in toks), len(toks), 0.6)
    bA, bB = setup(A)[5], setup(B)[5]
    both = [g for g in bA if g in bB]
    rd.thr('VR2', 'the match is stable', 'same best match in A and B', sum(bA[g] == bB[g] for g in both), len(both), 0.5)
    nm = T.names(AB)
    last, tot = Counter(), Counter()
    ends = defaultdict(Counter)
    for b, e in nm:
        for i, g in enumerate(b):
            tot[g] += 1
            last[g] += i == len(b) - 1
        if b:
            ends[b[-1]][e] += 1
    maj = lambda g: last[g] / tot[g] >= 0.5
    pr = [g for g in best if tot[g] and tot[best[g]]]
    rd.thr('VR3', 'the match has the same position', 'same majority position', sum(maj(g) == maj(best[g]) for g in pr), len(pr), 0.8)
    pe = [g for g in best if ends[g] and ends[best[g]]]
    rd.thr('VR4', 'the match takes the same ending', 'same majority ending',
           sum(ends[g].most_common(1)[0][0] == ends[best[g]].most_common(1)[0][0] for g in pe), len(pe), 0.7)
    ft = [(r['type'].startswith('SEAL'), g) for r in F for ln in r['seq'] for g in ln]
    rd.gtl('VR5', 'rare signs are off the seals', 'off seals, rare tokens', [not s for s, g in ft if g in rare], [not s for s, g in ft if g in common])
    gl = [(nonname(t), g) for t in AB if nonname(t) or R.name_of(t) for g in t]
    rd.gtl('VR6', 'rare signs are in formulas', 'formula, rare tokens', [f for f, g in gl if g in rare], [f for f, g in gl if g in common])
    cat = R.cat_of()
    pc = [g for g in best if g in cat and best[g] in cat]
    rd.thr('VR7', 'the match looks alike', 'same category', sum(cat[g] == cat[best[g]] for g in pc), len(pc), 0.3)
    lf = [(i == len(t) - 1, g) for t in AB for i, g in enumerate(t)]
    rd.gtl('VR8', 'rare signs close lines', 'last, rare tokens', [l_ for l_, g in lf if g in rare], [l_ for l_, g in lf if g in common])
    whole = {tuple(t) for t in AB}
    one = [t for t in AB if sum(g in rare for g in t) == 1 and any(g in best for g in t)]
    sub = lambda t: tuple(best[g] if g in best else g for g in t)
    rd.thr('VR9', 'the substitution gives a known line', 'lines with one rare sign', sum(sub(t) in whole for t in one), len(one), 0.1)
    top = {g for g, _ in tc.most_common(20)}
    rd.thr('VR10', 'the match is a very common sign', 'best match in the top 20', sum(best[g] in top for g in best), len(best), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
