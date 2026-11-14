from pathlib import Path
from collections import Counter
import csv,json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=P/'SHA256SUMS';assert m.is_file(),'Missing required pre-clear manifest'
names=[]
for line in m.read_text().splitlines():
 h,n=line.split('  ',1);assert sha(P/n)==h,n;names.append(n)
assert set(names)=={str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p!=m}
for r in json.loads((P/'input_provenance.json').read_text()):assert sha(R/r['original'])==sha(P/r['copy'])==r['sha256'],r
for r in json.loads((P/'sources.json').read_text()):assert sha(P/r['file'])==r['sha256'],r
read=lambda n:list(csv.DictReader((P/n).open(),delimiter='\t'))
rows=read('transcript.tsv');pred=read('predictions.tsv');wc={r['tokens']:r for r in read('evidence/clinton_word_constraints.tsv')}
assert len(rows)==len(pred)==200 and Counter(r['kind'] for r in rows)=={'W':139,'S':43,'C':18}
key={}
for l in (P/'evidence/armylist_titlepage_1778.txt').read_text().splitlines():
 if '\t' in l:
  n,s=l.split('\t',1);key[int(n)]=''.join(c.lower() for c in s if c.isalpha() or c=='&')
for r,p in zip(rows,pred):
 for k in r:assert r[k]==p[k]
 if r['kind']=='S':
  expected=''.join(key[int(a)][int(b)-1] for a,b in (v.split('-') for v in r['tokens'].split()))
 elif r['kind']=='W':expected=wc[r['tokens']]['local_readings'] if r['tokens'] in wc else '['+r['tokens']+']'
 else:expected=r['tokens']
 assert p['mechanical_prediction']==expected,(p,expected)
counts=Counter(r['basis'] for r in pred)
assert counts=={'uncovered word code':56,'Army List literal':43,'Clinton candidate lexical constraint':58,'Clinton qualified':25,'already clear on cipher witness':18}
assert json.loads((P/'FREEZE.json').read_text())['clear_consulted'] is False
print('PASS: intact pre-clear freeze; 200 units; unchanged key and Clinton table; 43 spelled groups, 58 unqualified + 25 qualified W predictions, 56 uncovered W. No clear text in predictor.')
