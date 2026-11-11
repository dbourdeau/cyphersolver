# Alignement itératif chiffre <-> gloses (TRAIN seulement) ; construit une clé candidate.
# usage : python3 align.py [n_iter] [--show]
import sys, collections, json, os
from lib import train_passages, norm, D

def lev(a, b):
    if a == b: return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

def items_of(p):
    it = []; g = ''
    for lid, toks, gl in p['lines']:
        for k, v in toks:
            if k == 'n': it.append(('n', v))
            else:
                t = norm(v)
                if t: it.append(('t', t))
        g += norm(gl)
    return it, g

def align(it, g, K):
    n, m = len(it), len(g); INF = 1e9
    dp = [[INF] * (m + 1) for _ in range(n + 1)]; bk = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            c = dp[i][j]
            if c >= INF: continue
            if j < m and c + 1 < dp[i][j + 1]: dp[i][j + 1] = c + 1; bk[i][j + 1] = (i, j, None)
            if i == n: continue
            kind, v = it[i]
            if c + 1 < dp[i + 1][j]: dp[i + 1][j] = c + 1; bk[i + 1][j] = (i, j, None)
            if kind == 't' or (kind == 'n' and v in K):
                val = v if kind == 't' else K[v]
                L = len(val)
                for k in range(max(1, L - 2), L + 3):
                    if j + k > m: break
                    cc = c + lev(val, g[j:j + k]) * (0.5 if kind == 't' else 1.0)
                    if cc < dp[i + 1][j + k]: dp[i + 1][j + k] = cc; bk[i + 1][j + k] = (i, j, g[j:j + k])
            else:
                if j + 1 <= m and c + 0.7 < dp[i + 1][j + 1]: dp[i + 1][j + 1] = c + 0.7; bk[i + 1][j + 1] = (i, j, g[j:j + 1])
                if len(v) >= 3:
                    for k in range(2, 26):
                        if j + k > m: break
                        if c + 1.6 < dp[i + 1][j + k]: dp[i + 1][j + k] = c + 1.6; bk[i + 1][j + k] = (i, j, g[j:j + k])
    # backtrack
    i, j = n, m; asg = []
    while (i, j) != (0, 0):
        pi, pj, s = bk[i][j]
        if pi == i - 1 and s is not None and it[pi][0] == 'n': asg.append((it[pi][1], s, pi))
        i, j = pi, pj
    return dp[n][m], asg[::-1]

def build(K0=None, n_iter=6, show=False):
    ps = [p for p in train_passages() if not p['nogloss']]
    K = dict(K0 or {})
    for it_ in range(n_iter):
        votes = collections.defaultdict(collections.Counter); tot = 0
        for p in ps:
            it, g = items_of(p)
            if not g or not it: continue
            c, asg = align(it, g, K); tot += c
            for num, s, _ in asg: votes[num][s] += 1
        newK = {}
        for num, cnt in votes.items():
            v, c = cnt.most_common(1)[0]
            if len(num) <= 2 and len(v) > 2: continue
            newK[num] = v
        print(f'iter {it_}: coût total {tot:.1f}, {len(newK)} nombres', file=sys.stderr)
        if newK == K: break
        K = newK
    return K, votes

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    K, votes = build(n_iter=n)
    for num in sorted(votes, key=int):
        print(num, K.get(num, ''), dict(votes[num].most_common(4)), sep='\t')
