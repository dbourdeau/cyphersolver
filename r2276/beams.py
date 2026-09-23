"""Beam decoder with a spaced LM: a space may be inserted after any token (scored by the LM)."""
import sys, json
sys.path.insert(0, '..')
from lang import lm
from decode import load
MODEL = sys.argv[4] if len(sys.argv) > 4 else 'fr-1530-despatches'
M = lm.load(MODEL, spaces=True)
A, K = M.A, M.order; IDX = M.index; SP = IDX[' ']
def cands(p):
    c = json.load(open(p, encoding='utf8'))
    return {s: [x.replace('j','i').replace('v','u') for x in (list('abcdefghilmnopqrstuxyz') if v == '*' else v.split(','))] for s, v in c.items()}
def lp(ctx, ch):
    x = list(ctx) + [ch]
    if len(x) < K: return -2.0
    i = 0
    for v in x[-K:]: i = i*A + v
    return float(M.lp[i])
def step(ctx, s, o):
    for letter in o:
        v = IDX[letter]; s += lp(ctx, v); ctx = (ctx + (v,))[-(K-1):]
    return ctx, s
def decode(seq, C, width=400):
    beams = {(SP,): ((SP,), 0.0, '')}
    for t in seq:
        nb = {}
        for ctx, sc, txt in beams.values():
            for o in C.get(t, list('abcdefghilmnopqrstuxyz')):
                c2, s2 = step(ctx, sc, o)
                for sp in (False, True):
                    c3, s3, t3 = c2, s2, txt + o
                    if sp and o:
                        c3, s3 = step(c2, s2, ' '); t3 += ' '
                    if c3 not in nb or nb[c3][1] < s3: nb[c3] = (c3, s3, t3)
        beams = dict(sorted(nb.items(), key=lambda kv: -kv[1][1])[:width])
    return max(beams.values(), key=lambda b: b[1])
if __name__ == '__main__':
    C = cands(sys.argv[1]); only = sys.argv[2]; files = sys.argv[3].split(',')
    for name, toks in load(files):
        if only and not name.startswith(only): continue
        parts = []; cur = []
        for t in toks + ['...']:
            if t == '...':
                if cur: parts.append(decode(cur, C)[2].strip())
                cur = []; parts.append('…')
            else: cur.append(t)
        print(name.ljust(6), ' '.join(parts[:-1]), flush=True)
