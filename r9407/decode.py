"""decode.py KEYFILE [--poly E=d/ch,n=w/b/t] [--set a=b] [--out FILE]
Beam decode of transcription.txt: each sign takes its key value, or for polyphonic signs the option the de-1500s
model prefers in context (beam over the whole line). Output: page.line decrypt (· marks a polyphonic choice)."""
import re, sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm
M = lm.load('de-1500s', spaces=False)
A = M.A; K = M.order; LP = M.lp
args = sys.argv[1:]
def opt(name, default=''):
    if name in args:
        i = args.index(name); v = args[i+1]; del args[i:i+2]; return v
    return default
poly = {k: v.split('/') for k, v in (kv.split('=') for kv in opt('--poly', 'E=d/ch,n=w/b/t/o,o=b/w,#=g/u,j=s/ch').split(',') if kv)}
setv = dict(kv.split('=') for kv in opt('--set').split(',') if kv)
out = opt('--out')
key = {}
for l in open(args[0], encoding='utf8'):
    p = l.split()
    if len(p) >= 2: key[p[0]] = p[1]
key.update(setv)
def idx(s): return [M.index[c] for c in s if c in M.index]

def lp_next(ctx, c):
    ctx = ctx[-(K-1):]
    if len(ctx) < K-1: return -3.0
    h = 0
    for x in ctx: h = h * A + x
    return float(LP[h * A + c])

def beam(signs, width=40):
    beams = [(0.0, [], '')]           # score, letter-idx history, text
    for c in signs:
        opts = poly.get(c, [key.get(c, '')])
        nb = []
        for sc, hist, txt in beams:
            for o in opts:
                s2, h2 = sc, list(hist)
                for ch in idx(o):
                    s2 += lp_next(h2, ch); h2.append(ch)
                mark = '·' if c in poly else ''
                nb.append((s2, h2[-(K-1):], txt + o.replace('_', '') + ('' if not mark else '')))
        nb.sort(key=lambda b: -b[0])
        seen, beams = set(), []
        for b in nb:
            k2 = tuple(b[1])
            if k2 in seen: continue
            seen.add(k2); beams.append(b)
            if len(beams) >= width: break
    return beams[0][2]

res, page, ctx = [], '', []
for l in open(os.path.join(HERE, 'transcription.txt'), encoding='utf8'):
    if l.startswith('=='): page = l.split()[1]; continue
    m = re.match(r'(\d\d)\s+(.*)', l.rstrip('\n'))
    if not m: continue
    parts = re.split(r'(\[[^\]]*\])', m.group(2))
    txt = ''
    for p in parts:
        if p.startswith('['): txt += ' ' + p + ' '; continue
        s = p.replace(':', '').replace('?', '').replace('jo', 'J').replace('mg', 'M').replace(' ', '')
        if s: txt += beam(s)
    res.append(f'{page}.{m.group(1)} {txt}')
print('\n'.join(res))
if out: open(out, 'w', encoding='utf8').write('\n'.join(res) + '\n')
