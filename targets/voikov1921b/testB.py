"""Blind test: the key from message A alone, applied to message B for every interference-gap length. Control: 200 random keys at the best gap."""
import json
from joint import *
o=json.load(open('keyA3.json'));w=24
B1=load('msgB1.txt');B2=load('msgB2.txt')
res=[]
for g in range(0,121):
    m=np.concatenate((B1,np.full(g,-1),B2));s,c=score(m[mapping(len(m),w,o)]);res.append((s/max(c,1),g,c))
res.sort(reverse=True);print([(round(a,3),g) for a,g,c in res[:8]]);print('worst',round(res[-1][0],3))
g=res[0][1];m=np.concatenate((B1,np.full(g,-1),B2))
rnd=random.Random(1);R=[]
for i in range(200):
    q=o[:];rnd.shuffle(q);s,c=score(m[mapping(len(m),w,q)]);R.append(s/max(c,1))
print('random keys: mean',round(sum(R)/200,3),'best',round(max(R),3),'key A',round(res[0][0],3))
t=show(m,o);print(len(t),'gap',g)
for i in range(0,len(t),w): print(t[i:i+w])
json.dump({'gap':g},open('gapB.json','w'))
