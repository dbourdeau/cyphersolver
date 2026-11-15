#!/usr/bin/env python3
"""Second aligner: monotone alignment scored by log-likelihood ratio log P(w|g)/P(w) (leave-one-despatch-out),
so that matching a rare word counts for much more than matching 'the'. Crib despatches only."""
import re, sys, json, math
from collections import Counter, defaultdict
from align import build, same, stem, norm

ALPHA = 0.7
def key(w): return stem(w)

def prep(D):
    uni = Counter(key(w) for d in D for w, _ in d['W'])
    N = sum(uni.values())
    for d in D:
        d['K'] = [key(w) for w, _ in d['W']]
    return {k: v/N for k, v in uni.items()}

def align(d, T, P, lam_line, lam_diag, gapg=1.4, gapw=1.6, edge=0.25):
    G, K = d['G'], d['K']; I, J = len(G), len(K)
    W = d['W']
    NEG = -1e9
    S = [[NEG]*(J+1) for _ in range(I+1)]; B = [[None]*(J+1) for _ in range(I+1)]
    S[0][0] = 0
    for i in range(I+1):
        Si = S[i]
        for j in range(J+1):
            cur = Si[j]
            if cur <= NEG/2: continue
            if i < I and j < J:
                g, gl, ul = G[i]; k = K[j]; p = P[k]
                t = T.get(g)
                if t:
                    n = sum(t.values()); c = t.get(k, 0)
                    s = math.log(((c + ALPHA*p)/(n + ALPHA))/p)
                else: s = 0.0
                s -= lam_line * abs(gl - W[j][1])
                s -= lam_diag * abs((i+0.5)/I - (j+0.5)/J) * 20
                if ul: s -= 2.5
                v = cur + s
                if v > S[i+1][j+1]: S[i+1][j+1] = v; B[i+1][j+1] = 'M'
            if i < I:
                ul = G[i][2]
                cost = 0.2 if ul else (edge if (j == 0 or j == J) else gapg)
                v = cur - cost
                if v > S[i+1][j]: S[i+1][j] = v; B[i+1][j] = 'G'
            if j < J:
                v = cur - gapw
                if v > Si[j+1]: Si[j+1] = v; B[i][j+1] = 'W'
    i, j = I, J; out = []
    while i or j:
        b = B[i][j]
        if b == 'M': out.append(['M', i-1, j-1]); i -= 1; j -= 1
        elif b == 'G': out.append(['G', i-1, None]); i -= 1
        else: out.append(['W', None, j-1]); j -= 1
    out.reverse()
    return out

def table(D, A, skip=None):
    T = defaultdict(Counter)
    for k, d in enumerate(D):
        if k == skip or A[k] is None: continue
        for op, i, j in A[k]:
            if op == 'M': T[d['G'][i][0]][d['K'][j]] += 1
    return T

def run(D, P, iters=25, log=sys.stderr):
    A = [align(d, {}, P, d['lam_line'], d['lam_diag']) for d in D]
    for it in range(iters):
        changed = 0
        f = max(0.3, 1 - it/8.0)
        for k, d in enumerate(D):
            T = table(D, A, skip=k)
            new = align(d, T, P, d['lam_line']*f, d['lam_diag']*f)
            if new != A[k]: changed += 1; A[k] = new
        print('iter', it, 'changed', changed, file=log)
        if not changed: break
    return A

def setpriors(D):
    for d in D:
        if any(x in d['file'] for x in ('ff132', 'ff185', 'ff219', 'No33', 'No34', 'n36')):
            d['lam_line'] = 0.0; d['lam_diag'] = 0.6
        else:
            d['lam_line'] = 0.5; d['lam_diag'] = 0.0

def summarize(D, A, top=0):
    T = table(D, A)
    multi = {g: t for g, t in T.items() if sum(t.values()) >= 2}
    tot = sum(sum(t.values()) for t in multi.values()); best = sum(max(t.values()) for t in multi.values())
    firm = {g: t for g, t in multi.items() if max(t.values()) >= 2 and max(t.values())/sum(t.values()) >= 0.6}
    print('groups with a word: %d; with >=2: %d; consistency %d/%d = %.3f; firm (top>=2, share>=0.6): %d' % (len(T), len(multi), best, tot, best/tot, len(firm)))
    return T, firm

if __name__ == '__main__':
    D = build(); P = prep(D); setpriors(D)
    A = run(D, P)
    json.dump({'A': A, 'files': [d['file'] for d in D]}, open('align2_out.json', 'w'))
    T, firm = summarize(D, A)
    from collections import Counter as C
    print(C(max(t, key=t.get) for t in firm.values()).most_common(50))
