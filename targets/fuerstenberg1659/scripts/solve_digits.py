# Hill-climb: cipher letter -> digit (homophonic), pairs -> key numbers -> plain letters; score with German trigrams
import re,sys,math,random,collections
B=sys.argv[1]; seed=int(sys.argv[2]) if len(sys.argv)>2 else 1
random.seed(seed)
KEY={'10':'a','12':'b','16':'c','30':'d','79':'e','80':'f','17':'g','60':'h','13':'i','45':'k','50':'l','24':'m','36':'n','22':'o','33':'p','42':'q','18':'r','15':'s','44':'t','64':'u','46':'w','39':'x','28':'y','56':'z'}
raw=open(B+'/work/corpus_raw.txt',encoding='utf8').read().lower()
lines=[l for l in raw.split('\n') if len(re.findall(r'\b(und|der|die|das|daß|dass|nicht|mit|sich|ich|zu|den)\b',l))>=2]
txt=re.sub(r'[^a-zäöüß]','',' '.join(lines))
txt=txt.replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','s').replace('j','i').replace('v','u')
tri=collections.Counter(txt[i:i+3] for i in range(len(txt)-2)); N=sum(tri.values())
def lp(g): return math.log((tri.get(g,0)+0.1)/N)
D={}
for l in open(B+'/transcription_fuerstenberg1659_pass1.txt',encoding='utf8'):
  if '\t' in l and not l.startswith('#'):
    a,b=l.strip().split('\t'); D[a]=re.sub(r'[^a-z]','',b)
P=[D['85.1']+D['85.2'],D['85.3']+D['85.4']+D['85.5'],D['85.6']+D['85.7']+D['85.8']+D['85.9']+D['85.10'],D['86.1']+D['86.2'],D['86.3']+D['86.4']+D['86.5']]
letters=sorted(set(''.join(P)))
def dec(m):
  out=[]
  for p in P:
    s=''
    for i in range(0,len(p)-1,2):
      s+=KEY.get(m[p[i]]+m[p[i+1]],'#')
    out.append(s)
  return out
def score(m):
  sc=0
  for s in dec(m):
    sc+=s.count('#')*-12
    for i in range(len(s)-2):
      g=s[i:i+3]
      if '#' not in g: sc+=lp(g)
  return sc
best=None
for restart in range(30):
  m={c:str(random.randint(0,9)) for c in letters}
  cur=score(m); T=5.0
  for it in range(20000):
    c=random.choice(letters); old=m[c]; m[c]=str(random.randint(0,9))
    s=score(m)
    if s>cur or random.random()<math.exp((s-cur)/T): cur=s
    else: m[c]=old
    T=max(0.05,T*0.9997)
  if best is None or cur>best[0]: best=(cur,dict(m)); print(restart,round(cur,1),dec(m))
print(best)
