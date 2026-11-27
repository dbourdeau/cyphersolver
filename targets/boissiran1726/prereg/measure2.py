# Mesure PREREG-2 Boissiran A. Usage : python3 -I measure2.py LIGNES   (LIGNES = "burned" ou "neuve")
import re, json, random, os, sys, itertools
H=os.path.dirname(os.path.abspath(__file__))
LEX=os.path.join(H,'..','besancon-ms1580-1582','ms62-test','LEXIQUE-FR-EARLY.txt')
TR=os.path.join(H,'transcription','TRANSCRIPTION-ARBITREE.txt')
lex=set(w.strip().lower() for w in open(LEX,encoding='utf-8') if len(w.strip())>=4)
H1={'0':'ax','1':'dp','2':'fr','3':'bh','4':'my','5':'el','6':'cgu','7':'in','8':'qs','9':'ot'}
SEL={'burned':lambda k: k in ('p2.23','p2.24') or re.match(r'p3\.0[1-8]$',k),
     'neuve': lambda k: re.match(r'p1\.0[1-9]$',k)}[sys.argv[1]]
def groups():
    out=[]
    for l in open(TR,encoding='utf-8'):
        m=re.match(r'(p\d\.\d\d)\s+(.*)',l)
        if m and SEL(m.group(1)): out+=m.group(2).split()
    return out
def tok(g):
    pos=[];i=0
    while i<len(g):
        c=g[i]
        if c=='[':
            j=g.index(']',i); pos.append([x for x in g[i+1:j].split('/') if x.isdigit()]); i=j+1
        elif c.isdigit(): pos.append([c]); i+=1
        else: return None   # tache, rature, signe non chiffré
    return pos
G=[tok(g) for g in groups()]
G=[p for p in G if p is not None and len(p)>=4]   # groupes de 4 chiffres et plus
def hit(pos,K):
    sets=[''.join(sorted(set(''.join(K[d] for d in p)))) for p in pos]
    for t in itertools.product(*sets):
        if ''.join(t) in lex: return True
    return False
def M(K): return sum(hit(p,K) for p in G)/len(G)
rng=random.Random(20261127)
digs=list(H1); sets=list(H1.values()); letters=''.join(sets); sizes=[len(s) for s in sets]
wp=[];wr=[]
while len(wp)<200:
    v=sets[:]; rng.shuffle(v); K=dict(zip(digs,v))
    if K!=H1: wp.append(M(K))
while len(wr)<200:
    L=list(letters); rng.shuffle(L); K={};i=0
    for d,s in zip(digs,sizes): K[d]=''.join(L[i:i+s]); i+=s
    if sorted(map(sorted,K.values()))!=sorted(map(sorted,H1.values())): wr.append(M(K))
m=M(H1); best=max(wp+wr)
res={'portion':sys.argv[1],'n_groupes_4plus':len(G),'M_H1':round(m,4),'max_perm':round(max(wp),4),'max_random':round(max(wr),4),
 'moy_temoins':round(sum(wp+wr)/400,4),'critere':'M>=0.50 et M>=max_temoins+0.30','succes':m>=0.50 and m>=best+0.30}
print(json.dumps(res,ensure_ascii=False,indent=1))
json.dump(res,open(os.path.join(H,'MESURE2-%s.json'%sys.argv[1]),'w'),ensure_ascii=False,indent=1)
