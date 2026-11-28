# Mesure unique selon PREREG. Accord caractères + 200 témoins permutés (graine 4683).
import sys, os, re, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import norm
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
K=json.load(open(os.path.join(B,'CLE-K.json'),encoding='utf-8'))
L={int(k):v for k,v in K['lettres'].items()}; C={int(k):v for k,v in K['codes'].items()}
def tokens():
    T=[]
    for l in open(os.path.join(B,'transcriptions','ARBITRE-297.txt'),encoding='utf-8'):
        m=re.match(r'(29\d[rv]) L(\d+) \| (.*)',l.strip())
        if not m: continue
        s=re.sub(r'\[[^\]]*\]',' ',m.group(3))
        for t in re.findall(r'\{[^}]*\}|\?\?|\d+\??',s):
            if t.startswith('{'): T.append(('W',norm(t[1:-1])))
            elif t=='??': T.append(('N',None))
            else: T.append(('N',int(t.rstrip('?'))))
    return T
def concept():
    txt=[]
    for l in open(os.path.join(B,'transcriptions','concept-298.txt'),encoding='utf-8'):
        if l.startswith('# Ratures'): break
        m=re.match(r'298[rv] L\d+ \| (.*)',l.strip())
        if m: txt.append(re.sub(r'\[\?\]','',m.group(1)))
    return norm(' '.join(txt))
def decipher(T,L):
    s=[];flag=[]
    for k,v in T:
        if k=='W': s+=list(v); flag+=[0]*len(v)
        else:
            if v is None: w='?'
            elif v>=200: w=C.get(v,'?') or '?'
            else: w=L.get(v,'?')
            s+=list(w); flag+=[1]*len(w)
    return s,flag
def nw(a,b):
    n,m=len(a),len(b); NEG=-10**9
    prev=list(range(0,-m-1,-1)); ptr=[]
    for i in range(1,n+1):
        cur=[-i]+[0]*m; p=bytearray(m+1); p[0]=1; ai=a[i-1]
        for j in range(1,m+1):
            d=prev[j-1]+(1 if ai==b[j-1] else -1); u=prev[j]-1; l=cur[j-1]-1
            if d>=u and d>=l: cur[j]=d; p[j]=0
            elif u>=l: cur[j]=u; p[j]=1
            else: cur[j]=l; p[j]=2
        ptr.append(p); prev=cur
    i,j=n,m; match=[False]*n
    while i>0 and j>0:
        p=ptr[i-1][j]
        if p==0: match[i-1]=(a[i-1]==b[j-1]); i-=1; j-=1
        elif p==1: i-=1
        else: j-=1
    return match
def score(L):
    s,f=decipher(T,L); mt=nw(s,ref)
    tot=sum(f); ok=sum(1 for x,y in zip(mt,f) if x and y)
    return ok/tot, tot
T=tokens(); ref=concept()
acc,tot=score(L)
print('caractères chiffrés',tot,'concept',len(ref)); print('ACCORD K',round(acc,4)); sys.stdout.flush()
rng=random.Random(4683); keys=list(L.keys()); vals=list(L.values()); ctl=[]
for i in range(int(sys.argv[1]) if len(sys.argv)>1 else 200):
    v=vals[:]; rng.shuffle(v); ctl.append(score(dict(zip(keys,v)))[0])
ctl.sort()
print('témoins n',len(ctl),'max',round(ctl[-1],4),'médiane',round(ctl[len(ctl)//2],4))
print('CRITÈRE', acc>=0.85 and acc>=ctl[-1]+0.30)
s,f=decipher(T,L); open(os.path.join(B,'transcriptions','DECHIFFRE-297-K.txt'),'w').write(''.join(c.upper() if x else c for c,x in zip(s,f)))
