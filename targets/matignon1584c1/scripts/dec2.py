# dec2.py key file : décode une transcription (ignore commentaires « ␣␣# »), tokens inconnus -> ‹tok›
import sys,re
key={}
for l in open(sys.argv[1],encoding='utf-8'):
  if l.startswith('#') or not l.strip(): continue
  p=l.rstrip('\n').split('\t'); key[p[0]]=p[1]
for l in open(sys.argv[2],encoding='utf-8'):
  m=re.match(r'^([RVH]\w*):\s*(.*)$',l)
  if not m: continue
  toks=re.split(r'\s\s#',m.group(2))[0].split(); out=[]
  for t in toks:
    t=t.strip('[]'); v=key.get(t)
    if v is None: out.append('‹'+t+'›')
    elif v!='-': out.append(v if len(v)==1 else '('+v+')')
  print(m.group(1)+': '+''.join(out))
