#!/usr/bin/env python3
"""Decode Brackx's transcription (../../ciphertext.txt, digits unchanged) with the partial table key/code_table_F_partial.tsv.
Output: one line per transcription line, each group as group=value; [n] = no value in the table.
usage: python decode.py ../../ciphertext.txt ../key/code_table_F_partial.tsv > ../decryptions/decryption_1797-07-13.txt"""
import csv, sys
key = {}
for r in csv.DictReader(open(sys.argv[2], encoding='utf-8'), delimiter='\t'):
    v = r['value']
    v = {'(null)': '0', '(full stop)': '.', '(unknown)': '?'}.get(v, v)
    key[int(r['group'])] = v + ('?' if r['class'] == 'C' and v not in ('0', '?') else '')
print('# Decryption of the 653 groups (Brackx transcription, digits unchanged) with key/code_table_F_partial.tsv.')
print('# group=value; 0 null, . full stop, ? unknown sign, value? = unsure (class C); [n] = number not in the table.')
print('# Unedited output of the key. Words are not divided; see ../readings/ for the sentences.')
n = 0
for line in open(sys.argv[1], encoding='utf-8'):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    if not s[0].isdigit():
        print('## ' + s); continue
    out = []
    for g in s.split():
        n += 1
        g = int(g)
        out.append(f'{g}={key[g]}' if g in key else f'[{g}]')
    print(' '.join(out))
print(f'# {n} groups', file=sys.stderr)
