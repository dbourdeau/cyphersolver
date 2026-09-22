"""Score every reading of the f. 101v / 102v figure-letter runs that key no. 16 allows.

Glyph options come from key16.txt (s = i/5, t = g/f, a = 8/9 ...). A few glyphs are ambiguous on the
microfilm (the 9 may be the tailed g = t; the z-like sign may be m or a form of r, as in the fr. 3416 sibling;
'h' is not a key-16 substitute) and get their alternatives or the whole alphabet. Candidates are scored as
unspaced text with the shared French model; the best readings per run are printed.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lang import lm

ALL = 'abcdefghilmnopqrstuxyz'
OPT = {
    '8': 'a', '9': 'at', '7': 'e', '6': 'e', '5': 'is', '4': 'i', '3': 'l', '2': 'ls',
    'i': 's', 'k': 'r', 'S': 'r', 'r': 'o', 'g': 'ot', 'f': 't', 'd': 'u', 'e': 'u',
    't': 'n', 'v': 'n', 'n': 'q', 'm': 'q', 'x': 'm', 'o': 'p', 'p': 'p', 'D': 'd',
    'Z': 'mrlg',  # the z-like sign
    'h': ALL,     # not in key 16
    'c': 'x', 'b': 'y', 'a': 'y', 'y': 'z',
}

RUNS = {
    # f.101v: '... 42 et' | 5 i 7 f Z r | d 6 5 i 8 t h 6 | D 7 2 5(overbar)  'pour ...'
    'A': '5i7fZrd65i8th6D725',
    # f.101v: 'de pouvoir G' | 5 i 7 D 6 2 9 v | 'vous entretenir'
    'B': '5i7D629v',
    # f.102v: '... avec les' | k 7 n 6 2 9 7 | 'faudra ...'
    'C': 'k7n6297',
}


def readings(run):
    pools = [OPT.get(ch, ch) for ch in run]
    for combo in itertools.product(*pools):
        yield ''.join('qu' if c == 'q' else c for c in combo)


def main():
    m = lm.load('fr-1530-despatches', spaces=False)
    for name, run in RUNS.items():
        scored = []
        for s in readings(run):
            scored.append((m.per_char(lm.norm(s, 'early')), s))
        scored.sort(reverse=True)
        print(name, run, len(scored))
        for sc, s in scored[:12]:
            print(f'   {sc:6.2f}  {s}')


if __name__ == '__main__':
    main()
