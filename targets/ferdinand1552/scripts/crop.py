import sys
from PIL import Image, ImageOps
# usage: crop.py img x0 y0 x1 y1 scale out
a=sys.argv
im=Image.open(a[1]).convert('L')
x0,y0,x1,y1=map(int,a[2:6]); s=float(a[6])
c=im.crop((x0,y0,x1,y1))
c=ImageOps.autocontrast(c,cutoff=1)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(a[7],quality=90)
