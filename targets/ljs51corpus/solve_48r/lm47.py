"""Hypothesis (c): keep the 47r key for shapes seen there, let unseen shapes take any letter; anneal with ar-mamluk."""
import sys, os, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
from lang import lm
lines = [l.split()[1:] for l in open('transcription.txt', encoding='utf8') if not l.startswith('#')]
toks = [t for l in lines for t in l if t != '|']
K47 = {'W':'و','X':'م','A':'ا','Q':'ق','TH':'ث','TT':'ط','E':'ف','KS':'ك','K':'ك','S':'س','SL':'ض','AY':'ع','v':'ب'}
free = sorted(set(toks) - set(K47)); L = lm.AR_LETTERS; m = lm.load('ar-mamluk', spaces=False)
for variant in ('W=و', 'W null'):
    tk = [t for t in toks if not (variant == 'W null' and t == 'W')]
    best = None
    for seed in range(4):
        random.seed(seed); k = dict(K47); k.update({s: random.choice(L) for s in free})
        f = lambda: m.score_idx(m.encode(''.join(k[t] for t in tk))); cur = f(); T = 2
        for _ in range(15000):
            s = random.choice(free); o = k[s]; k[s] = random.choice(L); n = f()
            if n >= cur or random.random() < math.exp((n - cur) / T): cur = n
            else: k[s] = o
            T = max(0.05, T * 0.9996)
        if best is None or cur > best[0]: best = (cur, dict(k))
    k = best[1]
    print(variant, 'signs', len(tk), 'per-char', round(best[0] / len(tk), 3))
    print({s: k[s] for s in free}); print(''.join(k[t] for t in tk))
