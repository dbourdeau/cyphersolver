"""Build a labelled training set: segmented lines of ff. 34r-35v matched to the eye transcription
(transcription_15oct_ff34r-35v.txt). Lines are paired by a monotone DP on sign counts; a pair is used
only when the counts are equal. Clear words (Sicut...) and ^insertions are dropped from both sides."""
import pickle, re, numpy as np
P=pickle.load(open('work/pages.pkl','rb'))
T={}
for l in open('transcription_15oct_ff34r-35v.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k,*toks=l.split()
    T.setdefault(k.split('.')[0],[]).append((k,[re.sub(r'\{.*','',t) for t in toks if not t.startswith('^')]))
def pair(tl,segs):
    n,m=len(tl),len(segs); NEG=-1e9
    S=np.full((n+1,m+1),NEG); S[0,:]=0; B={}
    for i in range(1,n+1):
        for j in range(1,m+1):
            best=(S[i,j-1],'s')
            d=abs(len(tl[i-1][1])-len(segs[j-1]['signs']))
            sc=3 if d==0 else (1 if d<=3 else -3)
            if S[i-1,j-1]+sc>best[0]: best=(S[i-1,j-1]+sc,'m')
            if S[i-1,j]-1>best[0]: best=(S[i-1,j]-1,'t')
            S[i,j]=best[0]; B[i,j]=best[1]
    i,j=n,int(np.argmax(S[n])); out=[]
    while i>0 and j>0:
        b=B[i,j]
        if b=='m': out.append((i-1,j-1)); i-=1; j-=1
        elif b=='s': j-=1
        else: i-=1
    return out[::-1]
train=[];pairs={}
for p,tl in T.items():
    segs=P[p]
    best=None
    for o in range(-5,15):
        pr=[(i,int(k.split('.')[1])-1+o) for i,(k,t) in enumerate(tl) if 0<=int(k.split('.')[1])-1+o<len(segs)]
        sc=sum(len(tl[i][1])==len(segs[j]['signs']) for i,j in pr)
        if best is None or sc>best[0]: best=(sc,o,pr)
    print(p,'offset',best[1],'equal-count lines',best[0],'of',len(tl))
    pr=best[2]; pairs[p]=pr
    for i,j in pr:
        toks=tl[i][1]; ss=sorted(segs[j]['signs'],key=lambda s:s['x0'])
        if len(ss)==len(toks) and not any(t in('Sicut','Insuper','Postq') for t in toks):
            for s,t in zip(ss,toks): train.append((s['m'],t))
print('signs',len(train))
pickle.dump((train,pairs,T),open('work/train_signs.pkl','wb'))
