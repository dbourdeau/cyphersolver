import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
# usage: crop.py src x0 y0 x1 y1 out [maxw]
src,x0,y0,x1,y1,out=sys.argv[1:7]
maxw=int(sys.argv[7]) if len(sys.argv)>7 else 1800
im=Image.open(src)
W,H=im.size
box=[float(v) for v in (x0,y0,x1,y1)]
if all(v<=1.0 for v in box): box=[box[0]*W,box[1]*H,box[2]*W,box[3]*H]
c=im.crop(tuple(int(v) for v in box))
c=ImageOps.autocontrast(c,cutoff=1)
if c.width>maxw: c=c.resize((maxw,int(c.height*maxw/c.width)),Image.LANCZOS)
c.save(out)
print(out,c.size,[int(v) for v in box])
