import sys
from PIL import Image
p,y,x0,x1,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
im=Image.open('img/IMG_R4158_I24487_%s.jpg'%p)
c=im.crop((x0,y-70,x1,y+70));c=c.resize((c.size[0]*2//1,c.size[1]*2//1),Image.LANCZOS) if (x1-x0)<900 else c
c.save(out)
