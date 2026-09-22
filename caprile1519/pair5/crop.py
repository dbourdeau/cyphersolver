import sys
from PIL import Image, ImageOps; Image.MAX_IMAGE_PIXELS=None
p,x0,y0,x1,y1,s,out=sys.argv[1:]
im=Image.open('img/IMG_R1131_I57%s.png'%p).convert('L')
x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); s=float(s)
c=im.crop((x0,y0,x1,y1)); c=ImageOps.autocontrast(c,cutoff=1)
c.resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS).save('pair5/crops/'+out)
