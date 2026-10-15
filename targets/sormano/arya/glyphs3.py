"""Final segmentation + clustering of the f.124r crib (BnF fr. 3096 no. 67). Pure Python; see glyphs.py."""
import sys, statistics
sys.path.insert(0,'.')
from glyphs import read_bmp, components, feat, dist
from glyphs2 import merge_overlaps

T=130
def bands_of(g,w,h,t=T):
    prof=[sum(1 for x in range(w) if g[y][x]<t) for y in range(h)]
    fl=statistics.median(prof); mx=max(prof); cut=fl+0.35*(mx-fl)
    bs=[];s=None
    for y,p in enumerate(prof):
        if p>cut and s is None: s=y
        if p<=cut and s is not None:
            if y-s>=10: bs.append((s,y-1))
            s=None
    if s is not None: bs.append((s,h-1))
    return bs

def run(bmp, xmin_first=0):
    w,h,g=read_bmp(bmp)
    cs=components(g,w,h,T,45,10)
    bs=bands_of(g,w,h)
    rows={i:[] for i in range(len(bs))}
    for c in cs:
        m=(c['y0']+c['y1'])/2
        bi=min(range(len(bs)), key=lambda i: 0 if bs[i][0]<=m<=bs[i][1] else min(abs(m-bs[i][0]),abs(m-bs[i][1])))
        if bi==0 and c['x0']<xmin_first: continue
        rows[bi].append(c)
    for i in rows: rows[i].sort(key=lambda c:c['x0'])
    seq=[]
    for i in sorted(rows):
        mg=merge_overlaps(rows[i])
        seq.append(mg)
    return bs, seq

def cluster(fs, thr):
    ld=[]
    for i,f in enumerate(fs):
        best,bi=None,-1
        for j,(lf,mem) in enumerate(ld):
            d=dist(f,lf)
            if best is None or d<best: best,bi=d,j
        if best is not None and best<thr: ld[bi][1].append(i)
        else: ld.append([f,[i]])
    lab=[0]*len(fs)
    for j,(_,mem) in enumerate(ld):
        for i in mem: lab[i]=j
    return lab,ld

if __name__=='__main__':
    bmp=sys.argv[1]
    xm=int(sys.argv[sys.argv.index('--xmin')+1]) if '--xmin' in sys.argv else 0
    bs,seq=run(bmp,xm)
    print('# bands',bs,file=sys.stderr)
    print('# glyphs per line:',[len(s) for s in seq],'total',sum(len(s) for s in seq),file=sys.stderr)
    fs=[feat(c) for s in seq for c in s]
    if '--sweep' in sys.argv:
        for thr in (0.10,0.12,0.14,0.16,0.18,0.20,0.24):
            lab,ld=cluster(fs,thr); print(f'# thr={thr} clusters={len(ld)}',file=sys.stderr)
        sys.exit()
    thr=float(sys.argv[sys.argv.index('--thr')+1]) if '--thr' in sys.argv else 0.16
    lab,ld=cluster(fs,thr)
    print(f'# thr={thr} clusters={len(ld)}',file=sys.stderr)
    k=0; A='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/=<>()[]{}'
    for li,s in enumerate(seq):
        out=[]
        for c in s:
            out.append(A[lab[k]] if lab[k]<len(A) else '?'); k+=1
        print(f'L{li+1}\t'+''.join(out))
