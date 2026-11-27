"""Align the 48r-48v signs to the f. 21r riddle (chain 20r.8) and learn the key from the alignment."""
import json, collections, sys, os
sys.path.insert(0,'../../..')
from lang import lm
lines=[l.split()[1:] for l in open('transcription_v2.txt',encoding='utf8') if not l.startswith('#')]
words=[];cur=[]
for l in lines:
    for t in l:
        if t=='|':
            if cur: words.append(cur); cur=[]
        else: cur.append(t)
    # line end: keep word open only if no divider (words run over)
if cur: words.append(cur)
toks=[t for w in words for t in w]
pt=json.loads(open('../chains_0030_0053.jsonl',encoding='utf8').read().split('\n')[[json.loads(x)['chain_id'] for x in open('../chains_0030_0053.jsonl',encoding='utf8') if x.strip()].index('20r.8')])['plaintext']['text']
pt=pt.replace('/',' ').replace('[?]','')
P=lm.norm_arabic(pt,spaces=False)
# DP global-local alignment: tokens vs a prefix of P; score = learned key consistency, iterate
key={}
def align(key):
    n,m=len(toks),len(P); INF=10**9
    D=[[INF]*(m+1) for _ in range(n+1)]; B=[[None]*(m+1) for _ in range(n+1)]
    D[0][0]=0
    for j in range(1,m+1): D[0][j]=j*1  # skip plaintext letters (dropped)
    for i in range(1,n+1): D[i][0]=i*1
    for i in range(1,n+1):
        for j in range(1,m+1):
            c=0 if key.get(toks[i-1])==P[j-1] else (0.6 if toks[i-1] not in key else 1.2)
            opts=[(D[i-1][j-1]+c,'m'),(D[i-1][j]+1,'s'),(D[i][j-1]+1,'d')]
            D[i][j],B[i][j]=min(opts)
    j=min(range(m+1),key=lambda j:D[n][j]); end=j; i=n; pairs=[]
    while i>0 and j>0:
        b=B[i][j]
        if b=='m': pairs.append((toks[i-1],P[j-1])); i-=1;j-=1
        elif b=='s': pairs.append((toks[i-1],None)); i-=1
        else: pairs.append((None,P[j-1])); j-=1
    return pairs[::-1], end
key=json.loads(open('anneal_best.json',encoding='utf8').read())
for it in range(6):
    pairs,end=align(key)
    cnt=collections.defaultdict(collections.Counter)
    for s,p in pairs:
        if s and p: cnt[s][p]+=1
    key={s:c.most_common(1)[0][0] for s,c in cnt.items()}
m=sum(1 for s,p in pairs if s and p and key[s]==p)
print('signs',len(toks),'plaintext letters used',end,'of',len(P),'matched',m, 'surplus signs',sum(1 for s,p in pairs if p is None),'dropped letters',sum(1 for s,p in pairs if s is None))
print('words in block',len(words))
for s,c in sorted(cnt.items(),key=lambda x:-sum(x[1].values())): print(s,dict(c))
print(''.join(key.get(t,'?') for t in toks))
print(P[:end])
json.dump(key,open('key_48r_v2.json','w',encoding='utf8'),ensure_ascii=False)
