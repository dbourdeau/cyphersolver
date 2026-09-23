"""Polyphonic beam decoder: each sign label has a candidate set (glyph conflations in the
transcription, homophones from Tomokiyo's Nevers-Piles table); the 5-gram picks per occurrence."""
import sys, json, math
import numpy as np
sys.path.insert(0, '..')
from lang import lm
from solve import build
import solve; solve.FIXED.clear()
M = lm.load('fr-1530-despatches', spaces=False)
A, K = M.A, M.order
IDX = M.index
ANY = [c for c in M.alpha]
def cands(path):
    c = json.load(open(path, encoding='utf8'))
    return {s: (ANY if v == '*' else v.split(',')) for s, v in c.items()}
def lp(ctx, ch):
    # ctx: tuple of last K-1 idx (may be shorter at start)
    x = list(ctx)[-(K - 1):] + [ch]
    if len(x) < K: return -2.5
    i = 0
    for v in x: i = i * A + v
    return float(M.lp[i])
def decode(seq, C, width=300):
    beams = [((), 0.0, [])]
    for t in seq:
        opts = C.get(t, ANY)
        nb = {}
        for ctx, sc, ch in beams:
            for o in opts:
                s = sc; c = ctx
                for letter in o:          # multi-letter values like 'de'
                    if letter not in IDX: continue
                    v = IDX[letter]; s += lp(c, v); c = (c + (v,))[-(K - 1):]
                key = c
                if key not in nb or nb[key][1] < s: nb[key] = (c, s, ch + [o])
        beams = sorted(nb.values(), key=lambda b: -b[1])[:width]
    return beams[0]
if __name__ == '__main__':
    C = cands(sys.argv[1]); only = sys.argv[2] if len(sys.argv) > 2 else ''
    L, _ = build(sys.argv[3].split(',') if len(sys.argv) > 3 else ['t1.txt', 't2.txt', 't3.txt'])
    tot = 0; n = 0; out = {}
    for name, toks in L:
        if only and not name.startswith(only): continue
        parts = []; cur = []
        for t in toks + ['...']:
            if t == '...':
                if cur:
                    c, s, ch = decode(cur, C); tot += s; n += len(''.join(ch)); parts.append(''.join(ch))
                cur = []
                parts.append('…')
            else: cur.append(t)
        out[name] = ''.join(parts[:-1])
        print(name.ljust(6), out[name], flush=True)
    print('per char', tot / max(n, 1))
    json.dump(out, open('beam_out.json', 'w'), ensure_ascii=False, indent=0)
