"""Viterbi decode of a System A' transcription: each sign has a small candidate set of plaintext strings;
the de-1500s n-gram model picks the value per occurrence. Secondary candidates cost PEN nats.
  python beam.py cands.json transcription.txt [out.txt]
"""
import re, sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm
SP = os.environ.get('SP') == '1'
M = lm.load('de-1500s', spaces=SP)
k = M.order; A = M.A; idx = M.index
C = json.load(open(sys.argv[1], encoding='utf8'))
PEN = C.pop('_pen', 1.0)
import math
COST = {}
for g, v in list(C.items()):
    if isinstance(v, dict):
        mx = max(v.values()); C[g] = list(v); COST[g] = [-math.log(p / mx) for p in v.values()]
ALL = [c for c in 'abcdefghiklmnoprstuwz']

def lp(ctx, ch):
    # ctx: tuple of up to k-1 indices
    if len(ctx) < k - 1:
        return 0.0
    i = 0
    for c in ctx: i = i * A + c
    return float(M.lp[i * A + ch])

def step(states, cands, costs=None):
    new = {}
    for ctx, (s, out) in states.items():
        for j, cand in enumerate(cands):
            jj = (j // 2 if SP else j); sc = s - (costs[jj] if costs else (PEN if jj else 0.0)); c2 = ctx
            for ch in cand:
                x = idx[ch]; sc += lp(c2, x); c2 = (c2 + (x,))[-(k - 1):]
            if c2 not in new or new[c2][0] < sc:
                new[c2] = (sc, out + [cand])
    return new

def decode(signs):
    states = {(): (0.0, [])}
    for g in signs:
        cands = C.get(g, ALL) if g != '|' else ['']
        if SP: cands = [c + e for c in cands for e in ('', ' ')]
        states = step(states, cands, COST.get(g))
    return max(states.values())[1]

def tokens(s):
    s = re.sub(r'\{[^}]*\}', '', s).replace('a+', 'B').replace('o-', '%').replace('E+', 'Z').replace('ɔo', 'ɔ').replace('ꝏo', 'ꝏ')
    s = re.sub(r'[-.:~?> ]', '', s)
    return s

lines = []
for l in open(sys.argv[2], encoding='utf8'):
    if l.startswith('=='): lines.append((l.strip(), None)); continue
    m = re.match(r'(\d\d) (.*)', l)
    if m: lines.append((m.group(1), tokens(m.group(2))))
# decode each page as one stream so context crosses lines; clear text [..] resets context
res = []; buf = []; ALN = []
def flush():
    if not buf: return
    seq = []; spans = []
    for no, s in buf:
        parts = re.split(r'(\[[^\]]*\])', s); spans.append((no, parts))
    stream = [g for no, parts in spans for p in parts if not p.startswith('[') for g in p]
    out = decode(stream); i = 0
    ALN.extend(zip(stream, out))
    for no, parts in spans:
        t = ''
        for p in parts:
            if p.startswith('['): t += p
            else: t += ''.join(out[i:i + len(p)]); i += len(p)
        res.append(f'{no} {t}')
    buf.clear()
for no, s in lines:
    if s is None: flush(); res.append(no)
    else: buf.append((no, s))
flush()
txt = '\n'.join(res)
if len(sys.argv) > 3: open(sys.argv[3], 'w', encoding='utf8').write(txt + '\n')
print(txt)
if len(sys.argv) > 3: json.dump(ALN, open(sys.argv[3] + '.aln.json', 'w', encoding='utf8'))
