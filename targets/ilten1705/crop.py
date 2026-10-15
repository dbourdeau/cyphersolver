import sys
from PIL import Image
# usage: crop.py src x0 y0 x1 y1 out   (fractions 0-1)
src,x0,y0,x1,y1,out=sys.argv[1:7]
im=Image.open(src); W,H=im.size
c=im.crop((int(float(x0)*W),int(float(y0)*H),int(float(x1)*W),int(float(y1)*H)))
c.thumbnail((1600,1600)); c.save(out,quality=90)
