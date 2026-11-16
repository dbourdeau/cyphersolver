import json,sys
sys.argv=[sys.argv[0]]+sys.argv[1:]
exec(open('refine.py').read().split('k=key(')[0])
k=key('ja.txt'); k['r']='b'
for s in set(t for l in L for t in l): k.setdefault(s,'x')
b0,h0=score(k,TR),score(k,HO)
res=[]
for s in sorted(set(t for l in L for t in l)):
    cur=k[s]
    for a in 'abcdefghilmnopqrstvz':
        if a==cur: continue
        k[s]=a; dt,dh=score(k,TR)-b0,score(k,HO)-h0
        if dt>5 and dh>5: res.append((dt+dh,s,cur,a,round(dt),round(dh)))
    k[s]=cur
for r in sorted(res,reverse=True)[:40]: print(r[1:])
