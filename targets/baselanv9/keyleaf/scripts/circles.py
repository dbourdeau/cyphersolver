"""Find pentacle circles on a page: circles.py page.jpg [ncols nrows] -> cx cy r_in r_out per circle (full-size px).
Red ink (R-G>22, R-B>22) at 1/8 scale; Hough circle transform (skimage) for radii 100-260 (scaled); the two
concentric red rings give r_in and r_out by a radial histogram around the Hough centre."""
import sys, numpy as np
from PIL import Image
from skimage.transform import hough_circle, hough_circle_peaks
f=sys.argv[1]; maxc=int(sys.argv[2]) if len(sys.argv)>2 else 6
im=Image.open(f).convert('RGB'); W,H=im.size
sc=8
sm=np.asarray(im.resize((W//sc,H//sc))).astype(int)
red=((sm[:,:,0]-sm[:,:,1])>18)&((sm[:,:,0]-sm[:,:,2])>18)
radii=np.arange(70,170,2)
hs=hough_circle(red,radii)
acc,cx,cy,rr=hough_circle_peaks(hs,radii,min_xdistance=60,min_ydistance=60,total_num_peaks=maxc)
ys,xs=np.nonzero(red)
out=[]
for a,x,y,r in zip(acc,cx,cy,rr):
    d=np.hypot(xs-x,ys-y); m=(d>r*0.75)&(d<r*1.25)
    hist,edges=np.histogram(d[m],bins=np.arange(r*0.75,r*1.25,1.5))
    pk=[]
    for i in np.argsort(hist)[::-1]:
        v=edges[i]+0.75
        if all(abs(v-p)>5 for p in pk): pk.append(v)
        if len(pk)==2: break
    pk=sorted(pk)
    out.append((y*sc,x*sc,pk[0]*sc,pk[-1]*sc,a))
out.sort(key=lambda t:(round(t[0]/1400),t[1]))
for y,x,a,b,acc in out: print('%d %d %d %d %.2f'%(x,y,a,b,acc))
