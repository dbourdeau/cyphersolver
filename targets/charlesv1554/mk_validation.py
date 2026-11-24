"""Pairs file for docs/_validate.py: every cipher sign of Ms 1582 f. 2 in text order with the value key.tsv gives it.
Source: transcription/cipher_reconciled_AB.tsv (signe_B, valeur) and transcription/cut_lines_r24_v26.tsv
(arbitrated, value). Run from anywhere: python targets/charlesv1554/mk_validation.py (rewrites validation.tsv only)."""
import csv, pathlib, sys
T = pathlib.Path(__file__).resolve().parent
rd = lambda f: [r for r in csv.reader(open(T / 'transcription' / f, encoding='utf-8'), delimiter='\t') if r and not r[0].startswith('#')][1:]
rec, cut = rd('cipher_reconciled_AB.tsv'), rd('cut_lines_r24_v26.tsv')
lines = {}
for r in rec:
    if r[5].strip(): lines.setdefault((r[0], int(r[1])), []).append((r[5].strip(), r[8].strip()))
for r in cut:
    if r[5].strip(): lines.setdefault((r[0], int(r[1])), []).append((r[5].strip(), r[7].strip()))
out = ['# model: fr-1530-despatches',
       '# source: transcription/cipher_reconciled_AB.tsv (signe_B, valeur) and transcription/cut_lines_r24_v26.tsv (arbitrated, value)',
       '# note: the value is the one key.tsv gives the sign (the re-derived key applied mechanically), not the edited reading; made at the write-up of 24 Nov 2026']
n = 0
for page in ('r', 'v'):
    for ln in sorted(l for p, l in lines if p == page):
        out.append(f'# {page}{ln}')
        for sign, val in lines[(page, ln)]:
            val = '-' if val == '∅' else '?' if val in ('', '?') else val
            out.append(f'{sign}\t{val}'); n += 1
(T / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8', newline='\n')
print(n, 'pairs,', len(lines), 'lines')
