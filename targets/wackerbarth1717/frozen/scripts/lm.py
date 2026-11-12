# Critères linguistiques L1/L2/L3 (PROTOCOLE-AVENANT-2 §4). Modèle 4-grammes de caractères interpolé.
import os, sys, math, json, collections, re, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import D, REL, norm, tokens, read_releve
COM = os.path.join(os.path.dirname(D), 'PISTES-AUTO/fable-api/lots/lot2/_communs/')
A = 'abcdefghiklmnopqrstuxyzjvw'
W = (0.05, 0.15, 0.3, 0.5); KADD = 0.1

class LM:
    def __init__(self):
        txt = ''
        for f in ('corpus-fr-henri4-extrait-1.9Mo.txt', 'corpus-fr-gutenberg-extrait-1.9Mo.txt'):
            txt += norm(open(COM + f, encoding='utf-8', errors='ignore').read()).replace('#', '')
        self.C = [collections.Counter() for _ in range(5)]
        for n in range(1, 5):
            c = self.C[n]
            for i in range(len(txt) - n + 1): c[txt[i:i + n]] += 1
        self.H = [collections.Counter() for _ in range(5)]  # contextes
        for n in range(2, 5):
            for g, v in self.C[n].items(): self.H[n][g[:-1]] += v
        self.N1 = sum(self.C[1].values()); self.V = 26; self.cache = {}
    def p(self, ctx, ch):
        key = (ctx, ch)
        if key in self.cache: return self.cache[key]
        pr = W[0] * (self.C[1][ch] + KADD) / (self.N1 + KADD * self.V)
        for n in range(2, 5):
            h = ctx[-(n - 1):] if len(ctx) >= n - 1 else None
            if h is None: pr += W[n - 1] * (self.C[1][ch] + KADD) / (self.N1 + KADD * self.V); continue
            pr += W[n - 1] * (self.C[n][h + ch] + KADD) / (self.H[n][h] + KADD * self.V)
        self.cache[key] = pr; return pr
    def L1(self, s):
        tot = 0.0; n = 0; ctx = ''
        for ch in s:
            if ch == '#': ctx = ''; continue
            tot += math.log(self.p(ctx, ch)); n += 1; ctx = (ctx + ch)[-3:]
        return tot / max(1, n)
    def L3(self, s):
        tot = 0.0; n = 0
        for seg in s.split('#'):
            if len(seg) < 4: continue
            ctx = ''
            for ch in seg: tot += math.log(self.p(ctx, ch)); n += 1; ctx = (ctx + ch)[-3:]
        return tot / max(1, n)

def make_L2():
    LEX = {w for w in json.load(open(COM + 'lexique-fr-cyphersolver.json')) if len(w) >= 4}
    LEX |= {w.strip() for w in open(os.path.join(D, 'LEXIQUE-AJOUT-TRAIN.txt')) if len(w.strip()) >= 4}
    ML = max(map(len, LEX))
    def cover(s):
        n = len(s); best = [0] * (n + 1)
        for i in range(n):
            if best[i + 1] < best[i]: best[i + 1] = best[i]
            for j in range(i + 4, min(n, i + ML) + 1):
                if s[i:j] in LEX and best[j] < best[i] + j - i: best[j] = best[i] + j - i
        return best[n] / max(1, n)
    return cover

def load_key(name):
    K = {}
    for line in open(os.path.join(D, name), encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        f = line.rstrip('\n').split('\t')
        K[f[0]] = norm(f[1].replace('[', '').replace(']', ''))
    return K

def dec(K, ns): return ''.join(K.get(n, '#') for n in ns)

def perms(K, rnd, n=200):
    codes = list(K); vals = list(K.values()); out = []
    for _ in range(n):
        v = vals[:]; rnd.shuffle(v); out.append(dict(zip(codes, v)))
    return out

def stats(f, K, ns, seed=1717):
    s = f(dec(K, ns)); t = [f(dec(k, ns)) for k in perms(K, random.Random(seed))]
    m = sum(t) / len(t); sd = (sum((x - m) ** 2 for x in t) / len(t)) ** 0.5
    return dict(score=s, moy=m, sd=sd, max=max(t), z=(s - m) / sd if sd else 0, gap=s - max(t))
