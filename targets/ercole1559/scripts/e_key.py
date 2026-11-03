import random,collections
R={}
for l in open('work/e50r_p1.txt'):
    a,b=l.split(None,1); R[int(a)]=b.split()
G={}
for l in open('work/e50r_gloss_firstread.txt'):
    a,b=l.strip().split(' ',1); G[int(a)]=b.replace(' ','').replace('v','u').replace('j','i')
def lcs_pairs(s,g):
    n,m=len(s),len(g); D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            D[i+1][j+1]=D[i][j]+1 if s[i]==g[j] else max(D[i][j+1],D[i+1][j])
    return D[n][m]
# 1. build the key from rows 1-9, table-free start: iterate alignment over a seed-free hill-climb
trainS=[x for r in range(1,10) for x in R[r]]
signs=sorted(set(x for r in R.values() for x in r if x not in '#?'))
letters='abcdefghilmnopqrstuz'
def total(key,rows):
    return sum(lcs_pairs([key.get(x,'#') for x in R[r] ],G[r]) for r in rows)
rng=random.Random(1559); best=None
for rs in range(4):
    key={s:rng.choice(letters) for s in signs}
    cur=total(key,range(1,10)); stall=0
    while stall<160:
        s=rng.choice(signs); old=key[s]; key[s]=rng.choice(letters)
        t=total(key,range(1,10))
        if t>=cur:
            if t>cur: stall=0
            cur=t
        else: key[s]=old; stall+=1
    print('restart',rs,cur,flush=True)
    if best is None or cur>best[0]: best=(cur,dict(key))
key=best[1]
tot=sum(len(G[r]) for r in range(1,10))
print('train LCS',best[0],'of gloss letters',tot)
print(sorted(key.items()))
import json; json.dump(key,open('work/key_e_rows1-9.json','w'))
# 2. frozen test on rows 10-19
hold=range(10,20)
real=total(key,hold); n=sum(len(G[r]) for r in hold); print('HELD OUT rows 10-19, LCS',real,'of',n,round(100*real/n,1))
ss=[]
vals=list(key.values())
for i in range(200):
    v=vals[:]; rng.shuffle(v); ss.append(total(dict(zip(key.keys(),v)),hold))
print('shuffled key, 200 runs: mean',round(100*sum(ss)/len(ss)/n,1),'max',round(100*max(ss)/n,1))
for r in range(1,20):
    print(f'{r:02d}',''.join(key.get(x,'?') for x in R[r]))
print('total signs',sum(len(v) for v in R.values()))
