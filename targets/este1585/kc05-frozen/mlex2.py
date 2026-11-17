# mlex2.py (KC03) : M5 bilingue = max(M5 fr, M5 it), même définition que mlex.py/m5.py (mots >= 5 lettres du lexique, fréquence >= 5,
# programmation dynamique, coupure sur forme sans valeur ou '?'). usage : python3 -I mlex2.py KEY CT [graine] ; témoins : 200 clés,
# valeurs d'une lettre de KEY mélangées entre formes à valeur d'une lettre (comme mlex.py), mesure bilingue appliquée à l'identique.
import sys,json,gzip,random,unicodedata
sys.path.insert(0,'/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/este-bnf-1556-1585')
from tools_metric import load_key,load_ct
B='/Users/bdudout/Documents/Veille cyber/_shared/cyphersolver/lang/lexicons/%s.json.gz'
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if c.isalpha() and ord(c)<128)
    return s.replace('j','i').replace('v','u').replace('y','i')
W={lg:{w for w in (norm(x) for x,f in json.load(gzip.open(B%lg)).items() if f>=5) if len(w)>=5} for lg in ('fr','it')}
def segs(toks,K):
    out=[];cur=''
    for t in toks:
        v=K.get(t)
        if v is None or t=='?':
            if cur: out.append(cur)
            cur=''; out.append(None); continue
        if v.startswith('['): v=v[1:-1]
        cur+=norm(v)
    if cur: out.append(cur)
    return out
def cover(s,Ws):
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        b=best[i-1]
        for L in range(5,min(18,i)+1):
            if s[i-L:i] in Ws: b=max(b,best[i-L]+L)
        best[i]=b
    return best[n]
def m5(sg,lg):
    cov=tot=0
    for x in sg:
        if x is None: tot+=1; continue
        tot+=len(x); cov+=cover(x,W[lg])
    return cov/tot if tot else 0
def bi(sg): a,b=m5(sg,'fr'),m5(sg,'it'); return max(a,b),a,b
if __name__=='__main__':
    if sys.argv[1]=='--clair':
        s=norm(open(sys.argv[2]).read()); print('clair : M5bi %.3f (fr %.3f, it %.3f)'%bi([s])); sys.exit()
    K=load_key(sys.argv[1]); toks=load_ct(sys.argv[2]); n=len(toks); c=sum(1 for t in toks if t in K and t!='?')
    m,a,b=bi(segs(toks,K)); print('signes %d, avec valeur %d (%.3f) ; M5bi = %.3f (fr %.3f, it %.3f)'%(n,c,c/n,m,a,b))
    if len(sys.argv)>3:
        lt=sorted(k for k,v in K.items() if v and not v.startswith('[') and len(v)==1); vals=[K[k] for k in lt]
        rnd=random.Random(int(sys.argv[3])); cs=[]
        for i in range(200):
            v=vals[:]; rnd.shuffle(v); K2=dict(K); K2.update(zip(lt,v)); cs.append(bi(segs(toks,K2))[0])
        cs.sort(); print('témoins (200, graine %s) : M5bi max %.3f méd %.3f ; ÉCART %.3f'%(sys.argv[3],cs[-1],cs[100],m-cs[-1]))
