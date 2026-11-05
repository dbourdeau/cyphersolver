# Single measure (PREREG rakoczi-1632): decode H gloss pairs with K, char agreement vs gloss, 200 shuffled-key controls.
import sys, random, re
sys.path.insert(0, __import__('os').path.dirname(__file__))
from common import norm, load_key
def toks(s): return [g.rstrip('?') if g!='?' else '?' for g in s.split('.') if not (g.rstrip('?').isdigit() and len(g.rstrip('?'))==3)]
def matches(dec, gl):
    # Levenshtein alignment; cost 0 if gloss letter in decoded set; returns max matched letters on an optimal path
    n,m=len(dec),len(gl)
    D=[[None]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j==0: D[i][j]=(0,0); continue
            c=[]
            if i>0: d,mt=D[i-1][j]; c.append((d+1,mt))
            if j>0: d,mt=D[i][j-1]; c.append((d+1,mt))
            if i>0 and j>0:
                d,mt=D[i-1][j-1]; ok=gl[j-1] in dec[i-1]; c.append((d+(0 if ok else 1), mt+(1 if ok else 0)))
            D[i][j]=min(c,key=lambda x:(x[0],-x[1]))
    return D[n][m][1]
def score(K, pairs):
    tot=sum(len(g) for _,g in pairs); mt=0
    for gs,gl in pairs: mt+=matches([K.get(t,set()) for t in gs], gl)
    return mt/tot
pairs=[]; allg=[]
for line in open(sys.argv[2],encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    _,gs,gl=line.rstrip('\n').split('\t'); pairs.append((toks(gs),norm(gl)))
for line in open(sys.argv[3],encoding='utf-8'):
    if line.startswith('#') or not line.startswith('y'): continue
    if 'EXCLUE' in line: continue
    for w in line.split()[1:]:
        if re.match(r'^[\d{}?.a-zA-Z]+$',w) and ('.' in w or w.startswith('{')): allg+=toks(w)
for kpath,label in ((sys.argv[1],'K'),(sys.argv[4],'key_frozen (descriptif)')):
    K=load_key(kpath)
    car=score(K,pairs)
    present=sorted({t for gs,_ in pairs for t in gs if t in K})
    rng=random.Random(1632); ctrl=[]
    for _ in range(200):
        vals=[K[g] for g in present]; rng.shuffle(vals); Kc=dict(K); Kc.update(zip(present,vals)); ctrl.append(score(Kc,pairs))
    C=sum(1 for t in allg if t in K)/len(allg)
    mx=max(ctrl); marge=car-mx
    verdict='VALIDÉ' if (car>=0.85 and marge>=0.30) else ('PARTIEL' if marge>=0.30 else 'ÉCHEC')
    print('%s: mots=%d lettres=%d car=%.3f C(H)=%.3f témoins moy=%.3f max=%.3f marge=%.3f -> %s'%(label,len(pairs),sum(len(g) for _,g in pairs),car,C,sum(ctrl)/200,mx,marge,verdict))
    if label=='K':
        for gs,gl in pairs:
            dec=''.join(('/'.join(sorted(K[t])) if len(K.get(t,()))>1 else (next(iter(K[t])) if t in K else '?')) if True else '' for t in gs)
            print('   %-28s %-14s %d/%d'%(dec,gl,matches([K.get(t,set()) for t in gs],gl),len(gl)))
