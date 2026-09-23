import sys,json
from PIL import Image
import numpy as np
ln=int(sys.argv[1]); x0=int(sys.argv[2]) if len(sys.argv)>2 else 0; x1=int(sys.argv[3]) if len(sys.argv)>3 else 3320
sc=float(sys.argv[4]) if len(sys.argv)>4 else 1.3
im=np.array(Image.open('p16171_P2.png').convert('L'))
T=json.load(open('p2_thirds.json'))
xs=[900,1650,2450]; ys=[T['900'][ln-1],T['1650'][ln-1],T['2450'][ln-1]]
H=int(sys.argv[5]) if len(sys.argv)>5 else 62
cols=[]
for x in range(x0,min(x1,im.shape[1])):
    y=int(np.interp(x,xs,ys,left=None,right=None)) if 900<=x<=2450 else int(ys[0]+(x-900)*(ys[1]-ys[0])/750 if x<900 else ys[2]+(x-2450)*(ys[2]-ys[1])/800)
    cols.append(im[max(0,y-H):y+H,x])
out=np.stack(cols,1)
# split into rows of 800 px
segs=[out[:,i:i+800] for i in range(0,out.shape[1],800)]
W=800;res=np.full((2*H*len(segs),W),255,np.uint8)
for j,s in enumerate(segs): res[j*2*H:j*2*H+s.shape[0],:s.shape[1]]=s
Image.fromarray(res).resize((int(W*sc),int(res.shape[0]*sc))).save('zs.png')
