import sys;sys.path.insert(0,'work')
from hsolve import *
lp=load4();pr=freqprior()
files=['cc15_16/transcription_c15r_pass1.txt','cc15_16/transcription_c15v_pass1.txt','cc15_16/transcription_c16r_pass1.txt']
def runs_mode(m):
    base=load_runs(files,'keep');out=[]
    for r in base:
        o=[]
        for x in r:
            if x in('_8','_9'):
                if (x=='_8' and m in('n8','n89')) or (x=='_9' and m in('n9','n89')):
                    if o: o.pop()
                continue
            o.append(x)
        if o: out.append(o)
    return out
for m in ('none','n8','n9','n89'):
    runs=runs_mode(m);seq,toks=encode(runs);L=int((seq>=0).sum())
    res=[anneal(seq,len(toks),lp,600000,6.0,0.4,s+1,pr,3.0) for s in range(12)]
    res.sort(key=lambda x:-x[0]);b=res[0]
    print(m,'L',L,'best',round(float(b[0])),'per letter',round(float(b[0])/L,3),[round(float(x[0])/L,2) for x in res[:4]])
    print('  ',plain(seq,b[1])[300:620])
