"""Polar-unwrap a pentacle rim: unwrap.py in.jpg cx cy r_in r_out out_prefix [start_deg]
Clockwise from start_deg (0 = top). Letters written with tops outward read left to right, upright."""
import sys, math
import numpy as np
from PIL import Image
f,cx,cy,ri,ro,out=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),sys.argv[6]
start=float(sys.argv[7]) if len(sys.argv)>7 else 0.0
im=np.asarray(Image.open(f).convert('RGB')).astype(np.float32)
H,W,_=im.shape
rm=(ri+ro)/2; N=int(2*math.pi*rm); h=int(ro-ri)
strip=np.zeros((h,N,3),np.float32)+255
for j in range(N):
    th=math.radians(start)+2*math.pi*j/N
    s,c=math.sin(th),math.cos(th)
    for i in range(h):
        r=ro-i
        x=cx+r*s; y=cy-r*c
        if 0<=x<W-1 and 0<=y<H-1:
            x0,y0=int(x),int(y); dx,dy=x-x0,y-y0
            p=(im[y0,x0]*(1-dx)*(1-dy)+im[y0,x0+1]*dx*(1-dy)+im[y0+1,x0]*(1-dx)*dy+im[y0+1,x0+1]*dx*dy)
            strip[i,j]=p
S=Image.fromarray(strip.clip(0,255).astype(np.uint8))
seg=N//3+40
for k in range(3):
    a=max(0,k*N//3-20); S.crop((a,0,min(N,a+seg),h)).save('%s_%d.jpg'%(out,k))
print(N,h)
