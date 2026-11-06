"""Write docs/reveal/farnese1541.json from the aligned reading: every code of a passage with its reading.

  python reveal91.py 65r.19 65r.24      first and last line of the passage

Uses align91's alignment of reading.txt under k2d, so the reveal shows exactly what the measurement counts:
nulls as 'null', unread digits as 'unk', words marked [?] as 'unc', emendations as 'unc'.
"""
import sys, os, json, importlib
import vdot
from align91 import parse_reading, align, HERE

a, b = sys.argv[1], sys.argv[2]
key = {k: list(v) for k, v in importlib.import_module('k2d').KEY.items()}
items = parse_reading(os.path.join(HERE, 'reading.txt'))
D = vdot.Dec(only=set(it[-1] for it in items))
path, info = align(items, key, D)
flat = [(name, t) for name, ts, _ in D.S for t in ts]
tgt_item = []
for k, it in enumerate(items):
    tgt_item += [k] * (len(it[1]) if it[0] == 'w' else 1)
labels = [n for n, _, _ in D.S]
lo, hi = labels.index(a), labels.index(b)
tokens = []
for pi, i, pj, j, inf in path:
    line = flat[pi][0]
    if not (lo <= labels.index(line) <= hi):
        continue
    digs = ' '.join(str(flat[q][1][0]) if flat[q][1][0] >= 0 else '_' for q in range(pi, i))
    kind = inf[0]
    if kind == 'U':
        for q in range(pi, i):
            d = flat[q][1][0]
            tokens.append({'g': str(d) if d >= 0 else '_', 'p': '?', 'cls': 'unk'})
    elif kind == 'skip':
        continue
    elif kind in ('code', 'emend'):
        out = inf[2]
        unc = kind == 'emend' or (out and pj < len(tgt_item) and items[tgt_item[pj]][0] == 'w' and items[tgt_item[pj]][2])
        g = digs.replace(' ', '')
        if inf[1].startswith("'"):
            g = '·' + g          # dotted code: the scribe's dot over the preceding digit
        tokens.append({'g': g, 'p': out if out else '·', 'cls': 'null' if not out else ('unc' if unc else '')})
doc = {
    'slug': 'farnese1541',
    'anchor': 'the-close',
    'title': 'The close of the cipher, f. 65r',
    'caption': f'Every figure group of 65r lines {a[4:]}–{b[4:]} with the value that k2d (Meister’s key no. 2 as '
               'corrected on the letter) gives it in the reading. A dot before a group is the dot the scribe set '
               'over the preceding digit; 11 is the null; grey groups are unread.',
    'unit': 'figure group',
    'key_note': 'a 3, e 5, i 7, o 9, u 0; b/c 02, d/f/g 01, l/p 2, n/m 4, r/t 6, s/z/et 1; syllables in two digits; '
                'dotted 80-89 = ta-to, qua-qui, che, chi, non; 11 null',
    'tokens': tokens,
}
out = os.path.join(HERE, '..', '..', 'docs', 'reveal', 'farnese1541.json')
json.dump(doc, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(tokens), 'tokens ->', out)
