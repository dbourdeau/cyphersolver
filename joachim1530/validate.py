"""Positive control: same length and line breaks, known simple substitution."""
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from lang import lm
from joachim1530.solve import PLAIN,load
from joachim1530.fastsolve import run

model=lm.load("it-cinquecento",order=4,spaces=False)
lengths=[len(x) for x in load("joachim1530/ciphertext.txt")]
raw=Path("lang/corpora/it-renaissance.txt").read_text(encoding="utf-8",errors="ignore")
norm=lm.norm(raw,"early",False)
plain="".join(c for c in norm[5000:] if c in PLAIN)[:sum(lengths)]
assert len(plain)==sum(lengths)
pi={c:i for i,c in enumerate(PLAIN)}
rng=np.random.default_rng(122)
enc_key=rng.permutation(len(PLAIN))
enc=[int(enc_key[pi[c]]) for c in plain]
noise=float(sys.argv[4]) if len(sys.argv)>4 else 0.0
for p in range(len(enc)):
    if rng.random()<noise:
        enc[p]=int(rng.integers(len(PLAIN)))
items=[];offset=0
for n in lengths:
    items.append(enc[offset:offset+n]);offset+=n
order=4
windows=np.array([item[i:i+order] for item in items for i in range(len(item)-order+1)],dtype=np.int64)
nsym=len(PLAIN)
touch=np.zeros((nsym,nsym,len(windows)),dtype=np.int64)
tlen=np.zeros((nsym,nsym),dtype=np.int64)
for a in range(nsym):
    for b in range(nsym):
        ids=np.flatnonzero(np.any((windows==a)|(windows==b),axis=1))
        touch[a,b,:len(ids)]=ids;tlen[a,b]=len(ids)
power=np.array([model.A**(order-1-i) for i in range(order)],dtype=np.int64)
letters=np.array([model.index[c] for c in PLAIN],dtype=np.int64)
truekey=np.zeros(nsym,dtype=np.int64)
for i,j in enumerate(enc_key):truekey[j]=letters[i]
true_score=float(model.lp[(truekey[windows]*power).sum(axis=1)].sum())
score,key,local=run(windows,touch,tlen,model.lp,power,letters,int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
accuracy=sum(key[x]==truekey[x] for x in set(enc))
print("NOISE",noise,"TRUE_SCORE",round(true_score,2),"BEST",round(score,2),"ACCURACY",accuracy,"/",len(set(enc)))
print("PLAINTEXT",plain[:120])
print("RECOVERED","".join(model.alpha[int(key[x])] for x in enc[:120]))
