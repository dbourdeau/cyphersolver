"""merge_o4.py (O4) - merged transcription of portion P (5r, 5v, 6r) per PREREG-O4 §3, written BEFORE any decoding.
Agreed positions: the common token. Disputed positions (same order as compare_o4.py): ARBITRAGE.tsv choice
(A -> pass A tokens, B -> pass B tokens, neither -> NIL repeated max(len A, len B)). Transcriber names keep their pass prefix
tA-... / tB-... (no letter). Punctuation and '?' are dropped exactly as compare.load does. Then counts (names only, column 1
of key.tsv, no value read) the tokens whose name is a key name, for the size rule of §2."""
import sys, os, re, difflib, csv
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'o2-2311', 'wainut-scripts'))
from compare import load
def pref(rows, X): return {k: [('t%s-%s' % (X, t) if re.match(r't(\d|\?)', t) else t) for t in r] for k, r in rows.items()}
A = pref(load('passe-A/transcription_passA.txt'), 'A'); B = pref(load('passe-B/transcription_passB.txt'), 'B')
arb = [r for r in csv.DictReader(open('ARBITRAGE/ARBITRAGE.tsv'), delimiter='\t')]
n = 0; out = []; cnt = {'A': 0, 'B': 0, 'neither': 0}
for k in A:
    a, b = A[k], B[k]; toks = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal': toks += a[i1:i2]; continue
        r = arb[n]; n += 1
        assert r['id'] == 'D%03d' % n and r['row'] == '%s %s' % k and r['A'] == ' '.join(a[i1:i2]) and r['B'] == ' '.join(b[j1:j2]), r
        c = r['choice'].strip(); cnt[c] += 1
        toks += a[i1:i2] if c == 'A' else b[j1:j2] if c == 'B' else ['NIL'] * max(i2 - i1, j2 - j1)
    out.append('%s %s: %s' % (k[0], k[1], ' '.join(toks)))
assert n == len(arb) == 104
names = {l.split('\t')[0] for l in open('../o2-2311/wainut-key.tsv', encoding='utf-8') if l.strip() and not l.startswith('# ')}
allt = [t for l in out for t in l.split(': ', 1)[1].split()]
nk = sum(1 for t in allt if t in names)
hdr = ('# transcription_1548-03-12_P_merged.txt - PREREG-O4 (f95a74e4...), 12 Mar 1548, cc. 5r L01-L14 + 5v L01-L30 + 6r L01-L27, 25 Nov 2026.\n'
       '# Blind pass A (2459fac4...) + blind pass B (037e227a...), agreement 0.926 (1377/1487), 104 disputes arbitrated blind by agent C\n'
       '# (A %d, B %d, neither %d -> NIL). tA-.. / tB-.. = transcribers\' own shapes (no letter). Built by tools/merge_o4.py.\n' % (cnt['A'], cnt['B'], cnt['neither']))
open('transcription_1548-03-12_P_merged.txt', 'w', encoding='utf-8').write(hdr + '\n'.join(out) + '\n')
print(len(out), 'rows', len(allt), 'tokens;', 'key-name tokens', nk, '; arbitration', cnt)
print('non-key, non-t, non-NIL names:', sorted({t for t in allt if t not in names and not t.startswith('t') and t != 'NIL'}))
