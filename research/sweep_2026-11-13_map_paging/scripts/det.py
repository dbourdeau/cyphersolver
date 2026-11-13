# det.py dir -> TSV: file, score, ncomp_small, rowmax  (own detector, 13 Nov 2026)
# idea: bare cipher = many isolated small glyphs of uniform size in lines; cursive text joins into long components
import sys,os,numpy as np
from PIL import Image,ImageFilter
from scipy import ndimage as ndi
def feat(p):
    im=Image.open(p).convert('L'); W,H=im.size
    a=np.asarray(im,dtype=np.float32)
    # background normalise via large box blur
    bg=np.asarray(im.filter(ImageFilter.BoxBlur(25)),dtype=np.float32)
    d=bg-a
    ink=d>max(18,np.percentile(d,97)*0.45)
    lab,n=ndi.label(ink,structure=np.ones((3,3)))
    if n==0: return 0,0,0
    sl=ndi.find_objects(lab)
    cnt=np.bincount(lab.ravel(),minlength=n+1)[1:]
    hs=np.array([s[0].stop-s[0].start for s in sl]); ws=np.array([s[1].stop-s[1].start for s in sl])
    ys=np.array([(s[0].start+s[0].stop)/2 for s in sl])
    sel=(hs>=7)&(hs<=26)&(ws>=4)&(ws<=24)&(cnt>=15)&(cnt<hs*ws*0.9)
    k=int(sel.sum())
    # rows: histogram of selected glyph centres in 24px bands -> max
    band=(ys[sel]//24).astype(int)
    rowmax=int(np.bincount(band).max()) if k else 0
    # number of bands with >=20 glyphs
    rows20=int((np.bincount(band,minlength=1)>=20).sum()) if k else 0
    return k,rowmax,rows20
if __name__=='__main__':
    d=sys.argv[1]
    for f in sorted(os.listdir(d)):
        if not f.endswith('.jpg'): continue
        try: k,r,r20=feat(os.path.join(d,f))
        except Exception as e: k=r=r20=-1
        print(f,k,r,r20,sep='\t')
