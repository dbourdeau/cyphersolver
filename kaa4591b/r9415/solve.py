"""Anneal a sign->letter key for an R9414/R9415 transcription, pinned crib values, lang/ model scoring (no spaces)."""
import re, sys, os, math, random, argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm
ap = argparse.ArgumentParser()
ap.add_argument('file'); ap.add_argument('--model', default='la'); ap.add_argument('--fix', default='')
ap.add_argument('--start', default=''); ap.add_argument('--iters', type=int, default=60000)
ap.add_argument('--restarts', type=int, default=4); ap.add_argument('--letters', default='abcdefghilmnopqrstuxz')
a = ap.parse_args()
M = lm.load(a.model, spaces=False)
segs = []
for l in open(a.file, encoding='utf8'):
    m = re.match(r'(\d\d) (.*)', l)
    if not m: continue
    for s in re.split(r'\[[^\]]*\]', m.group(2)): 
        s = s.replace('?', '')
        if s: segs.append(s)
toks = sorted({c for s in segs for c in s})
def parse(s): return dict(kv.split('=', 1) for kv in s.split(',') if kv)
fixed = parse(a.fix); start = parse(a.start)
free = [t for t in toks if t not in fixed]
LET = list(a.letters)
def text(k): return ' '.join(''.join(k[c] for c in s) for s in segs)
def score(k): return sum(M.score_idx(M.encode(''.join(k[c] for c in s))) for s in segs)
best_all = None
for r in range(a.restarts):
    random.seed(r)
    k = {t: fixed.get(t, start.get(t, random.choice(LET))) for t in toks}
    cur = score(k); best = (cur, dict(k))
    for i in range(a.iters):
        T = 3.0 * (1 - i / a.iters) + 0.05
        t = random.choice(free); old = k[t]; k[t] = random.choice(LET)
        s = score(k)
        if s >= cur or random.random() < math.exp((s - cur) / T): cur = s
        else: k[t] = old
        if cur > best[0]: best = (cur, dict(k))
    print(r, round(best[0], 1), flush=True)
    if best_all is None or best[0] > best_all[0]: best_all = best
k = best_all[1]
from collections import Counter
cnt = Counter(c for s in segs for c in s)
print(','.join(f'{t}={k[t]}' for t in sorted(toks, key=lambda t: -cnt[t])))
print(' '.join(f'{t}:{cnt[t]}' for t in sorted(toks, key=lambda t: -cnt[t])))
print(text(k))
