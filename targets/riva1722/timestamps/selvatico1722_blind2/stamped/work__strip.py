import sys
from PIL import Image
p,y0,y1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
x0=int(sys.argv[4]) if len(sys.argv)>4 else 0
x1=int(sys.argv[5]) if len(sys.argv)>5 else None
sc=float(sys.argv[6]) if len(sys.argv)>6 else 0.46
im=Image.open('/home/claude/en/trackB/b70_selvatico_read/img/%s.jpg'%p)
if x1 is None: x1=im.width
c=im.crop((x0,y0,x1,y1))
c=c.resize((int(c.width*sc),int(c.height*sc)),Image.LANCZOS)
out='work/s_%s_%d_%d_%d.jpg'%(p,y0,y1,x0)
c.save(out,quality=88); print(out,c.size)
