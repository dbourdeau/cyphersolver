"""Soft-EM key rebuild for the R1874 cipher: align each paragraph's code groups to its decipherment.

Each group g emits a plaintext string s (0..L letters; 0 = null) with probability t[g][s]. Forward-backward over
(group i, letter j) with a diagonal band; counts are sharpened each round so every group settles on one value.
Input: pairs of (groups list, plaintext letters). Output: key dict g -> best string with its count.
"""
import math, re, sys, json
from collections import defaultdict

L = 4          # longest string a group may stand for
BAND = 120     # letters either side of the diagonal


def norm(s):
    return re.sub(r'[^a-z]', '', s.lower())


def run(pairs, iters=30, init=None, sharpen=(1.0, 3.0)):
    # t[g][s] probabilities; start: length prior 1:.25 2:.35 3:.2 4:.1 5-7 small, 0:.02
    lp = {0: .02, 1: .25, 2: .35, 3: .2, 4: .1, 5: .04, 6: .02, 7: .02}
    t = defaultdict(dict)
    if init:
        for g, s in init.items():
            t[g][s] = 5.0
    for it in range(iters):
        cnt = defaultdict(lambda: defaultdict(float))
        tot_ll = 0
        for G, P in pairs:
            n, m = len(G), len(P)
            r = m / max(n, 1)

            def e(g, s):
                d = t.get(g)
                if d and s in d:
                    return d[s]
                return 1e-4 * lp[len(s)] if it > 0 else lp[len(s)]

            def lo(i):
                return max(0, int(i * r) - BAND)

            def hi(i):
                return min(m, int(i * r) + BAND)
            F = [dict() for _ in range(n + 1)]
            F[0][0] = 0.0
            for i in range(n):
                g = G[i]
                row = F[i]
                nxt = F[i + 1]
                for j, fv in row.items():
                    for k in range(1, L + 1):
                        jj = j + k
                        if jj > m:
                            break
                        if jj < lo(i + 1) or jj > hi(i + 1):
                            continue
                        v = fv + math.log(e(g, P[j:jj]))
                        o = nxt.get(jj)
                        nxt[jj] = v if o is None else (max(o, v) + math.log1p(math.exp(-abs(o - v))))
            if m not in F[n]:
                print('no path', n, m, file=sys.stderr)
                continue
            Z = F[n][m]
            tot_ll += Z
            B = [dict() for _ in range(n + 1)]
            B[n][m] = 0.0
            for i in range(n - 1, -1, -1):
                g = G[i]
                for j, fv in F[i].items():
                    acc = None
                    for k in range(1, L + 1):
                        jj = j + k
                        bv = B[i + 1].get(jj)
                        if bv is None:
                            continue
                        s = P[j:jj]
                        v = math.log(e(g, s)) + bv
                        post = fv + v - Z
                        if post > -12:
                            cnt[g][s] += math.exp(post)
                        acc = v if acc is None else (max(acc, v) + math.log1p(math.exp(-abs(acc - v))))
                    if acc is not None:
                        B[i][j] = acc
        a = sharpen[0] + (sharpen[1] - sharpen[0]) * it / max(1, iters - 1)
        t = defaultdict(dict)
        for g, d in cnt.items():
            z = sum(v ** a for v in d.values())
            for s, v in d.items():
                p = v ** a / z
                if p > 1e-3:
                    t[g][s] = p
        print(f'iter {it} ll {tot_ll:.1f} sharpen {a:.2f}', file=sys.stderr)
    return t, cnt


def viterbi(G, P, key):
    """Best segmentation of P under a hard key (g -> set of strings); returns list of (g, s)."""
    n, m = len(G), len(P)
    INF = -1e18
    F = [dict() for _ in range(n + 1)]
    F[0][0] = (0.0, None)
    for i in range(n):
        for j, (fv, _) in F[i].items():
            opts = key.get(G[i], {})
            for s, p in opts.items():
                if P.startswith(s, j):
                    jj = j + len(s)
                    v = fv + math.log(p)
                    if v > F[i + 1].get(jj, (INF,))[0]:
                        F[i + 1][jj] = (v, (j, s))
            # unknown fallback
            for k in range(0, 4):
                jj = j + k
                if jj <= m:
                    v = fv + math.log(1e-6)
                    if v > F[i + 1].get(jj, (INF,))[0]:
                        F[i + 1][jj] = (v, (j, '?' + P[j:jj]))
    out = []
    j = m
    for i in range(n, 0, -1):
        if j not in F[i]:
            return None
        _, (pj, s) = F[i][j]
        out.append((G[i - 1], s))
        j = pj
    return out[::-1]
