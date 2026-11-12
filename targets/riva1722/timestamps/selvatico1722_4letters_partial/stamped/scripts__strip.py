import sys
from PIL import Image
p,y0,y1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
x0=int(sys.argv[4]) if len(sys.argv)>4 else 0; x1=int(sys.argv[5]) if len(sys.argv)>5 else 99999
B='/home/claude/en/trackB/b70_selvatico_read/'
im=Image.open(B+'img/%s.jpg'%p); W,H=im.size; x1=min(x1,W)
c=im.crop((x0,y0,x1,min(y1,H))); sc=min(1.0,1560/c.width)
c=c.resize((int(c.width*sc),int(c.height*sc)),Image.LANCZOS); c.save(B+'crops/s_%s_%d.jpg'%(p,y0),quality=90); print(c.size)
