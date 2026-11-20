#!/usr/bin/env python3
"""Mesure P03 (PREREG-P03-KG25.md). Usage : python3 -I measure_p03.py SIGNES_FINAL.tsv GLOSE_FINAL.tsv [--blank]
SIGNES : 'id<TAB>jetons' (jetons Fxx[?], X:..., K:...). GLOSE : 'id<TAB>C/P<TAB>glose[<TAB>notes]'.
Dans la glose : {..} = mots portes par un jeton K: (retires) ; [..] = notes editoriales (retirees).
--blank : test a blanc sur donnees factices (ne lit pas les fichiers), pour verifier le script avant gel."""
import json, os, re, random, sys
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
KG=json.load(open(os.path.join(ROOT,'kg25','K_G25.json'),encoding='utf-8'))['formes']
MAP=json.load(open(os.path.join(ROOT,'kg25','MAP_F_vers_G.json'),encoding='utf-8'))
FORMS=sorted(MAP)                                   # F01..F39
KEY={f:KG[MAP[f]]['val'] for f in FORMS}
def norm(s):
    s=s.lower().replace('v','u').replace('j','i').replace('y','i').replace('k','c').replace('h','')
    s=re.sub(r'[^a-z]','',s); return re.sub(r'([a-z])\1+',r'\1',s)
def clean_gloss(g):
    g=re.sub(r'\{[^}]*\}',' ',g); g=re.sub(r'\[[^\]]*\]',' ',g); return g
def lev(a,b):
    p=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        c=[i]
        for j,cb in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(ca!=cb)))
        p=c
    return p[-1]
def ftok(t):
    t=t.rstrip('?')
    return t if re.fullmatch(r'F\d\d',t) else None
def decode(key,toks): return ''.join(key.get(ftok(t),'') if ftok(t) else '' for t in toks)
def score(key,U):
    E=N=0; w3h=w3t=wh=wt=0; det=[]
    for i,toks,g in U:
        d=norm(decode(key,toks)); gn=norm(g)
        if not gn: continue
        e=lev(d,gn); E+=e; N+=len(gn)
        ws=[norm(w) for w in re.split(r'[\s,.;:]+',g) if norm(w)]
        wt+=len(ws); wh+=sum(w in d for w in ws)
        w3=[w for w in ws if len(w)>=3]; w3t+=len(w3); w3h+=sum(w in d for w in w3)
        det.append((i,d,gn,round(1-e/len(gn),3)))
    return (1-E/N if N else float('nan')), (w3h/w3t if w3t else 0), (wh/wt if wt else 0), det, N
def load(fs,fg):
    S={}; G={}
    for L in open(fs,encoding='utf-8'):
        if L.startswith('#') or '\t' not in L or L.startswith('id\t'): continue
        a=L.rstrip('\n').split('\t'); S[a[0].strip()]=a[1].split()
    for L in open(fg,encoding='utf-8'):
        if L.startswith('#') or '\t' not in L or L.startswith('id\t'): continue
        a=L.rstrip('\n').split('\t'); G[a[0].strip()]=(a[1].strip(),clean_gloss(a[2]))
    U=[(i,S[i],G[i][1]) for i in S if i in G and G[i][0]=='C']
    return U,S,G
def run(U,S):
    nF=sum(1 for _,t,_ in U for x in t if ftok(x)); nX=sum(1 for _,t,_ in U for x in t if x.startswith('X:'))
    nK=sum(1 for _,t,_ in U for x in t if x.startswith('K:'))
    print('sequences C :',len(U),' jetons F :',nF,' X :',nX,' K :',nK,' (seuil F >= 300)')
    if nF<300: print('NON MESURABLE (< 300 jetons F sous glose complete)'); return
    acc,w3,w,det,N=score(KEY,U)
    for x in det: print(x)
    print('glose normalisee : %d car.'%N)
    print('K_G25 : accord car. = %.4f  mots>=3 = %.4f  mots tous = %.4f'%(acc,w3,w))
    vals=[KEY[f] for f in FORMS]; rng=random.Random(2380); W=[]; W3=[]
    for _ in range(200):
        v=vals[:]; rng.shuffle(v); r=score(dict(zip(FORMS,v)),U); W.append(r[0]); W3.append(r[1])
    W.sort()
    print('temoins (200) car. : meilleur = %.4f  moyenne = %.4f  mediane = %.4f'%(W[-1],sum(W)/200,W[100]))
    print('temoins (200) mots>=3 : meilleur = %.4f  moyenne = %.4f'%(max(W3),sum(W3)/200))
    allF=[x for _,t,_ in U for x in t]; cov=sum(1 for x in allF if ftok(x))/len(allF)
    print('part des jetons couverts par le catalogue F : %.4f'%cov)
    ok= acc>=0.85 and acc>=W[-1]+0.30
    print('CRITERE (car. >= 0,85 ET >= meilleur temoin + 0,30) :','VALIDE' if ok else 'NON VALIDE')
if __name__=='__main__':
    if '--blank' in sys.argv:
        inv={}
        for f in FORMS: inv.setdefault(KEY[f],f)
        txt='lapacecolpapaetnoisonofermatiperlaliberatadeitaliaesignorlodovicononvoleconsentire'*3
        toks=[inv[c] for c in txt if c in inv]
        U=[('t1',toks+['X:9','K:HH'],txt+' {signor}')]; U=[(i,t,clean_gloss(g)) for i,t,g in U]
        run(U,None)
    else:
        U,S,G=load(sys.argv[1],sys.argv[2]); run(U,S)
