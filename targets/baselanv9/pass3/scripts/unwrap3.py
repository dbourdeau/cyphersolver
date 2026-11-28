import sys, numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
# usage: unwrap3.py img out cx cy rin rout [start_deg]
img,out=sys.argv[1],sys.argv[2]; cx,cy,rin,rout=map(float,sys.argv[3:7]); st=float(sys.argv[7]) if len(sys.argv)>7 else -8
a=np.asarray(Image.open(img).convert('RGB'))
rm=(rin+rout)/2; n=int(2*np.pi*rm); h=int(rout-rin)
th=np.deg2rad(st)+np.arange(n)/rm
r=rout-np.arange(h)
X=(cx+np.outer(r,np.sin(th))).astype(int).clip(0,a.shape[1]-1)
Y=(cy-np.outer(r,np.cos(th))).astype(int).clip(0,a.shape[0]-1)
u=a[Y,X]
rows=3; w=n//rows+60
sheet=np.full((rows*(h+10),w,3),255,np.uint8)
for k in range(rows):
    seg=u[:,k*(n//rows):k*(n//rows)+w]
    sheet[k*(h+10):k*(h+10)+h,:seg.shape[1]]=seg
im=Image.fromarray(sheet)
if im.size[0]>1560: im=im.resize((1560,int(im.size[1]*1560/im.size[0])),Image.LANCZOS)
im.save(out,quality=88); print(out,im.size)
