from pathlib import Path
import csv,json
from collections import Counter
P=Path(__file__).resolve().parent
rows=list(csv.DictReader((P/'transcript.tsv').open(),delimiter='\t'));key={}
for l in (P/'evidence/armylist_titlepage_1778.txt').read_text().splitlines():
 if '\t' in l:
  n,s=l.split('\t',1);key[int(n)]=''.join(c.lower() for c in s if c.isalpha() or c=='&')
wc={r['tokens']:r for r in csv.DictReader((P/'evidence/clinton_word_constraints.tsv').open(),delimiter='\t')}
out=[]
for r in rows:
 kind=r['kind'];t=r['tokens'];basis='';prediction=''
 if kind=='S':
  chars=[]
  for a,b in (v.split('-') for v in t.split()):
   try:chars.append(key[int(a)][int(b)-1])
   except (IndexError,KeyError):chars.append('?')
  prediction=''.join(chars);basis='Army List literal'
 elif kind=='W':
  w=wc.get(t)
  if w:prediction=w['local_readings'];basis='Clinton '+w['constraint_status']
  else:prediction='['+t+']';basis='uncovered word code'
 else:prediction=t;basis='already clear on cipher witness'
 out.append(dict(r,mechanical_prediction=prediction,basis=basis))
with (P/'predictions.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys(),delimiter='\t');w.writeheader();w.writerows(out)
text=['# Mechanical predictions before clear-copy consultation\n','Unchanged Army List key and frozen Clinton constraints only. Bracketed pairs are uncovered; Q{…} marks a qualified association. No contextual corrections are silently incorporated. Clear writing on the cipher page is not a prediction.\n'];loc='';words=[]
for r in out:
 if r['loc']!=loc:
  if words:text.append(' '.join(words)+'\n')
  loc=r['loc'];words=[];text.append('## '+loc+'\n')
 v=r['mechanical_prediction']
 if r['basis']=='Clinton qualified':v='Q{'+v+'}'
 if r['kind']=='C':v='⟨'+v+'⟩'
 words.append(v)
text.append(' '.join(words)+'\n')
(P/'PREDICTIONS.md').write_text('\n'.join(text))
print(json.dumps(dict(Counter(r['basis'] for r in out)),indent=2))
for r in out:
 if r['kind']=='S':print(r['order'],r['loc'],r['mechanical_prediction'])
