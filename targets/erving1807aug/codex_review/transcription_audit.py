#!/usr/bin/env python3
from pathlib import Path
import re,json,csv,difflib
R=Path(__file__).resolve().parent;P=R.parent
rows=[]
for ln,l in enumerate((P/'transcription.txt').read_text().splitlines(),1):
 if l.startswith('#') or not l.strip():continue
 ref,txt=l.split('|',1);ref=ref.strip()
 # Acceptance clause is duplicated as catch-up at next page; keep only 0363L.
 if ref=='0362.3b':continue
 out=[]
 for b in re.findall(r'\[([^\]]*)(?:\]|$)',txt):
  if not re.search(r'\d|\.\.',b):continue
  b=re.sub(r'\([^)]*[A-Za-z?][^)]*\)','',b) # textual annotations including struck groups
  b=re.sub(r'\([^)]*\)',lambda m:m[0][1:-1],b) # numeric parentheses are real groups
  b=re.sub(r'\{[^}]*\}',lambda m:'X' if '..' in m[0] else m[0][1:-1],b)
  b=re.sub(r'\s+or\s+\d+\^?','',b) # keep first reading of explicit alternative
  out += [x.strip().strip('-') for x in b.split('.') if x.strip().strip('-')]
 for i,g in enumerate(out,1):rows.append(dict(ref=ref,line=ln,position=i,group=g))
with (R/'transcription_positions.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
aligned=list(csv.DictReader((R/'token_audit.tsv').open(),delimiter='\t'))
norm=lambda g:g.replace('#','').replace('^','')
x=[norm(r['group']) for r in rows];y=[norm(r['group']) for r in aligned]
diffs=[]
for tag,i,j,k,l in difflib.SequenceMatcher(a=x,b=y,autojunk=False).get_opcodes():
 if tag!='equal':diffs.append(dict(action=tag,transcription=rows[i:j],alignment=[{s:r[s] for s in ['ref','position','group','value']} for r in aligned[k:l]]))
s={'transcription_positions_after_duplicate_removed':len(rows),'alignment_entries':len(aligned),'differences':diffs}
(R/'transcription_differences.json').write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps(s,indent=2))
