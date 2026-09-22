# Seeded coordinate-ascent / annealing over the 13 blank code groups: each blank code (same value everywhere)
# takes a word from the 2000 most frequent en-1640s corpus words; objective = en-1640s LM score of both passages.
# Seed = the conjectures in key.C. Reports whether the optimum agrees with the conjectures.
import re, sys, collections, random
sys.path.insert(0, '.'); sys.path.insert(0, 'harley7001')
from lang import lm
from key import K, C
M = lm.load('en-1640s')
cnt = collections.Counter(re.findall(r"[a-z]+", open('lang/corpora/en-1640s-history.txt', encoding='utf8').read().lower()))
vocab = [w for w, _ in cnt.most_common(2000)]
P = {p: [x for x in (x for l in open('harley7001/ct.txt') if l.startswith(p + ':') for x in l[2:].split()) if K.get(x) != '·'] for p in 'AB'}
gaps = sorted({x for s in P.values() for x in s if x not in K})
def txt(a): return [' '.join(K.get(x) or a[x] for x in s) for s in P.values()]
def score(a): return sum(M.score(lm.norm(t)) for t in txt(a))
seed = {g: C.get(g, 'the').lower().strip('[]').split()[-1] for g in gaps}
a = dict(seed); best = score(a)
for sweep in range(2):
    for g in gaps:
        for w in vocab:
            old = a[g]; a[g] = w; s = score(a)
            if s > best: best = s
            else: a[g] = old
    print('sweep', sweep, round(best, 1))
agree = [g for g in gaps if a[g] == seed[g]]
print('seed score', round(score(seed), 1), 'final', round(best, 1))
for g in gaps: print(g, 'seed', seed[g], '-> anneal', a[g])
print('agree with conjecture:', len(agree), 'of', len(gaps))
