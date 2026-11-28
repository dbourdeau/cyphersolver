"""Per-sign score of a key on a run of cipher lines against a stretch of Kervyn's text (used for the held-out test
and, separately, for the in-sample check on build lines). Decode each token with the key (single tokens only; a
value may be one or two letters), align the decoded letters with the reference letters by edit distance, and count
a token as right when all its letters fall on equal reference letters. Not scored: '?', dotted numbers, tokens with
no value in the key, and tokens aligned into a bracketed word or a gap of the print."""
import random
def decode_units(toks, key):
    out = []   # (token, letters or None)
    for t in toks:
        if t == '?' or t.startswith('#') or t not in key: out.append((t, None))
        else: out.append((t, key[t]))
    return out
def score(toks, key, ref_units):
    dec = decode_units(toks, key)
    a = []; owner = []
    for k, (t, v) in enumerate(dec):
        if v:
            for ch in v: a.append(ch); owner.append(k)
    b = []; bmask = []
    for u in ref_units:
        if len(u) == 1: b.append(u); bmask.append(True)
        else:
            if u != '{GAP}':
                for ch in u.strip('{}'): b.append(ch); bmask.append(False)
            else: b.append('#'); bmask.append(False)
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): D[i][0] = i
    for j in range(1, m + 1): D[0][j] = j
    for i in range(1, n + 1):
        ai = a[i-1]; Di = D[i]; Dp = D[i-1]
        for j in range(1, m + 1):
            Di[j] = min(Dp[j] + 1, Di[j-1] + 1, Dp[j-1] + (0 if ai == b[j-1] else 1))
    ok = [True] * n; scorable = [True] * n; i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + (0 if a[i-1] == b[j-1] else 1):
            ok[i-1] = a[i-1] == b[j-1]; scorable[i-1] = bmask[j-1]; i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i-1][j] + 1: ok[i-1] = False; i -= 1
        else: j -= 1
    tok_ok = {}; tok_sc = {}
    for p, k in enumerate(owner):
        tok_ok[k] = tok_ok.get(k, True) and ok[p]; tok_sc[k] = tok_sc.get(k, True) and scorable[p]
    scored = [k for k in tok_ok if tok_sc[k]]
    right = sum(tok_ok[k] for k in scored)
    return right, len(scored), sum(1 for t, v in dec if v is None)
def controls(toks, key, ref_units, n=200, seed=1577):
    rng = random.Random(seed); signs = sorted(key); vals = [key[s] for s in signs]; res = []
    for _ in range(n):
        rng.shuffle(vals); kk = dict(zip(signs, vals)); r, s, _ = score(toks, kk, ref_units); res.append(r / s if s else 0)
    return res
