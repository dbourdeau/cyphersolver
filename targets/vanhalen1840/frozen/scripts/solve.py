"""Recuit sur l'apprentissage T seul (vanhalen-1840). python3 -I solve.py transcription.txt es.json.gz [inj] [seed]"""
import sys, gzip, json, math, random, unicodedata
from collections import defaultdict
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); return ''.join(c for c in s if 'a' <= c <= 'z' or c == ' ')
lexd = json.load(gzip.open(sys.argv[2], 'rt', encoding='utf-8'))
N = 4; cnt = defaultdict(float); ctx = defaultdict(float)
for w, c in lexd.items():
    if c < 3: continue
    w = ' ' + norm(w) + ' '
    if len(w) < 3: continue
    wt = math.log(1 + c)
    for i in range(len(w)):
        g = w[max(0, i - N + 1):i + 1]
        for k in range(1, len(g) + 1):
            cnt[g[-k:]] += wt; ctx[g[-k:-1]] += wt
AL = 'abcdefghijlmnopqrstuvxyz'
def lp(h, c):
    # interpolated backoff
    p = 0.0; lam = 1.0
    for k in range(min(len(h), N - 1), -1, -1):
        hh = h[len(h) - k:] if k else ''
        num = cnt.get(hh + c, 0); den = ctx.get(hh, 0)
        if den > 0:
            p += lam * 0.7 * num / den; lam *= 0.3
    return math.log(p + lam * 1e-4)
cache = {}
def score(s):
    t = 0.0; h = ' '
    for c in s:
        k = (h[-3:], c)
        if k not in cache: cache[k] = lp(h[-3:], c)
        t += cache[k]; h += c
    return t
runs = []
for l in open(sys.argv[1]):
    if l.startswith('#'): continue
    sid, p, n = l.rstrip('\n').split('\t')
    if p != 'T': continue
    toks = [x.split('|')[0].rstrip('?') for x in n.replace('58|5.8', '58').replace('5|4', '5').split('.')]
    runs.append(toks)
inj = len(sys.argv) > 3 and sys.argv[3] == 'inj'
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
rng = random.Random(seed)
syms = sorted({t for r in runs for t in r})
def dec(k): return ' | '.join(''.join(k[t] for t in r) for r in runs)
def sc(k): return sum(score(''.join(k[t] for t in r).replace('_', ' ')) for r in runs)
fixed = {}
if '70' in syms: fixed['70'] = '_'
import os
for kv in os.environ.get('FIX','').split(','):
    if kv: a, b = kv.split('='); fixed[a] = b
freq = 'eaosnrildtucmpbgvyqhfzjx'
k = {s: fixed.get(s, rng.choice(freq[:12])) for s in syms}
if inj:
    pool = list(freq); rng.shuffle(pool)
    for i, s in enumerate([s for s in syms if s not in fixed]): k[s] = pool[i] if pool[i] not in fixed.values() else pool[(i+len(syms))%len(pool)]
cur = sc(k); best = (cur, dict(k)); T = 3.0
for it in range(60000):
    T = 3.0 * (1 - it / 60000) + 0.05
    s = rng.choice([s for s in syms if s not in fixed]); old = k[s]
    if inj:
        s2 = rng.choice([x for x in syms if x not in fixed and x != s]); k[s], k[s2] = k[s2], k[s]
    else:
        k[s] = rng.choice(AL)
    new = sc(k)
    if new >= cur or rng.random() < math.exp((new - cur) / T): cur = new
    else:
        if inj: k[s2], k[s] = k[s], old
        else: k[s] = old
    if cur > best[0]: best = (cur, dict(k))
print(round(best[0] / sum(len(r) for r in runs), 3), dec(best[1]).replace('_', ' '))
print(' '.join(f'{s}={best[1][s]}' for s in sorted(syms, key=int)))
