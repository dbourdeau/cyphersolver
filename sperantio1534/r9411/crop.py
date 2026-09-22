import sys
from PIL import Image, ImageOps
f,x0,y0,x1,y1,out=sys.argv[1:7]
im=Image.open(f).convert('L'); s=im.size[1]/1467
c=im.crop((int(float(x0)*s),int(float(y0)*s),int(float(x1)*s),int(float(y1)*s)))
c=ImageOps.autocontrast(c,cutoff=1); w=int(sys.argv[7]) if len(sys.argv)>7 else 1600
c=c.resize((w,int(w*c.size[1]/c.size[0]))); c.save(out)
