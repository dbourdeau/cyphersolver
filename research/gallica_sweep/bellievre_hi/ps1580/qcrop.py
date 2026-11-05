import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
# qcrop.py src prefix y_center x0 x1 nparts [half_h]
src,pre,yc,x0,x1,n=sys.argv[1:7]
hh=int(sys.argv[7]) if len(sys.argv)>7 else 65
yc,x0,x1,n=int(yc),int(x0),int(x1),int(n)
im=Image.open(src)
w=(x1-x0)/n
for k in range(n):
    a=int(x0+k*w)-40; b=int(x0+(k+1)*w)+40
    c=im.crop((a,yc-hh,b,yc+hh))
    c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    c.save(f"{pre}_{k}.jpg"); print(pre,k,a,b)
