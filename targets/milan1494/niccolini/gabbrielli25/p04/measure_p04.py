#!/usr/bin/env python3
"""Mesure P04 (PREREG-P04.md). Usage : python3 -I measure_p04.py SIGNES_FINAL.tsv GLOSE_FINAL.tsv [--blank]
= measure_p03.py (decodage, normalisation, metrique, temoins identiques) + :
  1. filtre T97 : toute sequence C dont la glose normalisee contient en entier la glose normalisee d'une des 25 sequences
     de transcription/T_doc97_p443.txt de longueur >= 3 lettres (« et » exclu) est retiree AVANT decodage (s'applique a
     toute la portion, 443 et 444, comme ecrit dans le PREREG) ;
  2. rapport separe 443-reste / 444 (ids prefixes '443-' / '444-'), non decisif ;
  3. regle X: : si les jetons X: depassent 20 % des jetons (F + X + K) des sequences C retenues -> NON CONCLUANT.
SIGNES : 'id<TAB>jetons' (jetons Fxx[?], X:..., K:...). GLOSE : 'id<TAB>C/P<TAB>glose[<TAB>notes]'.
Dans la glose : {..} = mots portes par un jeton K: (retires) ; [..] = notes editoriales (retirees).
--blank : test a blanc sur donnees factices (ne lit pas les fichiers SIGNES/GLOSE), pour verifier le script avant gel."""
import json, os, re, random, sys
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
KG=json.load(open(os.path.join(ROOT,'kg25','K_G25.json'),encoding='utf-8'))['formes']
MAP=json.load(open(os.path.join(ROOT,'kg25','MAP_F_vers_G.json'),encoding='utf-8'))
FORMS=sorted(MAP)                                   # F01..F39
KEY={f:KG[MAP[f]]['val'] for f in FORMS}
T97=os.path.join(ROOT,'transcription','T_doc97_p443.txt')
XMAX=0.20
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
def t97_patterns(path=T97):
    P=[]
    for L in open(path,encoding='utf-8'):
        if L.startswith('#') or '|' not in L: continue
        a=[x.strip() for x in L.split('|')]
        if len(a)<3: continue
        g=norm(clean_gloss(a[2]))
        if len(g)>=3 and g!='et': P.append((a[0],g))
    return P
def t97_filter(U,P):
    keep=[]; out=[]
    for i,toks,g in U:
        gn=norm(g); hit=[pid for pid,p in P if p in gn]
        (out if hit else keep).append((i,toks,g,hit))
    return [(i,t,g) for i,t,g,_ in keep], out
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
def counts(U):
    nF=sum(1 for _,t,_ in U for x in t if ftok(x)); nX=sum(1 for _,t,_ in U for x in t if x.startswith('X:'))
    nK=sum(1 for _,t,_ in U for x in t if x.startswith('K:')); return nF,nX,nK
def witnesses(U):
    vals=[KEY[f] for f in FORMS]; rng=random.Random(2380); W=[]; W3=[]
    for _ in range(200):
        v=vals[:]; rng.shuffle(v); r=score(dict(zip(FORMS,v)),U); W.append(r[0]); W3.append(r[1])
    return W,W3
def run(U0,P):
    print('sequences C avant filtre :',len(U0),' jetons F/X/K :',counts(U0))
    U,out=t97_filter(U0,P)
    print('filtre T97 (%d motifs) : %d sequences C exclues'%(len(P),len(out)))
    for i,t,g,hit in out: print('  exclue',i,'F=%d'%sum(1 for x in t if ftok(x)),'motifs',hit)
    nF,nX,nK=counts(U); tot=nF+nX+nK
    print('sequences C retenues :',len(U),' jetons F :',nF,' X :',nX,' K :',nK,' (seuil F >= 300)')
    for pg in ('443','444'):
        Up=[u for u in U if u[0].startswith(pg+'-')]; c=counts(Up)
        print('  page %s%s : sequences %d  F %d  X %d  K %d'%(pg,'-reste' if pg=='443' else '',len(Up),*c))
    other=[u[0] for u in U if not (u[0].startswith('443-') or u[0].startswith('444-'))]
    if other: print('  ATTENTION ids hors 443/444 :',other)
    xs=nX/tot if tot else 0.0
    print('part des jetons X: dans les sequences C retenues : %.4f (seuil %.2f)'%(xs,XMAX))
    if nF<300: print('NON MESURABLE (< 300 jetons F sous glose complete apres filtre T97)'); return 'NON MESURABLE'
    acc,w3,w,det,N=score(KEY,U)
    for x in det: print(x)
    gl=''.join(norm(g) for _,_,g in U); bgz=sum(gl.count(c) for c in 'bgz')
    print('glose normalisee : %d car. ; plafond b/g/z (absents de K_G25) : %d car. = %.4f'%(N,bgz,bgz/N if N else 0))
    print('K_G25 : accord car. = %.4f  mots>=3 = %.4f  mots tous = %.4f'%(acc,w3,w))
    W,W3=witnesses(U); Ws=sorted(W)
    print('temoins (200) car. : meilleur = %.4f  moyenne = %.4f  mediane = %.4f'%(Ws[-1],sum(W)/200,Ws[100]))
    print('temoins (200) mots>=3 : meilleur = %.4f  moyenne = %.4f'%(max(W3),sum(W3)/200))
    allF=[x for _,t,_ in U for x in t]; cov=sum(1 for x in allF if ftok(x))/len(allF)
    print('part des jetons couverts par le catalogue F : %.4f'%cov)
    for pg in ('443','444'):
        Up=[u for u in U if u[0].startswith(pg+'-')]
        if not Up: print('  [non decisif] page %s : aucune sequence'%pg); continue
        a,b3,b,_,n=score(KEY,Up); Wp,_=witnesses(Up)
        print('  [non decisif] page %s : car. = %.4f (glose %d car.)  mots>=3 = %.4f  meilleur temoin = %.4f'%(pg,a,n,b3,max(Wp)))
    ok= acc>=0.85 and acc>=Ws[-1]+0.30
    print('CRITERE (car. >= 0,85 ET >= meilleur temoin + 0,30) :','VALIDE' if ok else 'NON VALIDE')
    if xs>XMAX:
        print('REGLE X: : part X: > 20 % -> NON CONCLUANT (catalogue F inadapte a la main de Niccolini) ; ne vaut ni validation ni infirmation')
        return 'NON CONCLUANT'
    return 'VALIDE' if ok else 'NON VALIDE'
if __name__=='__main__':
    if '--blank' in sys.argv:
        inv={}
        for f in FORMS: inv.setdefault(KEY[f],f)
        P=t97_patterns()
        txt='larepublicaetnoisonofermatiperlaliberatadeitaliaesignorlodovicononvuoleconsentire'
        txt2='ilremandaraaltrigentiamesserfrancescosenzaindugioperchelafacendaimportamoltoatutti'
        enc=lambda s:[inv[c] for c in s if c in inv]
        U=[('443-01-1',enc(txt)+['X:9','K:HH'],txt+' {signor}'),('443-02-1',enc(txt2),txt2),
           ('444-01-1',enc(txt2)+['X:5'],txt2),('444-02-1',enc(txt),txt),
           ('443-03-1',enc('ilsignorlodovicoandavaagenova'),'il signor lodovico andava a genova'),  # doit etre exclue (andava, agenova)
           ('443-04-1',enc(txt2)*2,txt2*2)]
        U=[(i,t,clean_gloss(g)) for i,t,g in U]
        print('BLANC 1 (donnees factices)'); print('->',run(U,P))
        print('\nBLANC 2 (meme chose, 25 % de X:)')
        U2=[(i,t+['X:5']*(len(t)//3),g) for i,t,g in U]; print('->',run(U2,P))
        print('\nBLANC 3 (< 300 F)'); print('->',run(U[:2],P))
    else:
        U,S,G=load(sys.argv[1],sys.argv[2]); run(U,t97_patterns())
