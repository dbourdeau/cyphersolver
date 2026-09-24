"""Test of the twenty-third registered prediction set (PREDICTIONS.md, G1-G8, C1-C5): ligatures, and a classification
that must pass its numeral check first.

Usage: python predict_test23.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test23.md.
"""
import os
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations

import numpy as np

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test14 import cat_of, hyper_ge
from predict_test18 import n700
from predict_test19 import cosd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
GRAMMAR = {'740', '520', '90', '400', '151', '817', '820', '861', '2'}
FORMULA = {'705', '706', '33'}
LIGS = [('G1', '154', '151', '740'), ('G2', '156', '151', '520'), ('G3', '555', '550', '482'),
        ('G4', '742', '740', '2'), ('G5', '702', '700', '2'), ('G6', '703', '700', '3')]
random.seed(43)


def say(s=''):
    OUT.append(s)
    print(s)


def lr(lines):
    L, R = defaultdict(Counter), defaultdict(Counter)
    for t in lines:
        s = ['^'] + list(t) + ['$']
        for i in range(1, len(s) - 1):
            L[s[i]][s[i - 1]] += 1
            R[s[i]][s[i + 1]] += 1
    return L, R


def seq_score(L, R, lig, x, y):
    a = (cosd(L[lig], L[x]) + cosd(R[lig], R[y])) / 2
    b = (cosd(L[lig], L[y]) + cosd(R[lig], R[x])) / 2
    return max(a, b)


def lig_test(lines, lig, x, y):
    tok = Counter(g for t in lines for g in t)
    if min(tok[lig], tok[x], tok[y]) < 10:
        return None
    L, R = lr(lines)
    S = [g for g in tok if tok[g] >= 5 and g != lig]
    q = T.quintiles(tok, S)
    byq = defaultdict(list)
    for g in S:
        byq[q[g]].append(g)
    obs = seq_score(L, R, lig, x, y)
    ge = 0
    for _ in range(N):
        while True:
            a, b = random.choice(byq[q[x]]), random.choice(byq[q[y]])
            if a != b:
                break
        ge += seq_score(L, R, lig, a, b) >= obs
    base = (cosd(L[lig], L[x]) + cosd(R[lig], R[x])) / 2
    return obs, (ge + 1) / (N + 1), base, tok[lig]


def cluster_v(lines, signs, mode, k=8, seed=42, dims=20, posfeat=None):
    ctx = sorted({g for t in lines for g in t} | {'^', '$'})
    ci = {g: i for i, g in enumerate(ctx)}
    si = {g: i for i, g in enumerate(signs)}
    Lm = np.zeros((len(signs), len(ctx)))
    Rm = np.zeros((len(signs), len(ctx)))
    for t in lines:
        s = ['^'] + list(t) + ['$']
        for i in range(1, len(s) - 1):
            if s[i] in si:
                Lm[si[s[i]], ci[s[i - 1]]] += 1
                Rm[si[s[i]], ci[s[i + 1]]] += 1

    def ppmi(M):
        tot = M.sum()
        rs, cs = M.sum(1, keepdims=True), M.sum(0, keepdims=True)
        with np.errstate(divide='ignore', invalid='ignore'):
            p = np.log(M * tot / (rs * cs))
        p[~np.isfinite(p)] = 0
        p = np.maximum(p, 0)
        return p / (np.linalg.norm(p, axis=1, keepdims=True) + 1e-12)
    X = {'left': ppmi(Lm), 'right': ppmi(Rm)}.get(mode)
    if X is None:
        X = np.hstack([ppmi(Lm), ppmi(Rm)])
    U, S_, _ = np.linalg.svd(X, full_matrices=False)
    d = min(dims, len(signs) - 1)
    Z = U[:, :d] * S_[:d]
    Z = Z / (np.linalg.norm(Z, axis=1, keepdims=True) + 1e-12)
    if posfeat is not None:
        Z = np.hstack([Z, 0.5 * np.array([posfeat.get(g, (0, 0, 0)) for g in signs])])
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(50):
        C = Z[rng.choice(len(Z), k, replace=False)]
        for _ in range(200):
            lab = ((Z[:, None, :] - C[None]) ** 2).sum(2).argmin(1)
            newC = np.array([Z[lab == j].mean(0) if (lab == j).any() else C[j] for j in range(k)])
            if np.allclose(newC, C):
                break
            C = newC
        inert = ((Z - C[lab]) ** 2).sum()
        if best is None or inert < best[0]:
            best = (inert, lab.copy())
    return {g: int(best[1][i]) for g, i in si.items()}


def perm_labels(lab, signs):
    v = [lab[g] for g in signs]
    random.shuffle(v)
    return dict(zip(signs, v))


def main(path):
    A, B = T.sample('A'), T.sample('B')
    cat = cat_of()
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    say('# Twenty-third registered predictions: ligatures, and a validated classification')
    say()

    # G1-G6
    seq_vs_base = []
    for key, lig, x, y in LIGS:
        say('## %s %s as %s + %s' % (key, lig, x, y))
        ok = True
        rA = lig_test(A, lig, x, y)
        if rA is None:
            tok = Counter(g for t in A for g in t)
            say('- A: under 10 tokens (%s %d, %s %d, %s %d); not testable.' % (lig, tok[lig], x, tok[x], y, tok[y]))
            rec_(key, False)
            continue
        o, p, base, n_ = rA
        seq_vs_base.append(o > base)
        ok = p < 0.05
        say('- A: %s tokens %d; sequence score %.3f (modified-base score %.3f); p = %.4f.' % (lig, n_, o, base, p))
        rB = lig_test(B, lig, x, y)
        if rB is not None:
            o, p, base, n_ = rB
            ok = ok and p < 0.05
            say('- B: %s tokens %d; sequence score %.3f; p = %.4f.' % (lig, n_, o, p))
        else:
            say('- B: under 10 tokens; A decides.')
        rec_(key, ok)

    say('## G7 sequence rather than modification')
    say('- testable ligatures %d; sequence score above the modified-base score in %d.' % (
        len(seq_vs_base), sum(seq_vs_base)))
    rec_('G7', len(seq_vs_base) >= 5 and sum(seq_vs_base) >= 5)

    say('## G8 the pot-with-strokes signs are counts')
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    tabs = [r for r in intact if r['type'].startswith('TAB')]
    w = [len(r['flat']) <= 2 for r in tabs if {'702', '703'} & set(r['flat'])]
    o_ = [len(r['flat']) <= 2 for r in tabs if not ({'702', '703'} & set(r['flat'])) and not n700(r)]
    p = hyper_ge(sum(w), len(w) - sum(w), sum(o_), len(o_) - sum(o_))
    say('- tablets with 702 / 703: %d, of 1-2 signs %d; other non-count tablets %d of %d; p = %.4f.' % (
        len(w), sum(w), sum(o_), len(o_), p))
    rec_('G8', len(w) > 0 and p < 0.05 and sum(w) / len(w) > sum(o_) / len(o_))

    # C1
    tokA = Counter(g for t in A for g in t)
    tokB = Counter(g for t in B for g in t)
    content = sorted((g for g in tokA if tokA[g] >= 10 and g not in NUMS and g not in GRAMMAR and g not in FORMULA),
                     key=int)
    nums = sorted(g for g in tokA if tokA[g] >= 10 and g in NUMS)
    posA = defaultdict(Counter)
    for b, _ in T.names(A):
        for i, g in enumerate(b):
            posA[g]['last' if i == len(b) - 1 else ('first' if i == 0 else 'inside')] += 1
    posfeat = {g: tuple(c[w] / sum(c.values()) for w in ('first', 'inside', 'last')) for g, c in posA.items()}
    variants = [('V1 left only', dict(mode='left')), ('V2 right only', dict(mode='right')),
                ('V3 both + positions', dict(mode='both', posfeat=posfeat)), ('V4 both, k = 12', dict(mode='both', k=12))]
    say('## C1 a variant that passes the numeral check')
    chosen = None
    for name, kw in variants:
        lab1 = cluster_v(A, content + nums, **kw)
        allp = list(combinations(content + nums, 2))
        base = sum(lab1[a] == lab1[b] for a, b in allp) / len(allp)
        rate = sum(lab1[a] == lab1[b] for a, b in combinations(nums, 2)) / len(list(combinations(nums, 2)))
        say('- %s: numeral same-cluster rate %.2f, all pairs %.2f, ratio %.1f.' % (name, rate, base, rate / base))
        if rate / base >= 3 and chosen is None:
            chosen = (name, kw)
    say('- chosen: %s.' % (chosen[0] if chosen else 'none'))
    rec_('C1', chosen is not None)

    if chosen is None:
        for k in ('C2', 'C3', 'C4', 'C5'):
            say('## %s' % k)
            say('- no variant passed C1; not testable.')
            rec_(k, False)
    else:
        kw = chosen[1]
        lab = cluster_v(A, content, **kw)
        say('## C2 the chosen clusters predict B contexts')
        vecB = T.contexts(B)
        sb = [g for g in content if tokB[g] >= 10 and g in vecB]
        cosm = {(a, b): T.cos(vecB[a], vecB[b]) for a, b in combinations(sb, 2)}

        def st(l_):
            s_ = [v for (a, b), v in cosm.items() if l_[a] == l_[b]]
            d_ = [v for (a, b), v in cosm.items() if l_[a] != l_[b]]
            return sum(s_) / max(1, len(s_)) - sum(d_) / max(1, len(d_))
        obs = st(lab)
        ge = sum(st(perm_labels(lab, sb)) >= obs for _ in range(N))
        p = (ge + 1) / (N + 1)
        say('- difference %+.3f; p = %.4f.' % (obs, p))
        rec_('C2', obs > 0 and p < 0.05)
        say('## C3 the chosen clusters follow picture categories')
        catd = [g for g in content if g in cat]
        obs = T.mi([lab[g] for g in catd], [cat[g] for g in catd])
        ge = 0
        for _ in range(N):
            l2 = perm_labels(lab, catd)
            ge += T.mi([l2[g] for g in catd], [cat[g] for g in catd]) >= obs
        p = (ge + 1) / (N + 1)
        say('- MI %.3f bits over %d signs; p = %.4f.' % (obs, len(catd), p))
        rec_('C3', p < 0.05)
        say('## C4 human figures share a chosen cluster')
        hum = [g for g in catd if cat[g] == 'A']
        hp = list(combinations(hum, 2))
        st4 = lambda l_: sum(l_[a] == l_[b] for a, b in hp) / max(1, len(hp))
        obs = st4(lab)
        ge = sum(st4(perm_labels(lab, catd)) >= obs for _ in range(N))
        p = (ge + 1) / (N + 1)
        say('- human signs %s; same-cluster share %.2f; p = %.4f.' % (', '.join('%s:%d' % (g, lab[g]) for g in hum), obs, p))
        rec_('C4', p < 0.05)
        say('## C5 the chosen clusters differ in position in B')
        toks = [(g, 'last' if i == len(b) - 1 else ('first' if i == 0 else 'inside'))
                for b, _ in T.names(B) for i, g in enumerate(b) if g in lab]
        mi_pos = lambda l_: T.mi([l_[g] for g, _ in toks], [w for _, w in toks])
        obs = mi_pos(lab)
        ge = sum(mi_pos(perm_labels(lab, content)) >= obs for _ in range(N))
        p = (ge + 1) / (N + 1)
        say('- MI %.3f bits over %d tokens; p = %.4f.' % (obs, len(toks), p))
        rec_('C5', p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test23.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
