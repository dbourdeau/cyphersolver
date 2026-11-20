"""Reconcile marked groups of No. 21 strictly and retain all positions."""
import csv
import re
from pathlib import Path

p=Path(__file__).resolve().parent
base=p.parents[1]

def read(reader):
    lines={}
    for raw in (base/f'vienna21_{reader}.txt').read_text().splitlines():
        if raw.strip():
            line, *tokens=raw.split()
            assert re.fullmatch('[AB][0-9]{2}',line) and line not in lines
            lines[line]=tokens
    return lines

a,b=read('a'),read('b')
assert list(a)==list(b)==[f'A{i:02}' for i in range(1,13)]+[f'B{i:02}' for i in range(1,15)]
all_rows=[]
for line in a:
    assert len(a[line])==len(b[line])
    for idx,(one,two) in enumerate(zip(a[line],b[line]),1):
        loc=f'{line}.{idx:02}'
        normalized=one.replace('^','')
        reasons=[]
        if one!=two:reasons.append('readers differ')
        if '?' in one+two:reasons.append('reader uncertainty')
        if normalized.isdigit(): normalized+='_'
        if not reasons:assert re.fullmatch(r'[0-9]+[:ov+#_](~)?',normalized)
        all_rows.append((len(all_rows)+1,loc,one,two,'?' if reasons else normalized,', '.join(reasons)))
assert len(all_rows)==432
with (p/'groups21.tsv').open('w') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(['ordinal','position','reader_a','reader_b','strict','qualification'])
    writer.writerows(all_rows)
print('total',len(all_rows),'strict',sum(row[4]!='?' for row in all_rows),'holes',[(r[0],r[1],r[2],r[3]) for r in all_rows if r[4]=='?'])
