import sys,os,random,math,re
sys.path.insert(0,'.')
from lang import lm
m=lm.load('fr-1530-despatches')
L=[l for l in open('vieuville1587/ct_101r.txt',encoding='utf8') if not l.startswith('#')]
ct=' '.join(L).split()[1:]  # drop 'monsr'
text=' '.join(ct)
syms=sorted(set(text)-{' ','?'})
print('symbols',len(syms),''.join(syms))
# baseline: raw as French
print('raw per_char', m.per_char(lm.norm(text,'early')))
ctrl=list(text.replace(' ',''));random.shuffle(ctrl)
print('shuffled per_char', m.per_char(lm.norm(''.join(ctrl),'early')))
alpha='abcdefghilmnopqrstuxyz'
def dec(key): return ''.join(key.get(c,c) if c!=' ' else ' ' for c in text)
def score(key): return m.per_char(dec(key))
best=None
for rs in range(6):
  random.seed(rs)
  key={s:random.choice(alpha) for s in syms}; sc=score(key); T=0.05
  for it in range(12000):
    s=random.choice(syms);old=key[s];key[s]=random.choice(alpha);n=score(key)
    if n>sc or random.random()<math.exp((n-sc)/T): sc=n
    else: key[s]=old
    T=max(0.002,T*0.9996)
  print(rs,round(sc,3),dec(key)[:200])
  if best is None or sc>best[0]: best=(sc,dict(key))
