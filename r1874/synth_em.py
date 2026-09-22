import random,re,em
random.seed(1)
txt=open('tx/decipherment.txt',encoding='utf8').read()
paras=[em.norm(b) for b in re.split(r'\[\d+\]',txt)[1:]]
# syllabary: CV syllables + letters; greedy longest-match encoding, 1-2 homophones for letters
syl=set()
for c in 'bcdfglmnpqrstvz':
  for v in 'aeiou': syl.add(c+v)
units=sorted(syl|set('abcdefghilmnopqrstuvxyz')|{'che','il','per','con','non','del','di'})
codes={}
pool=list(range(100,999));random.shuffle(pool)
for u in units: codes[u]=[str(pool.pop()) for _ in range(2 if len(u)==1 and u in 'aeio' else 1)]
def enc(p):
  G=[];i=0
  while i<len(p):
    for k in (3,2,1):
      if p[i:i+k] in codes: G.append(random.choice(codes[p[i:i+k]]));i+=k;break
    else: i+=1
  return G
pairs=[(enc(p),p) for p in paras]
print(sum(len(g) for g,_ in pairs),'groups')
t,_=em.run(pairs,iters=25)
inv={c:u for u,cs in codes.items() for c in cs}
ok=sum(1 for g,d in t.items() if max(d,key=d.get)==inv[g]);print('correct',ok,'/',len(t))
