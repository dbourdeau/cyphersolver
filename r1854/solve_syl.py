"""Annealer where each sign maps to a letter, a common syllable/word, or null. Usage: solve_syl.py tokens model restarts iters"""
import os, sys, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

path, model = sys.argv[1], sys.argv[2]
R, IT = int(sys.argv[3]), int(sys.argv[4])
m = lm.load(model, spaces=False)
toks = [t for l in open(path, encoding='utf-8') if ':' in l for t in l.split(':', 1)[1].split()]
signs = sorted(set(toks))
LET = list(m.alpha)
SYL = ['et', 'con', 'per', 'pro', 'us', 'um', 'quod', 'que', 'qui', 'ne', 're', 'in', 'ch', 'de', 'ri', 'ar', 'er', 'or', 'an', 'en', 'is', 'st', 'nt', 'ti', 'la', 'il', 'di', '']
VALS = LET + SYL
lf = {c: 1.0 for c in VALS}
C = float(os.environ.get('NULLC', '-3.0'))


import collections
Q = {'a':.08,'b':.015,'c':.04,'d':.035,'e':.11,'f':.01,'g':.012,'h':.01,'i':.10,'l':.035,'m':.045,'n':.065,'o':.07,'p':.03,'q':.015,'r':.065,'s':.07,'t':.075,'u':.07,'x':.004,'y':.001,'z':.001,'k':.001,'w':.001}
def kl(s):
    c = collections.Counter(s); n = max(1, len(s))
    return sum((v/n)*math.log((v/n)/Q.get(ch, .001)) for ch, v in c.items())
def score(key):
    s = ''.join(key[t] for t in toks)
    extra = sum(len(key[t]) - 1 for t in toks)          # letters beyond one per sign
    nulls = sum(1 for t in toks if key[t] == '')
    return m.score(s) - len(s) * kl(s) + C * nulls + 0.6 * C * max(0, extra - 0)  # syllables allowed but priced


best_all = (-1e18, None)
for r in range(R):
    key = {s: random.choice(LET) for s in signs}
    cur = score(key); best = (cur, dict(key))
    for it in range(IT):
        T = 10 * (1 - it / IT) + 0.2
        s = random.choice(signs); old = key[s]
        key[s] = random.choice(VALS) if random.random() < 0.3 else random.choice(LET)
        new = score(key)
        if new >= cur or random.random() < math.exp((new - cur) / T):
            cur = new
            if cur > best[0]: best = (cur, dict(key))
        else:
            key[s] = old
    print('restart', r, round(best[0] / len(toks), 3), flush=True)
    if best[0] > best_all[0]: best_all = best
key = best_all[1]
print('key', ' '.join(f'{s}={key[s] or "_"}' for s in signs))
for l in open(path, encoding='utf-8'):
    if ':' in l:
        lab, t = l.split(':', 1)
        print(lab, '|'.join(key[x] for x in t.split()))
