"""Test whether the 1589 key is the Zifra Prima (R1789) with base letters permuted and/or a constant
offset per base letter (mod 99). Coordinate ascent on the Italian LM score of the decode."""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
m = lm.load('it-cinquecento')
key = {}
for l in open('keys/zifra_prima_R1789.tsv', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t'); key[k] = v
toks = [t for t in open('ct_all.txt', encoding='utf8').read().split() if t[0] in 'acdfgh' and t[1:].isdigit()]
B = 'acdfgh'
def dec(perm, off):
    out = []
    for t in toks:
        b = t[0]; n = int(t[1:])
        n2 = (n - 1 + off[b]) % 99 + 1
        v = key.get(perm[b] + str(n2))
        if v is None: out.append('x')
        elif v == '_' or v.startswith('#'): continue
        else: out.append(v)
    return lm.norm(''.join(out), 'early')
def score(perm, off):
    s = dec(perm, off)
    return m.per_char(s) if s else -99
best = None
for trial in range(3):
    perm = dict(zip(B, random.sample(B, 6))) if trial else {b: b for b in B}
    off = {b: 0 for b in B}
    cur = score(perm, off)
    for it in range(4):
        for b in B:
            for b2 in B:
                for k in range(99):
                    p2 = dict(perm); p2[b] = b2
                    # keep perm a bijection: swap
                    for o in B:
                        if o != b and perm[o] == b2: p2[o] = perm[b]
                    o2 = dict(off); o2[b] = k
                    s = score(p2, o2)
                    if s > cur: cur, perm, off = s, p2, o2
        print(trial, it, round(cur, 3), perm, off, flush=True)
    print(dec(perm, off)[:400])
