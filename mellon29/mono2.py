import sys,os,random,math
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lang import lm
M=lm.load(sys.argv[1],order=4,spaces=(os.environ.get('NOSP') is None)); alpha=[c for c in M.alpha if c!=' ']
Z='srcon pggy|lrqrlrpnqsr7g|qrqrsipqsop 3g|irqpshkscel|rqlpsonspyh B|pqyqpqs q st|9 qsgqxqkb3|prk syqs7qp|xin ak 7 sqol|7n qqpypt7r|qk sqrongya|7t by hqph yv'.replace('|',' ').replace('q','g')
A='osor rerpij leor sglgr3 hshr hyor larohgt gsg yh3y solir t3s noyp ylior lay gnotrh ghplr agksro 3shukss gpr sgrghs hr hqih3 y3 set v3 vs sn qrpt'.replace('q','g')
ct={'Z':Z,'A':A,'ZA':Z+' '+A}[sys.argv[2]]
if os.environ.get('NOSP'): ct=ct.replace(' ','')
syms=sorted(set(ct)-{' '})
def dec(k): return ''.join(k.get(c,c) for c in ct)
best=[]
for r in range(int(sys.argv[3])):
    pool=alpha[:]+random.sample(alpha,max(0,len(set(ct)-{' '})-len(alpha))); random.shuffle(pool); k={c:pool[i] for i,c in enumerate(syms)}; spare=pool[len(syms):]
    s=M.score(dec(k)); T=3.0
    for it in range(40000):
        a=random.choice(syms)
        if spare and random.random()<0.3:
            j=random.randrange(len(spare)); o=k[a]; k[a],spare[j]=spare[j],o; n=M.score(dec(k))
            if n>s or random.random()<math.exp((n-s)/T): s=n
            else: spare[j]=k[a]; k[a]=o
        else:
            b=random.choice(syms); k[a],k[b]=k[b],k[a]; n=M.score(dec(k))
            if n>s or random.random()<math.exp((n-s)/T): s=n
            else: k[a],k[b]=k[b],k[a]
        T=max(0.05,T*0.9997)
    best.append((s/len(ct),dec(k)))
for s,d in sorted(best)[-3:]: print(round(s,3),d)
