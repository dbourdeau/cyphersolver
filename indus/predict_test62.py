"""Sixty-second registered prediction set (PREDICTIONS.md, DC1-DC10): sign classes from context. Writes
results/predict_test62.md."""
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from predict_test43 import sp_perm
from signs import FISH

random.seed(82)


def sims(lines, k=20):
    tc = Counter(g for t in lines for g in t)
    S = sorted(g for g in tc if tc[g] >= k)
    vec = T.contexts([list(t) for t in lines])
    C = {}
    for a, b in combinations(S, 2):
        C[(a, b)] = C[(b, a)] = T.cos(vec.get(a, {}), vec.get(b, {}))
    return tc, S, C


def nn(S, C):
    return {a: max((b for b in S if b != a), key=lambda b: C[(a, b)]) for a in S}


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    head, attr = R.classes(A)
    rd = R.Round('Sixty-second registered predictions: sign classes from context', 'predict_test62')
    tc, S, C = sims(AB)
    rd.say('- signs with 20+ tokens %d.' % len(S))
    rd.say()
    q = T.quintiles(tc, S)
    byq = defaultdict(list)
    for s in S:
        byq[q[s]].append(s)
    mean = lambda xs: sum(C[p] for p in combinations(xs, 2)) / max(1, len(xs) * (len(xs) - 1) // 2)

    def cohesion(key, title, cls):
        m = [g for g in S if g in cls]
        obs = mean(m)
        ge = 0
        for _ in range(R.N):
            pick = set()
            for g in m:
                while True:
                    x = random.choice(byq[q[g]])
                    if x not in pick or len(pick) >= len(S):
                        break
                pick.add(x)
            ge += mean(sorted(pick)) >= obs
        p = (ge + 1) / (R.N + 1)
        rd.rec(key, title, 'members %d; mean cosine %.3f; p = %.4f' % (len(m), obs, p), p < 0.05)
    cohesion('DC1', 'fish signs keep company', FISH)
    cohesion('DC2', 'numerals keep company', set(R.NUMS))
    cohesion('DC3', 'heads keep company', head)
    tA, SA, CA = sims(A)
    tB, SB, CB = sims(B)
    com = sorted(set(SA) & set(SB))
    pr = list(combinations(com, 2))
    o, p = sp_perm([CA[x] for x in pr], [CB[x] for x in pr], n=1000)
    rd.rec('DC4', 'the classes hold across transcriptions', 'signs %d, pairs %d; Spearman %.3f; p = %.4f (1,000 shuffles)' % (
        len(com), len(pr), o, p), o >= 0.5 and p < 0.05)
    fl = lambda site: [ln for r in F if r['site'].strip() == site for ln in r['seq'] if ln]
    tM, SM, CM = sims(fl('Mohenjo-daro'))
    tH, SH, CH = sims(fl('Harappa'))
    com2 = sorted(set(SM) & set(SH))
    pr2 = list(combinations(com2, 2))
    o, p = sp_perm([CM[x] for x in pr2], [CH[x] for x in pr2], n=1000)
    rd.rec('DC5', 'the classes hold across cities', 'signs %d, pairs %d; Spearman %.3f; p = %.4f (1,000 shuffles)' % (
        len(com2), len(pr2), o, p), o >= 0.4 and p < 0.05)
    cat = R.cat_of()
    cs = [g for g in S if g in cat]
    same = [C[(a, b)] for a, b in combinations(cs, 2) if cat[a] == cat[b]]
    diff = [C[(a, b)] for a, b in combinations(cs, 2) if cat[a] != cat[b]]
    rd.rank('DC6', 'look-alikes keep company', 'same-category against cross-category pairs', same, diff)
    N_ = nn(S, C)
    for key, title, cls, t in (('DC7', 'a fish is nearest a fish', FISH, 0.5), ('DC8', 'a numeral is nearest a numeral', set(R.NUMS), 0.7),
                               ('DC9', 'a head is nearest a head', head, 0.5)):
        m = [g for g in S if g in cls]
        rd.thr(key, title, 'nearest neighbour in the class', sum(N_[g] in cls for g in m), len(m), t)
    nA, nB = nn(SA, CA), nn(SB, CB)
    rd.thr('DC10', 'the neighbour holds across transcriptions', 'same nearest neighbour in A and B', sum(nA[g] == nB[g] for g in com), len(com), 0.3)
    rd.finish()


if __name__ == '__main__':
    main()
