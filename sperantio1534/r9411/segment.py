import sys, numpy as np
from PIL import Image, ImageOps
from scipy.signal import find_peaks
f,tag,xl,xr,ytop,ybot=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7])
im=Image.open(f).convert('L'); a=np.asarray(ImageOps.autocontrast(im,cutoff=1)).astype(float)
band=a[ytop:ybot, xl:xl+(xr-xl)//2]   # left half: less slant effect
ink=(band<np.percentile(band,6)).sum(1).astype(float)
k=np.convolve(ink,np.ones(31)/31,'same')
pk,_=find_peaks(k,distance=60,prominence=k.max()*0.05)
pk=pk+ytop; print(tag,len(pk)); print(list(pk))
half=(xr-xl)//2
for i,y in enumerate(pk):
    for j,(a0,a1) in enumerate([(xl,xl+half+80),(xl+half-80,xr)]):
        c=im.crop((a0,int(y-70),a1,int(y+95)))
        c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((1600,int(1600*c.size[1]/c.size[0])))
        c.save(f'r9411/c/{tag}_{i+1:02d}{"ab"[j]}.png')
