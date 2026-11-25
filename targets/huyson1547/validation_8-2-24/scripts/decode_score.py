# C17 — décodage mécanique + score (PREREG.md). usage :
#   decode_score.py CLE TRANSCRIPTION decode            -> écrit le décodage (positions = ensembles de valeurs)
#   decode_score.py CLE TRANSCRIPTION score REFERENCE   -> score + 200 témoins (graines 1..200)
import json,re,sys,random,unicodedata
K=json.load(open(sys.argv[1]));L=K['lettres']
toks=[]
for l in open(sys.argv[2]):
    if re.match(r'^L\d:',l):toks+= [w.strip('‹›') for w in l.split(':',1)[1].split()]
def decode(lettres):
    out=[]  # liste d'ensembles
    for w in toks:
        if w in K['nulles'] or w in K['code']:continue
        if w in lettres:
            vals=lettres[w]
            if len(vals)==1 and len(vals[0])>1: out+=[{c} for c in vals[0]]  # et
            else: out.append(set(vals))
        elif w in K['nombres']: out+=[{c} for c in K['nombres'][w]]
        else: out.append({'?'})
    return out
def norm(s):
    s=unicodedata.normalize('NFD',s.lower());s=s.replace('æ','e').replace('ę','e')
    s=''.join(c for c in s if 'a'<=c<='z');return s.replace('j','i').replace('v','u')
def align(dec,ref):
    # semi-global : brèches de bout gratuites côté référence ; +1 identité, -1 substitution, -1 brèche
    n,m=len(dec),len(ref);NEG=-10**9
    S=[[0]*(m+1) for _ in range(n+1)];B=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):S[i][0]=-i;B[i][0]=1
    for i in range(1,n+1):
        di=dec[i-1];Si=S[i];Sp=S[i-1]
        for j in range(1,m+1):
            d=Sp[j-1]+(1 if ref[j-1] in di else -1);u=Sp[j]-1;l=Si[j-1]-1
            if d>=u and d>=l:Si[j]=d;B[i][j]=0
            elif u>=l:Si[j]=u;B[i][j]=1
            else:Si[j]=l;B[i][j]=2
    j=max(range(m+1),key=lambda j:S[n][j]);jend=j;i=n;ident=0;pairs=[]
    while i>0:
        b=B[i][j]
        if j==0:b=1
        if b==0:
            ok=ref[j-1] in dec[i-1];ident+=ok;pairs.append((i-1,j-1,ok));i-=1;j-=1
        elif b==1:pairs.append((i-1,None,False));i-=1
        else:pairs.append((None,j-1,False));j-=1
    jstart=j;span=jend-jstart
    return ident,span,jstart,jend,pairs[::-1]
mode=sys.argv[3]
dec=decode(L)
if mode=='decode':
    print('# positions décodées :',len(dec))
    print(''.join(sorted(s)[0] if len(s)==1 else '['+'|'.join(sorted(s))+']' for s in dec))
    sys.exit()
refraw=open(sys.argv[4]).read();ref=norm(refraw)
ident,span,js,je,pairs=align(dec,ref)
score=ident/max(len(dec),span)
# mots de la référence entièrement justes dans la tranche
words=[];pos=0;wn=[]
for w in re.findall(r"[A-Za-zÀ-ÿæę]+",refraw):
    nw=norm(w)
    if nw:words.append((pos,pos+len(nw),nw));pos+=len(nw)
okpos=set(j for i,j,ok in pairs if ok and j is not None)
inw=[w for w in words if w[0]>=js and w[1]<=je]
wok=sum(1 for a,b,_ in inw if all(p in okpos for p in range(a,b)))
print('positions décodées %d ; tranche de référence %d lettres [%d:%d] ; identités %d'%(len(dec),span,js,je,ident))
print('ACCORD CARACTÈRES = %.3f'%score)
print('accord en mots (non décisif) = %d/%d = %.3f'%(wok,len(inw),wok/max(1,len(inw))))
codes=[c for c in L if c in toks];vals=[L[c] for c in codes];T=[]
for g in range(1,201):
    r=random.Random(g);v=vals[:];r.shuffle(v);L2=dict(L);L2.update(dict(zip(codes,v)))
    d2=decode(L2);i2,s2,_,_,_=align(d2,ref);T.append(i2/max(len(d2),s2))
T.sort()
print('témoins (200) : moyenne %.3f ; médiane %.3f ; max %.3f'%(sum(T)/200,T[100],T[-1]))
print('critère : >= 0.85 et >= max témoin + 0.30 (%.3f) ->'%(T[-1]+0.30),'SUCCÈS' if score>=0.85 and score>=T[-1]+0.30 else 'ÉCHEC')
# trace d'alignement
fd=lambda s:sorted(s)[0] if len(s)==1 else '['+'|'.join(sorted(s))+']'
print('DEC:',''.join(fd(dec[i]) if i is not None else '-' for i,j,ok in pairs))
print('REF:',''.join(ref[j] if j is not None else '-' for i,j,ok in pairs))
print('    ',''.join(' ' if ok else ('^' if (i is not None and j is not None) else '·') for i,j,ok in pairs))
