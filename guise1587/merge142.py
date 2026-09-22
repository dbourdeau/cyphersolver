import re,sys
P=open('f142_pinned.txt',encoding='utf8').read().splitlines()
for f in sys.argv[1:]:
    new={}
    cur=None
    for ln in open(f,encoding='utf8'):
        m=re.match(r'(#R )?(\d\d) \|',ln)
        if m: new[(bool(m[1]),m[2])]=ln.rstrip('\n')
    out=[]
    for l in P:
        m=re.match(r'(#R )?(\d\d) \|',l)
        out.append(new.get((bool(m[1]),m[2]),l) if m else l)
    P=out
open('f142_pinned.txt','w',encoding='utf8').write('\n'.join(P)+'\n')
T=U=0
for l in P:
    m=re.search(r'\|\|\s*(\d+)\s+(\d+)',l)
    if m and l.startswith('#R'): T+=int(m[1]);U+=int(m[2])
print('f142',T,U,round(1-U/T,3))
