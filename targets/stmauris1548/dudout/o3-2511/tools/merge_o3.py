"""merge_o3.py (O3) - merged transcription of c. 1v + 2r (PREREG-O3 §3), written BEFORE any decoding.
Agreed positions: the common token. Disputed positions: ARBITRAGE.tsv choice (A -> pass A tokens, B -> pass B tokens,
neither -> NIL, a name absent from the key: no letter, breaks word coverage).
N-shapes of the transcribers (N1-N8 of the c. 1r conventions, N9+ added here) are renamed tN.. (common), tA-N.. / tB-N..
(chosen from one pass), so that they never collide with WAINUT's own N-names of key.tsv: PREREG-O3 §3 'N-shapes have no
value in the key: they give no letter'. Punctuation ('.', '/', '(') and '?' are dropped exactly as compare.load does."""
import sys, os, re, difflib, csv
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'o2-2311', 'wainut-scripts'))
from compare import load
A = load('passe-A/transcription_passA.txt'); B = load('passe-B/transcription_passB.txt')
arb = {r['id']: r['choice'] for r in csv.DictReader(open('ARBITRAGE/ARBITRAGE.tsv'), delimiter='\t')}
isN = lambda t: re.fullmatch(r'N\d+', t) is not None
n = 0; out = []
for k in A:
    a, b = A[k], B[k]; toks = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            toks += ['t' + t if isN(t) else t for t in a[i1:i2]]; continue
        n += 1; c = arb['D%02d' % n]
        if c == 'A': toks += ['tA-' + t if isN(t) else t for t in a[i1:i2]]
        elif c == 'B': toks += ['tB-' + t if isN(t) else t for t in b[j1:j2]]
        else: toks += ['NIL'] * max(i2 - i1, j2 - j1)
    out.append('%s %s: %s' % (k[0], k[1], ' '.join(toks)))
assert n == len(arb) == 31
hdr = ('# transcription_1547_c1v2r_merged.txt - PREREG-O3 (fd80c823...), c. 1v L01-L26 + c. 2r L01-L09, 25 Nov 2026.\n'
       '# Blind pass A (691d2051...) + blind pass B (e3b9ae6f...), agreement 0.961 (760/791), 31 disputes arbitrated blind by\n'
       '# agent C (A 18, B 12, neither 1 -> NIL). tN.. / tA-N.. / tB-N.. = transcribers\' N-shapes (no value). Built by tools/merge_o3.py.\n')
open('transcription_1547_c1v2r_merged.txt', 'w', encoding='utf-8').write(hdr + '\n'.join(out) + '\n')
print(len(out), 'rows', sum(len(l.split(': ')[1].split()) for l in out), 'tokens')
