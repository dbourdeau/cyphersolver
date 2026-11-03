import json,random,re
import numpy as np
A='abcdefghilmnopqrstuz'; idx={c:i for i,c in enumerate(A)}
Q=np.load('scans/corpus/q4.npy')
kA=json.load(open('work/key_A.json')); kB=json.load(open('work/key_B.json'))
com=[s for s in kA if s in kB and s not in '#&hi3S']
print('agree',[(s,kA[s],kB[s]) for s in com if kA[s]==kB[s]])
print('differ',[(s,kA[s],kB[s]) for s in com if kA[s]!=kB[s]])
ct=open('work/half_B.txt').read().replace('3','B')
def sc(pt):
    P=np.array([idx[c] for c in pt]); return Q[P[:-3],P[1:-2],P[2:-1],P[3:]].mean()
dec=lambda k:''.join(k.get(c,'e') for c in ct)
t=dec(kA); print('half B under key frozen from half A:',t[:170]); real=sc(t)
print('score per quadgram',round(float(real),3))
rng=random.Random(1); ss=[]
vals=list(kA.values())
for i in range(200):
    v=vals[:]; rng.shuffle(v); ss.append(sc(dec(dict(zip(kA.keys(),v)))))
print('200 shuffled key values: mean',round(float(np.mean(ss)),3),'best',round(float(max(ss)),3))
# fraction of plaintext letters covered by dictionary words from period corpus, longest-match
import unicodedata
exec(open('scripts/words.py').read()) if False else None
