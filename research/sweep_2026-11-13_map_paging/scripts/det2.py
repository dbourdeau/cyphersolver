# det2.py: run-based detector. For each page: sort small glyph components along text lines, find runs of >=R consecutive small,
# similarly sized, closely spaced glyphs with no big component inside (signs/figures), score = total glyphs in such runs.
import sys,os,numpy as np
from PIL import Image,ImageFilter
from scipy import ndimage as ndi
def feat(p,R=7):
    im=Image.open(p).convert('L')
    a=np.asarray(im,dtype=np.float32)
    bg=np.asarray(im.filter(ImageFilter.BoxBlur(25)),dtype=np.float32)
    d=bg-a
    ink=d>max(18,np.percentile(d,97)*0.45)
    lab,n=ndi.label(ink,structure=np.ones((3,3)))
    if n==0: return 0,0
    sl=ndi.find_objects(lab)
    cnt=np.bincount(lab.ravel(),minlength=n+1)[1:]
    y0=np.array([s[0].start for s in sl]);y1=np.array([s[0].stop for s in sl])
    x0=np.array([s[1].start for s in sl]);x1=np.array([s[1].stop for s in sl])
    h=y1-y0;w=x1-x0;yc=(y0+y1)/2
    ok=(cnt>=12)
    small=ok&(h>=6)&(h<=24)&(w>=3)&(w<=22)
    big=ok&((w>30)|(h>26))
    # order comps by line band then x
    idx=np.where(ok)[0]
    band=(yc[idx]//22).astype(int)
    tot=0;best=0
    for b in np.unique(band):
        # include neighbours' comps lightly: use own band only
        ii=idx[band==b]; ii=ii[np.argsort(x0[ii])]
        run=0;prev=None;runh=[]
        for i in ii:
            if small[i] and (prev is None or (x0[i]-prev<=10 and abs(h[i]-np.median(runh) if runh else 0)<=8)):
                run+=1;runh.append(h[i]);prev=x1[i]
            else:
                if run>=R: tot+=run;best=max(best,run)
                if small[i]: run=1;runh=[h[i]];prev=x1[i]
                else: run=0;runh=[];prev=None
        if run>=R: tot+=run;best=max(best,run)
    return tot,best
if __name__=='__main__':
    d=sys.argv[1]; lo=int(sys.argv[2]) if len(sys.argv)>2 else 0; hi=int(sys.argv[3]) if len(sys.argv)>3 else 10**9
    for f in sorted(os.listdir(d)):
        if not f.endswith('.jpg'): continue
        try:
            if not (lo<=int(f[1:8])<=hi): continue
        except ValueError: pass
        try: t,b=feat(os.path.join(d,f))
        except Exception as e: t=b=-1
        print(f,t,b,sep='\t')
