import re,sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from lang import lm
root=Path(__file__).parent
m=lm.load('es-golden-age',order=5,spaces=False)
name=sys.argv[1] if len(sys.argv)>1 else 'corrected'
s=(root/'cipher_draft.txt').read_text()
s=s.replace('bar8 n L','e D bar8 n L').replace('k l L e Yd L three','k l L e Yd J three')
if 'split' in name:
 for a,b in [('dc','c d'),('lb','l b'),('B','l three')]:s=re.sub(r'\b'+a+r'\b',b,s)
if 'dots' in name:
 for a,b in [('Hd','H'),('rd','r'),('ad','a'),('ud','u'),('Yd','Y')]:s=re.sub(r'\b'+a+r'\b',b,s)
parts=re.split(r'(\[[^\]]*\])',s)
syms=sorted(set(t for p in parts if not p.startswith('[') for t in p.split()))
items=[]
for p in parts:
 if p.startswith('['):items.extend(-(m.index[c]+1) for c in lm.norm(p[1:-1],'early',spaces=False))
 else:items.extend(syms.index(t) for t in p.split())
d=root/name;d.mkdir(exist_ok=True)
m.lp.tofile(d/'lm.bin')
(d/'input.txt').write_text(m.alpha+'\n'+' '.join(syms)+'\n'+' '.join(map(str,items))+'\n')
(d/'transcription.txt').write_text(s)
print(name,len(syms),sum(i>=0 for i in items))
