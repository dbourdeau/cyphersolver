"""Decode R9426 with the fixed key; flag words that do not look like German."""
import os, sys, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from solve import parse, is_code

K = {}
for ln in open(os.path.join(HERE, 'key.txt'), encoding='utf8'):
    if ln.startswith('#') or not ln.strip(): continue
    a, b = ln.split(); K[a] = b

def dec(w):
    return ''.join(K.get(t, '?') for t in w)

if __name__ == '__main__':
    m = lm.load('de-1500s')
    P = parse()
    out, bad = [], []
    nw = nb = 0
    for lid, items in P:
        o = []
        for it in items:
            if it[0] == 'clear': o.append('[' + it[1] + ']')
            elif it[0] == 'word':
                w = it[1]
                if is_code(w): o.append('<' + '.'.join(w) + '>')
                else:
                    d = dec(w); nw += 1
                    s = m.per_char(' ' + d + ' ')
                    if s < -3.2 or '?' in d:
                        bad.append((lid, '.'.join(w), d, round(s, 2))); nb += 1; o.append(d.upper())
                    else: o.append(d)
        out.append(lid + ' ' + ' '.join(o))
    print('\n'.join(out))
    print(f'\n--- {nb} of {nw} cipher words flagged ---')
    for b in bad: print(*b)
