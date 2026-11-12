"""python crop.py src out x0 y0 x1 y1 [scale]  (fractions 0-1 of the image)"""
import sys
from PIL import Image
src,out=sys.argv[1],sys.argv[2]; x0,y0,x1,y1=map(float,sys.argv[3:7]); s=float(sys.argv[7]) if len(sys.argv)>7 else 1
im=Image.open(src); W,H=im.size; c=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
if s!=1: c=c.resize((int(c.width*s),int(c.height*s)))
c.save(out,quality=90); print(out,c.size)
