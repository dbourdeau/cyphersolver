# zoom: python cp12/zoom.py P x0 x1 yc out [scale]  (orig image coords)
import sys
from PIL import Image, ImageOps
p,x0,x1,yc,out=sys.argv[1],*map(int,sys.argv[2:5]),sys.argv[5]
sc=int(sys.argv[6]) if len(sys.argv)>6 else 4
im=Image.open(f'../img/IMG_R9414_I44519_P{p}.jpg').convert('L')
c=ImageOps.autocontrast(im.crop((x0,yc-70,x1,yc+60)),cutoff=1)
c.resize((c.width*sc,c.height*sc),Image.LANCZOS).save(out)
