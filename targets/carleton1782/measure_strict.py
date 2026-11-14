"""Strict share of cipher units read: a word-code or spelled unit counts only when the frozen key and the code
table give the clear-copy word unchanged. Not counted: spelled groups that differ from the clear copy (i/j allowed),
the unread unit, units under glare, and occurrences of codes whose readings conflict (listed below).
The 25 Sep letter is taken from the post-test layer: the hand alignment posttest/clear_alignment_25sep.tsv and the
transcription corrections in posttest/corrections.tsv (13 Nov 2026); 43-19 is thousand in both letters.
    python targets/carleton1782/measure_strict.py"""
import csv
from pathlib import Path
F = Path(__file__).resolve().parent
CONFLICT = {'22-19', '9-8', '13-14', '2-5', '46-9', '9-19', '23-6', '49-9', '2-2', '11-1', '5-22'}
key = {}
for l in (F / 'key/armylist_titlepage_1778.txt').read_text(encoding='utf-8').splitlines():
    if '\t' in l and not l.startswith('#'):
        n, s = l.split('\t', 1); key[int(n)] = ''.join(c.lower() for c in s if c.isalpha() or c == '&')
def spell(t):
    try: return ''.join(key[int(a)][int(b) - 1] for a, b in (v.split('-') for v in t.split()))
    except (KeyError, IndexError): return '?'
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha()).replace('j', 'i')
def tally(units):
    n = good = 0
    for kind, toks, clear, note in units:
        if kind not in ('W', 'S', 'U'): continue
        n += 1
        if kind == 'U' or 'glare' in note: continue
        if kind == 'S' and norm(spell(toks)) != norm(clear): continue
        if kind == 'W' and toks in CONFLICT: continue
        good += 1
    return good, n
cl = [(r['kind'], r['tokens'], r['clear'], r['note']) for r in csv.DictReader((F / 'clinton_1782-02-22/alignment.tsv').open(encoding='utf-8'), delimiter='\t')]
s6 = []
for l in (F / 'carleton_1782-09-06/alignment.tsv').read_text(encoding='utf-8').splitlines():
    if l[:2] in ('W\t', 'S\t', 'C\t'):
        k, t, c = l.split('\t'); s6.append((k, t, c.split(' (')[0], ''))
s25 = []
fix = {int(r['unit']): r['now'].split(' (')[0] for r in csv.DictReader((F / 'posttest/corrections.tsv').open(encoding='utf-8'), delimiter='\t')
       if r['letter'] == 'carleton_1782-09-25' and r['tokens'] != '22-19'}
for r in csv.DictReader((F / 'posttest/clear_alignment_25sep.tsv').open(encoding='utf-8'), delimiter='\t'):
    o, k, c, t = int(r['order']), r['kind'], r['clear_p102'], fix.get(int(r['order']), r['tokens'])
    if o in (7, 194): c = c[:-1]                      # the final letter is the next unit (17-17 y, 23-1 g)
    if o in (8, 195): k = 'S'                          # boundary letters spelled on the key
    if o == 1: c = 'duplicate'                         # heading, 3-4 = duplicate in the 6 Sep letter
    if o in (66, 67, 68): c = {66: 'to', 67: 'pines', 68: 'creek'}[o]   # cipher only, read
    if o == 19: c = 'principal'                        # p.102 principle, B.146 p.54 Principal
    s25.append((k, t, c, r['note']))
tot = [0, 0]
for name, u in (('clinton_1782-02-22', cl), ('carleton_1782-09-06', s6), ('carleton_1782-09-25', s25)):
    g, n = tally(u); tot[0] += g; tot[1] += n
    print(f'{name}: {g} of {n} cipher units read strictly ({g / n:.3f})')
print(f'all three: {tot[0]} of {tot[1]} ({tot[0] / tot[1]:.3f})')
