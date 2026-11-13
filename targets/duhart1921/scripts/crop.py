import sys
from PIL import Image
# usage: crop.py src out x0 y0 x1 y1 scale  (coords in original pixels)
src,out,x0,y0,x1,y1,s=sys.argv[1:8]
im=Image.open(src).crop((int(x0),int(y0),int(x1),int(y1)))
s=float(s); im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS); im.save(out)
