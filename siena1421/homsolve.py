"""Ciphertext-only homophonic anneal for the Siena slips.

Tokens are whitespace-separated glyph names in a transcript file (lines starting '#' ignored; clear words in
[brackets] break the cipher into runs). Each glyph maps to one plaintext letter (homophones allowed). Score =
n-gram log-prob (no spaces) + a unigram KL penalty against the language's letter frequencies.

usage: python homsolve.py transcripts/r4794.txt [model] [iters] [restarts] [fix=GLYPH:x,...] [skip=G1,G2]
"""
import sys, os, re, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

args = [a for a in sys.argv[1:] if '=' not in a]
opts = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
path = args[0]
model = args[1] if len(args) > 1 else 'it-cinquecento'
ITERS = int(args[2]) if len(args) > 2 else 60000
RESTARTS = int(args[3]) if len(args) > 3 else 20
ORDER = int(opts.get('order', 4))
KLW = float(opts.get('klw', 2.0))
M = lm.load(model, order=ORDER, spaces=False)
A = len(M.alpha)
LETTERS = [c for c in M.alpha if c.isalpha()]
FREQ = {'it-cinquecento': 'eaoinlrtscdpumghfbqvz', 'la': 'eiatusnrmocldpqbgfvh'}.get(model, 'eaoinlrtscdpumghfbqvz')
ENG = np.array([11.8, 11.7, 9.8, 10.1, 6.9, 6.5, 6.4, 5.6, 5.0, 4.5, 3.7, 3.0, 5.1, 2.5, 1.6, 1.1, 1.0, 0.9, 0.5, 0.9, 0.5])
freq = np.full(A, 0.002)
for c, f in zip(FREQ, ENG / ENG.sum()):
    if c in M.index: freq[M.index[c]] = f
freq /= freq.sum()

skip = set(opts.get('skip', '').split(',')) - {''}
runs = []
for line in open(path, encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    for part in re.split(r'\[[^\]]*\]', line):
        toks = [t for t in part.split() if t not in skip and not t.startswith('{')]
        if toks: runs.append(toks)
glyphs = sorted({t for r in runs for t in r})
gi = {g: i for i, g in enumerate(glyphs)}
x = np.concatenate([np.array([gi[t] for t in r]) for r in runs])
bounds = np.cumsum([len(r) for r in runs])[:-1]
cnt = np.bincount(x, minlength=len(glyphs)).astype(float)
N = cnt.sum()
valid = np.ones(len(x) - ORDER + 1, bool)
for b in bounds:
    valid[max(0, b - ORDER + 1):b] = False
letters = [M.index[c] for c in LETTERS]
fixed = {}
for kv in opts.get('fix', '').split(','):
    if ':' in kv:
        g, c = kv.split(':'); fixed[gi[g]] = M.index[c]


def score(key):
    y = key[x]
    ctx = np.zeros(len(y) - ORDER + 1, dtype=np.int64)
    for j in range(ORDER): ctx = ctx * A + y[j:len(y) - ORDER + 1 + j]
    s = M.lp[ctx][valid].sum()
    obs = np.bincount(key, weights=cnt, minlength=A) / N
    m = obs > 0
    return s - KLW * N * float((obs[m] * np.log(obs[m] / freq[m])).sum())


rnd = random.Random(int(opts.get('seed', 1)))
free = [i for i in range(len(glyphs)) if i not in fixed]
results = []
for r in range(RESTARTS):
    key = np.array([rnd.choice(letters) for _ in glyphs])
    for i, c in fixed.items(): key[i] = c
    cur = score(key); T = 8.0; best = (cur, key.copy())
    for it in range(ITERS):
        i = rnd.choice(free); old = key[i]; key[i] = rnd.choice(letters)
        s = score(key)
        if s >= cur or rnd.random() < math.exp((s - cur) / T): cur = s
        else: key[i] = old
        if cur > best[0]: best = (cur, key.copy())
        T = max(0.2, T * (1 - 6.0 / ITERS))
    results.append(best)
    dec = ' | '.join(''.join(M.alpha[best[1][gi[t]]] for t in rr) for rr in runs)
    print('%3d %9.1f  %s' % (r, best[0], dec[:200]), flush=True)
results.sort(key=lambda z: -z[0])
sc, key = results[0]
print('\nbest', round(sc, 1), 'per-char', round(sc / N, 3))
print(' '.join('%s=%s' % (g, M.alpha[key[gi[g]]]) for g in glyphs))
for rr in runs:
    print(''.join(M.alpha[key[gi[t]]] for t in rr))
