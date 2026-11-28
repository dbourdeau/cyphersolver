# polar unwrap, clockwise from start_deg (0 = top), text upright when written along the circle reading clockwise
# usage: unwrap5.py img outprefix cx cy rin rout start_deg nseg [scale] [ccw]
import sys, numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
img,out=sys.argv[1],sys.argv[2]; cx,cy,rin,rout,st=map(float,sys.argv[3:8]); nseg=int(sys.argv[8])
sc=float(sys.argv[9]) if len(sys.argv)>9 else 0.6; ccw=len(sys.argv)>10 and sys.argv[10]=='ccw'
a=np.asarray(Image.open(img).convert('RGB'))
rm=(rin+rout)/2; n=int(2*np.pi*rm); h=int(rout-rin)
th=np.deg2rad(st)+np.arange(n)/rm*(-1 if ccw else 1)
r=(rout-np.arange(h)) if not ccw else (rin+np.arange(h))
X=(cx+np.outer(r,np.sin(th))).astype(int).clip(0,a.shape[1]-1)
Y=(cy-np.outer(r,np.cos(th))).astype(int).clip(0,a.shape[0]-1)
u=a[Y,X]
L=n//nseg; ov=int(0.06*L)
for k in range(nseg):
    seg=u[:,k*L:min(n,(k+1)*L+ov)]
    if seg.shape[1]<(k+1)*L+ov-k*L and k==nseg-1: seg=np.concatenate([seg,u[:,:ov]],axis=1)
    im=Image.fromarray(np.ascontiguousarray(seg)); im=im.resize((int(im.size[0]*sc),int(im.size[1]*sc)),Image.LANCZOS)
    im.save('%s_%d.jpg'%(out,k),quality=88); print('%s_%d.jpg'%(out,k),im.size)
ims=[Image.open('%s_%d.jpg'%(out,k)) for k in range(nseg)]
W=max(i.size[0] for i in ims); H=sum(i.size[1]+8 for i in ims)
sh=Image.new('RGB',(W,H),'white'); y=0
for i in ims: sh.paste(i,(0,y)); y+=i.size[1]+8
sh.save(out+'_sheet.jpg',quality=88); print(out+'_sheet.jpg',sh.size)
