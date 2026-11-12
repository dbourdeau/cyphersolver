"""Mesure unique C03 (PREREG.md). Usage: measure.py key.json holdout.txt clear.txt START SEED
D = décodage du tenu-à-l'écart par la clé (valeur absente/None -> rien, comptée inconnue).
R = clair normalisé à partir de START (fin de l'alignement de construction).
M = lettres de R couvertes par des blocs communs D/R de longueur >= 4 (difflib, autojunk=False) / len(R).
Témoins : 200 clés à valeurs permutées (mêmes chaînes, attribuées au hasard aux mêmes valeurs)
          + 200 ordres mélangés du tenu-à-l'écart (clé vraie). Graine SEED."""
import sys, json, random, difflib, re, unicodedata
def norm(s):
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z]','',s.lower())
def groups(path):
    g=[]
    for l in open(path):
        if l.startswith('L'): g+=[t for t in l.split(' ',1)[1].strip().split('.') if t]
    return g
def dec(key,G): return ''.join(key.get(t) or '' for t in G)
def M(D,R):
    sm=difflib.SequenceMatcher(None,D,R,autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size>=4)/len(R)
key=json.load(open(sys.argv[1])); H=groups(sys.argv[2])
clear=norm(''.join(l.split(' ',1)[1] for l in open(sys.argv[3]) if not l.startswith('#') and ' ' in l).replace('[?]',''))
R=clear[int(sys.argv[4]):]; rng=random.Random(int(sys.argv[5]))
D=dec(key,H); real=M(D,R)
known=sum(1 for t in H if key.get(t)); 
ctl_k=[]; vals=list(key.keys()); strs=[key[v] for v in vals]
for _ in range(200):
    s=strs[:]; rng.shuffle(s); ctl_k.append(M(dec(dict(zip(vals,s)),H),R))
ctl_s=[]
for _ in range(200):
    h=H[:]; rng.shuffle(h); ctl_s.append(M(dec(key,h),R))
mx=max(ctl_k+ctl_s)
out={'n_holdout_groups':len(H),'known_groups':known,'len_D':len(D),'len_R':len(R),'M_real':round(real,4),
     'ctl_key_max':round(max(ctl_k),4),'ctl_key_mean':round(sum(ctl_k)/200,4),
     'ctl_shuf_max':round(max(ctl_s),4),'ctl_shuf_mean':round(sum(ctl_s)/200,4),'ctl_max':round(mx,4),
     'margin':round(real-mx,4),'VALID':bool(real>=0.35 and real>mx and real-mx>=0.15),'D':D,'R':R}
print(json.dumps(out,ensure_ascii=False,indent=1))
