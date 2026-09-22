"""Homophonic annealer for R9407 (System A' hand), numpy-scored against lang de-1500s (order 5, no spaces).
Reads transcription.txt cipher lines (NN text), drops [clear] runs, ':' and '?'.
  python r9407/solve.py [--iters N] [--restarts R] [--fix a=b,...] [--keyfile K] [--out K] [--seed S]
Each sign maps to one letter of the model alphabet (a-z less j, v) or '_' (null)."""
import argparse, math, random, re, sys, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

ap = argparse.ArgumentParser()
ap.add_argument('--iters', type=int, default=200000); ap.add_argument('--restarts', type=int, default=4)
ap.add_argument('--fix', default=''); ap.add_argument('--seed', type=int, default=1)
ap.add_argument('--model', default='de-1500s'); ap.add_argument('--file', default=os.path.join(HERE, 'transcription.txt'))
ap.add_argument('--out', default=''); ap.add_argument('--keyfile', default=''); ap.add_argument('--nonull', action='store_true')
ap.add_argument('--pages', default=''); ap.add_argument('--kl', type=float, default=1.0); ap.add_argument('--null', action='store_true')
a = ap.parse_args()
random.seed(a.seed); np.random.seed(a.seed)
M = lm.load(a.model, spaces=False)
ALPHA = M.alpha; A = M.A; K = M.order

def read_lines(path):
    out, page = [], ''
    for l in open(path, encoding='utf8'):
        if l.startswith('=='): page = l.split()[1]; continue
        m = re.match(r'(\d\d)\s+(.*)', l.rstrip('\n'))
        if not m: continue
        if a.pages and page not in a.pages.split(','): continue
        s = re.sub(r'\[[^\]]*\]', ' ', m.group(2)).replace(':', '').replace('?', '')
        out.append((page + '.' + m.group(1), s))
    return out

lines = read_lines(a.file)
lines = [(n, s.replace('jo', 'J').replace('mg', 'M')) for n, s in lines]
seq = [c for _, s in lines for c in s if c != ' ']
toks = sorted(set(seq)); tid = {t: i for i, t in enumerate(toks)}
S = np.array([tid[c] for c in seq]); N = len(S)
from collections import Counter
cnt = Counter(seq)
LET = list(ALPHA) + (['_'] if a.null else []) + ['ch', 'fg']
NUL = len(ALPHA)
V = np.full((len(LET), 2), -1)
for i, v in enumerate(LET):
    if v != '_':
        for j, ch in enumerate(v): V[i, j] = ALPHA.index(ch)
A_INIT0 = dict(kv.split('=') for kv in "w=e q=n 4=e E=d #=g D=f 3=u v=r x=s y=t 8=n X=u 6=d 5=a 9=o 7=m m=i p=i j=h o=a n=w L=s t=z b=l d=l c=c u=i I=e z=r".split())
A_INIT = dict(A_INIT0, J="h")
fixed = {}
for kv in a.fix.split(','):
    if kv: k_, v = kv.split('='); fixed[k_] = v
init = {t: fixed.get(t, A_INIT.get(t, random.choice('etnrsiah'))) for t in toks}
if a.keyfile:
    for l in open(a.keyfile, encoding='utf8'):
        p = l.split()
        if len(p) >= 2 and p[0] in init and p[0] not in fixed: init[p[0]] = p[1]
def li(v): return LET.index(v) if v in LET else ALPHA.index(v[0])
free = [tid[t] for t in toks if t not in fixed]
LP = M.lp
POW = A ** np.arange(K - 1, -1, -1)
U = lm.load(a.model, order=1, spaces=False).lp.reshape(-1)[:A]
PREF = np.exp(U) / np.exp(U).sum()
TOKC = np.bincount(S, minlength=len(toks)).astype(float)

def score(key):
    x = V[key[S]].ravel(); x = x[x >= 0]
    if len(x) < K: return -1e9
    idx = np.lib.stride_tricks.sliding_window_view(x, K) @ POW
    lc = np.bincount(V[key].ravel()[V[key].ravel() >= 0], weights=np.repeat(TOKC, 2)[V[key].ravel() >= 0], minlength=A)[:A]
    q = lc / max(1, lc.sum()); m = q > 0
    kl = float((q[m] * np.log(q[m] / PREF[m])).sum())
    return float(LP[idx].sum()) + (N - len(x)) * 0 - a.kl * N * kl

best_all = None
for r in range(a.restarts):
    if r == 0: key = np.array([li(init[t]) for t in toks])
    else:
        key = np.array([li(init[t]) if t in fixed else random.randrange(len(LET)) for t in toks])
    cur = score(key); best = (cur, key.copy())
    T0 = 6.0
    for i in range(a.iters):
        T = T0 * (1 - i / a.iters) + 0.02
        t = random.choice(free); old = key[t]
        if random.random() < 0.3:
            u = random.choice(free); key[t], key[u] = key[u], key[t]; sw = u
        else:
            key[t] = random.randrange(len(LET)); sw = None
        s = score(key)
        if s >= cur or random.random() < math.exp((s - cur) / T):
            cur = s
            if s > best[0]: best = (s, key.copy())
        else:
            if sw is not None: key[t], key[sw] = key[sw], key[t]
            else: key[t] = old
    print(f'restart {r}: {best[0]:.1f}', flush=True)
    if best_all is None or best[0] > best_all[0]: best_all = best
key = best_all[1]
val = {t: LET[key[tid[t]]] for t in toks}
print('BEST', round(best_all[0], 1), 'per sign', round(best_all[0] / N, 3))
print(' '.join(f'{t}={val[t]}({cnt[t]})' for t in sorted(toks, key=lambda t: -cnt[t])))
for n, s in lines:
    print(n, ''.join(val[c].replace('_', '·') if c != ' ' else ' | ' for c in s))
if a.out:
    open(a.out, 'w', encoding='utf8').write('\n'.join(f'{t} {val[t]} {cnt[t]}' for t in sorted(toks, key=lambda t: -cnt[t])) + '\n')
