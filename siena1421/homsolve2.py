"""Stronger homophonic solver: staged anneal (order 3 -> 4 [-> 5]), frequency-seeded starts, many restarts,
optional word spaces. Works on .tok files: plain token lines (spaces inside a line separate signs), or word
files where signs inside a word are joined by '_' (pass words=1).

usage: python homsolve2.py FILE [model] [restarts] [iters] [words=0] [skip=A,B] [fix=S:x] [seed=1] [top=3]
"""
import sys, os, re, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

a = [x for x in sys.argv[1:] if '=' not in x]
o = dict(x.split('=', 1) for x in sys.argv[1:] if '=' in x)
path = a[0]; model = a[1] if len(a) > 1 else 'it-cinquecento'
R = int(a[2]) if len(a) > 2 else 20; IT = int(a[3]) if len(a) > 3 else 60000
WORDS = o.get('words', '0') == '1'; KLW = float(o.get('klw', 1.5))
skip = set(o.get('skip', '').split(',')) - {''}
stages = [int(s) for s in o.get('stages', '3,4').split(',')]
Ms = {k: lm.load(model, order=k, spaces=WORDS) for k in stages}
M = Ms[stages[-1]]; A = len(M.alpha)
LET = [c for c in M.alpha if c.isalpha()]
ORD = {'la': 'eiatusnrmocldpqbgfvh', 'es-golden-age': 'eaosnrildtucmpbqyvgfh', 'ca-modern': 'easlnritocdupmqgvbfhx'}.get(model, 'eaoinlrtscdpumghfbqvz')
WF = np.array([11.8, 11.7, 9.8, 10.1, 6.9, 6.5, 6.4, 5.6, 5.0, 4.5, 3.7, 3.0, 5.1, 2.5, 1.6, 1.1, 1.0, 0.9, 0.5, 0.9, 0.5])
freq = np.full(A, 0.001)
for c, f in zip(ORD, WF / WF.sum()):
    if c in M.index: freq[M.index[c]] = f
if WORDS: freq[M.index[' ']] = 0
freq /= freq.sum()

if WORDS:
    units = [w.split('_') for w in open(path, encoding='utf-8').read().split()]
    runs = [units]  # one run, words separated by space
else:
    runs = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        for part in re.split(r'\[[^\]]*\]', line):
            t = [x for x in part.split() if x not in skip]
            if t: runs.append(t)
signs = sorted({s for r in runs for s in (sum(r, []) if WORDS else r)})
si = {s: i for i, s in enumerate(signs)}; S = len(signs)
SPACE = S; BREAK = S + 1
seq = []
if WORDS:
    seq.append(SPACE)
    for w in units: seq += [si[s] for s in w if s in si] + [SPACE]
else:
    for r in runs: seq += [si[s] for s in r] + [BREAK]
x = np.array(seq)
cnt = np.bincount(x, minlength=S + 2)[:S].astype(float); N = cnt.sum()
letters = [M.index[c] for c in LET]
fixed = {}
for kv in o.get('fix', '').split(','):
    if ':' in kv:
        g, c = kv.rsplit(':', 1)
        if g in si: fixed[si[g]] = M.index[c]


def make_scorer(Mk):
    k = Mk.order; Ak = len(Mk.alpha); lp = Mk.lp
    remap = np.array([Mk.index[c] for c in M.alpha])
    def score(key):
        full = np.concatenate([key, [M.index[' '] if WORDS else 0, 0]])
        y = remap[full[x]]
        n = len(y) - k + 1
        ctx = np.zeros(n, dtype=np.int64)
        for j in range(k): ctx = ctx * Ak + y[j:n + j]
        ok = np.ones(n, bool)
        if not WORDS:
            br = np.where(x == BREAK)[0]
            for b in br: ok[max(0, b - k + 1):b + 1] = False
        s = lp[ctx][ok].sum()
        ob = np.bincount(key, weights=cnt, minlength=A) / N; m = ob > 0
        return s - KLW * N * float((ob[m] * np.log(ob[m] / freq[m])).sum())
    return score


scorers = [make_scorer(Ms[k]) for k in stages]
rnd = random.Random(int(o.get('seed', 1)))
free = [i for i in range(S) if i not in fixed]
order_by_freq = sorted(range(S), key=lambda i: -cnt[i])
exp = [M.index[c] for c in ORD if c in M.index]


def seeded():
    key = np.zeros(S, dtype=np.int64)
    # distribute letters by frequency share with jitter
    budget = {l: freq[l] * N for l in exp}
    for i in order_by_freq:
        cands = sorted(exp, key=lambda l: -(budget[l] + rnd.random() * N * 0.03))
        l = cands[0]; key[i] = l; budget[l] -= cnt[i]
    return key


def show(key):
    if WORDS: return ' '.join(''.join(M.alpha[key[si[s]]] for s in w) for w in units)
    return ' | '.join(''.join(M.alpha[key[si[s]]] for s in r) for r in runs)


res = []
for r in range(R):
    key = seeded() if r % 2 == 0 else np.array([rnd.choice(letters) for _ in range(S)])
    for i, c in fixed.items(): key[i] = c
    for sc in scorers:
        cur = sc(key); T = 6.0
        for it in range(IT):
            if rnd.random() < 0.8:
                i = rnd.choice(free); old = key[i]; key[i] = rnd.choice(letters)
                s = sc(key)
                if s >= cur or rnd.random() < math.exp((s - cur) / T): cur = s
                else: key[i] = old
            else:
                i, j = rnd.sample(free, 2); key[i], key[j] = key[j], key[i]
                s = sc(key)
                if s >= cur or rnd.random() < math.exp((s - cur) / T): cur = s
                else: key[i], key[j] = key[j], key[i]
            T = max(0.15, T * (1 - 7.0 / IT))
    res.append((cur, key.copy()))
    print('%3d %9.1f  %s' % (r, cur, show(key)[:170]), flush=True)
res.sort(key=lambda z: -z[0])
for sc_, key in res[:int(o.get('top', 1))]:
    print('\nscore', round(sc_, 1), 'per-token', round(sc_ / len(x), 3))
    print(' '.join('%s=%s' % (s, M.alpha[key[si[s]]]) for s in signs))
    print(show(key))
