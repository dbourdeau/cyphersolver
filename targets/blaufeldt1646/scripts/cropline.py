"""cropline.py SRC PREFIX y x0 x1 nparts scale : cut a deskewed line into overlapping pieces, sharpen"""
import sys
from PIL import Image, ImageOps, ImageFilter
src,pre=sys.argv[1],sys.argv[2]; y,x0,x1,n=map(int,sys.argv[3:7]); s=float(sys.argv[7])
im=Image.open(src).convert('L')
w=(x1-x0)/n
for k in range(n):
    a=int(x0+k*w-20); b=int(x0+(k+1)*w+20)
    c=im.crop((a,y-32,b,y+26)); c=ImageOps.autocontrast(c,cutoff=2)
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=3,percent=120))
    c.save(f'{pre}_{k}.png')
