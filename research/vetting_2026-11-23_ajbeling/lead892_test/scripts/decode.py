import json, random, re, sys
from common import *
VAL=json.load(open(O+'sign_values_frozen_key.json'))
NUM={'12':'tt','13':'ss','14':'rr','16':'nn','3':None}
NULLWORDS={'cum','porro','spo','dar','atq','atque','etiam','idcirco','dac','der'}
def value(code,V):
    if code in ('ras',): return ['§']
    if code in NULLWORDS: return []
    if code in ('12','13','14','15','16'): return [{c} for c in {'12':'tt','13':'ss','14':'rr','15':'pp','16':'nn'}[code]]
    v=V.get(code)
    if v is None or v.startswith('NOT') or code=='??': return [{'?'}]
    if v=='null': return []
    if v in ('Imperator Turcorum',): return ['§']
    first=v.split('|')[0]
    if first=='null': return []
    if code=='q': return [{'e','u'}]
    return [{c} for c in first]
def decode(T,V):
    out=[];lines={}
    for k in sorted(T):
        seq=[]
        for t in T[k]:
            seq+=value(norm(t).lower() if norm(t).lower() in ('ras',) or t.startswith('{') else norm(t),V)
        lines[k]=seq; out+=seq
    return out,lines
def reftext():
    t=' '.join(l for l in open(O+'reference_19c_decipherment.txt') if not l.startswith('#'))
    t=t.lower().replace('j','i').replace('v','u').replace('ae','e')
    words=re.findall(r'[a-z]+',t)
    return words
def prep(seq):
    # map to plain letters; ae handled in ref; normalise
    res=[]
    for s in seq:
        if s=='§': continue
        res.append({c.replace('j','i').replace('v','u') for c in s})
    return res
def score(seq,words):
    ref=''.join(w for w in words if w!='sultanum')
    a=seq; b=ref; n,m=len(a),len(b)
    import numpy as np
    D=np.zeros((n+1,m+1),dtype=np.int32); D[:,0]=-np.arange(n+1); D[0,:]=-np.arange(m+1)
    for i in range(1,n+1):
        ai=a[i-1]
        row=D[i-1]
        for j in range(1,m+1):
            s=row[j-1]+(1 if b[j-1] in ai else -1)
            D[i,j]=max(s,row[j]-1,D[i,j-1]-1)
    i,j=n,m; match=[False]*m; got=['']*m
    while i>0 and j>0:
        if D[i,j]==D[i-1,j-1]+(1 if b[j-1] in a[i-1] else -1):
            match[j-1]=b[j-1] in a[i-1]; got[j-1]='/'.join(sorted(a[i-1])); i-=1;j-=1
        elif D[i,j]==D[i-1,j]-1: i-=1
        else: j-=1
    return sum(match)/m, match, got, ref
if __name__=='__main__':
    words=reftext()
    res={}
    for tag in ('T1','T2'):
        T=load(O+f'transcription_{tag}.txt')
        seq,lines=decode(T,VAL); s=prep(seq)
        sc,match,got,ref=score(s,words)
        # words
        pos=0; wr=0; nw=0; holes=[]; outw=[]
        for w in words:
            if w=='sultanum': outw.append('[Ras=Imperator Turcorum]'); continue
            mm=match[pos:pos+len(w)]; g=got[pos:pos+len(w)]; pos+=len(w); nw+=1
            if all(mm): wr+=1; outw.append(w)
            else: outw.append(''.join(c if ok else '['+(gg or '-')+']' for c,ok,gg in zip(w,mm,g)))
        res[tag]=(sc,wr,nw)
        print(tag,'letters',len(ref),'agree',round(sc,4),'words read',wr,'/',nw,round(wr/nw,4))
        open(O+f'decode_{tag}.txt','w').write(' '.join(outw)+'\n')
        mech=' | '.join(k+': '+''.join(('/'.join(sorted(x)) if isinstance(x,set) else x) if (len(x)==1 or x=='§') else '('+'/'.join(sorted(x))+')' for x in v) for k,v in lines.items())
        open(O+f'mechanical_{tag}.txt','w').write(mech.replace(' | ','\n')+'\n')
        if tag=='T2':
            codes=[c for c,v in VAL.items() if not v.startswith('NOT') and v not in ('null','Imperator Turcorum')]
            vals=[VAL[c] for c in codes]
            rng=random.Random(1550); cs=[]
            for r in range(200):
                vv=vals[:]; rng.shuffle(vv); V2=dict(VAL); V2.update(dict(zip(codes,vv)))
                sq,_=decode(T,V2); cs.append(score(prep(sq),words)[0])
            print('controls n=200 mean',round(sum(cs)/len(cs),4),'max',round(max(cs),4))
