import sys,os,random,itertools
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lang import lm
M=lm.load('it-modern',order=4,spaces=False)
E=['srconpggy','lrqrlrpnqsr7g','qrqrsipqsop3g','irqpshkscel','rqlpsonspyhs','pqyqpqsqst','9qsgqxqkb3','prksyqs7qp','xinak7sqol','7nqqpypt7r','qksqrongya','7tbyhqphyv']
A=sys.argv[1]; n=len(A)
E=[e.replace('3','z') for e in E]
E=[e for e in E] 
def dec(key,restart,sign):
    out=[];i=0
    for e in E:
        if restart: i=0
        s=''
        for ch in e:
            if ch in A: s+=A[(A.index(ch)-sign*key[i%len(key)])%n]
            else: s+=ch
            i+=1
        out.append(s)
    return out
def score(ws): return sum(M.score(w) for w in ws)/sum(map(len,ws))
for restart in (True,False):
  for sign in (1,-1):
    best=(-99,)
    for per in range(2,8):
        for r in range(6):
            key=[random.randrange(n) for _ in range(per)]; s=score(dec(key,restart,sign))
            improved=True
            while improved:
                improved=False
                for j in range(per):
                    for v in range(n):
                        k2=key[:];k2[j]=v;s2=score(dec(k2,restart,sign))
                        if s2>s: key,s,improved=k2,s2,True
            if s>best[0]: best=(s,per,key,dec(key,restart,sign))
    print(restart,sign,round(best[0],3),best[1],' '.join(best[3]))
