"""Homophonic annealer for the Sperantio letters (R9411/R9412), Latin, no word spaces.

  python kaa4591/r9411/solve.py TRANSCRIPTION [TRANSCRIPTION ...] [--fix x=s,5=a] [--iters N] [--restarts R]
Transcription format: lines "N code code ... {plain text} ...", ':' dividers dropped, '|' ignored.
Plain text in braces is scored as known letters (context), never keyed.
"""
import argparse, math, random, re, sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm

ap = argparse.ArgumentParser()
ap.add_argument('files', nargs='+'); ap.add_argument('--fix', default='')
ap.add_argument('--iters', type=int, default=300000); ap.add_argument('--restarts', type=int, default=4)
ap.add_argument('--seed', type=int, default=1); ap.add_argument('--model', default='la')
ap.add_argument('--nulls', type=int, default=3); ap.add_argument('--cap', default='e4,i4,a3,u3,t3,s3,n3,o3,r3,m3,c2,l2,p2,d2,q1,b2,g2,f2,h1,x1'); ap.add_argument('--out', default=''); ap.add_argument('--poly', default=''); ap.add_argument('--letters', default='abcdefghilmnopqrstux'); ap.add_argument('--init', default=''); ap.add_argument('--files2', nargs='*', default=[]); ap.add_argument('--model2', default='de-1500s')
a = ap.parse_args()
random.seed(a.seed)
M = lm.load(a.model, spaces=False)
M2 = lm.load(a.model2, spaces=False) if a.files2 else None

def parse(files):
    lines = []
    for f in files:
        for l in open(f, encoding='utf8'):
            m = re.match(r'(\d+)\s+(.*)', l.strip())
            if not m: continue
            toks = []
            for part in re.split(r'(\{[^}]*\})', m.group(2)):
                if part.startswith('{'):
                    toks.append(('P', re.sub('[^a-z]', '', part.lower())))
                else:
                    toks += [('C', t) for t in part.split() if t not in (':', '|', '?')]
            lines.append((m.group(1), toks))
    return lines

LINES1 = parse(a.files); LINES2 = parse(a.files2) if a.files2 else []
LINES = LINES1 + LINES2
POLY = dict(kv.split('=') for kv in a.poly.split(',') if kv)
ALLOW = {}
_k = 0
for _, ts in LINES:
    for i, (k, v) in enumerate(ts):
        if k == 'C' and v in POLY:
            _k += 1; nv = f'{v}~{_k}'; ts[i] = ('C', nv); ALLOW[nv] = POLY[v].split('/') if '/' in POLY[v] else list(POLY[v])
SEQ = [t for _, ts in LINES for t in ts]
SEQ1 = [t for _, ts in LINES1 for t in ts]; SEQ2 = [t for _, ts in LINES2 for t in ts]
CNT = Counter(v for k, v in SEQ if k == 'C')
toks = sorted(CNT)
fixed = dict(kv.split('=') for kv in a.fix.split(',') if kv)
LET = a.letters.split(',') if ',' in a.letters else list(a.letters)
free = [t for t in toks if t not in fixed]
capped = [t for t in free if t not in ALLOW]

def text(key, sep='', seq=None):
    out = []
    for k, v in (SEQ1 if seq is None else seq):
        out.append(v if k == 'P' else key[v].replace('_', ''))
    return sep.join(out)

def score(key):
    s = M.score_idx(M.encode(text(key)))
    if M2: s += M2.score_idx(M2.encode(text(key, seq=SEQ2)))
    return s

INIT = dict(kv.split('=', 1) for kv in open(a.init, encoding='utf8').readline().split()) if a.init else {}
CAP = {kv[0]: int(kv[1:]) for kv in a.cap.split(',') if kv}
def full(key, l): return sum(1 for t in capped if key.get(t) == l) >= CAP.get(l, 2)
def rand_key():
    k = dict(fixed)
    for t in sorted(free, key=lambda t: -CNT[t]):
        if t in ALLOW: k[t] = random.choice(ALLOW[t]); continue
        if t in INIT: k[t] = INIT[t]; continue
        opts = [l for l in LET if not full(k, l)] or list(LET)
        k[t] = random.choice(opts)
    return k

def nnulls(key): return sum(1 for t in free if key[t] == '_')

best_all = None
for r in range(a.restarts):
    key = rand_key(); cur = score(key); best = (cur, dict(key))
    T0 = 8.0
    for i in range(a.iters):
        T = T0 * (1 - i / a.iters) + 0.05
        t = random.choice(free); old = key[t]
        new = random.choice(ALLOW[t]) if t in ALLOW else random.choice(LET + (['_'] if a.nulls else []))
        if new == old: continue
        if new == '_' and (nnulls(key) >= a.nulls or CNT[t] > 40): continue
        swap = None
        if t not in ALLOW and new != '_' and full(key, new):
            cands = [u for u in capped if key[u] == new]; swap = random.choice(cands); key[swap] = old
        key[t] = new; s = score(key)
        if s >= cur or random.random() < math.exp((s - cur) / T):
            cur = s
            if s > best[0]: best = (s, dict(key))
        else:
            key[t] = old
            if swap: key[swap] = new
    print(f'restart {r}: {best[0]:.1f}', flush=True)
    if best_all is None or best[0] > best_all[0]: best_all = best

key = best_all[1]
N = sum(len(key[v].replace('_','')) if k == 'C' else len(v) for k, v in SEQ)
print(f'best {best_all[0]:.1f}  per char {best_all[0]/max(N,1):.3f}')
print(' '.join(f'{t}={key[t]}' for t in sorted(toks, key=lambda t: -CNT[t]) if t not in ALLOW))
res = []
for n, ts in LINES:
    res.append(n + ' ' + ''.join(v.upper() if k == 'P' else key[v].replace('_', '·') for k, v in ts))
print('\n'.join(res))
if a.out:
    open(a.out, 'w', encoding='utf8').write(' '.join(f'{t}={key[t]}' for t in toks if t not in ALLOW) + '\n' + '\n'.join(res) + '\n')
