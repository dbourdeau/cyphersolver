"""Per-line beam decode for f. 119. Labels as in f119_glyphs.txt (see LABELS.md).
python bl.py            -> decode every line of f119_glyphs.txt, carrying context across lines
python bl.py 12         -> only line 12 (with the previous line as context)"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
import beam

beam.CAND.update({'6': 'erm', 'c': 'fr', 'C': 'lrf', '%': 'sy', '~': 'g', 'k': 'iq', 'q': 'qc', '4': 'cq',
                  '3': 'dc', 'P': 'd', 'Y': 's', 'Z': 'upr', 'e': 'a', 'L': 'l', 'B': 'b', 'j': 'acp', 'W': 'm',
                  'd': 'dl', 'w': 'mh', 'X': 't', 't': 'q', 'E': 'uv', 'O': 'o', 'H': 'h', 'b': 'lbm', 'r': 'r', 'O': 'o', '=': 'p'})
beam.NOM.update({'[fbn]': ['les'], '[fbi]': ['les'], '[fm]': ['et', 'des'], '[ffmm]': ['que'], '[ffß]': ['que'],
                 '[fi]': ['au'], '[ffb]': ['qui'], '[ffn]': ['par'], '[fmm]': ['le'], '[ffy]': ['mon'],
                 '[fffi]': ['leur', 'son'], '[ffm]': ['que', 'pour'], '[fb]': ['la'], '[f6]': ['la', 'qui'],
                 '[fn]': ['des'], '[ffu]': ['le', 'et'], '[ffuu]': ['que', 'pour']})
for n in ['43', '23', '21', '71', '73', '89', 'N', '&', '9b']:
    beam.NOM['[' + n + ']'] = ['X']

def lines(path='f119_glyphs.txt'):
    out = []
    for ln in open(path, encoding='utf8'):
        if ln.startswith('#') or not ln.strip():
            continue
        num, g = ln.split('|', 1)
        out.append((num.strip(), re.findall(r"\[[^\]]+\]|'[a-z]+|\S", g)))
    return out

if __name__ == '__main__':
    L = lines()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for i, (num, toks) in enumerate(L):
        if only and num != only:
            continue
        ctx = L[i - 1][1] + ['|'] if i and only else []
        s, x, d = beam.beam(ctx + toks)
        print(num, d.split('\n')[-1], round(s / max(1, len(x)), 2))
