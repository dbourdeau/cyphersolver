import sys, os, re, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import norm
from sw import sw_match
import importlib.util
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
K=json.load(open(os.path.join(B,'CLE-K.json'),encoding='utf-8'))
v=collections.defaultdict(collections.Counter)
for n,c in K['votes'].items():
    for ch,k in c.items(): v[int(n)%24][ch]+=k
T={}
for r in range(24):
    mc=v[r].most_common(); T[r]='?' if not mc or (len(mc)>1 and mc[0][1]==mc[1][1]) else mc[0][0]
C={int(k):x for k,x in K['codes'].items()}
json.dump({'table_mod24':T,'codes':K['codes']},open(os.path.join(B,'CLE-K24.json'),'w'),ensure_ascii=False,indent=1)
APPR={l.split('\t')[0] for f in ['T1.tsv','T2.tsv','T3.tsv','T4.tsv'] for l in open(os.path.join(B,'apprentissage',f),encoding='utf-8') if '\t' in l}
GRILLE={'297r','297v','298r','298v'}
S1=[]
for l in open(os.path.join(B,'transcriptions','ARBITRE-P3.tsv'),encoding='utf-8'):
    c=l.rstrip('\n').split('\t')
    if len(c)<3 or l.startswith('#'): continue
    assert c[0] not in APPR|GRILLE; S1.append(c[2].split())
S2=[]
for l in open(os.path.join(B,'transcriptions','ARBITRE-336-321.tsv'),encoding='utf-8'):
    c=l.rstrip('\n').split('\t')
    if len(c)<5 or l.startswith('#'): continue
    assert c[0] not in APPR|GRILLE
    if c[4]=='1': S2.append((c[2].split(),c[3]))
ref=[]
for l in open(os.path.join(B,'transcriptions','P3-C-concepts.txt'),encoding='utf-8'):
    m=re.match(r'(31[89][rv]) L\d+ \| (.*)',l.strip())
    if m: ref.append(re.sub(r'\[[^\]]*\]',' ',m.group(2)))
ref=norm(' '.join(ref))
def dec(b,T):
    s=''
    for t in b:
        if t=='??': s+='?'; continue
        n=int(t.rstrip('?'))
        s+=(C.get(n,'?') if n>=200 else T.get(n%24,'?')) if n>=40 else '?'
    return s
def nwm(a,b):
    n,m=len(a),len(b); prev=list(range(0,-m-1,-1)); P=[]
    for i in range(1,n+1):
        cur=[-i]+[0]*m; p=bytearray(m+1); p[0]=1
        for j in range(1,m+1):
            d=prev[j-1]+(1 if a[i-1]==b[j-1] else -1); u=prev[j]-1; l=cur[j-1]-1
            if d>=u and d>=l: cur[j]=d; p[j]=0
            elif u>=l: cur[j]=u; p[j]=1
            else: cur[j]=l; p[j]=2
        P.append(p); prev=cur
    i,j=n,m; ok=0
    while i>0 and j>0:
        p=P[i-1][j]
        if p==0: ok+=a[i-1]==b[j-1]; i-=1; j-=1
        elif p==1: i-=1
        else: j-=1
    return ok
def score(T):
    o1=t1=o2=t2=0
    for b in S1: s=dec(b,T); o1+=sw_match(s,ref); t1+=len(s)
    for b,g in S2: s=dec(b,T); o2+=nwm(s,norm(g)); t2+=len(s)
    return (o1+o2)/(t1+t2),o1,t1,o2,t2
nn=sum(len(b) for b in S1)+sum(len(b) for b,_ in S2)
acc,o1,t1,o2,t2=score(T)
seuil=(0.555*t1+0.85*t2)/(t1+t2)
print('table',''.join(T[r] for r in range(24)))
print('nombres',nn,'| S1',t1,'car. accord',round(o1/t1,4),'| S2',t2,'car. accord',round(o2/t2,4))
print('ACCORD GLOBAL',round(acc,4),'seuil',round(seuil,4)); sys.stdout.flush()
rng=random.Random(24683); ctl=[]
for i in range(200):
    vals=[T[r] for r in range(24)]; rng.shuffle(vals); ctl.append(score(dict(enumerate(vals)))[0])
ctl.sort(); print('témoins 200 max',round(ctl[-1],4),'médiane',round(ctl[100],4))
print('TAILLE>=300',nn>=300,'| CRITÈRE',nn>=300 and acc>=seuil and acc>=ctl[-1]+0.30)
for b in S1: print('S1',' '.join(b),'=>',dec(b,T).upper())
for b,g in S2: print('S2',g,'=>',dec(b,T).upper())
