"""Classes among the signs inside names: which signs behave alike?

Names = the text before the ending, heading removed (ICIT-derived + M77 additions). For every sign with 15+ tokens
inside names, a profile: share of its tokens name-initial, name-final and inside; the ending its names take when it
is last (740 / 520); and positive-PMI vectors of its left and right neighbours inside names (with name start and end
as neighbours), reduced to 10 dimensions (SVD) and length-normalised. Profiles are clustered with k-means (k = 8, 30 restarts); stability = for each pair
of signs, how often they fall in the same cluster across 30 bootstrap resamples of the names (reported per cluster
as the mean co-assignment of its members).

Writes results/name_classes.md.
"""
import math
import os
import random
from collections import Counter, defaultdict

import numpy as np

from numerals import NUMS
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPEN = ('817', '820', '861')


def say(s=''):
    OUT.append(s)
    print(s)


def names_of(rows):
    out = []
    for r in rows:
        for t in r['seq']:
            t = [g for g in t if g != '?']
            if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1'):
                t = t[2:]
            if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
                out.append((t[:-2], t[-2]))
            elif len(t) >= 2 and t[-1] in ('740', '520'):
                out.append((t[:-1], t[-1]))
    return [(s, e) for s, e in out if s]


def profiles(names, signs):
    ctx = [f for f in sorted({g for s, _ in names for g in s} | {'^', '$'})]
    idx = {g: i for i, g in enumerate(ctx)}
    L = np.zeros((len(signs), len(ctx)))
    R = np.zeros((len(signs), len(ctx)))
    pos = np.zeros((len(signs), 3))
    end = np.zeros((len(signs), 2))
    si = {g: i for i, g in enumerate(signs)}
    for s, e in names:
        seq = ['^'] + s + ['$']
        for j in range(1, len(seq) - 1):
            g = seq[j]
            if g not in si:
                continue
            i = si[g]
            L[i, idx[seq[j - 1]]] += 1
            R[i, idx[seq[j + 1]]] += 1
            pos[i, 0 if j == 1 else (2 if j == len(seq) - 2 else 1)] += 1
        if s[-1] in si:
            end[si[s[-1]], 0 if e == '740' else 1] += 1

    def ppmi(M):
        tot = M.sum()
        rs, cs = M.sum(1, keepdims=True), M.sum(0, keepdims=True)
        with np.errstate(divide='ignore', invalid='ignore'):
            p = np.log((M * tot) / (rs * cs))
        p[~np.isfinite(p)] = 0
        return np.maximum(p, 0)
    posn = pos / np.maximum(pos.sum(1, keepdims=True), 1)
    endn = (end[:, 1:2] + 0.5) / (end.sum(1, keepdims=True) + 1)
    C = np.hstack([ppmi(L), ppmi(R)])
    C = C / (np.linalg.norm(C, axis=1, keepdims=True) + 1e-9)
    U, S, _ = np.linalg.svd(C - C.mean(0), full_matrices=False)
    Z = U[:, :10] * S[:10]
    Z = Z / (np.linalg.norm(Z, axis=1, keepdims=True) + 1e-9)
    X = np.hstack([Z, 0.6 * posn, 0.6 * endn])
    return X, posn, end


def kmeans(X, k, rng, restarts=30, iters=100):
    best = None
    for _ in range(restarts):
        C = X[rng.choice(len(X), k, replace=False)]
        for _ in range(iters):
            lab = ((X[:, None, :] - C[None]) ** 2).sum(2).argmin(1)
            newC = np.array([X[lab == j].mean(0) if (lab == j).any() else C[j] for j in range(k)])
            if np.allclose(newC, C):
                break
            C = newC
        inert = ((X - C[lab]) ** 2).sum()
        if best is None or inert < best[0]:
            best = (inert, lab)
    return best[1]


def main():
    rng = np.random.default_rng(163)
    rows = [r for rs in (load(), load(only_m77=True)) for r in rs if r['flat']]
    names = names_of(rows)
    tok = Counter(g for s, _ in names for g in s)
    signs = sorted((g for g, c in tok.items() if c >= 15), key=lambda g: -tok[g])
    X, posn, end = profiles(names, signs)
    lab = kmeans(X, 8, rng)
    co = np.zeros((len(signs), len(signs)))
    for _ in range(30):
        samp = [names[i] for i in rng.integers(0, len(names), len(names))]
        Xb, _, _ = profiles(samp, signs)
        lb = kmeans(Xb, 8, rng, restarts=10)
        co += (lb[:, None] == lb[None, :])
    co /= 30
    say('# Classes among the signs inside names')
    say()
    say('- names: %d; signs with 15+ tokens inside names: %d.' % (len(names), len(signs)))
    say()
    say('| class | signs (tokens) | initial / inside / final | 520 when last | stability |')
    say('|---|---|---|---|---|')
    for j in range(8):
        mem = [i for i in range(len(signs)) if lab[i] == j]
        if not mem:
            continue
        p = posn[mem].mean(0)
        e = end[mem].sum(0)
        stab = co[np.ix_(mem, mem)].mean() if len(mem) > 1 else float('nan')
        tag = []
        if sum(1 for i in mem if signs[i] in FISH) >= len(mem) / 2:
            tag.append('fish')
        if sum(1 for i in mem if signs[i] in NUMS) >= len(mem) / 2:
            tag.append('numerals')
        say('| %d%s | %s | %.0f%% / %.0f%% / %.0f%% | %d of %d | %.2f |' % (
            j + 1, (' (' + ', '.join(tag) + ')') if tag else '',
            ', '.join('%s (%d)' % (signs[i], tok[signs[i]]) for i in sorted(mem, key=lambda i: -tok[signs[i]])[:12]),
            100 * p[0], 100 * p[1], 100 * p[2], e[1], e.sum(), stab))
    say()
    say('Stability is the mean share of bootstrap runs in which two members of a class fall together (1 = always).')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'name_classes.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
