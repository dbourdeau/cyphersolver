"""Anneal a one-to-one substitution key (sign label -> distinct Arabic letter) for the 48r-48v block."""
import sys, os, random, math, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from lang import lm
here = os.path.dirname(__file__)
lines = [l.split()[1:] for l in open(os.path.join(here, 'transcription.txt'), encoding='utf8') if not l.startswith('#')]
toks = [t for l in lines for t in l if t != '|']
syms = sorted(set(toks))
L = lm.AR_LETTERS
m = lm.load('ar-mamluk', spaces=False)
def dec(k): return ''.join(k[t] for t in toks)
def sc(k): return m.score_idx(m.encode(dec(k)))
best = None
for restart in range(int(sys.argv[1]) if len(sys.argv) > 1 else 20):
    random.seed(restart)
    perm = random.sample(L, len(L)); k = dict(zip(syms, perm)); spare = perm[len(syms):]; cur = sc(k)
    T = 2.0
    for it in range(30000):
        a = random.choice(syms)
        if random.random() < 0.15:
            j = random.randrange(len(spare)); k[a], spare[j] = spare[j], k[a]; undo = ('s', a, j)
        else:
            b = random.choice(syms); k[a], k[b] = k[b], k[a]; undo = ('w', a, b)
        n = sc(k)
        if n >= cur or random.random() < math.exp((n - cur) / T): cur = n
        elif undo[0] == 's': k[a], spare[undo[2]] = spare[undo[2]], k[a]
        else: k[a], k[undo[2]] = k[undo[2]], k[a]
        T = max(0.05, T * 0.9998)
    pc = cur / len(toks)
    print(restart, round(pc, 3), dec(k)[:80], flush=True)
    if best is None or cur > best[0]: best = (cur, dict(k))
print('BEST per-char', best[0] / len(toks)); print(json.dumps(best[1], ensure_ascii=False)); print(dec(best[1]))
