# strips.py image rot y0 y1 n tag [x0 x1] : full-width strips of a rotated page into sm2/<tag>_k.jpg
import sys
from PIL import Image, ImageOps
f,rot,y0,y1,n,tag=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),sys.argv[6]
im=Image.open(f).convert('L').rotate(rot,expand=True); im=ImageOps.autocontrast(im,cutoff=1)
x0=int(sys.argv[7]) if len(sys.argv)>7 else 150; x1=int(sys.argv[8]) if len(sys.argv)>8 else im.size[0]-100
for k in range(n):
    a=y0+k*(y1-y0)//n-40; b=y0+(k+1)*(y1-y0)//n+40
    c=im.crop((x0,a,x1,b)); s=1600/c.size[0]; c.resize((1600,int(c.size[1]*s))).save(f'sm2/{tag}_{k}.jpg',quality=90)
