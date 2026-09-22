import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lang import lm
M=lm.load('it-modern',order=4,spaces=True)
E={'Ariete':'srconpggy','Taurus':'lrqrlrpnqsr7g','Gemini':'qrqrsipqsop3g','Cancer':'irqpshkscel','Leo':'rqlpsonspyhB','Virgo':'pqyqpqsqst','Libra':'9qsgqxqkb3','Scorpio':'prksyqs7qp','Sagit':'xinak7sqol','Capri':'7nqqpypt7r','Aquario':'qksqrongya','Pissis':'7tbyhqphyv'}
ALPHS=['abcdefghiklmnopqrstuxyz','abcdefghiklmnopqrstuxyz7','abcdefghiklmnopqrstuvxyz','abcdefghijklmnopqrstuvwxyz','abcdefghiklmnopqrstuvxyz379']
for name,c in E.items():
    c=c.replace('3','z').replace('B','s')
    res=[]
    for A in ALPHS:
        n=len(A)
        if any(ch not in A for ch in c): continue
        for k in range(n):
            for step in (0,1,-1,2,-2):
                p=''.join(A[(A.index(ch)-k-step*i)%n] for i,ch in enumerate(c))
                p2=p.replace('7','e').replace('9','con')
                res.append((M.per_char(' '+p2+' '),p,A[:3]+str(n),k,step))
    res.sort(reverse=True)
    print(name,c,[ (round(r[0],2),r[1],r[3],r[4]) for r in res[:4]])
