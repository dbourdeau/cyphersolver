"""Checks the transcribed Japanese key tables and redoes the worked examples of the reports.

  python decode.py

V0  rotation check: every row of each June-July 1940 table is a rotation of one 109-figure cycle (0 disagreements expected).
V1  JACAR C01004832600 image 4: two stations received 6 July 1940 04:00 Japan time (still the 5th, an odd day, in
    Moscow -> table 3), key group 22244. The key stream drawn from the transcribed table must equal the stream printed
    in the report (亂數) and the decipherment must give back the report's clear text (生文), 60 of 60 figures.
    The example (image 4) and the tables (images 6-7) are on different images.
V2  JACAR C01004816500 image 2: example of Moscow "type 17040" (February 1940), 25 figures.
V3  Brian Audric (RMetS Occasional Paper 2, 2000): the British example of the same Russian system, 25 figures.
All arithmetic is "non-arithmetical" (figure by figure, without carrying): 7 - 9 = 8.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tables_1940 import TABLES, ROWS, COLS

L = 109

def cycle_of(tab):
    seqs = {r: ''.join(tab[r]) for r in ROWS}
    ref = seqs['000']
    m = lambda a, b: sum(x == y for x, y in zip(a, b) if x != '?')
    shift = {r: max(range(L), key=lambda k: m(seqs[r], (ref * 2)[k:k + L])) for r in ROWS}
    votes = [{} for _ in range(L)]
    for r in ROWS:
        for i, ch in enumerate(seqs[r]):
            if ch != '?':
                j = (i + shift[r]) % L
                votes[j][ch] = votes[j].get(ch, 0) + 1
    return ''.join(max(v, key=v.get) for v in votes), shift

def nsub(a, b):
    return str((int(a) - int(b)) % 10)

print('[V0] rotation check')
for t, tab in TABLES.items():
    cyc, shift = cycle_of(tab)
    bad = unread = 0
    for r in ROWS:
        for i, ch in enumerate(''.join(tab[r])):
            if ch == '?':
                unread += 1
            elif ch != cyc[(i + shift[r]) % L]:
                bad += 1
    print(f'  table {t}: {11 * L - unread} figures read, {bad} disagree with the cycle, {unread} illegible (restored)')

print('\n[V1] example of 6 July 1940, key 22244, table 3')
tab = TABLES[3]
cyc, shift = cycle_of(tab)
row, col = '222', '44'
start = (sum(len(x) for x in tab[row][:COLS.index(col)]) + shift[row]) % L
stream = (cyc * 3)[start:start + 60]
doc_key = ['991426739324458613541594278616', '365778294628213346595171922364']
cipher = ['X32526015536660044X145X45X8806', '298XX82636264134X8XX9101922664']
clear = ['841100386212212431273080300290', '933000079008200132284030000300']

def dec(ct, ks):
    out = ''
    for x, k in zip(ct, ks):
        x = '7' if x == 'X' else ('X' if x == '7' else x)     # third operation: 7 <-> X
        out += nsub(x, k) if x != 'X' else 'X'
    return out

for s in range(2):
    ks = stream[30 * s:30 * s + 30]
    d = dec(cipher[s], ks)
    print(f'  station {s + 1}: key from table {ks} == report: {ks == doc_key[s]}')
    print(f'             clear          {d} == report: {d == clear[s]}')

print('\n[V2] Moscow type 17040 (February 1940)')
CT, SUB, MINUS = '0123456789X', '5238X071964', '12654573263'
def dec_indicator(groups, sub, minus, alphabet):
    out = []
    for gi, g in enumerate(groups):
        pos = 4 if gi == 0 else 0                   # 5th figure of group 1, 1st figure of the others
        c = g[pos]
        s, m = sub[alphabet.index(c)], minus[alphabet.index(c)]
        rest = ''.join(nsub(x, m) if x != 'X' else 'X' for j, x in enumerate(g) if j != pos)
        out.append(rest + s if gi == 0 else s + rest)
    return out
print('  ', ' '.join(dec_indicator(['40455', '56145', '12425', '29112', '30365'], SUB, MINUS, CT)),
      ' report: 95900 01690 20203 3355[6] 85810')

print('\n[V3] Audric 2000, British example of the same system')
print('  ', ' '.join(dec_indicator(['99369', '21553', '09895', '39875', '56167'], '3201789645', '7495368201', '0123456789')),
      ' Audric: 88255 02664 32128 14320 80501')
