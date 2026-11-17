"""Detect printed text lines in a two-column dictionary page image by projection profiles.
Functions: analyse(path) -> dict with page box, divider x, header line, and per-column line boxes (line 1 = first line under the running head)."""
from PIL import Image, ImageOps
import numpy as np

def runs(mask, minlen):
    out=[];start=None
    for i,v in enumerate(list(mask)+[False]):
        if v and start is None: start=i
        if not v and start is not None:
            if i-start>=minlen: out.append((start,i))
            start=None
    return out

def analyse(path):
    im=Image.open(path).convert('L')
    sc=1600/im.size[0]; small=im.resize((1600,int(im.size[1]*sc)))
    a=np.asarray(small).astype(float)
    H,W=a.shape
    # page area: paper is bright; find columns/rows with mean brightness > 110
    colmean=a.mean(axis=0); rowmean=a.mean(axis=1)
    bright_cols=runs(colmean>70, 300); bright_rows=runs(rowmean>70, 300)
    x0,x1=max(bright_cols,key=lambda r:r[1]-r[0]); y0,y1=max(bright_rows,key=lambda r:r[1]-r[0])
    ink_full=(a<110)
    vcf=ink_full[int(y0+(y1-y0)*0.15):int(y0+(y1-y0)*0.9),:].mean(axis=0)
    # divider: strongest thin vertical rule in the central part of the image, must be dark over most of the height
    cands=range(int(W*0.3),int(W*0.8))
    dxa=max(cands,key=lambda x:vcf[x])
    colw=x1-dxa
    x0=max(0,dxa-colw)
    pg=a[y0:y1,x0:x1]; ph,pw=pg.shape
    ink=(pg<110)
    dx=dxa-x0
    res={'scale':sc,'page':(x0,y0,x1,y1),'divider':dx+x0,'cols':{}}
    for c,(cx0,cx1) in {'a':(int(pw*0.01),dx-3),'b':(dx+4,pw-int(pw*0.02))}.items():
        sub=ink[:,cx0:cx1]
        prof=sub.mean(axis=1)
        thr=max(0.02,prof.max()*0.08)
        lines=runs(prof>thr,4)
        # merge fragments closer than 3px
        m=[]
        for s,e in lines:
            if m and s-m[-1][1]<3: m[-1]=(m[-1][0],e)
            else: m.append((s,e))
        hts=sorted(e-s for s,e in m); med=hts[len(hts)//2] if hts else 0
        m=[(s,e) for s,e in m if e-s>=med*0.45]
        res['cols'][c]={'x':(cx0+x0,cx1+x0),'lines':[(s+y0,e+y0) for s,e in m]}
    return res
