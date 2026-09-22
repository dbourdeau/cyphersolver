"""Per-occurrence decoding: every glyph label has a candidate set taken from Lasry's key (shapes I could not
tell apart are merged under one label); a beam search picks the letter for each occurrence under the French LM.
Usage: python beam.py f142_glyphs.txt"""
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lang import lm

M = lm.load('fr-1600-letters', order=5, spaces=False)
ALL = list('abcdefghilmnopqrstuxyz')
CAND = {'n': 'e', '6': 'e', 'u': 'ed', 'l': 'as', ':': 't', '#': 'u', 'C': 'lr', 'm': 'nio', 'h': 'ino',
        'M': 'gn', 'x': 'n', '%': 's', ')': 'sd', 'p': 'c', '1': 'ca', 'Z': 'up', 'A': 'o', 'T': 'l', 'z': 'i',
        'D': 'r', '8': 'nbt', '9': 'dc', '3': 'da', '7': 'o', '2': 'f', '4': 'c', 'g': 'mqd', 'w': 'hg',
        'y': 'f', 'X': 'ty', 'd': 'd', 'j': 'ac', 'I': 'b', 'R': 'qb', 'v': 'x', 'Y': 'x', '"': 'h', '*': 'u',
        'S': 's', 'P': 'd', 'F': 'u'}
NOM = {'[ffuy]': ['la'], '[fuy]': ['la'], '[ff6]': ['qui'], '[fbu]': ['les'], '[fu]': ['et', 'des'],
       '[ffm]': ['que', 'pour'], '[fff]': ['vous'], '[ffff]': ['leur', 'son'], '[ffu]': ['le', 'et'],
       '[ffbm]': ['nous']}
WORDS = ['de', 'au', 'la', 'et', 'des', 'que', 'les', 'mon', 'le', 'qui', 'pour', 'par', 'vous', 'nous', 'ils',
         'leur', 'son', '']

def cands(t):
    if t.startswith("'"):
        return [t[1:]]
    if t.startswith('['):
        return NOM.get(t, WORDS)
    return list(CAND.get(t, ALL)) + ([''] if t not in CAND else [])

def load(path):
    toks = []
    for ln in open(path, encoding='utf8'):
        if ln.startswith('#') or not ln.strip():
            continue
        toks += re.findall(r'\[[^\]]+\]|\S', ln) + ['|']
    return toks

def lp(ctx, s):
    x = M.encode(ctx[-4:] + s)
    return M.score_idx(x) - (M.score_idx(M.encode(ctx[-4:])) if ctx[-4:] else 0)

def beam(toks, width=400):
    B = [(0.0, '', '')]  # score, text (letters), display
    for t in toks:
        if t == '|':
            B = [(s, x, d + '\n') for s, x, d in B]; continue
        nb = {}
        for s, x, d in B:
            for c in cands(t):
                sc = s + (lp(x, c) if c else -4.0)
                key = (x + c)[-5:]
                disp = d + (c.upper() if t.startswith('[') else c) + ('' if len(CAND.get(t, ALL)) == 1 or t.startswith('[') else '')
                if key not in nb or nb[key][0] < sc:
                    nb[key] = (sc, x + c, disp)
        B = sorted(nb.values(), key=lambda z: -z[0])[:width]
    return B[0]

if __name__ == '__main__':
    s, x, d = beam(load(sys.argv[1]))
    print(d); print('per char', s / max(1, len(x)))
