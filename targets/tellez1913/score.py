from pathlib import Path
import math,random,collections,unicodedata,re,json
base=Path(__file__).resolve().parent
work=base.parents[1]
def norm(s): return re.sub('[^a-z]','',unicodedata.normalize('NFKD',s.lower()))
s=(work/'crawford_rebase/targets/esp318/lit/quijote.txt').read_text()
s=norm(s[s.index('*** START'):s.rindex('*** END')])
s=s[:len(s)*9//10]
t=collections.Counter(s[i:i+3] for i in range(len(s)-2))
b=collections.Counter(s[i:i+2] for i in range(len(s)-1))
runs=[l.split() for l in (base/'oct14.runs').read_text().splitlines()]
def score(key):
 count=adj=hits=letters=0; logp=0; out=[]; pieces=[]
 for run in runs:
  prior=''; accum=''; sub=[]
  for n in run:
   value=key.get(n,'?'); accum+=value;sub.append(value); count+=1
   if value=='?':prior='';continue
   hits+=1; letters+=len(value)
   if prior:adj+=1
   for j,c in enumerate(value):
    if j<2 and len(prior)>=2:
     g=prior[-2:]+c;logp+=math.log((t[g]+.1)/(b[g[:2]]+2.6));stat[0]+=1
    prior=(prior+c)[-2:]
  out.append(accum);pieces.append(sub)
 return dict(n=count,known=hits,adj=adj,boundary_trigrams=stat[0],score=logp/stat[0] if stat[0] else -1000,raw=out,pieces=pieces)
data={}
for label,path in [('July26',work/'batch18/mexico/diez_gloss.tsv'),('July_Oct8',base/'candidate.tsv')]:
 key=dict(x.split() for x in path.read_text().splitlines()); stat=[0]; result=score(key)
 control=[]; rng=random.Random(19131014);v=list(key.values())
 for i in range(1000):
  rng.shuffle(v);stat=[0];control.append(score(dict(zip(key,v)))['score'])
 passed=sum(x<result['score'] for x in control)
 result.update(controls_lower=passed,p=(1001-passed)/1001,q995=sorted(control)[994],maxcontrol=max(control),pass_stats=(result['known']/result['n']>=.4 and result['adj']>=10 and result['boundary_trigrams']>=12 and passed>=995))
 data[label]=result
print(json.dumps(data,indent=2))
