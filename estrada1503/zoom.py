import sys
from PIL import Image, ImageOps
src,out=sys.argv[1],sys.argv[2]; x0,y0,x1,y1=map(int,sys.argv[3:7]); s=float(sys.argv[7]) if len(sys.argv)>7 else 5
im=Image.open(src).convert('L'); c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=1)
c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(out)
