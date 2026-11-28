"""Selection des chaines (lot L fixe + lot E tire, graine 5151) et extraction des .sig.
Le clair n'est JAMAIS affiche ; il est seulement lu pour (a) l'eligibilite (clair present)
et (b) le controle de fuite des 12-grammes (seule la proportion est imprimee)."""
import json, subprocess, sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
C = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/cyphersolver-pr/clone"
REF = "d8ac608093e1149f9456eaa2c99bb456ca0abc92"
OUT = sys.argv[1]
def show(p): return subprocess.run(["git","-C",C,"show",f"{REF}:{p}"],capture_output=True,text=True,check=True).stdout
LOT_L = ["20r.8+47r.1","22r.1","19r.7","105v.6","18r.11","23r.9","61r.3","30r.4","42r.2","39v.12"]
EXCL = {"14v.7","22v.9","37v.12","48r.8","3v.12","98v.10","1r.2","30v.7","47r.1","20r.8"}
EXCL_PREFIX = ("12v.","106v.","63v.")
BRACKETS = [(30,45),(46,60),(61,75),(76,90)]
chains = {c['chain_id']: c for c in json.loads(show("targets/ljs51corpus/chains_all.json"))}
names = [n for n in subprocess.run(["git","-C",C,"ls-tree","--name-only",REF,"targets/ljs51corpus/keys_eye/"],capture_output=True,text=True).stdout.split() if n.endswith('.json')]
def lines_of(d):
    cl = d.get('cipher_lines') or {}
    if not isinstance(cl,(dict,list)): return []
    vals = list(cl.values()) if isinstance(cl,dict) else list(cl)
    return [' '.join(v) if isinstance(v,list) else v for v in vals]
def plain_of(cid):
    c = chains.get(cid)
    if not c or not c.get('plaintext') or not isinstance(c['plaintext'],dict): return None
    if c.get('answered') != 'yes': return None
    t = c['plaintext'].get('text')
    return t if t else None
# corpus d'entrainement : 12-grammes (sans espaces)
grams=set()
for f in TRAIN:
    s=''.join(words(strip_meta(open(CORPUS+f,encoding='utf8').read())))
    for i in range(len(s)-11): grams.add(hash(s[i:i+12]))
def leak(cid):
    p=''.join(words(plain_of(cid)))
    g=[p[i:i+12] for i in range(len(p)-11)]
    return sum(hash(x) in grams for x in g)/max(1,len(g))
info={}
for n in names:
    cid=os.path.basename(n)[:-5]
    d=json.loads(show(n)); L=lines_of(d)
    toks=[t for l in L for t in l.split() if t!='|']
    info[cid]=dict(lines=L, signs=len(toks), K=len(set(toks)), plain=plain_of(cid) is not None)
rows=[]
for cid in LOT_L:
    rows.append(('L',cid,info[cid]['signs'],info[cid]['K'],info[cid]['plain'],round(leak(cid),4) if info[cid]['plain'] else None,'draw-'))
rnd=random.Random(5151)
for lo,hi in BRACKETS:
    cands=sorted(c for c,v in info.items() if lo<=v['signs']<=hi and v['plain'] and c not in EXCL and c not in LOT_L and not c.startswith(EXCL_PREFIX))
    order=rnd.sample(cands,len(cands)); kept=0
    for rank,cid in enumerate(order):
        lk=leak(cid)
        status = 'E' if (kept<2 and lk<=0.05) else ('E-fuite' if kept<2 else None)
        if status is None: break
        if status=='E': kept+=1
        rows.append((status,cid,info[cid]['signs'],info[cid]['K'],True,round(lk,4),f'{lo}-{hi}#{rank}'))
with open(os.path.join(OUT,'SELECTION.tsv'),'w') as f:
    f.write("lot\tchain\tsigns\tclasses\tclair\tfuite12\ttirage\n")
    for r in rows: f.write('\t'.join(map(str,r))+'\n')
for r in rows:
    if r[0] in ('L','E'):
        cid=r[1]
        with open(os.path.join(OUT,cid+'.sig'),'w') as f:
            f.write('\n'.join(info[cid]['lines'])+'\n')
print(open(os.path.join(OUT,'SELECTION.tsv')).read())
