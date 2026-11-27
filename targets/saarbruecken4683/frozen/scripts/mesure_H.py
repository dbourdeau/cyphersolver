# PREREG-H : clé H = majorité sur les paires [sur nombres] : glose de 290r (passe A, longueur égale) ; test groupe par groupe sur 290v.
import sys, os, re, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import norm
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','transcriptions')
def pairs(fol):
    P=[]; cur=None
    for l in open(os.path.join(B,'H-A-290.txt'),encoding='utf-8'):
        m=re.match(r'(290[rv]) L',l)
        if m: cur=m.group(1)
        if l.startswith('GLOSE'):
            nxt=fol  # gloses précèdent la ligne ; dossier déterminé par la ligne suivante -> on garde la section courante
            for nums,g in re.findall(r'\[sur ([^\]]*)\]\s*:\s*([^|]*)',l):
                nums=re.sub(r',\s*L\d+','',nums).replace('/',' ')
                toks=re.findall(r'\?\?|\d+\??',nums); g=g.strip()
                if toks and '?' not in g: P.append((cur,toks,g))
    return P
allp=pairs(None)
# une glose avant 290r L01 a cur=None ; une glose avant 290v L01 a cur='290r' -> rattacher par position : on reprend la section de la ligne SUIVANTE
lines=open(os.path.join(B,'H-A-290.txt'),encoding='utf-8').read().splitlines(); P=[]
for i,l in enumerate(lines):
    if not l.startswith('GLOSE'): continue
    fol=next((re.match(r'(290[rv]) L',x).group(1) for x in lines[i+1:] if re.match(r'290[rv] L',x)),None)
    for nums,g in re.findall(r'\[sur ([^\]]*)\]\s*:\s*([^|]*)',l):
        nums=re.sub(r',\s*L\d+','',nums).replace('/',' ')
        toks=re.findall(r'\?\?|\d+\??',nums); g=g.strip()
        if toks and '?' not in g and fol: P.append((fol,toks,g))
train=[p for p in P if p[0]=='290r']; test=[p for p in P if p[0]=='290v']
V=collections.defaultdict(collections.Counter); used=0
for _,t,g in train:
    gn=norm(g)
    if len(gn)!=len(t): continue
    for n,c in zip(t,gn):
        if '?' not in n: V[int(n)][c]+=1; used+=1
H={}
for n,c in V.items():
    mc=c.most_common(); H[n]='?' if len(mc)>1 and mc[0][1]==mc[1][1] else mc[0][0]
print('clé H',' '.join(f'{n}={H[n]}' for n in sorted(H)),'| paires',used)
def dec(t,H): return ''.join('?' if x=='??' else H.get(int(x.rstrip('?')),'?') for x in t)
def nwm(a,b):
    n,m=len(a),len(b); prev=list(range(0,-m-1,-1)); P2=[]
    for i in range(1,n+1):
        cur=[-i]+[0]*m; p=bytearray(m+1); p[0]=1
        for j in range(1,m+1):
            d=prev[j-1]+(1 if a[i-1]==b[j-1] else -1); u=prev[j]-1; l=cur[j-1]-1
            if d>=u and d>=l: cur[j]=d; p[j]=0
            elif u>=l: cur[j]=u; p[j]=1
            else: cur[j]=l; p[j]=2
        P2.append(p); prev=cur
    i,j=n,m; ok=0
    while i>0 and j>0:
        p=P2[i-1][j]
        if p==0: ok+=a[i-1]==b[j-1]; i-=1; j-=1
        elif p==1: i-=1
        else: j-=1
    return ok
def score(H):
    ok=tot=0
    for _,t,g in test: s=dec(t,H); ok+=nwm(s,norm(g)); tot+=len(s)
    return ok/tot,tot
acc,tot=score(H); print('test 290v groupes',len(test),'caractères',tot,'ACCORD',round(acc,4))
rng=random.Random(290); ks=list(H); vs=list(H.values()); ctl=[]
for i in range(200): v=vs[:]; rng.shuffle(v); ctl.append(score(dict(zip(ks,v)))[0])
ctl.sort(); print('témoins max',round(ctl[-1],4),'médiane',round(ctl[100],4))
print('TAILLE>=300',tot>=300,'CRITÈRE',tot>=300 and acc>=0.85 and acc>=ctl[-1]+0.30)
