#!/usr/bin/env python3
"""Order-preserving match between a table's predictions for a run of groups and the words of a decipherment.
score = length of the longest common subsequence between (predicted headwords of the groups that have a table entry, in order)
and (the decipherment's words, in order); a match is the same word or the same headword in another form (align.same)."""
import random
from align import same, norm
def lcs(pred, words):
    n, m = len(pred), len(words)
    L = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            L[i+1][j+1] = L[i][j] + 1 if same(pred[i], words[j]) else max(L[i][j+1], L[i+1][j])
    return L[n][m]
def run(groups, words, tab, nshuf=200, seed=35):
    """tab: dict group -> headword. Returns (covered, lcs, [shuffled scores])."""
    words = [norm(w) for w in words]
    pred = [tab[g] for g in groups if g in tab]
    real = lcs(pred, words)
    rng = random.Random(seed); keys = sorted(tab); vals = [tab[k] for k in keys]; sh = []
    for _ in range(nshuf):
        v = vals[:]; rng.shuffle(v); t2 = dict(zip(keys, v))
        sh.append(lcs([t2[g] for g in groups if g in t2], words))
    return len(pred), real, sh
