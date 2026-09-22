import sys
from PIL import Image
# usage: crop.py id x0 y0 x1 y1 out   (coords on 800-px-wide version)
i,x0,y0,x1,y1,out=sys.argv[1],*map(float,sys.argv[2:6]),sys.argv[6]
im=Image.open(f'img/full_{i}.jpg'); s=im.width/800
c=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
if c.width>1900: c=c.resize((1900,int(c.height*1900/c.width)))
c.save(f'sheets/{out}.jpg')
