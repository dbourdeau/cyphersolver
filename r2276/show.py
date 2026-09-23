import sys,json
sys.path.insert(0,'..')
from solve import build,plain,score,FIXED,M
k=json.load(open(sys.argv[1],encoding='utf8'))
L,segs=build(['p1.txt','p2.txt','p3.txt'])
syms=sorted({t for s in segs for t in s})
n=sum(len(p) for p in plain(segs,{s:k.get(s,'?') for s in syms}))
print('score/char',score(segs,{s:k.get(s,'e') for s in syms})/n)
print('unset',[s for s in syms if s not in k and s not in FIXED])
for name,toks in L:
    if len(sys.argv)>2 and not name.startswith(sys.argv[2]): continue
    print(name.ljust(6),''.join('…' if t=='...' else (FIXED.get(t) or k.get(t,'['+t+']')) for t in toks))
