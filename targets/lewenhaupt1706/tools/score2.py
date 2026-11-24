"""Score n-grammes d'un décodage. Importé par measure2.py et calib.py.
decode(runs, key) -> liste de segments (code inconnu ou valeur hors alphabet = coupure).
score(lm, segs) -> log2-vraisemblance moyenne par caractère L ; N = (L - U) / (R - U)."""
import re, json, math, random
from ngram import norm, A
U = math.log2(1.0 / A)
def read_runs(files):
    runs, cur = [], []
    for f in files:
        for line in open(f, encoding='utf-8'):
            if line.startswith('#'): continue
            line = re.sub(r'\[[^\]]*\]', ' ', line.split('#')[0])
            for m in re.finditer(r'\{([^}]*)\}|(\d+)\??', line):
                if m.group(1) is not None:
                    if cur: runs.append(cur); cur = []
                else: cur.append(m.group(2))
    if cur: runs.append(cur)
    return runs
def decode(runs, key):
    segs = []
    for r in runs:
        cur = ''
        for c in r:
            if c in key: cur += norm(key[c])
            else:
                if cur: segs.append(cur)
                cur = ''
        if cur: segs.append(cur)
    return segs
def score(lm, segs):
    s = n = 0
    for g in segs:
        a, b = lm.ll(g); s += a; n += b
    return s / n if n else U
def permuted_keys(key, n, seed):
    codes = sorted(key, key=int); vals = [key[c] for c in codes]; rng = random.Random(seed); out = []
    for _ in range(n):
        v = vals[:]; rng.shuffle(v); out.append(dict(zip(codes, v)))
    return out
