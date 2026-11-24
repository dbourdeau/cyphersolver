"""Verify exported witness provenance, alignment, denominators and public scores."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json

p=Path(__file__).resolve().parent
def need(condition,message):
    if not condition:
        raise SystemExit(message)
alias={'page1.txt':'oct15_visual1_page1.txt','page2.txt':'oct15_visual1_page2.txt',
       'ambiguities.txt':'oct15_visual1_ambiguities.txt','FREEZE.txt':'oct15_visual1_FREEZE.txt',
       'reading.txt':'oct15_visual2.txt'}
for rec in sorted(p.glob('*.sha256')):
    for line in rec.read_text().splitlines():
        digest,source=line.split(maxsplit=1)
        leaf=Path(source.strip()).name
        if leaf=='quijote.txt':
            continue
        dest=p/alias.get(leaf,leaf)
        need(dest.is_file(),f'Missing {dest} cited in {rec.name}')
        need(hashlib.sha256(dest.read_bytes()).hexdigest()==digest,f'Hash mismatch for {dest}')
rows=list(csv.DictReader((p/'oct15_boundaries.tsv').open(),delimiter='\t'))
tokens=(p/'oct15.runs').read_text().split()
need([r['agreed'] for r in rows]==tokens,'October 15 frozen tokens differ from alignment')
need(all(r['agreed']=='?' or r['agreed']==r['visual1']==r['visual2'] for r in rows),
     'Unagreed token counted')
need((len(tokens),tokens.count('?'))==(104,6),'October 15 denominator mismatch')
for day,scoretag in [(14,'July_Oct8'),(15,'expanded')]:
    raw=json.loads((p/f'oct{day}_results.json').read_text())[scoretag]['raw']
    wordrows=list(csv.DictReader((p/f'oct{day}_words.tsv').open(),delimiter='\t'))
    if day==14:
        rebuilt=[''.join(row['raw'] for row in wordrows if int(row['run'])==n) for n in range(1,len(raw)+1)]
        need(sum(row['status']=='sure' for row in wordrows)==7 and len(wordrows)==16,'October 14 word share')
    else:
        rebuilt=[row['raw'] for row in wordrows]
        need(sum(len(row['core_sure_words'].split()) for row in wordrows)==7
             and sum(int(row['estimated_words']) for row in wordrows)==29,'October 15 word share')
    need(rebuilt==raw,f'October {day} word ledger differs from the frozen mechanical output')
    print(f'October {day} word ledger reproduces all {len(raw)} runs')
print('Frozen input hashes and October 15 consensus verified; corpus and archive JPEGs are external.')
