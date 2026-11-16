# count_v7.py [FOLDER]: open code numbers and per-letter labels under key_v7.tsv (key_v6.tsv of PR #646 + the rows read
# under Sehested's glosses, gloss/KEY_v7_DIFF.md), against key_v5.tsv and key_v6.tsv. Writes counts_v7.txt.
# Label rule copied from scripts/count_v6.py (itself from scripts/count_twelve.py lab()): N if any token is not in the key
# (incl. '~'), is tier C, or the note starts with '!N'; E if any value is longer than three letters, is 'et', or is tier G;
# else S. One change for v7: a tier ending in '?' (doubtful, value disputed) counts N, like tier C.
# Nothing here is a count of record: no decryption was made with key v7. Standard library only; run with python3 -I.
import sys, os, re, glob, collections
F = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(F, *a)
def load(p):
    k = {}
    for l in open(p, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        x = l.rstrip('\n').split('\t'); k[x[0]] = (x[1], x[2])
    return k
K = {v: load(P('key_%s.tsv' % v)) for v in ('v5', 'v6', 'v7')}
doubt = lambda key, t: key[t][1].endswith('?')
L = ['counts_v7.txt: written by scripts/count_v7.py (python3 -I). Not a count of record: nothing was decoded with key v7.', '']

# 1. The 21 code numbers with no value after key v5 (NOTES, Remaining gaps, as filed before #646), checked against each key.
V5_OPEN = ['40', '108', '134', '135', '151', '181', '197', '198', '235', '248', '330', '344', '346', '351', '370', '374', '376',
           '388', '390', '394', '399']
assert all(t not in K['v5'] for t in V5_OPEN), 'a listed number has a v5 value'
L.append('1. The %d numbers open after key v5: %s' % (len(V5_OPEN), ', '.join(V5_OPEN)))
for v in ('v6', 'v7'):
    filled = [t for t in V5_OPEN if t in K[v]]
    dbt = [t for t in filled if doubt(K[v], t)]
    still = [t for t in V5_OPEN if t not in K[v]]
    L.append('   %s: filled %d (%s)%s; no value %d (%s)' % (v, len(filled), ', '.join('%s = %s [%s]' % (t, K[v][t][0], K[v][t][1]) for t in filled),
             ('; of these doubtful %d (%s)' % (len(dbt), ', '.join(dbt))) if dbt else '', len(still), ', '.join(still)))
f6 = [t for t in V5_OPEN if t in K['v6']]; f7 = [t for t in V5_OPEN if t in K['v7'] and t not in K['v6']]
d7 = [t for t in V5_OPEN if t in K['v7'] and doubt(K['v7'], t)]
n7 = len(V5_OPEN) - len(f6) - len(f7)
L.append('   arithmetic: %d - %d (#646: %s) - %d (v7: %s) = %d with no value; %d + %d doubtful (%s) = %d without a settled value'
         % (len(V5_OPEN), len(f6), ', '.join(f6), len(f7), ', '.join(f7), n7, n7, len(d7), ', '.join(d7), n7 + len(d7)))
L.append('')

# 2. Code numbers in use with no value: every digit token of the first-reader transcriptions (method of count_v6.py).
L.append('2. Code numbers in the first-reader transcriptions (transcriptions/*.txt, not *_blind*) with no value (occurrences):')
occ = collections.Counter()
for tx in sorted(glob.glob(P('transcriptions', '*.txt'))):
    if '_blind' in tx: continue
    for l in open(tx, encoding='utf8'):
        if l.startswith('#') or '|' not in l: continue
        for r in re.findall(r'<([^>]*)>', l):
            for t in r.split('.'):
                t = t.strip().rstrip('~')
                if t.isdigit(): occ[t] += 1
used = sorted(occ, key=int)
L.append('   distinct code numbers in use: %d; occurrences: %d' % (len(used), sum(occ.values())))
prev = pv = None
for v in ('v5', 'v6', 'v7'):
    nov = [t for t in used if t not in K[v]]
    dbt = [t for t in used if t in K[v] and doubt(K[v], t)]
    L.append('   %s: %d numbers, %d occurrences with no value: %s' % (v, len(nov), sum(occ[t] for t in nov), ', '.join('%s x%d' % (t, occ[t]) for t in nov)))
    if dbt: L.append('   %s: doubtful rows in use: %s; numbers without a settled value: %d + %d = %d' % (v, ', '.join('%s x%d' % (t, occ[t]) for t in dbt), len(nov), len(dbt), len(nov) + len(dbt)))
    if prev is not None:
        gone = [t for t in prev if t not in nov]
        L.append('      %s against %s: %d - %d filled = %d (%s)' % (v, pv, len(prev), len(gone), len(nov), ', '.join(gone) or '-'))
    prev = nov; pv = v
L.append('')

# 3. Per letter, v6 against v7 (word divisions units/*.seg).
def readseg(p):
    rows = []
    for l in open(p, encoding='utf8'):
        if not l.strip(): continue
        x = l.rstrip('\n').split(' ', 2); rows.append((x[0].split('.'), x[1] if len(x) > 1 else '', x[2] if len(x) > 2 else ''))
    return rows
def lab(toks, note, KEY):
    if any(t not in KEY for t in toks): return 'N'
    if any(KEY[t][1] == 'C' or KEY[t][1].endswith('?') for t in toks): return 'N'
    if note.startswith('!N'): return 'N'
    if any(len(KEY[t][0]) > 3 or KEY[t][0] == 'et' or KEY[t][1] == 'G' for t in toks): return 'E'
    return 'S'
NEW = [t for t in K['v7'] if K['v7'].get(t) != K['v6'].get(t)]
L.append('3. Per letter, v6 (#646) against v7; rows new or changed in v7: %s. Doubtful rows count N.' % ', '.join(NEW))
L.append('letter\treader\tS v6\tE v6\tN v6\tS v7\tE v7\tN v7\tunits\tstrict v6\tstrict v7\tunits that move (token: value)')
moved = collections.Counter(); tot = collections.Counter()
for seg in sorted(glob.glob(P('units', '*.seg'))):
    i = os.path.basename(seg)[:-4]; rd = 'blind' if i.endswith('_blind') else 'first'; base = i[:-6] if rd == 'blind' else i
    c6 = collections.Counter(); c7 = collections.Counter(); mv = []
    for t, u, n in readseg(seg):
        a, b = lab(t, n, K['v6']), lab(t, n, K['v7']); c6[a] += 1; c7[b] += 1
        if a != b:
            mv.append('%s>%s %s' % (a, b, ', '.join('%s: %s' % (x, K['v7'][x][0]) for x in t if x in NEW))); moved.update(x for x in t if x in NEW)
            tot[a + '>' + b] += 1
    n = sum(c6.values())
    if True:
        L.append('%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%.2f%%\t%.2f%%\t%s' % (base, rd, c6['S'], c6['E'], c6['N'], c7['S'], c7['E'], c7['N'], n,
                 100.0 * c6['S'] / n, 100.0 * c7['S'] / n, '; '.join(mv) or '-'))
L.append('units that move: %s; new or changed v7 rows met: %s' % (', '.join('%s x%d' % kv for kv in sorted(tot.items())) or 'none',
         ', '.join('%s x%d' % kv for kv in sorted(moved.items())) or 'none'))
open(P('counts_v7.txt'), 'w', encoding='utf8').write('\n'.join(L) + '\n'); print('\n'.join(L))
