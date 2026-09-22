"""Homophonic annealer for R8499: each sign type -> one letter, scored with lang en-1640s (no spaces)."""
import os, sys, re, random, collections, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
FIXED = {'C.': 'and', 'C:': 'and'}


TRAIL = {'/', '+', '0', 'q', 'r', '2', 'N', 'y', 'h'}   # signs whose trailing dot is part of the glyph


def runs_dotted(path=os.path.join(HERE, 'transcription.txt')):
    out = []
    for r0 in runs(path, drop=()):
        r = [t for j, t in enumerate(r0) if t != ':' and not (t == '.' and j > 0 and r0[j - 1] == ':')]
        toks, i = [], 0
        while i < len(r):
            t = r[i]
            if t == '.':
                i += 1; continue
            pre = i > 0 and r[i - 1] == '.' and not (i > 1 and r[i - 2] in TRAIL)
            post = i + 1 < len(r) and r[i + 1] == '.' and t not in TRAIL
            toks.append(('.' if pre else '') + t + ('.' if post else ''))
            i += 1
        out.append(toks)
    return out


def runs(path=os.path.join(HERE, 'transcription.txt'), drop=('.', ':')):
    out, cur = [], []
    for l in open(path, encoding='utf8'):
        if not l.startswith('p'):
            continue
        body = l.split(' ', 1)[1]
        for part in re.split(r'(\[[^\]]*\])', body):
            if part.startswith('['):
                if cur: out.append(cur); cur = []
                continue
            cur += [t for t in part.split() if t not in drop]
    if cur: out.append(cur)
    return out


def main(seed=0, iters=200000, order=5, W=1.0):
    m = lm.load('en-1640s', order=order, spaces=False)
    A, lp = m.A, m.lp
    R = runs()
    types = sorted({t for r in R for t in r if t not in FIXED})
    ti = {t: i for i, t in enumerate(types)}
    # build flat stream with fixed expansions; positions per type
    stream, owner = [], []
    for r in R:
        for t in r:
            if t in FIXED:
                for ch in FIXED[t]:
                    stream.append(m.index[ch]); owner.append(-1)
            else:
                stream.append(0); owner.append(ti[t])
        stream.append(-1); owner.append(-2)   # run break
    stream = np.array(stream); owner = np.array(owner)
    brk = owner == -2
    rng = random.Random(seed)
    # init by frequency
    freq = collections.Counter(t for r in R for t in r if t in ti)
    eng = 'etaoinshrdlucmfwygpbkqx'
    key = np.array([m.index[rng.choice('etaoinshrdlu')] for _ in types])
    def decode(key):
        x = stream.copy()
        mask = owner >= 0
        x[mask] = key[owner[mask]]
        return x
    k = order
    def score(key):
        x = decode(key)
        s = 0.0
        # score each run separately
        idx = np.where(brk)[0]
        start = 0
        for e in idx:
            seg = x[start:e]
            if len(seg) >= k:
                ctx = np.zeros(len(seg) - k + 1, dtype=np.int64)
                for j in range(k):
                    ctx = ctx * A + seg[j:len(seg) - k + 1 + j]
                s += lp[ctx].sum()
            start = e + 1
        return s
    txt0 = lm.norm(open(os.path.join(HERE, '..', 'lang', 'corpora', 'en-1640s-history.txt'), encoding='utf8', errors='replace').read()[:2000000], 'early', spaces=False)
    fx = m.encode(txt0); fexp = np.bincount(fx, minlength=A) / len(fx) + 1e-4
    base_score = score
    N = int((owner >= 0).sum()) + int((owner == -1).sum())
    def score(key, W=W):
        x = decode(key); x = x[x >= 0]
        n = np.bincount(x, minlength=A)
        pen = ((n - N * fexp) ** 2 / (N * fexp)).sum()
        return base_score(key) - W * pen
    cur = score(key); best = (cur, key.copy())
    T0 = 30.0
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.5
        i = rng.randrange(len(types))
        old = key[i]
        key[i] = rng.randrange(A)
        if key[i] == old: continue
        new = score(key)
        if new >= cur or rng.random() < np.exp((new - cur) / T):
            cur = new
            if cur > best[0]: best = (cur, key.copy())
        else:
            key[i] = old
    key = best[1]
    x = decode(key)
    txt = ''.join(' ' if v < 0 else m.alpha[v] for v in x)
    return best[0], {t: m.alpha[key[ti[t]]] for t in types}, txt


if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    it = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
    s, key, txt = main(seed, it)
    print(s)
    print(txt[:1500])
    json.dump({'score': float(s), 'key': key, 'text': txt}, open(os.path.join(HERE, f'run_{seed}.json'), 'w'))
