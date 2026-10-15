"""Segmentation + agglomerative shape clustering of the cipher glyphs. Pure Python; see glyphs.py header."""
import sys, statistics
sys.path.insert(0,'.')
from glyphs import read_bmp, components
from glyphs2 import merge_overlaps
from glyphs3 import bands_of

N=16
def mask(c):
    """Binary N x N mask of the component, deskewed only by its bounding box."""
    w=c['x1']-c['x0']+1; h=c['y1']-c['y0']+1
    acc=[[0]*N for _ in range(N)]
    for (x,y) in c['px']:
        gx=min(N-1,(x-c['x0'])*N//w); gy=min(N-1,(y-c['y0'])*N//h)
        acc[gy][gx]+=1
    cell=max(1,(w*h)//(N*N))
    return [1 if acc[i][j]>=max(1,cell//3) else 0 for i in range(N) for j in range(N)]

def d_mask(a,b):
    inter=sum(1 for p,q in zip(a,b) if p and q)
    uni=sum(1 for p,q in zip(a,b) if p or q)
    return 1.0-(inter/uni if uni else 1.0)

def agglom(items, k):
    """Average-linkage agglomerative clustering down to k clusters."""
    cl=[[i] for i in range(len(items))]
    D={}
    for i in range(len(items)):
        for j in range(i+1,len(items)):
            D[(i,j)]=d_mask(items[i],items[j])
    def cd(a,b):
        s=0.0;n=0
        for i in a:
            for j in b:
                s+=D[(i,j)] if i<j else D[(j,i)]; n+=1
        return s/n
    while len(cl)>k:
        best=None;bi=bj=-1
        for i in range(len(cl)):
            for j in range(i+1,len(cl)):
                d=cd(cl[i],cl[j])
                if best is None or d<best: best,bi,bj=d,i,j
        cl[bi]=cl[bi]+cl[bj]; cl.pop(bj)
    lab=[0]*len(items)
    for ci,mem in enumerate(cl):
        for i in mem: lab[i]=ci
    return lab

if __name__=='__main__':
    bmp=sys.argv[1]
    xm=int(sys.argv[sys.argv.index('--xmin')+1]) if '--xmin' in sys.argv else 0
    k=int(sys.argv[sys.argv.index('--k')+1]) if '--k' in sys.argv else 40
    w,h,g=read_bmp(bmp)
    cs=components(g,w,h,130,45,10)
    bs=bands_of(g,w,h)
    rows={i:[] for i in range(len(bs))}
    for c in cs:
        m=(c['y0']+c['y1'])/2
        bi=min(range(len(bs)), key=lambda i: 0 if bs[i][0]<=m<=bs[i][1] else min(abs(m-bs[i][0]),abs(m-bs[i][1])))
        if bi==0 and c['x0']<xm: continue
        rows[bi].append(c)
    seq=[]
    for i in sorted(rows):
        rows[i].sort(key=lambda c:c['x0'])
        mg=merge_overlaps(rows[i])
        mg=[c for c in mg if c['n']>=60 and (c['x1']-c['x0'])<=90]   # drop specks and run-together blobs
        seq.append(mg)
    flat=[c for s in seq for c in s]
    print('# per line',[len(s) for s in seq],'total',len(flat),file=sys.stderr)
    ms=[mask(c) for c in flat]
    lab=agglom(ms,k)
    print(f'# clusters={k}',file=sys.stderr)
    A='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    t=0
    for li,s in enumerate(seq):
        print(f'L{li+1}\t'+''.join(A[lab[t+i]] for i in range(len(s))))
        t+=len(s)
