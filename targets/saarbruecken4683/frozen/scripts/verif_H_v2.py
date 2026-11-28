# Vérification (non décisive, après PREREG-H) : 290v arbitré v2 déchiffré par H, aligné globalement (NW) sur la concaténation des gloses de 290v (passe B)
import sys,os,re,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import norm
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','transcriptions')
H={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',17:'r',18:'s',19:'t',20:'u',21:'w',22:'i',24:'z'}
cip=[]
for l in open(os.path.join(B,'ARBITRE-H-290-v2.txt')):
    m=re.match(r'290v L\d+ \| (.*)',l.strip())
    if m: cip+=re.findall(r'\?\?|\d+\??',m.group(1))
gl=[];lines=open(os.path.join(B,'H-B-290.txt'),encoding='utf-8').read().splitlines()
for i,l in enumerate(lines):
    if l.startswith('GLOSE'):
        nxt=next((x for x in lines[i+1:] if re.match(r'290[rv] L',x)),'')
        if nxt.startswith('290v'):
            for g in re.findall(r':\s*([^;|]*)',l): gl.append(re.sub(r'\([^)]*\)|\?','',g))
ref=norm(' '.join(gl))
def dec(H): return ''.join('?' if t=='??' else H.get(int(t.rstrip('?')),'?') for t in cip)
def nw(a,b):
    n,m=len(a),len(b);prev=list(range(0,-m-1,-1));P=[]
    for i in range(1,n+1):
        cur=[-i]+[0]*m;p=bytearray(m+1);p[0]=1
        for j in range(1,m+1):
            d=prev[j-1]+(1 if a[i-1]==b[j-1] else -1);u=prev[j]-1;l=cur[j-1]-1
            if d>=u and d>=l:cur[j]=d;p[j]=0
            elif u>=l:cur[j]=u;p[j]=1
            else:cur[j]=l;p[j]=2
        P.append(p);prev=cur
    i,j=n,m;ok=0
    while i>0 and j>0:
        p=P[i-1][j]
        if p==0: ok+=a[i-1]==b[j-1];i-=1;j-=1
        elif p==1:i-=1
        else:j-=1
    return ok/n
a=nw(dec(H),ref);print('290v nombres',len(cip),'gloses car.',len(ref),'accord',round(a,4))
rng=random.Random(290);ks=list(H);ctl=[]
for _ in range(50):
    v=list(H.values());rng.shuffle(v);ctl.append(nw(dec(dict(zip(ks,v))),ref))
print('témoins(50) max',round(max(ctl),4))
