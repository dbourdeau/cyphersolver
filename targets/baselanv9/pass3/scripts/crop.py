import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
# usage: crop.py src out x0 y0 x1 y1 (fractions) [maxw]
src,out=sys.argv[1],sys.argv[2]; x0,y0,x1,y1=map(float,sys.argv[3:7]); mw=int(sys.argv[7]) if len(sys.argv)>7 else 1560
im=Image.open(src); W,H=im.size
c=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
if c.size[0]>mw: c=c.resize((mw,int(c.size[1]*mw/c.size[0])),Image.LANCZOS)
c.save(out,quality=88); print(out,c.size)
