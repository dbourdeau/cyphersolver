# arb_dev.py key p1files p2files out : arbitrage DEV par le sens (couverture lexicale), diff par diff ; trace dans out.log
import sys,re,difflib,gzip,json
D='/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/matignon-1584-f151/'
lex=json.load(gzip.open(D+'daniel_tools/lang/lexicons/fr.json.gz'))
W={w for w,c in lex.items() if (len(w)>=3 and (c if isinstance(c,(int,float)) else 1)>=20) or w in ('a','y','de','le','la','il','en','et','ne','se','ce','qu','du','au','si','on','sa','son','les','des','ses','que','qui','luy','roy')}
key={}
for l in open(sys.argv[1],encoding='utf-8'):
  if l.startswith('#') or not l.strip(): continue
  p=l.rstrip('\n').split('\t'); key[p[0]]=p[1]
def dec(toks): return ''.join((key.get(t,'?') if key.get(t,'?')!='-' else '').replace('=','') for t in toks)
def cover(s):
  n=len(s); best=[0]*(n+1)
  for i in range(n):
    best[i+1]=max(best[i+1],best[i])
    for j in range(i+1,min(n,i+16)+1):
      if s[i:j] in W: best[j]=max(best[j],best[i]+(j-i))
  return best[n]
def load(fs):
  d={}
  for f in fs.split(','):
    for l in open(f,encoding='utf-8'):
      m=re.match(r'^([RV]\d\d):\s*(.*)$',l)
      if m: d[m.group(1)]=re.split(r'\s\s#',m.group(2))[0].split()
  return d
A=load(sys.argv[2]); B=load(sys.argv[3]); out=open(sys.argv[4],'w'); log=open(sys.argv[4]+'.log','w')
for k in sorted(A):
  if k not in B: continue
  a,b=A[k],B[k]; cur=list(a); sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
  ops=[o for o in sm.get_opcodes()]; res=[]; 
  # construire segment par segment, en choisissant pour chaque diff l'option qui couvre le mieux (contexte = ligne entière)
  choice=[]
  for op in ops:
    choice.append('a')
  def build():
    r=[]
    for op,c in zip(ops,choice):
      t,i1,i2,j1,j2=op; r+= a[i1:i2] if (t=='equal' or c=='a') else b[j1:j2]
    return r
  for idx,op in enumerate(ops):
    if op[0]=='equal': continue
    choice[idx]='a'; sa=cover(dec(build())); choice[idx]='b'; sb=cover(dec(build()))
    choice[idx]='b' if sb>sa else 'a'
    log.write(f"{k} {' '.join(a[op[1]:op[2]])!r} | {' '.join(b[op[3]:op[4]])!r} -> {choice[idx]} ({sa} vs {sb})\n")
  out.write(k+': '+' '.join(build())+'\n')
