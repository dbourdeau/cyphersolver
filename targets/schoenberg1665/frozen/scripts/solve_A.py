# Recherche de clé sur A SEULEMENT (L1-L5). Recuit simulé, score = trigrammes de mots du lexique + bonus mots entiers.
import sys, gzip, json, math, random, os
sys.path.insert(0, os.path.dirname(__file__)); import parse
LEX = sys.argv[2]; lang = sys.argv[3]; seed = int(sys.argv[4])
d = {w: c for w, c in json.load(gzip.open(LEX)).items() if c >= 5 and w.isalpha() and w.isascii()}
from collections import Counter
tri = Counter(); bi = Counter()
for w, c in d.items():
    s = '^^' + w + '$'
    for i in range(len(s) - 2): tri[s[i:i+3]] += c; bi[s[i:i+2]] += c
def lp(s):
    s = '^^' + s + '$'; t = 0
    for i in range(len(s) - 2): t += math.log((tri[s[i:i+3]] + 0.1) / (bi[s[i:i+2]] + 2.6))
    return t
A = parse.words(sys.argv[1], set(range(1, 6)))
cl = sorted(set(''.join(A))); P = 'abcdefghiklmnopqrstuwxyz'  # 24 lettres (i/j, u/v confondus)
def dec(k, w): return ''.join(k[c] for c in w)
def score(k):
    t = 0
    for w in A:
        p = dec(k, w); t += lp(p) + (3 * math.log(d[p]) if p in d and len(p) > 1 else 0)
    return t
rng = random.Random(seed); best = None
for r in range(30):
    vals = rng.sample(P, len(cl)); k = dict(zip(cl, vals)); s = score(k); T = 20.0
    for it in range(20000):
        k2 = dict(k); a = rng.choice(cl)
        if rng.random() < 0.5:
            b = rng.choice(cl); k2[a], k2[b] = k2[b], k2[a]
        else:
            used = set(k2.values()); free = [x for x in P if x not in used]
            if not free: continue
            k2[a] = rng.choice(free)
        s2 = score(k2)
        if s2 > s or rng.random() < math.exp((s2 - s) / T): k, s = k2, s2
        T = max(0.2, T * 0.9997)
    if best is None or s > best[0]: best = (s, k)
    print(round(s, 1), ' '.join(dec(k, w) for w in A), flush=True)
print('BEST', round(best[0], 1), ''.join(best[1][c] for c in cl), cl)
