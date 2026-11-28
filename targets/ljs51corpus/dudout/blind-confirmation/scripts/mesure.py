"""MESURE UNIQUE (ljs51-aveugle). Ne s'execute qu'avec --hash-poste=<URL ou note> et si mesure/RESULTATS.tsv n'existe pas.
Verifie d'abord le MANIFEST gele. Pour chaque chaine : decodage aveugle (graine 2811), 200 temoins
(signes melanges, positions des separateurs conservees, meme solveur), accord en caracteres
(difflib, sur la plus longue chaine, lettres seules) avec le clair du compilateur.
Critere : accord >= 0.85 ET accord >= meilleur temoin + 0.30."""
import sys, os, json, random, difflib, subprocess, hashlib, time
from multiprocessing import Pool
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from common import *
from sigparse import read_sig
from solve import solve
BASE=os.path.normpath(os.path.join(HERE,'..'))
C="/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/cyphersolver-pr/clone"
REF="d8ac608093e1149f9456eaa2c99bb456ca0abc92"
LAM,R,IT,SEED,NW=8.0,20,500000,2811,200
def show(p): return subprocess.run(["git","-C",C,"show",f"{REF}:{p}"],capture_output=True,text=True,check=True).stdout
def acc(a,b):
    a=a.replace(' ',''); b=b.replace(' ','')
    m=sum(x.size for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks())
    return m/max(len(a),len(b),1)
def wacc(a,b):
    a=a.split(); b=b.split()
    m=sum(x.size for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks())
    return m/max(len(a),len(b),1)
def job(args):
    cid,i,toks,K,sp=args
    if i==0: t=toks; seed=SEED
    else:
        rnd=random.Random(SEED*100003+i); pos=[j for j,x in enumerate(toks) if x>=0]; vals=[toks[j] for j in pos]; rnd.shuffle(vals)
        t=list(toks)
        for j,v in zip(pos,vals): t[j]=v
        seed=SEED+i
    d,o,l,dec,key=solve(t,K,sp,LAM,R,IT,seed)
    return cid,i,d,o,l,dec,key
def main():
    arg=[a for a in sys.argv[1:] if a.startswith('--hash-poste=')]
    if not arg: sys.exit("refus : --hash-poste=<URL du commentaire #1023> manquant (empreinte non publiee)")
    out=os.path.join(BASE,'mesure','RESULTATS.tsv')
    if os.path.exists(out): sys.exit("refus : RESULTATS.tsv existe deja (mesure unique)")
    man=os.path.join(BASE,'gel','MANIFEST.sha256')
    for line in open(man):
        h,p=line.split(None,1); p=p.strip()
        if hashlib.sha256(open(os.path.join(BASE,p),'rb').read()).hexdigest()!=h: sys.exit("refus : fichier gele modifie : "+p)
    sel=[l.split('\t') for l in open(os.path.join(BASE,'transcriptions','SELECTION.tsv')).read().split('\n')[1:] if l]
    chains=[r[1] for r in sel if r[0] in ('L','E')]; lot={r[1]:r[0] for r in sel}
    allc={c['chain_id']:c for c in json.loads(show("targets/ljs51corpus/chains_all.json"))}
    ref={}; dkey={}
    for cid in chains:
        ke=json.loads(show(f"targets/ljs51corpus/keys_eye/{cid}.json"))
        if cid=='20r.8+47r.1': ref[cid]=' '.join(words(ke['plaintext']))
        else: ref[cid]=' '.join(words(allc[cid]['plaintext']['text']))
        dkey[cid]={lab:{norm(k):v for k,v in d.items()} for lab,d in (ke.get('key') or {}).items()}
    jobs=[]; meta={}
    for cid in chains:
        toks,K,labels=read_sig(os.path.join(BASE,'transcriptions',cid+'.sig'))
        sp=any(t<0 for t in toks); meta[cid]=(toks,K,labels,sp)
        jobs+= [(cid,i,toks,K,sp) for i in range(NW+1)]
    t0=time.time(); res={}
    with Pool(8) as p:
        for cid,i,d,o,l,dec,key in p.imap_unordered(job,jobs,chunksize=1):
            res[(cid,i)]=(d,o,l,dec,key)
    rows=[]; dis=[]
    for cid in chains:
        toks,K,labels,sp=meta[cid]; d,o,l,dec,key=res[(cid,0)]
        a=acc(dec,ref[cid]); w=wacc(dec,ref[cid])
        wit=[acc(res[(cid,i)][3],ref[cid]) for i in range(1,NW+1)]
        mw=max(wit); mean=sum(wit)/NW; sd=(sum((x-mean)**2 for x in wit)/NW)**.5
        rank=1+sum(x>=a for x in wit)
        ok = a>=0.85 and a>=mw+0.30
        n=sum(1 for t in toks if t>=0)
        rows.append([lot[cid],cid,n,K,int(sp),d,round(o,2),round(l,3),round(a,4),round(w,4),round(mw,4),round(mean,4),round((a-mean)/sd if sd else 0,2),rank,'OUI' if ok else 'NON',dec])
        if ok:
            for j,lab in enumerate(labels):
                ours=LETTERS[key[j]-1]; theirs=dkey[cid].get(lab,{})
                maj=max(theirs,key=theirs.get) if theirs else '?'
                cnt=sum(1 for t in toks if t==j)
                if ours!=maj: dis.append((cid,lab,cnt,ours,maj,json.dumps(theirs,ensure_ascii=False)))
    with open(out,'w') as f:
        f.write("lot\tchaine\tsignes\tclasses\tseparateurs\tsens_inverse\tobjectif\tlm_par_symbole\taccord_car\taccord_mots\tmeilleur_temoin\tmoyenne_temoins\tz\trang_sur_201\tvalide\tdecodage_aveugle\n")
        for r in rows: f.write('\t'.join(map(str,r))+'\n')
    with open(os.path.join(BASE,'mesure','DESACCORDS.md'),'w') as f:
        f.write("# Desaccords cle aveugle / cle de Daniel (chaines validees seulement)\n\n| chaine | signe | occurrences | aveugle | Daniel (majoritaire) | Daniel (detail) |\n|---|---|---|---|---|---|\n")
        for x in dis: f.write('| '+' | '.join(map(str,x))+' |\n')
    with open(os.path.join(BASE,'mesure','COURBE.md'),'w') as f:
        f.write("# Taux de reussite selon la longueur\n\n| tranche (signes) | chaines | validees | accord moyen |\n|---|---|---|---|\n")
        for lo,hi in [(30,45),(46,60),(61,75),(76,90),(91,120),(121,170),(171,400)]:
            s=[r for r in rows if lo<=r[2]<=hi]
            if s: f.write(f"| {lo}-{hi} | {len(s)} | {sum(r[14]=='OUI' for r in s)} | {sum(r[8] for r in s)/len(s):.2f} |\n")
        f.write("\n| classes | chaines | validees |\n|---|---|---|\n")
        for lo,hi in [(0,19),(20,22),(23,25),(26,40)]:
            s=[r for r in rows if lo<=r[3]<=hi]
            if s: f.write(f"| {lo}-{hi} | {len(s)} | {sum(r[14]=='OUI' for r in s)} |\n")
        f.write("\n| chaine | signes | classes | signes/classe | accord | meilleur temoin | valide |\n|---|---|---|---|---|---|---|\n")
        for r in sorted(rows,key=lambda r:r[2]): f.write(f"| {r[1]} | {r[2]} | {r[3]} | {r[2]/r[3]:.1f} | {r[8]:.2f} | {r[10]:.2f} | {r[14]} |\n")
    with open(os.path.join(BASE,'mesure','HEURE.txt'),'w') as f:
        f.write(f"mesure lancee apres publication : {arg[0]}\nfin UTC {time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}\nduree {time.time()-t0:.0f}s\n")
    print(open(os.path.join(BASE,'mesure','COURBE.md')).read())
if __name__=='__main__': main()
