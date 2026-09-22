import sys, numpy as np
from PIL import Image
p=int(sys.argv[1]); x0,x1=int(sys.argv[2]),int(sys.argv[3]); y0,y1=int(sys.argv[4]),int(sys.argv[5]); rot=len(sys.argv)>6
im=Image.open(f'../img/IMG_R9414_I44519_P{p}.jpg').convert('L')
if rot: im=im.rotate(180)
a=np.asarray(im).astype(float); w=(x1-x0)//3
for b in range(3):
    band=a[y0:y1,x0+b*w:x0+(b+1)*w]; thr=np.percentile(band,6)+15
    s=np.convolve((band<thr).sum(1).astype(float),np.ones(31)/31,'same')
    c=[i for i in range(45,len(s)-45) if s[i]==s[i-45:i+46].max() and s[i]>0.25*s.max()]
    print(b,len(c),[y0+i for i in c])
