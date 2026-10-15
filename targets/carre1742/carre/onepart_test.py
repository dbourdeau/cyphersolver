# Does the value order look alphabetical (one-part code)? Compare observed group frequencies with the frequency
# a one-part code list would put at that position, against random relabellings of the values.
import re,unicodedata,random,sys
from collections import Counter
sys.path.insert(0,'../../..'); sys.path.insert(0,'.')
from lang import corpora
from parse import L
txt=corpora.text(['fr-gutenberg']).lower()   # fetched and cached by lang/corpora.py
txt=unicodedata.normalize('NFD',txt); txt=''.join(ch for ch in txt if not unicodedata.combining(ch))
W=Counter(re.findall(r"[a-z]+",txt))
tot=sum(W.values())
N=int(sys.argv[1]) if len(sys.argv)>1 else 700
top=[w for w,_ in W.most_common(N)]
lst=sorted(top)
f=[W[w]/tot for w in lst]
def dens(v,k=8):
    p=(v-1)/799*(len(lst)-1); i=int(round(p))
    return max(f[max(0,i-k):i+k+1])
T=sum(L.values(),[]); c=Counter(T)
obs=[(v,n) for v,n in c.most_common(30)]
def score(pairs): return sum(n*__import__('math').log(dens(v)) for v,n in pairs)
s0=score(obs)
vals=list(range(1,801)); rs=[]
for _ in range(2000):
    rs.append(score([(random.choice(vals),n) for v,n in obs]))
print('observed',round(s0,1),'random mean',round(sum(rs)/len(rs),1),'frac random >= obs',sum(r>=s0 for r in rs)/len(rs))
for v,n in obs[:15]:
    p=int(round((v-1)/799*(len(lst)-1))); print(v,n,lst[max(0,p-4):p+5])
# Token mass per 50-value bin, observed vs what a one-part list of the same top-N French words predicts.
import numpy as np
pred=np.zeros(16); 
for i,w in enumerate(lst): pred[min(15,int(i/len(lst)*16))]+=W[w]
pred/=pred.sum()
obs_b=np.zeros(16)
for v,n in c.items(): obs_b[min(15,(v-1)//50)]+=n
obs_b/=obs_b.sum()
r=np.corrcoef(pred,obs_b)[0,1]
print('bins pred',np.round(pred*100,1)); print('bins obs ',np.round(obs_b*100,1)); print('pearson r',round(r,3))
