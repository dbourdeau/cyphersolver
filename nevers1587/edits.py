"""Score one- and two-edit variants of the key reading of the f.30 tail (writer or reading slips)."""
import os, sys, string
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lang import lm
m = lm.load('fr-1600-letters')
pre, suf = 'grandealarmepassantpreslyon', 'etsansaucunsubiect'
A = 'abcdefghilmnopqrstuxyz'
def edits(w):
    out = set()
    for i in range(len(w) + 1):
        for c in A: out.add(w[:i] + c + w[i:])
        if i < len(w):
            out.add(w[:i] + w[i+1:])
            for c in A: out.add(w[:i] + c + w[i+1:])
    return out
for base in ['apcetais', 'aetcetais']:
    e1 = edits(base); e2 = set()
    for w in e1: e2 |= edits(w)
    sc = sorted(((m.per_char(pre + w + suf), w) for w in e2), reverse=True)
    print(base, [f'{w} {s:.2f}' for s, w in sc[:30]])
