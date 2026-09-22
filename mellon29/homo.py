import sys,os,random,math
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lang import lm
model=sys.argv[1]; part=sys.argv[2]; R=int(sys.argv[3])
M=lm.load(model,order=4,spaces=True)
alpha=[c for c in M.alpha if c!=' ']
Z='srcon pggy|lrqrlrpnqsr7g|qrqrsipqsop 3g|irqpshkscel|rqlpsonspyh B|pqyqpqs q st|9 qsgqxqkb3|prk syqs7qp|xin ak 7 sqol|7n qqpypt7r|qk sqrongya|7t by hqph yv'.replace('|',' ')
A='osor rerpij leor sglgr3 hshr hyor larohgt gsg yh3y solir t3s noyp ylior lay gnotrh ghplr agksro 3shukss gpr sgrghs hr hqih3 y3 set v3 vs sn qrpt'
ct={'Z':Z,'A':A,'ZA':Z+' '+A}[part]
if len(sys.argv)>4: ct=ct.replace("q","g")
syms=sorted(set(ct)-{' '})
def dec(k): return ''.join(k.get(c,c) for c in ct)
def sc(k):
    d=dec(k); s=M.score(d)
    # penalise runs of same letter >2 and too-uniform keys
    s-=5*sum(1 for i in range(len(d)-2) if d[i]==d[i+1]==d[i+2])
    return s
res=[]
for r in range(R):
    k={s:random.choice(alpha) for s in syms}; s=sc(k); T=4.0
    for it in range(30000):
        c=random.choice(syms); o=k[c]; k[c]=random.choice(alpha); n=sc(k)
        if n>s or random.random()<math.exp((n-s)/T): s=n
        else: k[c]=o
        T=max(0.05,T*0.9997)
    res.append((s/len(ct),dec(k)))
for s,d in sorted(res)[-3:]: print(round(s,3),d)
