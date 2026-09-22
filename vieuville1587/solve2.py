import sys,random,math,collections
sys.path.insert(0,'.')
from lang import lm
m=lm.load('fr-1530-despatches')
L=[l for l in open(sys.argv[1],encoding='utf8') if not l.startswith('#')]
text=' '.join(' '.join(L).split()[1:])
syms=sorted(set(text)-{' ','?'})
F={'e':.15,'s':.08,'a':.08,'i':.075,'t':.07,'n':.07,'r':.065,'u':.065,'l':.055,'o':.05,'d':.04,'c':.033,'p':.03,'m':.028,'q':.012,'v':.015,'g':.01,'f':.011,'b':.009,'h':.008,'x':.004,'y':.004,'z':.002}
alpha=list(F)
cnt=collections.Counter(c for c in text if c in syms);N=sum(cnt.values())
def dec(key): return ''.join(key.get(c,c) for c in text)
def score(key):
  p=collections.Counter();[p.__setitem__(key[s],p[key[s]]+cnt[s]) for s in syms]
  kl=sum((p[a]/N)*math.log((p[a]/N)/F[a]) for a in p if p[a])
  return m.per_char(dec(key))-3*kl
res=[]
for rs in range(8):
  random.seed(rs);key={s:random.choice(alpha) for s in syms};sc=score(key);T=0.1
  for it in range(15000):
    s=random.choice(syms);old=key[s];key[s]=random.choice(alpha);n=score(key)
    if n>sc or random.random()<math.exp((n-sc)/T): sc=n
    else: key[s]=old
    T=max(0.003,T*0.9996)
  print(rs,round(sc,3),round(m.per_char(dec(key)),3),dec(key)[:220],flush=True)
