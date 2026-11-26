# Mesure unique PREREG-BOISSIRAN-A. Usage : python3 -I measure.py
import re, json, random, hashlib, os
H=os.path.dirname(os.path.abspath(__file__))
LEX=os.path.join(H,'..','besancon-ms1580-1582','ms62-test','LEXIQUE-FR-EARLY.txt')
TR=os.path.join(H,'transcription','TRANSCRIPTION-ARBITREE.txt')
lex=set(w.strip().lower() for w in open(LEX,encoding='utf-8') if w.strip())
ok=lambda w: w in lex and (len(w)>=2 or w in ('a','y'))
maxlen=max(len(w) for w in lex)
H1={'0':'ax','1':'dp','2':'fr','3':'bh','4':'my','5':'el','6':'cgu','7':'in','8':'qs','9':'ot'}
def groups():
    out=[]
    for l in open(TR,encoding='utf-8'):
        m=re.match(r'(p\d\.\d\d)\s+(.*)',l)
        if not m: continue
        k=m.group(1)
        if k in ('p2.23','p2.24') or re.match(r'p3\.0[1-8]$',k):
            out+=m.group(2).split()
    return out
def tok(g):
    # liste de positions, chacune = ensemble de chiffres admis ; None si tache
    pos=[];i=0
    while i<len(g):
        c=g[i]
        if c=='[':
            j=g.index(']',i); pos.append(set(x for x in g[i+1:j].split('/') if x.isdigit())); i=j+1
        elif c.isdigit(): pos.append({c}); i+=1
        elif c in '#?': return None
        else: i+=1
    return pos
def readable(pos,K):
    n=len(pos)
    sets=[set(''.join(K[d] for d in p)) for p in pos]
    # DP : reach[i] = la position i est atteignable par une suite de mots
    reach=[False]*(n+1); reach[0]=True
    for i in range(n):
        if not reach[i]: continue
        # énumérer les mots partant de i (préfixes compatibles)
        frontier=['']
        for j in range(i,min(n,i+maxlen)):
            frontier=[p+c for p in frontier for c in sets[j]]
            if len(frontier)>200000: frontier=frontier[:200000]
            if any(ok(w) for w in frontier): reach[j+1]=True
    return reach[n]
G=groups(); P=[tok(g) for g in G]
def M(K): return sum(1 for p in P if p is not None and readable(p,K))/len(P)
m1=M(H1)
rng=random.Random(20261126); vals=list(H1.values()); digs=list(H1.keys()); wit=[]
while len(wit)<200:
    v=vals[:]; rng.shuffle(v); K=dict(zip(digs,v))
    if K==H1: continue
    wit.append(M(K))
best=max(wit)
res={'n_groupes':len(G),'n_chiffres':sum(len(p) for p in P if p),'M_H1':round(m1,4),'max_temoin':round(best,4),
 'moy_temoin':round(sum(wit)/len(wit),4),'critere':'M>=0.85 et M>=max+0.30','succes':m1>=0.85 and m1>=best+0.30}
print(json.dumps(res,ensure_ascii=False,indent=1))
json.dump(res,open(os.path.join(H,'MESURE-BOISSIRAN-A.json'),'w'),ensure_ascii=False,indent=1)
