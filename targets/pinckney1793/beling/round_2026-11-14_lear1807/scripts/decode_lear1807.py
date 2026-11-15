"""Decode Lear's coded passages of 8 Nov and 31 Dec 1807 with Code No. 16 key v5 as it stands, and write the target's files.

Run from targets/pinckney1793:   python beling/round_2026-11-14_lear1807/scripts/decode_lear1807.py

Reads   beling/round_2026-11-14_lear1807/transcriptions/reconciled.txt
        beling/round_2026-11-11/code16_key_v5.tsv      (checked against code16_key_v5.sha256; never written)
        beling/round_2026-11-14_lear1807/local_values.tsv
Writes  beling/round_2026-11-14_lear1807/decode_v5.tsv  (one row per group)
        ct/lear_18071108.txt, ct/lear_18071231.txt      (the groups, one line per passage)
        texts/lear_18071108_decryption.txt, texts/lear_18071231_decryption.txt
The readings (texts/*_reading.txt) are written by hand from decode_v5.tsv and are not touched.
No network.
"""
import csv, hashlib, re
from pathlib import Path

T = Path(__file__).resolve().parents[3]          # targets/pinckney1793
R = T / 'beling' / 'round_2026-11-14_lear1807'
KEY = T / 'beling' / 'round_2026-11-11' / 'code16_key_v5.tsv'

want = (KEY.parent / 'code16_key_v5.sha256').read_text().split()[0]
got = hashlib.sha256(KEY.read_bytes()).hexdigest()
assert got == want, f'key v5 hash {got} != {want}'

key = {}
for r in csv.DictReader(open(KEY, encoding='utf-8'), delimiter='\t'):
    key[int(r['group'])] = (r['value'], r['grade'])
local = {}
for r in csv.DictReader((l for l in open(R / 'local_values.tsv', encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
    g = int(r['group'])
    assert g not in key, f'local value {g} is in the key'
    local[g] = (r['value'], r['basis'])

P = []
for line in open(R / 'transcriptions' / 'reconciled.txt', encoding='utf-8'):
    if line.startswith('P') and '|' in line:
        pid, date, c1, c2, ctx, groups = line.rstrip('\n').split('|')
        toks = [t for t in groups.split() if t != '--']
        P.append((pid, date, c1, c2, ctx, toks))

rows, out = [], {'8 Nov 1807': ([], []), '31 Dec 1807': ([], [])}
n_all = n_key = n_loc = 0
for pid, date, c1, c2, ctx, toks in P:
    ct, de = out[date]
    ct.append(f'{pid} ' + ' '.join(toks))
    dtoks = []
    for i, t in enumerate(toks, 1):
        caret = t.endswith('^')
        g = int(t.rstrip('^'))
        n_all += 1
        if g in key:
            v, grade = key[g]; basis = 'key v5'; n_key += 1
            shown = v + (v[-1] if caret else '')
        elif g in local:
            v, grade = local[g][0], local[g][1]; basis = 'local'; n_loc += 1
            shown = v + (v[-1] if caret else '')
        else:
            v, grade, basis, shown = '', '', 'unknown', ''
        rows.append([pid, i, g, '^' if caret else '', v, grade, basis, shown])
        dtoks.append(f'{t}={shown}' if basis == 'key v5' else (f'{t}=<{shown}>' if basis == 'local' else f'{t}=?'))
    de.append(f'{pid} ' + ' '.join(dtoks))

with open(R / 'decode_v5.tsv', 'w', encoding='utf-8', newline='\n') as f:
    f.write('# Lear 1807, group by group. value/grade from key v5 (sha256 %s...) or from local_values.tsv (basis local, grade =\n'
            '# pencil or recurrence). caret ^ doubles the last letter. shown = what the decryption files print.\n' % got[:8])
    f.write('passage\tn\tgroup\tcaret\tvalue\tgrade\tbasis\tshown\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')

HEAD_CT = ('# {title} (Code No. 16): code groups as reconciled from two copies, one line per coded passage; ^ = caret mark\n'
           '# written under the group (doubles the last letter). Clear text is left out. Source: {src}.\n'
           '# Transcription: Andrew Beling, with AI agents (beling/round_2026-11-14_lear1807/transcriptions/, 14 Nov 2026).\n')
HEAD_DE = ('# {title} (Code No. 16): decoded with key v5 as it stands (beling/round_2026-11-11/code16_key_v5.tsv, unaltered).\n'
           '# group=value from the key; group=<value> from local_values.tsv (not in the key: pencil decipherment of 1808 or fixed by\n'
           '# recurrence); group=? no value. Built by beling/round_2026-11-14_lear1807/scripts/decode_lear1807.py.\n')
docs = {'8 Nov 1807': ('lear_18071108', 'Tobias Lear to James Madison, Algiers, 8 November 1807',
                       'NARA M23 roll 9 frame 0182 and roll 10 frame 0072'),
        '31 Dec 1807': ('lear_18071231', 'Tobias Lear to James Madison, Algiers, 31 December 1807',
                        'NARA M23 roll 9 frames 0187-0199 ("Triplicate") and roll 10 frames 0075-0082 ("(Copy)")')}
for date, (doc, title, src) in docs.items():
    ct, de = out[date]
    (T / 'ct' / f'{doc}.txt').write_text(HEAD_CT.format(title=title, src=src) + '\n'.join(ct) + '\n', encoding='utf-8', newline='\n')
    (T / 'texts' / f'{doc}_decryption.txt').write_text(HEAD_DE.format(title=title) + '\n'.join(de) + '\n', encoding='utf-8', newline='\n')

print(f'groups {n_all}; key v5 values {n_key} ({n_key / n_all:.3f}); local values {n_loc}; '
      f'no value {n_all - n_key - n_loc}; distinct groups {len({r[2] for r in rows})}')
for pid, *_ , toks in P:
    k = sum(1 for r in rows if r[0] == pid and r[6] == 'key v5')
    print(f'  {pid}: {len(toks)} groups, {k} in key v5')
