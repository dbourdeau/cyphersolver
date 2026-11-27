# PREREG-3 : K' (table mod 24 depuis les votes de CLE-K.json), mesure unique sur ARBITRE-P3.tsv vs P3-C-concepts (318r+318v+319r)
import sys, os, re, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import norm
from sw import sw_match
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
GRILLE={'297r','297v','298r','298v','336r','321r'}
blocks=[]
for l in open(os.path.join(B,'transcriptions','ARBITRE-P3.tsv'),encoding='utf-8'):
    c=l.rstrip('\n').split('\t')
    if len(c)<3 or l.startswith('#'): continue
    assert c[0] not in APPR and c[0] not in GRILLE, c[0]
    blocks.append(c[2].split())
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
        s+= (C.get(n,'?') if n>=200 else T.get(n%24,'?')) if n>=40 else '?'
    return s
def score(T):
    ok=tot=0
    for b in blocks:
        s=dec(b,T); ok+=sw_match(s,ref); tot+=len(s)
    return ok/tot,tot
nnum=sum(len(b) for b in blocks)
acc,tot=score(T)
print('table',''.join(T[r] for r in range(24)))
print('nombres',nnum,'caractères déchiffrés',tot,'référence',len(ref))
print('ACCORD K24',round(acc,4)); sys.stdout.flush()
rng=random.Random(24683); ctl=[]
for i in range(200):
    vals=[T[r] for r in range(24)]; rng.shuffle(vals); ctl.append(score(dict(enumerate(vals)))[0])
ctl.sort(); print('témoins 200 max',round(ctl[-1],4),'médiane',round(ctl[100],4))
print('CRITÈRE (>=0,555 et >= max+0,30)', acc>=0.555 and acc>=ctl[-1]+0.30)
print('TAILLE >= 300 nombres', nnum>=300)
for b in blocks: print(' '.join(b),'=>',dec(b,T).upper())
