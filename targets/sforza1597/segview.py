import sys,re,math,collections
sys.argv=[sys.argv[0]]+sys.argv[1:]
src=open('keyrefine.py',encoding='utf-8').read().split("toks = [l.split()")[0]
f=sys.argv[1]; n=int(sys.argv[2])
sys.argv=['x','a','b','c']
exec(src)
def seg(t):
    nn=len(t); best=[1e9]*(nn+1); back=[0]*(nn+1); best[0]=0
    for i in range(nn):
        if best[i]>=1e9: continue
        if best[i]+UNK<best[i+1]: best[i+1]=best[i]+UNK; back[i+1]=i
        for L in range(4,13):
            if i+L>nn: break
            c=cost.get(t[i:i+L])
            if c is not None and best[i]+c<best[i+L]: best[i+L]=best[i]+c; back[i+L]=i
    out=[];i=nn
    while i>0:
        j=back[i]; w=t[j:i]; out.append(' '+w+' ' if (len(w)>=4 and w in cost) else '.'*len(w)); i=j
    return ''.join(out[::-1])
for l in open(f).read().split('\n')[:n]:
    if l: print(seg(l))
