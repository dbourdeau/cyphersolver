import sys,os,random,math
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lang import lm
M=lm.load('it-modern',order=4,spaces=True)
OUT='abcdefgilmnopqrstuxz1234'
segs=['osor','erpii leor sglgrz hshr hyor larohgt gsg yhzy solir tzs noyp','ylior lay gnotrh ghplr agksro','zshukss','gpr sgrghs hr hqihz yz set','z','s sn qrpt',
'srcon pggy','lrqrlrpnqsr&g','qrqrsipqsop zg','irqpshkscel','rqlpsonspyh','pqyqpqs q st','qsgqxqkbz','prk syqs&qp','xin ak & sqol','&n qqpypt&r','qk sqrongya','&t by hqph yu']
if len(sys.argv)>2 and sys.argv[2]=='one': segs=[' '.join(segs)]
INN=sorted(set(''.join(segs))-{' '})
print(len(INN),''.join(INN))
INN+= [c for c in 'abcdefghijklmnopqrstuvwxyz&'  if c not in INN][:24-len(INN)]
def dec(pos,offs):
    out=[]
    for s,o in zip(segs,offs):
        out.append(''.join(OUT[(pos[c]+o)%24] if c!=' ' else ' ' for c in s))
    return out
def score(pos,offs):
    d=dec(pos,offs); t=' '.join(d); t2=t.translate(str.maketrans('','','1234'))
    return M.score(' '+t2+' ')/len(t2) - 0.3*sum(t.count(x) for x in '1234')/len(t)
best=(-99,)
for r in range(int(sys.argv[1])):
    perm=list(range(24)); random.shuffle(perm); pos=dict(zip(INN,perm)); offs=[random.randrange(24) for _ in segs]
    s=score(pos,offs); T=0.3
    for it in range(30000):
        if random.random()<0.5:
            a,b=random.sample(INN,2); pos[a],pos[b]=pos[b],pos[a]; n=score(pos,offs)
            if n>s or random.random()<math.exp((n-s)/T): s=n
            else: pos[a],pos[b]=pos[b],pos[a]
        else:
            i=random.randrange(len(segs)); o=offs[i]; offs[i]=random.randrange(24); n=score(pos,offs)
            if n>s or random.random()<math.exp((n-s)/T): s=n
            else: offs[i]=o
        T=max(0.005,T*0.9997)
    if s>best[0]: best=(s,dict(pos),list(offs))
    print(round(s,3),' | '.join(dec(pos,offs))[:240],flush=True)
print('BEST',best[0],' | '.join(dec(best[1],best[2])))
