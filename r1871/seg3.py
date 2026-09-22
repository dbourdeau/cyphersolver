"""Segment R1871 digit lines into 3-digit groups; rare digits (0,7,8,9) belong in the last place.
Groups of 2 or 4 digits are allowed at a penalty to absorb transcription slips."""
import os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
RARE = set('0789')

def cost(g):
    c = 0.0
    if len(g) != 3:
        c += 6.0
    for ch in g[:-1]:
        if ch in RARE:
            c += 4.0
    return c

def seg(s):
    n = len(s); INF = 1e9
    best = [INF] * (n + 1); back = [0] * (n + 1); best[0] = 0
    for i in range(n):
        if best[i] >= INF:
            continue
        for L in (2, 3, 4):
            if i + L <= n:
                c = best[i] + cost(s[i:i + L])
                if c < best[i + L]:
                    best[i + L] = c; back[i + L] = L
    out = []; i = n
    while i > 0:
        out.append(s[i - back[i]:i]); i -= back[i]
    return out[::-1]

if __name__ == '__main__':
    lines = [l.split() for l in open(os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'tx.txt')) if l.strip()]
    allg = []
    with open(os.path.join(HERE, 'groups.txt'), 'w') as f:
        for n, s in lines:
            g = seg(s); allg += g
            f.write(n + ' ' + ' '.join(g) + '\n')
    c = Counter(allg)
    print(len(allg), len(c), Counter(len(x) for x in allg))
    print(c.most_common(60))
