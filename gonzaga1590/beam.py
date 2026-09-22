"""Beam decoder for the Mantua 'Per Cavare 1590' cipher (fr. 3995 f. 64).

Input: a digit string as transcribed, possibly with clear words or signs in braces {..}.
Each digit may be a misreading of a look-alike (3/9, 0/8, 1/3); pairs 11-40 are letters,
41-99 are code words (unknown here, emitted as [nn]). The Italian LM picks the reading.
Usage: python beam.py file   (lines 'tag | digits')
"""
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

K = {11: 'm', 12: 'f', 13: 'a', 14: 'h', 15: 'e', 16: 'n', 17: 'p', 18: 'g', 19: 'b', 20: 'z', 21: 'd', 22: 'a',
     23: 't', 24: 'u', 25: 'o', 28: 'u', 30: 'l', 31: 'r', 32: 'ti', 33: 'c', 34: 'ti', 35: 'o', 36: 'ce',
     37: 'i', 38: 'a', 39: 'o', 40: 's'}
ALT = {'3': '39', '9': '93', '0': '08', '8': '807', '1': '1', '2': '2', '4': '4', '5': '5', '6': '6', '7': '78'}
PEN_ALT = 6.0      # cost of reading a digit as its look-alike
PEN_CODE = 16.0     # cost of a code-word token
M = lm.load('it-cinquecento', order=5, spaces=False)
A, IDX, O = M.A, M.index, M.order


def lp(ctx, ch):
    x = [IDX[c] for c in (ctx + ch)[-O:]]
    if len(x) < O:
        return -2.5
    i = 0
    for v in x:
        i = i * A + v
    return float(M.lp[i])


def decode(s, beam=400):
    s = re.sub(r'\s', '', s)
    toks = re.findall(r'\{[^}]*\}|.', s)
    # states: pos -> list of (score, ctx, out)
    states = {0: [(0.0, '', [])]}
    n = len(toks)
    for p in range(n):
        cur = sorted(states.pop(p, []), key=lambda t: -t[0])[:beam]
        for sc, ctx, out in cur:
            t = toks[p]
            if not t.isdigit():
                states.setdefault(p + 1, []).append((sc, ctx, out + [t]))
                continue
            if p + 1 < n and toks[p + 1].isdigit():
                for a in ALT[t]:
                    for b in ALT[toks[p + 1]]:
                        pen = PEN_ALT * ((a != t) + (b != toks[p + 1]))
                        v = int(a + b)
                        if v in K:
                            for ch in K[v]:
                                states.setdefault(p + 2, []).append((sc - pen + lp(ctx, ch), (ctx + ch)[-8:], out + [ch]))
                        elif 41 <= v <= 99 or v in (26, 27, 29):
                            states.setdefault(p + 2, []).append((sc - pen - PEN_CODE, '', out + ['[%d]' % v]))
            # drop a stray digit
            states.setdefault(p + 1, []).append((sc - 12.0, ctx, out + ['<%s>' % t]))
    best = max(states[n], key=lambda t: t[0])
    return ''.join(best[2])


if __name__ == '__main__':
    for line in open(sys.argv[1], encoding='utf-8'):
        if '|' in line:
            tag, ct = line.split('|', 1)
            print(tag.strip(), ':', decode(ct.strip()))
