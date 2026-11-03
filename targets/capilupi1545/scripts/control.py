# Synthetic control: real Italian, enciphered homophonically with 37 tokens, same run lengths, then solved
import sys;sys.path.insert(0,'work')
from hsolve import *
import random,time
lp=load4();pr=freqprior()
files=['cc15_16/transcription_c15r_pass1.txt','cc15_16/transcription_c15v_pass1.txt','cc15_16/transcription_c16r_pass1.txt']
runs=load_runs(files,'drop');L=sum(map(len,runs));print('runs',len(runs),'letters',L)
t=open('work/corpus.txt').read()
start=200000;txt=t[start:start+L]
homs={'a':4,'e':4,'i':4,'o':4,'n':2,'r':2,'s':2,'t':2,'l':2,'c':2,'d':2,'u':1,'p':1,'m':1,'g':1,'h':1,'f':1,'b':1,'q':1,'z':1}
tokmap={};n=0
for c,k in homs.items():
    tokmap[c]=list(range(n,n+k));n+=k
print('tokens',n)
for noise in (0.0,0.08,0.15):
    random.seed(1);seq=[];i=0;truth=[]
    for r in runs:
        for _ in r:
            c=txt[i];i+=1;truth.append(c)
            x=random.choice(tokmap[c])
            if random.random()<noise: x=random.randrange(n)
            seq.append(x)
        seq.append(-1);truth.append('|')
    seq=np.array(seq,dtype=np.int32)
    res=[]
    t0=time.time()
    for s in range(6):
        res.append(anneal(seq,n,lp,400000,6.0,0.4,s+1,pr))
    best=max(res,key=lambda x:x[0])
    p=plain(seq,best[1]);ok=sum(a==b for a,b in zip(p,truth) if b!='|')/L
    print('noise',noise,'score',round(float(best[0]),1),'acc',round(ok,3),'t',round(time.time()-t0));print(p[:160])
