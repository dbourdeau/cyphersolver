"""Polar unwrap of pentacle rims (vectorised version of ../scripts/unwrap.py, same geometry: clockwise from
start_deg, 0 = top, tops of letters outward).  unwrap2.py page.jpg out.jpg cx cy r_in r_out [start_deg] [rows] [scale]
Writes one image: the strip cut into <rows> rows stacked, scaled by <scale>."""
import sys, math, numpy as np
from PIL import Image
from scipy.ndimage import map_coordinates
f,out=sys.argv[1],sys.argv[2]; cx,cy,ri,ro=map(float,sys.argv[3:7])
start=float(sys.argv[7]) if len(sys.argv)>7 else -10.0
rows=int(sys.argv[8]) if len(sys.argv)>8 else 3
scale=float(sys.argv[9]) if len(sys.argv)>9 else 0.6
im=np.asarray(Image.open(f).convert('L')).astype(np.float32)
rm=(ri+ro)/2; N=int(2*math.pi*rm*scale); h=int((ro-ri)*scale)
th=math.radians(start)+2*math.pi*np.arange(N)/N
r=ro-np.arange(h)/scale
R,T=np.meshgrid(r,th,indexing='ij')
X=cx+R*np.sin(T); Y=cy-R*np.cos(T)
S=map_coordinates(im,[Y,X],order=1,cval=255)
seg=N//rows; ov=int(40*scale)
parts=[S[:,max(0,k*seg-ov):min(N,(k+1)*seg+ov)] for k in range(rows)]
w=max(p.shape[1] for p in parts)
canvas=np.full((h*rows+6*(rows-1),w),255,np.float32)
for k,p in enumerate(parts): canvas[k*(h+6):k*(h+6)+h,:p.shape[1]]=p
Image.fromarray(canvas.clip(0,255).astype(np.uint8)).save(out,quality=92)
print(N,h,w)
