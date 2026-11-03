"""Held-out test: key learned on c. 42r (c0) lines only, frozen, then used on 42v and 43r (c1, c2).
For each held-out line the sign sequence is aligned with the interlinear clear by the same DP, using the frozen key
only (no re-estimation); we report the share of letters matched by a frozen unit whose top value is that letter.
Baseline: the same with 200 shuffled tables (the frozen values permuted among the units).
usage: heldout.py PASSFILE GLOSS FROZENKEY"""
import sys, math, random, collections
sys.path.insert(0, __import__('os').path.dirname(__file__))
from learn import toks, letters, align
tr = dict(l.rstrip('\n').split('\t', 1) for l in open(sys.argv[1], encoding='utf8') if '\t' in l)
gl = {}
for l in open(sys.argv[2], encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if len(p) == 3 and p[1] == 'G': gl[p[0]] = p[2]
fk = {}
for l in open(sys.argv[3], encoding='utf8'):
    u, n, vals = l.rstrip('\n').split('\t')
    if int(n) >= 3: fk[u] = {v.split(':')[0]: int(v.split(':')[1]) for v in vals.split()}
def P(k):
    def f(u, l):
        c = k.get(u)
        if not c: return 6.0
        return -math.log((c.get(l, 0) + 0.05) / (sum(c.values()) + 1.5))
    return f
def score(k):
    hit = tot = 0
    for n in tr:
        if n.startswith('c0') or n not in gl: continue
        L = letters(gl[n]); _, path = align(toks(tr[n]), L, P(k))
        tot += len(L)
        for u, l in path:
            if u and l and u in k and max(k[u], key=k[u].get) == l: hit += 1
    return hit, tot
h, t = score(fk)
random.seed(1); units = list(fk); vals = [fk[u] for u in units]; sh = []
for _ in range(200):
    random.shuffle(vals); sh.append(score(dict(zip(units, vals)))[0])
print(f'held-out c1+c2: {t} clear letters; matched by the frozen key (top value): {h} ({100*h/t:.1f}%); '
      f'shuffled tables: mean {sum(sh)/len(sh)/t*100:.1f}%, max {max(sh)/t*100:.1f}%')
