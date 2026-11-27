# decode.py key.tsv transcription.txt -> lignes "Lnn: tok tok" au format de measure.py (lettre(s), =mot, ?)
import sys,re
key={}
for l in open(sys.argv[1],encoding='utf-8'):
  if l.startswith('#') or not l.strip(): continue
  p=l.rstrip('\n').split('\t'); key[p[0]]=p[1]
for l in open(sys.argv[2],encoding='utf-8'):
  m=re.match(r'^\s*(\w+):\s*(.+)$',l)
  if not m: continue
  out=[]
  for t in re.sub(r'\[.*?\]','',m.group(2)).split():
    v=key.get(t,'?')
    if v=='-': continue
    out.append(v)
  lab=m.group(1); n=re.sub(r'\D','',lab)
  print('L%02d: %s'%(int(n) if n else 99, ' '.join(out)))   # HV (dernière ligne f. 151v) -> L99
