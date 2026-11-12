import sys
from PIL import Image
p,y0,y1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
x0=int(sys.argv[4]) if len(sys.argv)>4 else 0; x1=int(sys.argv[5]) if len(sys.argv)>5 else 99999
tw=int(sys.argv[6]) if len(sys.argv)>6 else 1900
im=Image.open('img/%s.jpg'%p); W,H=im.size; x1=min(x1,W)
c=im.crop((x0,y0,x1,min(y1,H))); sc=tw/c.width
c=c.resize((int(c.width*sc),int(c.height*sc)),Image.LANCZOS); c.save('crops/s_%s_%d_%d.jpg'%(p,y0,x0),quality=90); print(c.size)
