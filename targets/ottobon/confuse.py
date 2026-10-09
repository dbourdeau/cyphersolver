"""Zifra Prima (R1789) decode of ct_all.txt allowing systematic digit misreadings of the first-pass transcription.
Each token TYPE picks one code among its digit-confusion variants (cost per changed digit); simulated annealing on
LM log-prob + CLEN*len - COST*changes. Prints the chosen re-readings and the text."""
import sys, os, random, math, collections, itertools, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
m = lm.load('it-cinquecento', order=5, spaces=False)
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
ctf = sys.argv[2] if len(sys.argv) > 2 else 'ct_all.txt'
CLEN = float(os.environ.get('CLEN', 1.9)); COST = float(os.environ.get('COST', 2.0)); STEPS = int(os.environ.get('STEPS', 40000))
random.seed(seed)
key = {}
for l in open('keys/zifra_prima_R1789.tsv', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t'); key[k] = v
CONF = {'0': '08', '1': '17', '2': '237', '3': '325', '4': '4', '5': '583', '6': '68', '7': '7129', '8': '8503', '9': '97'}
def variants(t):
    b, n = t[0], t[1:]
    out = {}
    for combo in itertools.product(*[CONF.get(d, d) for d in n]):
        s = ''.join(combo).lstrip('0')
        if not s or int(s) > 99: continue
        c = sum(1 for x, y in zip(n, combo) if x != y)
        k = b + s
        if k in key and (k not in out or out[k] > c): out[k] = c
    return out
def val(k):
    v = key[k]
    return '' if v == '_' or v.startswith('#') else lm.norm(v, 'early')
toks = [t for t in open(ctf, encoding='utf8').read().split() if t[0] in 'acdfgh' and t[1:].isdigit()]
cnt = collections.Counter(toks)
types = sorted(cnt)
V = {t: variants(t) for t in types}
for t in types:
    if not V[t]: V[t] = {None: 0}
choice = {t: (t if t in V[t] else min(V[t], key=V[t].get)) for t in types}
def text(ch):
    return ''.join(val(ch[t]) if ch[t] else 'x' for t in toks)
def score(ch):
    s = text(ch)
    return m.per_char(s) * len(s) + CLEN * len(s) - COST * sum(cnt[t] ** 0.5 * V[t][ch[t]] for t in types)
cur = score(choice); best, bestch = cur, dict(choice)
multi = [t for t in types if len(V[t]) > 1]
for i in range(STEPS):
    T = 4.0 * (1 - i / STEPS) + 0.05
    t = random.choice(multi)
    old = choice[t]; new = random.choice(list(V[t]))
    if new == old: continue
    choice[t] = new
    s = score(choice)
    if s >= cur or random.random() < math.exp((s - cur) / T):
        cur = s
        if s > best: best, bestch = s, dict(choice)
    else: choice[t] = old
ch = bestch
out = text(ch)
print('seed', seed, 'score %.1f per_char %.3f' % (best, m.per_char(out)))
chg = sorted([(cnt[t], t, ch[t], key.get(ch[t], '?')) for t in types if ch[t] != t], reverse=True)
print('re-read:', ' '.join('%s>%s=%s(%d)' % (t, c, v, n) for n, t, c, v in chg[:80]))
print(out[:2500])
json.dump(ch, open('confuse_choice_%d.json' % seed, 'w'))
