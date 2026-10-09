"""Hypothesis: the 1589 key is the Zifra Prima (R1789) with part of its allocation changed.
Every token type with count >= MINC may keep its Zifra Prima value or be re-assigned to a single letter,
a CV syllable or a null. Simulated annealing on: LM log-prob + C*len + BETA*(occurrences keeping ZP value).
Usage: python zp_repair.py [seed] [ct file]"""
import sys, os, random, math, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
m = lm.load('it-cinquecento', order=5, spaces=False)
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
ctf = sys.argv[2] if len(sys.argv) > 2 else 'ct_all.txt'
C_LEN, BETA, MINC = float(os.environ.get('CLEN', 2.0)), float(os.environ.get('BETA', 1.0)), 2
random.seed(seed)
key = {}
for l in open('keys/zifra_prima_R1789.tsv', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t'); key[k] = v
def zp(t):
    v = key.get(t)
    if v is None: return None
    if v == '_' or v.startswith('#'): return ''
    return lm.norm(v, 'early')
toks = [t for t in open(ctf, encoding='utf8').read().split() if t[0] in 'acdfgh' and t[1:].isdigit()]
cnt = collections.Counter(toks)
letters = list('abcdefghilmnopqrstuz')
sylls = [c + v for c in 'bcdfglmnprstv' for v in 'aeiou']
alts = letters + sylls + ['']
types = sorted(cnt)
val = {}
for t in types:
    z = zp(t)
    val[t] = z if z is not None else random.choice(letters)
free = [t for t in types if cnt[t] >= MINC]
def total():
    s = ''.join(val[t] for t in toks)
    lp = m.per_char(s) * len(s) if s else -1e9
    keep = sum(cnt[t] for t in types if zp(t) is not None and val[t] == zp(t))
    return lp + C_LEN * len(s) + BETA * keep
cur = total(); best = cur; bestval = dict(val)
T0, steps = 3.0, 60000
for i in range(steps):
    T = T0 * (1 - i / steps) + 0.05
    t = random.choice(free)
    old = val[t]
    z = zp(t)
    r = random.random()
    if z is not None and r < 0.15: new = z
    else: new = random.choice(alts)
    if new == old: continue
    val[t] = new
    s = total()
    if s >= cur or random.random() < math.exp((s - cur) / T):
        cur = s
        if s > best: best, bestval = s, dict(val)
    else:
        val[t] = old
val = bestval
out = ''.join(val[t] for t in toks)
print('seed', seed, 'score', round(best, 1), 'per_char', round(m.per_char(out), 3))
changed = [(t, cnt[t], key.get(t, '?'), val[t]) for t in types if zp(t) != val[t] and cnt[t] >= MINC]
changed.sort(key=lambda x: -x[1])
print('changed:', ' '.join('%s(%d):%s>%s' % c for c in changed))
print(out[:1500])
