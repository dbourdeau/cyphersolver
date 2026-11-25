#!/usr/bin/env python3
"""Mesure P05 = plan B (PREREG-P05.md) : gloses PARTIELLES, alignement local.
Usage :
  python3 -I measure_p05.py --measure P05_SIGNES_FINAL.tsv P05_GLOSE_FINAL.tsv P05_BORDS_P03.tsv
  python3 -I measure_p05.py --list-p03     (liste des sequences P03 a faire marquer par E ; aucun decodage)
  python3 -I measure_p05.py --size P05_SIGNES_FINAL.tsv P05_GLOSE_FINAL.tsv P05_BORDS_P03.tsv  (comptes seuls, aucun decodage)
  python3 -I measure_p05.py --blank        (test a blanc sur donnees factices)
Reprend measure_p03/p04 : KEY (F -> G -> K_G25), norm, clean_gloss, ftok, decode, filtre T97, temoins graine 2380.
Nouveau (plan B) :
  - unites = sequences P dont le bord est marque 'gauche' ou 'droite' AVANT la mesure (incertaine/absent = exclue) ;
    doc. 97 (ids 443-/444-) : bord lu dans les notes de la glose ('aligne:gauche|droite|incertaine') ;
    P03 (autres ids) : bord lu dans P05_BORDS_P03.tsv (passe aveugle E) ;
  - glose -> fragments lisibles (coupes aux lacunes : '...', '..', '…', crochet isole [..], jeton fait seulement de '?') ;
    {..} retires (mots portes par K:) ; crochet colle a un mot retire sans coupure ; fragments normalises < 5 lettres retires ;
  - metrique : cout minimal d'alignement des fragments, DANS L'ORDRE, sur des sous-chaines disjointes du decodage
    (cout 1 par substitution / trou a l'interieur d'un fragment ; decodage saute gratuitement avant, entre et apres les
    fragments) = alignement local (Smith-Waterman a couts unitaires, ajustement de la glose) ; accord = 1 - S cout / S lettres ;
  - temoins cle : 200 permutations des valeurs de K_G25 (graine 2380), meme alignement ;
    temoins glose : 200 permutations des listes de fragments entre unites (graine 2381), cle K_G25, meme alignement
    (points fixes permis : conservateur) ;
  - critere : S lettres >= 300 ; accord >= 0,85 ET >= max(meilleur temoin cle, meilleur temoin glose) + 0,30 ;
    regle X: > 20 % des jetons (F+X+K) des unites -> NON CONCLUANT."""
import json, os, re, random, sys, hashlib, unicodedata
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
KG=json.load(open(os.path.join(ROOT,'kg25','K_G25.json'),encoding='utf-8'))['formes']
MAP=json.load(open(os.path.join(ROOT,'kg25','MAP_F_vers_G.json'),encoding='utf-8'))
FORMS=sorted(MAP)
KEY={f:KG[MAP[f]]['val'] for f in FORMS}
T97=os.path.join(ROOT,'transcription','T_doc97_p443.txt')
P03FILES=[os.path.join(ROOT,'p03',x) for x in ('P03_SIGNES_T2.tsv','P03_GLOSE_T2.tsv','P03X_SIGNES_A2.tsv','P03X_GLOSE_A2.tsv')]
XMAX=0.20; MINFRAG=5; NW=200; SEEDK=2380; SEEDG=2381; NMIN=300
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
# ---- repris de P03/P04 ----
def norm(s):
    s=s.lower().replace('v','u').replace('j','i').replace('y','i').replace('k','c').replace('h','')
    s=re.sub(r'[^a-z]','',s); return re.sub(r'([a-z])\1+',r'\1',s)
def clean_gloss(g):
    g=re.sub(r'\{[^}]*\}',' ',g); g=re.sub(r'\[[^\]]*\]',' ',g); return g
def ftok(t):
    t=t.rstrip('?')
    return t if re.fullmatch(r'F\d\d',t) else None
def decode(key,toks): return ''.join(key.get(ftok(t),'') if ftok(t) else '' for t in toks)
def t97_patterns(path=T97):
    P=[]
    for L in open(path,encoding='utf-8'):
        if L.startswith('#') or '|' not in L: continue
        a=[x.strip() for x in L.split('|')]
        if len(a)<3: continue
        g=norm(clean_gloss(a[2]))
        if len(g)>=3 and g!='et': P.append((a[0],g))
    return P
# ---- plan B ----
GAP='\x00'
def fragments(g):
    """glose brute -> liste ordonnee de fragments normalises (>= MINFRAG lettres)."""
    g=unicodedata.normalize('NFC',g)
    g=re.sub(r'\{[^}]*\}',' ',g)                       # mots sur K: retires (comme P03/P04)
    g=g.replace('…','...')
    g=re.sub(r'(?:(?<=\s)|^)\[[^\]]*\](?=\s|$|[.,;:])',' '+GAP+' ',g)   # crochet isole = lacune
    g=re.sub(r'\[[^\]]*\]','',g)                       # crochet colle a un mot = retire, sans coupure
    g=re.sub(r'\.{2,}',' '+GAP+' ',g)                  # '...' / '..' = lacune
    toks=[]
    for w in g.split():
        if w==GAP or re.fullmatch(r'[?]+[.,;:]*',w): toks.append(GAP)
        else: toks.append(w)
    fr=[]; cur=[]
    for w in toks+[GAP]:
        if w==GAP:
            s=norm(' '.join(cur)); cur=[]
            if len(s)>=MINFRAG: fr.append(s)
        else: cur.append(w)
    return fr
def fitcost(d,frs):
    """cout minimal : fragments dans l'ordre sur sous-chaines disjointes de d ; sauts gratuits hors fragments."""
    P=''.join(frs); m=len(P)
    if m==0: return 0
    ends=set(); k=0
    for f in frs: k+=len(f); ends.add(k)
    n=len(d); INF=10**9
    prev=[0]*(n+1)                                     # i=0 : debut libre partout
    for i in range(1,m+1):
        c=P[i-1]; cur=[prev[0]+1]+[INF]*n
        for j in range(1,n+1):
            v=prev[j-1]+(c!=d[j-1])
            if prev[j]+1<v: v=prev[j]+1
            if cur[j-1]+1<v: v=cur[j-1]+1
            cur[j]=v
        if i in ends:                                  # fragment fini : saut gratuit du decodage
            for j in range(1,n+1):
                if cur[j-1]<cur[j]: cur[j]=cur[j-1]
        prev=cur
    return min(prev)
def score(key,U,glosses=None):
    C=N=0; wh=wt=0; det=[]
    for idx,(i,toks,frs,_) in enumerate(U):
        if glosses is not None: frs=glosses[idx]
        d=norm(decode(key,toks)); m=sum(len(f) for f in frs)
        if not m: continue
        c=fitcost(d,frs); C+=c; N+=m
        ws=[w for f in frs for w in re.findall(r'[a-z]+',f)]   # fragments deja normalises : mots non recoupables
        det.append((i,d,'|'.join(frs),round(1-c/m,3)))
    return (1-C/N if N else float('nan')), det, N
def words3(key,U,raw):
    """accord en mots (non decisif) : mots de glose >= 3 lettres (normalises), pris dans les fragments retenus,
    retrouves tels quels dans le decodage normalise."""
    h=t=0
    for i,toks,frs,_ in U:
        d=norm(decode(key,toks))
        for w in raw[i]:
            if len(w)>=3: t+=1; h+=(w in d)
    return h/t if t else 0.0
def frag_words(g):
    """mots normalises des fragments retenus (pour l'accord en mots)."""
    frs=fragments(g); out=[]
    g2=unicodedata.normalize('NFC',g); g2=re.sub(r'\{[^}]*\}',' ',g2); g2=re.sub(r'\[[^\]]*\]',' ',g2); g2=re.sub(r'\.{2,}|…',' ',g2)
    for w in g2.split():
        nw=norm(w)
        if len(nw)>=3 and any(nw in f for f in frs): out.append(nw)
    return out
def key_witnesses(U):
    vals=[KEY[f] for f in FORMS]; rng=random.Random(SEEDK); W=[]
    for _ in range(NW):
        v=vals[:]; rng.shuffle(v); W.append(score(dict(zip(FORMS,v)),U)[0])
    return W
def gloss_witnesses(U):
    G=[u[2] for u in U]; rng=random.Random(SEEDG); W=[]
    for _ in range(NW):
        g=G[:]; rng.shuffle(g); W.append(score(KEY,U,g)[0])
    return W
def counts(U):
    nF=sum(1 for u in U for x in u[1] if ftok(x)); nX=sum(1 for u in U for x in u[1] if x.startswith('X:'))
    nK=sum(1 for u in U for x in u[1] if x.startswith('K:')); return nF,nX,nK
# ---- chargement ----
def read_tsv(p,ncol):
    R={}
    for L in open(p,encoding='utf-8'):
        if L.startswith('#') or '\t' not in L or L.startswith('id\t'): continue
        a=L.rstrip('\n').split('\t'); a+=['']*(ncol-len(a)); R[a[0].strip()]=a[1:]
    return R
def edge_p04(notes):
    m=re.search(r'aligne\s*:\s*(gauche|droite|incertaine)',notes.lower())
    return m.group(1) if m else 'absent'
def is97(i): return i.startswith('443-') or i.startswith('444-')
def load_all(fs,fg,fb):
    S={}; G={}
    for i,a in read_tsv(fs,2).items(): S[i]=a[0].split()
    for i,a in read_tsv(fg,4).items(): G[i]=(a[0].strip(),a[1],a[2])
    p03s=dict(read_tsv(P03FILES[0],2)); p03s.update(read_tsv(P03FILES[2],2))
    p03g=dict(read_tsv(P03FILES[1],3)); p03g.update(read_tsv(P03FILES[3],3))
    B={i:a[0].strip().lower() for i,a in read_tsv(fb,2).items()}
    rows=[]   # (id, toks, cp, gloss, edge, source)
    for i in S:
        if i in G: rows.append((i,S[i],G[i][0],G[i][1],edge_p04(G[i][2]),'P04'))
    for i,a in p03s.items():
        if i in p03g: rows.append((i,a[0].split(),p03g[i][0].strip(),p03g[i][1],B.get(i,'absent'),'P03'))
    return rows
def select(rows,P,verbose=True):
    U=[]; raw={}; ex=[]
    for i,toks,cp,g,edge,src in rows:
        if cp!='P': continue
        if edge not in ('gauche','droite'): continue
        if src=='P04' and is97(i):
            gn=norm(clean_gloss(g)); hit=[pid for pid,p in P if p in gn]
            if hit: ex.append((i,sum(1 for x in toks if ftok(x)),len(gn),hit)); continue
        frs=fragments(g)
        if not frs: continue
        U.append((i,toks,frs,src)); raw[i]=frag_words(g)
    if verbose:
        print('filtre T97 (%d motifs, doc. 97 seulement) : %d sequences exclues'%(len(P),len(ex)))
        for e in ex: print('  exclue %s F=%d lettres=%d motifs=%s'%e)
    return U,raw,ex
def report_sizes(U):
    nF,nX,nK=counts(U); N=sum(len(f) for u in U for f in u[2])
    print('unites retenues : %d  lettres de glose (fragments) : %d (seuil %d)  jetons F %d X %d K %d'%(len(U),N,NMIN,nF,nX,nK))
    for src in ('P04','P03'):
        Us=[u for u in U if u[3]==src]; c=counts(Us)
        print('  source %s : unites %d  lettres %d  F %d  X %d  K %d'%(src,len(Us),sum(len(f) for u in Us for f in u[2]),*c))
    pages=sorted({u[0].split('-')[0] for u in U})
    for pg in pages:
        Up=[u for u in U if u[0].split('-')[0]==pg]
        print('  page %s : unites %d  lettres %d  F %d'%(pg,len(Up),sum(len(f) for u in Up for f in u[2]),counts(Up)[0]))
    tot=nF+nX+nK; xs=nX/tot if tot else 0.0
    print('part X: dans les unites : %.4f (seuil %.2f)'%(xs,XMAX))
    return N,xs
def run(U,raw,label=''):
    N,xs=report_sizes(U)
    if N<NMIN: print('NON MESURABLE (< %d lettres de glose sous bord marque)'%NMIN); return 'NON MESURABLE'
    acc,det,_=score(KEY,U)
    for x in det: print('  ',x)
    gl=''.join(f for u in U for f in u[2]); bgz=sum(gl.count(c) for c in 'bgz')
    print('plafond b/g/z (absents de K_G25) : %d lettres = %.4f'%(bgz,bgz/N))
    WK=key_witnesses(U); WG=gloss_witnesses(U); sk=sorted(WK); sg=sorted(WG)
    w3=words3(KEY,U,raw)
    print('K_G25 : accord local = %.4f  (lettres %d)  mots>=3 = %.4f'%(acc,N,w3))
    print('temoins cle   (200, graine %d) : meilleur = %.4f  moyenne = %.4f  mediane = %.4f'%(SEEDK,sk[-1],sum(WK)/NW,sk[NW//2]))
    print('temoins glose (200, graine %d) : meilleur = %.4f  moyenne = %.4f  mediane = %.4f'%(SEEDG,sg[-1],sum(WG)/NW,sg[NW//2]))
    for name,sel in (('source P04 (doc. 97)',lambda u:u[3]=='P04'),('source P03',lambda u:u[3]=='P03')):
        Us=[u for u in U if sel(u)]
        if not Us: print('  [non decisif] %s : aucune unite'%name); continue
        a,_,n=score(KEY,Us); print('  [non decisif] %s : accord = %.4f (lettres %d) meilleur temoin cle = %.4f  glose = %.4f  mots>=3 = %.4f'%(
            name,a,n,max(key_witnesses(Us)),max(gloss_witnesses(Us)) if len(Us)>1 else float('nan'),words3(KEY,Us,raw)))
    for pg in sorted({u[0].split('-')[0] for u in U}):
        Up=[u for u in U if u[0].split('-')[0]==pg]; a,_,n=score(KEY,Up)
        print('  [non decisif] page %s : accord = %.4f (lettres %d, unites %d)  meilleur temoin cle = %.4f'%(pg,a,n,len(Up),max(key_witnesses(Up))))
    ok= acc>=0.85 and acc>=max(sk[-1],sg[-1])+0.30
    print('CRITERE (>= 0,85 ET >= max(temoin cle, temoin glose) + 0,30) :','VALIDE' if ok else 'NON VALIDE')
    if xs>XMAX:
        print('REGLE X: : part X: > 20 % -> NON CONCLUANT (catalogue F inadapte) ; ni validation ni infirmation'); return 'NON CONCLUANT'
    return 'VALIDE' if ok else 'NON VALIDE'
def list_p03():
    """sequences P03 (P, au moins un fragment >= 5 lettres) a soumettre a la passe aveugle E (bords) ; aucun decodage."""
    p03g=dict(read_tsv(P03FILES[1],3)); p03g.update(read_tsv(P03FILES[3],3))
    out=[(i,a[1]) for i,a in p03g.items() if a[0].strip()=='P' and fragments(a[1])]
    return out
# ---- test a blanc ----
def blank():
    inv={}
    for f in FORMS: inv.setdefault(KEY[f],f)
    enc=lambda s:[inv[c] for c in norm(s) if c in inv]
    rnd=random.Random(1)
    T=['la republica et noi sono fermati per la liberta de italia et il signor lodovico non vuole consentire',
       'il re mandera altri genti a messer francesco senza indugio perche la facenda importa molto a tutti',
       'non posso scrivere mai perche le cose di milano sono troppo incerte al presente et aspetto altre lettere',
       'dissemi che lo ambasciatore del re era molto contento di quello che si era trattato con la santita',
       'il trattato de la concordia con venetia si andava risolvendo et che la fine saria secondo il desiderio',
       'questa mattina sono stato al castello et ho lasciato il signore con la lettera di vostre signorie in mano',
       'mi pare che el duca habbia animo di tenere le genti in romagna fino a tanto che intenda la volonta',
       'el cardinale ascanio parlo lungamente meco et mostro desiderare buona amicitia con la vostra republica',
       'le provisioni fatte per terra et per mare non bastano et bisogna pensare a nuovi rimedi molto presto',
       'scrivo a vostre signorie quanto mi occorre et prego dio vi conservi in pace et prosperita lungamente',
       'il conte di caiazzo e partito questa notte con cento huomini darme verso parma secondo si dice qui',
       'molti cittadini di questa terra si lamentano delle gravezze et temono che non segua qualche tumulto',
       'aspettiamo di hora in hora la risposta di francia la quale dara forma a tutte le cose di qua']
    def mk(pref,k,t,cut,gapmid=True):
        toks=enc(t)+['X:9','K:HH']
        g=t[:cut]
        if gapmid:
            k=g.find(' ',cut//3); k2=g.find(' ',k+1); g=g[:k]+' ... '+g[k2:]     # un mot illisible au premier tiers
        return (pref,toks,'P',g+' [gloss ends]','aligne:gauche','P04' if pref.startswith('44') else 'P03')
    rows=[(i,t,c,g,edge_p04(e),s) for i,t,c,g,e,s in
          [mk('299-%02d-1'%(n+10),None,T[n],62) for n in range(6)]+[mk('158-%02d-1'%(n+16),None,T[n+6],56) for n in range(3)]+
          [mk('443-%02d-1'%(n+3),None,T[n+9],62) for n in range(2)]+[mk('444-%02d-1'%(n+1),None,T[n+11],56) for n in range(2)]]
    P=t97_patterns()
    rows.append(('443-30-1',enc('ilsignorlodouicoandauaagenoua'),'P','il signor lodovico andava a genova','gauche','P04'))  # T97 -> exclue
    rows.append(('443-31-1',enc(T[0]),'P',T[0][:50],'incertaine','P04'))   # bord incertain -> exclue
    rows.append(('443-32-1',enc(T[1]),'C',T[1],'gauche','P04'))            # C -> hors plan B
    def runrows(rs,lab):
        print('\n=== %s ==='%lab); U,raw,_=select(rs,P); return run(U,raw)
    r1=runrows(rows,'BLANC 1 : gloses partielles alignees a gauche (lacune interne), cle juste')
    # BLANC 2 : inflation de l'alignement local : gloses courtes (5-6 lettres) sur sequences longues (~80 lettres)
    rows2=[]
    for n in range(60):
        t=norm(T[n%13])+norm(T[(n+5)%13])[:20]; a=rnd.randrange(0,len(t)-6); rows2.append(('299-%02d-%d'%(n%30+5,n//30+1),enc(t)+['X:9'],'P',t[a:a+6],'gauche','P03'))
    r2=runrows(rows2,'BLANC 2 : INFLATION (gloses de 6 lettres sur ~80 lettres decodees), cle juste')
    rows2b=[]
    for n in range(70):
        t=norm(T[n%13])+norm(T[(n+4)%13])+norm(T[(n+7)%13])[:20]; a=rnd.randrange(0,len(t)-5)
        rows2b.append(('299-%02d-%d'%(n%35+3,n//35+1),enc(t),'P',t[a:a+5],'gauche','P03'))
    r2b=runrows(rows2b,'BLANC 2b : INFLATION FORTE (gloses de 5 lettres sur ~180 lettres decodees), cle juste')
    # BLANC 3 : X: 25 %
    rows3=[(i,t+['X:5']*(len(t)//3),c,g,e,s) for i,t,c,g,e,s in rows]
    r3=runrows(rows3,'BLANC 3 : meme que 1 + X: ~25 %')
    r4=runrows(rows[:3],'BLANC 4 : < 300 lettres')
    # BLANC 5 : cle fausse (sequences chiffrees avec une permutation de K_G25)
    vals=[KEY[f] for f in FORMS]; random.Random(99).shuffle(vals); bad=dict(zip(FORMS,vals)); invb={}
    for f in FORMS: invb.setdefault(bad[f],f)
    rows5=[(i,[invb.get(KEY[x],x) if ftok(x) else x for x in t],c,g,e,s) for i,t,c,g,e,s in rows]
    r5=runrows(rows5,'BLANC 5 : signes produits par une autre cle (la cle K_G25 est fausse pour eux)')
    # BLANC 6 : 30 % des jetons F remplaces au hasard (erreurs de transcription)
    rows6=[(i,[rnd.choice(FORMS) if ftok(x) and rnd.random()<0.30 else x for x in t],c,g,e,s) for i,t,c,g,e,s in rows]
    r6=runrows(rows6,'BLANC 6 : cle juste, 30 % des jetons F faux')
    rows7=[(i,[rnd.choice(FORMS) if ftok(x) and rnd.random()<0.15 else x for x in t],c,g,e,s) for i,t,c,g,e,s in rows]
    r7=runrows(rows7,'BLANC 7 : cle juste, 15 % des jetons F faux')
    # controle du decoupage en fragments
    for g in ['homo del v... [struck?] andare ... con ... remiss... ... a bologna','non pote[?] intrare[?] ... con ... bene[?] sappi',
              '[?] [?]sarebbe? ad uno?','molto potemo ?? ?? ?? [..]','{credo?} che andranno ... ... ... [struck]','per ... [ri?]sentire[?] ... lui il[?] ... bench[e?] io ... non']:
        print('fragments(%r) = %s'%(g,fragments(g)))
    print('\nRESUME BLANCS : 1',r1,'| 2',r2,'| 2b',r2b,'| 3',r3,'| 4',r4,'| 5',r5,'| 6',r6,'| 7',r7)
if __name__=='__main__':
    a=sys.argv
    if '--blank' in a: blank()
    elif '--list-p03' in a:
        L=list_p03(); print('# %d sequences P03 P avec au moins un fragment >= %d lettres'%(len(L),MINFRAG))
        for i,g in L: print(i+'\t'+g)
    elif '--size' in a or '--measure' in a:
        k=a.index('--size') if '--size' in a else a.index('--measure'); fs,fg,fb=a[k+1:k+4]
        for p in [os.path.join(ROOT,'kg25','K_G25.json'),os.path.join(ROOT,'kg25','MAP_F_vers_G.json'),T97,os.path.abspath(__file__),fs,fg,fb]+P03FILES:
            print('sha256 %s  %s'%(sha(p),os.path.basename(p)))
        rows=load_all(fs,fg,fb); U,raw,_=select(rows,t97_patterns())
        if '--size' in a: report_sizes(U)
        else: print('->',run(U,raw))
    else: print(__doc__)
