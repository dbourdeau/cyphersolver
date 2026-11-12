import sys
from PIL import Image, ImageDraw
page,y0,pitch,n,xs,xe=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])
im=Image.open(f'img/{page}_full.jpg')
H=330; segw=1500; step=(xe-xs-segw)//2
for i in range(n):
    cy=int(y0+i*pitch)
    out=Image.new('RGB',(segw,3*H+20),'white')
    for s in range(3):
        x=xs+s*step
        out.paste(im.crop((x,cy-H//2,x+segw,cy+H//2)),(0,s*(H+10)))
    out.save(f'crops2/{page}_L{i+1:02d}.jpg',quality=90)
