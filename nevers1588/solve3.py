import sys,random,math
sys.path.insert(0,'..')
from lang import lm
from collections import Counter
mode=sys.argv[1]  # 'space' or 'null' or 'letter'
m=lm.load('fr-1530-despatches',order=5,spaces=(mode=='space'))
runs=[l.strip() for l in open('runs.txt') if l.strip()]
syms=sorted(set(''.join(runs)))
fixed={}
if mode=='space': fixed['i']=' '
if mode=='null': fixed['i']=''
letters='abcdefghilmnopqrstuxyz'
FR=dict(e=.16,s=.08,a=.08,i=.07,t=.07,n=.07,r=.07,u=.06,l=.055,o=.05,d=.04,c=.03,m=.03,p=.03,q=.012,f=.012,v=.01,b=.01,g=.01,h=.008,x=.004,y=.004,z=.002)
def dec(k,r): return ''.join(k[c] for c in r)
def score(k):
    txt=[dec(k,r) for r in runs]
    s=sum(m.score(' '+t+' ' if mode=='space' else t) for t in txt)
    all_=''.join(txt).replace(' ','');n=len(all_);c=Counter(all_)
    pen=sum(v*math.log(v/n/FR.get(ch,.002)) for ch,v in c.items())
    return s-3*pen
for rs in range(int(sys.argv[2])):
    random.seed(rs)
    k={c:random.choice(letters) for c in syms}; k.update(fixed)
    free=[c for c in syms if c not in fixed]
    s=score(k);T=5.0
    for it in range(200000):
        c=random.choice(free);old=k[c];k[c]=random.choice(letters)
        ns=score(k)
        if ns>s or random.random()<math.exp((ns-s)/T): s=ns
        else: k[c]=old
        T=max(0.05,T*0.99997)
    print(rs,round(s,1),' | '.join(dec(k,r) for r in runs),flush=True)
    print('  ',' '.join(f'{c}={k[c]}' for c in free),flush=True)
