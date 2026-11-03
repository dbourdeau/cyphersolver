# Held-out test: frozen table (from ff. 9r-9v only) on f. 10r, machine shape labels with no eye correction,
# against the 10r gloss as typed before any key existed (marginal_gloss_9r_9v.txt).
import re, random, numpy as np, sys
key={}
for l in open('key_frozen.tsv',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    a,b=l.rstrip('\n').split('\t'); key[a]=b
g=open('marginal_gloss_9r_9v.txt',encoding='utf8').read().split('f. 10r, left margin')[1].split('\n',1)[1]
g=re.sub(r'\[further down:\]',' ',g).replace('[er]','er').replace('...',' ')
P=''.join(c for c in g.lower() if c.isalpha()).replace('j','i').replace('v','u').replace('y','i')
C=[]
for l in open('pass_A_machine.txt',encoding='utf8'):
    if l.startswith('10r.') or l.startswith('10rb.'):
        C+= [x.rstrip('?') for x in l.split()[1:] if x.rstrip('?')!='|']
print('signs',len(C),'gloss letters',len(P))
def score(k):
    D=''.join(k.get(c,'#') if k.get(c,'#')!='null' else '' for c in C)
    # local alignment score: matches, in the best in-order chain (LCS with penalty-free gaps is too generous, so use affine-free DP)
    n,m=len(D),len(P)
    prev=np.zeros(m+1,dtype=int); 
    Pa=np.frombuffer(P.encode(),dtype=np.uint8)
    best=0
    for ch in D.encode():
        cur=np.zeros(m+1,dtype=int)
        t=prev[:-1]+np.where(Pa==ch,2,-1)
        t=np.maximum(t,prev[1:]-1); t=np.maximum(t,0)
        cur[1:]=t
        for j in range(1,m+1):
            pass
        c=cur.copy()
        # left gap
        c=np.maximum.accumulate(c+ (-1)*(-np.arange(m+1)))-np.arange(m+1)*1
        c=np.maximum(c,0)
        prev=c
        best=max(best,int(c.max()))
    return best,D
s,D=score(key)
print('frozen table score',s,'of max',2*len(P))
random.seed(5)
vals=[v for k,v in key.items()]
ctrl=[]
for i in range(int(sys.argv[1])):
    v=vals[:]; random.shuffle(v); k=dict(zip(key.keys(),v)); ctrl.append(score(k)[0])
print('shuffled tables: mean',np.mean(ctrl),'max',max(ctrl),'n',len(ctrl))
def lcs(a,b):
    A=np.frombuffer(a.encode(),dtype=np.uint8); prev=np.zeros(len(A)+1,dtype=np.int32)
    for ch in b.encode():
        d=prev[:-1]+(A==ch); c=np.maximum(d,prev[1:]); c=np.concatenate([[0],c]); c=np.maximum.accumulate(c); prev=c
    return int(prev[-1])
print('gloss letters found in order, frozen table',lcs(P,D),'of',len(P),round(lcs(P,D)/len(P),3))
l=[]
for i in range(100):
    v=vals[:]; random.shuffle(v); k=dict(zip(key.keys(),v)); l.append(lcs(P,score(k)[1])/len(P))
print('same, shuffled tables: mean',round(float(np.mean(l)),3),'max',round(max(l),3))
print(D[:600])
print(P[:600])
