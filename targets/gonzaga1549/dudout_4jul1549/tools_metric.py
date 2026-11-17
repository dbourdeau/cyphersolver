import sys,random,re
def norm(s):
    s=s.lower().replace('j','i').replace('y','i').replace('v','u')
    s=re.sub('[àâä]','a',s);s=re.sub('[éèêë]','e',s);s=re.sub('[îï]','i',s);s=re.sub('[ôö]','o',s);s=re.sub('[ùûü]','u',s);s=s.replace('ç','c')
    return s
def letters(s): return re.sub('[^a-z]','',norm(s))
def load_key(p):
    K={}
    for l in open(p):
        if l.startswith('# ') or not l.strip(): continue
        a=l.rstrip('\n').split('\t'); K[a[0]]=a[1] if len(a)>1 else ''
    return K
def load_ct(p):
    toks=[]
    for l in open(p):
        if l.startswith('#') or not l.strip(): continue
        toks+=l.split()[1:]
    return toks
def decode(toks,K):
    out=[]
    for t in toks:
        v=K.get(t,'?')
        if v.startswith('['): v=v[1:-1]
        out.append(v)
    return out
def align(a,b):
    n,m=len(a),len(b)
    D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0]=i
    for j in range(m+1): D[0][j]=j
    for i in range(1,n+1):
        ai=a[i-1];Di=D[i];Dp=D[i-1]
        for j in range(1,m+1):
            Di[j]=min(Dp[j]+1,Di[j-1]+1,Dp[j-1]+(ai!=b[j-1]))
    # backtrack: which b positions matched exactly
    i,j=n,m;ok=[False]*m
    while i>0 and j>0:
        if D[i][j]==D[i-1][j-1]+(a[i-1]!=b[j-1]):
            if a[i-1]==b[j-1]: ok[j-1]=True
            i-=1;j-=1
        elif D[i][j]==D[i-1][j]+1: i-=1
        else: j-=1
    return D[n][m],ok
def metrics(dec,ref_text):
    words=[letters(w) for w in norm(ref_text).split()]
    words=[w for w in words if w]
    ref=''.join(words)
    d,ok=align(dec,ref)
    mc=max(0,1-d/len(ref))
    pos=0;good=tot=0
    for w in words:
        if len(w)>=2:
            tot+=1; good+=all(ok[pos:pos+len(w)])
        pos+=len(w)
    return mc,good/tot
if __name__=='__main__':
    ctp,keyp,refp,seed=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])
    K=load_key(keyp);toks=load_ct(ctp)
    cov=sum(1 for t in toks if t in K)/len(toks)
    dec=''.join(decode(toks,K)).replace('?','#').replace(' ','')
    dec=re.sub('[^a-z#]','',dec)
    ref=open(refp).read() if refp!='-' else None
    print('signes',len(toks),'couverture',round(cov,3))
    print('dec',' '.join(decode(toks,K)))
    if ref is None: sys.exit()
    mc,mw=metrics(dec,ref)
    print('M_car %.3f M_mots %.3f'%(mc,mw))
    rnd=random.Random(seed); syms=[k for k in K if K[k] and not K[k].startswith('[')]; vals=[K[k] for k in syms]
    W=[]
    for _ in range(200):
        v=vals[:]; rnd.shuffle(v); K2=dict(K); K2.update(zip(syms,v))
        d2=re.sub('[^a-z#]','',''.join(decode(toks,K2)).replace('?','#'))
        W.append(metrics(d2,ref))
    wc=[w[0] for w in W]; ww=[w[1] for w in W]
    print('temoins car max %.3f p99 %.3f | mots max %.3f'%(max(wc),sorted(wc)[197],max(ww)))
    print('rang car',1+sum(x>=mc for x in wc),'/201 ; rang mots',1+sum(x>=mw for x in ww),'/201')
