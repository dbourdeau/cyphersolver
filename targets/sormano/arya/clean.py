"""Cleanup pass over segmented components: drop edge artefacts, split run-together glyphs, absorb fragments."""
import sys
sys.path.insert(0,'.')
from glyphs5 import extract

def split_wide(c, maxw):
    """Split a component wider than maxw at the deepest minima of its vertical ink profile."""
    w=c['x1']-c['x0']+1
    if w<=maxw: return [c]
    prof=[0]*w
    for (x,y) in c['px']: prof[x-c['x0']]+=1
    k=max(1,round(w/ (maxw*0.62)))          # expected number of glyphs in the blob
    if k<2: return [c]
    cuts=[]
    seg=w//k
    for i in range(1,k):
        lo=max(2,i*seg-seg//3); hi=min(w-3,i*seg+seg//3)
        if hi<=lo: continue
        cuts.append(min(range(lo,hi), key=lambda t: prof[t]))
    cuts=sorted(set(cuts))
    bounds=[0]+cuts+[w]
    out=[]
    for a,b in zip(bounds,bounds[1:]):
        px=[(x,y) for (x,y) in c['px'] if a<=x-c['x0']<b]
        if len(px)<60: continue
        xs=[p[0] for p in px]; ys=[p[1] for p in px]
        out.append(dict(x0=min(xs),x1=max(xs),y0=min(ys),y1=max(ys),n=len(px),px=px))
    return out or [c]

def absorb(row, minn, minw, maxgap):
    """Merge a small fragment into whichever neighbour is closer in x."""
    out=[]
    for c in row:
        small = c['n']<minn or (c['x1']-c['x0']+1)<minw
        if small and out:
            prev=out[-1]; gp=c['x0']-prev['x1']
            nxt=None
            if gp<=maxgap:
                prev['x0']=min(prev['x0'],c['x0']); prev['x1']=max(prev['x1'],c['x1'])
                prev['y0']=min(prev['y0'],c['y0']); prev['y1']=max(prev['y1'],c['y1'])
                prev['px']=prev['px']+c['px']; prev['n']+=c['n']; continue
        out.append(dict(c))
    return out

def pipeline(bmp, xmin=0, xmax=10**9, maxw=72, minn=200, minw=16, maxgap=14):
    bs,seq=extract(bmp,xmin)
    res=[]
    for s in seq:
        s=[c for c in s if c['x1']<=xmax]
        t=[]
        for c in s: t.extend(split_wide(c,maxw))
        t.sort(key=lambda c:c['x0'])
        t=absorb(t,minn,minw,maxgap)
        t=[c for c in t if c['n']>=120]
        res.append(t)
    return bs,res

if __name__=='__main__':
    bmp=sys.argv[1]
    xmin=int(sys.argv[sys.argv.index('--xmin')+1]) if '--xmin' in sys.argv else 0
    xmax=int(sys.argv[sys.argv.index('--xmax')+1]) if '--xmax' in sys.argv else 10**9
    bs,seq=pipeline(bmp,xmin,xmax)
    print('per line',[len(s) for s in seq],'total',sum(len(s) for s in seq))
