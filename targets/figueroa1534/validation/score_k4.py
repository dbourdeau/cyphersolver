# score_k4.py K4.tsv transcription.txt clear_full.txt : décodage mécanique (étiquettes -> valeurs K4), référence = fenêtre du clair choisie par alignement local, précision LCS caractères (métrique C04) + 200 témoins à valeurs permutées
import sys,re,random
key={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or l.startswith('label\t') or not l.strip(): continue
    f=l.rstrip('\n').split('\t'); key.setdefault(f[0],f[1].split('|')[0])
lines=[l.split(None,1)[1] for l in open(sys.argv[2],encoding='utf-8') if l.strip() and not l.startswith('#')]
toks=[t for l in lines for t in l.strip().split('|') if t]
def val(t,m): 
    v=m.get(t,'?'); return '' if v=='NUL' else v
def norm(s):
    s=s.lower()
    for a,b in [('v','b'),('u','b'),('ç','c'),('z','c'),('ñ','n'),('h',''),('y','i'),('j','i'),('ll','l'),('ss','s'),('rr','r')]: s=s.replace(a,b)
    return re.sub('[^a-z]','',s)
clear=' '.join(l for l in open(sys.argv[3],encoding='utf-8').read().split('\n') if not l.startswith('#'))
C=norm(clear)
def dec(m): return norm(''.join(val(t,m) for t in toks if val(t,m)!='?'))
D0=dec(key)
# fenêtre de référence : alignement local Smith-Waterman (+2/-1/-1) du décodage réel sur le clair complet, +40 car. de chaque côté
def sw(a,b):
    H=[[0]*(len(b)+1) for _ in range(len(a)+1)]; best=(0,0,0)
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            h=max(0,H[i-1][j-1]+(2 if a[i-1]==b[j-1] else -1),H[i-1][j]-1,H[i][j-1]-1); H[i][j]=h
            if h>best[0]: best=(h,i,j)
    # remonter pour trouver le début dans b
    h,i,j=best
    while i>0 and j>0 and H[i][j]>0:
        if H[i][j]==H[i-1][j-1]+(2 if a[i-1]==b[j-1] else -1): i-=1;j-=1
        elif H[i][j]==H[i-1][j]-1: i-=1
        else: j-=1
    return j,best[2]
j0,j1=sw(D0,C); R=C[max(0,j0-40):j1+40]
def lcs(a,b):
    prev=[0]*(len(b)+1)
    for x in a:
        cur=[0]
        for j,y in enumerate(b): cur.append(prev[j]+1 if x==y else max(prev[j+1],cur[j]))
        prev=cur
    return prev[-1]
def score(m):
    d=dec(m); return lcs(d,R)/max(1,len(d))
s0=score(key)
used=sorted(set(t for t in toks if t in key and key[t] not in ('NUL',)))
vals=[key[t] for t in used]
random.seed(744); null=[]
for _ in range(200):
    p=vals[:]; random.shuffle(p); m=dict(key); m.update(dict(zip(used,p))); null.append(score(m))
null.sort()
unk=sum(1 for t in toks if t not in key)
print(f'jetons={len(toks)} hors_cle={unk} ({unk/len(toks):.1%}) car_decodes={len(D0)} ref={len(R)} car (clair {j0}-{j1})')
print(f'score={s0:.3f} témoins médiane={null[100]:.3f} p99={null[197]:.3f} max={null[-1]:.3f}')
ok = s0>=0.85 and s0>=null[-1]+0.30 and unk/len(toks)<=0.20
print('VERDICT', 'VALIDÉ' if ok else 'NON VALIDÉ')
print('DECODE', D0)
print('REF', R)
