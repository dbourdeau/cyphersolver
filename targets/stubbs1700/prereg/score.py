#!/usr/bin/env python3
"""sal-stubbs — single held-out measure (frozen with PREREG). Usage:
   score.py KEY.json HELDOUT.json  -> prints JSON result
KEY.json   = {"lang": "en"|"la", "map": {sign: letter or "" (null)}}
HELDOUT.json = {"signs": [sign codes in reading order]}  ('?' flags stripped before lookup)
"""
import json, sys, re, random, collections, os
HERE=os.path.dirname(os.path.abspath(__file__))
LM=os.path.join(HERE,'..','lm')
SHORT={'en':"a i o an as at be by do he if in is it me my no of on or so to up us we ye am go oh".split(),
       'la':"a e o ab ad an at de di ea ei eo et ex id in is me ne nc ob re se si te tu ut uo nos uos".split()}
def norm(s):
    s=s.lower().replace('ſ','s').replace('j','i').replace('v','u')
    return re.sub('[^a-z]','',s)
def lexicon(lang):
    c=collections.Counter()
    for f in sorted(os.listdir(LM)):
        if f.startswith(lang+'_') and f.endswith('.txt'):
            for w in re.findall(r"[A-Za-zſ]+",open(os.path.join(LM,f),errors='ignore').read()):
                c[norm(w)]+=1
    L={w for w,n in c.items() if n>=2 and len(w)>=3}
    L|=set(norm(w) for w in SHORT[lang])
    return L
def coverage(text,L,maxw=20):
    n=len(text); best=[0]*(n+1)
    for i in range(1,n+1):
        b=best[i-1]
        for l in range(1,min(maxw,i)+1):
            w=text[i-l:i]
            if '?' in w: continue
            if w in L and best[i-l]+l>b: b=best[i-l]+l
        best[i]=b
    return best[n]
def decode(signs,m):
    out=[]
    for s in signs:
        s=s.replace('?','')
        v=m.get(s,'?')
        out.append(norm(v) if v not in ('?',) else '?')
    return ''.join(out)
def S(signs,m,L):
    t=decode(signs,m)
    return (coverage(t,L)/len(t) if t else 0.0), t
if __name__=='__main__':
    K=json.load(open(sys.argv[1])); H=json.load(open(sys.argv[2]))
    L=lexicon(K['lang']); m=K['map']; signs=H['signs']
    s,t=S(signs,m,L)
    keys=sorted(m); vals=[m[k] for k in keys]; ctr=[]
    for k in range(200):
        r=random.Random(1700+k); v=vals[:]; r.shuffle(v)
        ctr.append(S(signs,dict(zip(keys,v)),L)[0])
    res={'n_signs':len(signs),'lexicon_size':len(L),'score':round(s,4),'best_control':round(max(ctr),4),
         'mean_control':round(sum(ctr)/len(ctr),4),'pass':bool(s>=0.85 and s>=max(ctr)+0.30),'decoded':t}
    print(json.dumps(res,indent=1,ensure_ascii=False))
