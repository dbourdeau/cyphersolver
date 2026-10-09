from pathlib import Path
import re,collections
P=Path(__file__).resolve().parent.parent
for l in (P/'transcription.txt').read_text().splitlines():
 if l.startswith('#') or not l.strip():continue
 r,txt=l.split('|',1);out=[]
 for b in re.findall(r'\[([^\]]*)(?:\]|$)',txt):
  if not re.search(r'\d|\.\.',b):continue
  b=re.sub(r'\([^)]*[A-Za-z?][^)]*\)','',b)
  b=re.sub(r'\([^)]*\)',lambda m:m[0][1:-1],b)
  b=re.sub(r'\{[^}]*\}',lambda m: 'X' if '..' in m[0] else m[0][1:-1],b)
  b=re.sub(r'\s+or\s+\d+\^?','',b)
  for x in b.split('.'):
   x=x.strip().strip('-')
   if x:out.append(x)
 print(r.strip(),len(out), ' '.join(out))
