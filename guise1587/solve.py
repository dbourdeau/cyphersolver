"""Seeded homophonic anneal over glyph labels: each glyph type gets a letter (or null), each
nomenclator group a word. Seed = Lasry's 2022 key (GL_BnFfr15564.png) as read onto my labels."""
import os, sys, random, math, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lang import lm

M = lm.load('fr-1600-letters', order=5, spaces=False)
LET = list('abcdefghilmnopqrstuxyz')
WORDS = ['de', 'au', 'la', 'et', 'des', 'que', 'les', 'mon', 'le', 'qui', 'pour', 'par', 'vous', 'nous',
         'ils', 'leur', 'son', 'ne', 'en', 'se', 'ce', 'est', 'sa', 'si', 'il', 'un', 'a']
SEED = {'n': 'e', '6': 'e', 'u': 'e', 'l': 's', ':': 't', '#': 'u', 'C': 'l', 'm': 'n', 'x': 'n', '%': 's',
        ')': 's', 'p': 'c', '1': 'c', 'A': 'o', 'T': 'l', 'z': 'i', 'D': 'r', '9': 'd', '3': 'd', '7': 'o',
        '2': 'f', '4': 'c', 'h': 'i', 'Z': 'p', 'F': 'u', 'I': 'b', 'P': 'd', 'S': 's', 'g': 'q', 'w': 'h',
        'M': 'g', '8': 'n', 'j': '', 'y': 'f', 'X': 't', 'd': 'd', 'R': 'q', 'v': 'x', 'Y': 'x', '"': 'h',
        '*': 'u', 'o': 'o', 'k': 'e', 'f': 'e', '&': 's', 'N': 'e',
        '[ffuy]': 'la', '[fuy]': 'la', '[ff6]': 'qui', '[fbu]': 'les', '[fu]': 'et', '[ffm]': 'que',
        '[fff]': 'vous', '[ffff]': 'leur', '[ffu]': 'le', '[ffuu]': 'le', '[ffbm]': 'nous', '[bw]': 'les'}

def load(path):
    toks = []
    for ln in open(path, encoding='utf8'):
        if ln.startswith('#') or not ln.strip():
            continue
        toks += re.findall(r'\[[^\]]+\]|\S', ln)
    return toks

def opts(t):
    return WORDS + [''] if t.startswith('[') else LET + ['']

def text(toks, k):
    return ''.join(k[t] for t in toks)

def score(toks, k):
    s = text(toks, k)
    nulls = sum(1 for t in toks if k[t] == '')
    return M.score_idx(M.encode(s)) - 3.0 * nulls if s else -1e9

def anneal(toks, seed, iters=60000, T0=3.0, fixed=()):
    k = dict(seed)
    types = [t for t in sorted(set(toks)) if t not in fixed]
    cur = score(toks, k); best = (cur, dict(k))
    for i in range(iters):
        T = T0 * (1 - i / iters) + 0.05
        t = random.choice(types); old = k[t]
        k[t] = random.choice(opts(t))
        s = score(toks, k)
        if s >= cur or random.random() < math.exp((s - cur) / T):
            cur = s
            if s > best[0]: best = (s, dict(k))
        else:
            k[t] = old
    return best

if __name__ == '__main__':
    toks = load(sys.argv[1])
    seed = {t: SEED.get(t, 'e' if not t.startswith('[') else 'de') for t in set(toks)}
    print('seed :', text(toks, seed))
    print('per-char', M.per_char(text(toks, seed)))
    best = None
    for r in range(int(sys.argv[2]) if len(sys.argv) > 2 else 4):
        b = anneal(toks, seed)
        print(r, round(b[0]), text(toks, b[1])[:200])
        if best is None or b[0] > best[0]: best = b
    k = best[1]
    print('BEST:', text(toks, k))
    print({t: k[t] for t in sorted(k) if k[t] != seed[t]})
