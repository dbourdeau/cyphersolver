"""Write key.tsv and key_frozen.tsv for Clave Extra 3 from work/key_all.tsv (pairs of 14.1943.1)
plus documented resolutions. Source codes: pairs = majority of aligned cipher/gloss pairs;
resolved = the aligner split a word wrongly, value set from the segment named; table = cell not
attested in any pair, value predicted from the table layout (see NOTES.md)."""
import csv
import os, pathlib
T = str(pathlib.Path(__file__).resolve().parent.parent)   # the target folder
B = T
rows = {}
for r in csv.DictReader(open(os.path.join(B, 'work', 'key_all.tsv'), encoding='utf8'), delimiter='\t'):
    rows[r['group']] = (r['value'], 'pairs', r['votes'])
res = {'46': ('ñ', 'resolved', 'S21 campaña (ñ)'), '49': ('ll', 'resolved', 'S22 ella; cell ll of the layout'),
       '87': ('para', 'resolved', 'S22 gloss "para" written small over 87'), '99': ('que', 'resolved', 'S09, S20 gloss "que"'),
       '91': ('la', 'resolved', 'S01, S07, S21 "la"'), '88': ('?', 'unread', 'S13, the gloss skips it'),
       '97': ('?', 'unread', 'S12, the gloss skips it')}
rows.update(res)
table = {'11': 'j', '13': 'h', '15': 'f', '25': 'f', '31': 'rr', '33': 'q', '36': 'ñ', '39': 'll', '43': 'q', '53': 'z'}
for g, v in table.items():
    if g not in rows: rows[g] = (v, 'table', 'not in pairs')
with open(os.path.join(B, 'key.tsv'), 'w', encoding='utf8') as f:
    f.write('group\tvalue\tsource\tevidence\n')
    for g in sorted(rows, key=int): f.write(f'{g}\t{rows[g][0]}\t{rows[g][1]}\t{rows[g][2]}\n')
with open(os.path.join(B, 'key_frozen.tsv'), 'w', encoding='utf8') as f:
    f.write('# Clave Extra 3, frozen 12 Nov 2026 before 17.2435.1 and 23.3165.1 were decrypted\ngroup\tvalue\tsource\n')
    for g in sorted(rows, key=int):
        if rows[g][0] != '?': f.write(f'{g}\t{rows[g][0]}\t{rows[g][1]}\n')
print(len(rows))
