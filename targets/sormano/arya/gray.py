"""Grayscale normalised-cross-correlation matching of glyphs, as an alternative to binary masks.

Binarising a grainy microfilm at one threshold throws away most of the stroke evidence. Here each
component's bounding box is cut from the greyscale image, area-averaged to N x N, mean-centred and
variance-normalised, and compared by NCC maximised over small shifts.
"""
import sys, math, statistics, collections
sys.path.insert(0,'.')
from glyphs import read_bmp
from clean import pipeline

N=18
def patch(g, c, pad=2):
    x0=max(0,c['x0']-pad); x1=min(len(g[0])-1,c['x1']+pad)
    y0=max(0,c['y0']-pad); y1=min(len(g)-1,c['y1']+pad)
    w=x1-x0+1; h=y1-y0+1
    out=[]
    for i in range(N):
        for j in range(N):
            ya=y0+(i*h)//N; yb=max(ya+1,y0+((i+1)*h)//N)
            xa=x0+(j*w)//N; xb=max(xa+1,x0+((j+1)*w)//N)
            s=0;n=0
            for y in range(ya,min(yb,y1+1)):
                for x in range(xa,min(xb,x1+1)):
                    s+=g[y][x]; n+=1
            out.append(s/max(1,n))
    m=sum(out)/len(out)
    out=[v-m for v in out]
    sd=math.sqrt(sum(v*v for v in out)/len(out)) or 1.0
    return [v/sd for v in out]

def shifted(p, dx, dy):
    q=[0.0]*(N*N)
    for i in range(N):
        for j in range(N):
            si=i-dy; sj=j-dx
            q[i*N+j]=p[si*N+sj] if 0<=si<N and 0<=sj<N else 0.0
    return q

def ncc(a,b,sh=1):
    best=None
    for dy in range(-sh,sh+1):
        for dx in range(-sh,sh+1):
            v=shifted(a,dx,dy)
            s=sum(p*q for p,q in zip(v,b))/(N*N)
            if best is None or s>best: best=s
    return best

if __name__=='__main__':
    w,h,g=read_bmp('/tmp/crib.bmp')
    bs,seq=pipeline('/tmp/crib.bmp',2115,3270,maxw=64)
    flat=[c for s in seq for c in s]
    P=sys.argv[1]
    print('glyphs',len(flat),'labels',len(P))
    ps=[patch(g,c) for c in flat]
    n=len(ps)
    S=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            v=max(ncc(ps[i],ps[j]), ncc(ps[j],ps[i]))
            S[i][j]=S[j][i]=v
    # leave-one-out 1-NN over the labels
    ok=0
    conf=collections.Counter()
    for i in range(n):
        j=max((k for k in range(n) if k!=i), key=lambda k:S[i][k])
        if P[i]==P[j]: ok+=1
        else: conf[(P[i],P[j])]+=1
    print(f'grayscale NCC leave-one-out 1-NN: {ok}/{n} = {100*ok/n:.1f}%')
    print('top confusions:', conf.most_common(8))
