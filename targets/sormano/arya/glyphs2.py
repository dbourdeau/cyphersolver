"""Glyph segmentation and shape clustering for the fr. 3096 cipher, pure Python (see glyphs.py header)."""
import struct, sys, math
from collections import deque
sys.path.insert(0,'.')
from glyphs import read_bmp, otsu, components, feat, dist

def rows_by_profile(g, w, h, thresh, minrun=12):
    """Find text bands from the horizontal ink profile."""
    prof=[sum(1 for x in range(w) if g[y][x]<thresh) for y in range(h)]
    mx=max(prof) or 1
    on=[p > 0.06*mx for p in prof]
    bands=[]; s=None
    for y,v in enumerate(on):
        if v and s is None: s=y
        if not v and s is not None:
            if y-s>=minrun: bands.append((s,y-1))
            s=None
    if s is not None and h-s>=minrun: bands.append((s,h-1))
    return bands

def assign(cs, bands):
    out={i:[] for i in range(len(bands))}
    for c in cs:
        m=(c['y0']+c['y1'])/2
        best,bi=None,None
        for i,(a,b) in enumerate(bands):
            d=0 if a<=m<=b else min(abs(m-a),abs(m-b))
            if best is None or d<best: best,bi=d,i
        out[bi].append(c)
    for i in out: out[i].sort(key=lambda c:c['x0'])
    return out

def merge_overlaps(row, frac=0.55):
    """Merge components that sit on top of each other (dots, broken strokes, i-dots)."""
    res=[]
    for c in row:
        if res:
            p=res[-1]
            ov=min(p['x1'],c['x1'])-max(p['x0'],c['x0'])+1
            wmin=min(p['x1']-p['x0']+1, c['x1']-c['x0']+1)
            if ov > frac*wmin:
                p['x0']=min(p['x0'],c['x0']); p['x1']=max(p['x1'],c['x1'])
                p['y0']=min(p['y0'],c['y0']); p['y1']=max(p['y1'],c['y1'])
                p['px']=p['px']+c['px']; p['n']=p['n']+c['n']; continue
        res.append(dict(c))
    return res

def kmed(fs, thr):
    leaders=[]
    for i,f in enumerate(fs):
        best,bi=None,-1
        for j,(lf,mem) in enumerate(leaders):
            d=dist(f,lf)
            if best is None or d<best: best,bi=d,j
        if best is not None and best<thr: leaders[bi][1].append(i)
        else: leaders.append([f,[i]])
    lab=[0]*len(fs)
    for j,(_,mem) in enumerate(leaders):
        for i in mem: lab[i]=j
    return lab,leaders

if __name__=='__main__':
    bmp=sys.argv[1]
    minpx=int(sys.argv[sys.argv.index('--minpx')+1]) if '--minpx' in sys.argv else 45
    minh=int(sys.argv[sys.argv.index('--minh')+1]) if '--minh' in sys.argv else 10
    w,h,g=read_bmp(bmp); t=otsu(g,w,h)
    cs=components(g,w,h,t,minpx,minh)
    bands=rows_by_profile(g,w,h,t)
    rows=assign(cs,bands)
    print(f'# {w}x{h} thr={t} comps={len(cs)} bands={bands}',file=sys.stderr)
    merged={i:merge_overlaps(rows[i]) for i in rows}
    print('# per-band counts raw/merged: '+', '.join(f'{i+1}:{len(rows[i])}/{len(merged[i])}' for i in rows),file=sys.stderr)
    if '--thrsweep' in sys.argv:
        fs=[feat(c) for i in merged for c in merged[i]]
        for thr in (0.10,0.14,0.18,0.22,0.26,0.30):
            lab,ld=kmed(fs,thr)
            print(f'# thr={thr} clusters={len(ld)}',file=sys.stderr)
        sys.exit()
