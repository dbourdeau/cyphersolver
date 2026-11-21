"""Decode rows of the T-S NS J479 CTTS project (labels_corrected6) into Hebrew letters and test each word against a lexicon of
Arabic in Hebrew letters (Arabic papyri + Qur'an, corpus/ja_translit.txt). Box order is reading order (bands are cut so the
scribe's direction runs left to right). Words are split at gaps >= GAP px between boxes. A 7 is bet on side 1 and tav on side 2.
Usage: decode_ctts.py [band ...]   (default: the open rows)"""
import json, re, sys, itertools
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
GAP = 38
P = Path(r'C:\Users\dbour\cypher\research\ctts\projects\tsnsj479')
boxes = json.load(open(P / 'boxes_corrected7.json', encoding='utf-8')); labels = json.load(open(P / 'labels_corrected7.json', encoding='utf-8'))
H = dict(zip('I U E A N 4 c B d - < p P q w O 6 S X 9 C 7'.split(), 'abgdhwzcvyklmnsefxqrjt'))   # Latin code of alef..tav
H.update({'Bc': 'c', 'J': 'y', '<5': 'k', 'f': 'm', 'a': 't', 's': 'r', '8': 'r', '5': 'r', 'e': 'c', 'b': 'l', 't': 'n', 'n': 'h'})
HEB = dict(zip('abgdhwzcvyklmnsefxqrjt', 'אבגדהוזחטיכלמנסעפצקרשת'))
LEX = set()
for w in open(r'C:\Users\dbour\cypher\targets\tsnsj479\corpus\ja_translit.txt', encoding='utf-8').read().split(): LEX.add(w)
def code(lab, side):
    unc = lab.startswith('?'); l = lab.lstrip('?').rstrip('.')
    if l == '7': return ('b' if side == 1 else 't'), unc
    return H.get(l, '*'), unc
def decode(band):
    img = band + '.png'; side = int(band[1]); bx = sorted(boxes[img], key=lambda b: b['x']); words = [[]]; prev = None
    for b in bx:
        lab = labels[img][str(b['n'])]
        if lab.startswith('_') or lab.startswith('#'): continue
        if prev is not None and b['x'] - prev > GAP: words.append([])
        c, u = code(lab, side); words[-1].append((c, u, lab)); prev = b['x'] + b['w']
    return [w for w in words if w]
rows = sys.argv[1:] or ['S1L05', 'S1L06', 'S1L07', 'S1L08', 'S1L13', 'S2L10', 'S2L13', 'S2L17', 'S2U01']
for band in rows:
    out = []
    for w in decode(band):
        lat = ''.join(c for c, u, l in w); heb = ''.join(('?' if u else '') + HEB.get(c, '*') for c, u, l in w)
        sub = [lat[i:j] for i in range(len(lat)) for j in range(i + 3, len(lat) + 1) if lat[i:j] in LEX]
        out.append(f"{heb}{' =' + lat if lat in LEX else (' ~' + max(sub, key=len) if sub else '')}")
    print(band, ' | '.join(out))
