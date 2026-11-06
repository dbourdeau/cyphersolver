"""Coordinate ascent on the single-letter part of key 2, the printed syllable table held fixed.

Each consonant (and 'et') sits on one code from 0-9, '01' or nowhere; vowels a3 e5 i7 o9 u0 and 11 = null stay fixed
unless --vowels. Every placement of every letter is tried in turn, the best kept, until a sweep changes nothing.
"""
import sys, time
from key1 import beam_decode, lm, lines
from key2 import K2
m = lm.load('it-cinquecento', order=5, spaces=False)
d = ''.join(t[0] for _, _, toks, _ in lines() for t in toks)
B = int(sys.argv[1]) if len(sys.argv) > 1 else 16
SYL = {k: v for k, v in K2.items() if len(k) == 2 and k not in ('01',)}
place = {'a': '3', 'e': '5', 'i': '7', 'o': '9', 'u': '0', 'b': '8', 'c': '8', 'd': '01', 'f': '01', 'g': '01',
         'l': '2', 'p': '2', 'n': '4', 'm': '4', 'r': '6', 't': '6', 'et': '1', 's': None, 'z': None, 'q': None, 'h': None}
movable = [k for k in place if k not in 'aeiou' or '--vowels' in sys.argv]
spots = [str(x) for x in range(10)] + ['01', None]
def key_of(pl):
    K = {k: list(v) for k, v in SYL.items()}
    for L, c in pl.items():
        if c is not None:
            K.setdefault(c, []).append(L)
    return K
def score(pl):
    return beam_decode(d, key_of(pl), m, B)[0]
cur = score(place); print('start', round(cur, 1), flush=True)
changed = True
while changed:
    changed = False
    for L in movable:
        best = (cur, place[L])
        for c in spots:
            if c == place[L]: continue
            pl = dict(place); pl[L] = c
            s = score(pl)
            if s > best[0] + 1.0: best = (s, c)
        if best[1] != place[L]:
            print(f'{L}: {place[L]} -> {best[1]}  {best[0] - cur:+.1f}', flush=True)
            place[L] = best[1]; cur = best[0]; changed = True
print('final', round(cur, 1), place)
s, path = beam_decode(d, key_of(place), m, 64)
print(''.join(o for _, o in path))
