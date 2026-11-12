import sys
from PIL import Image
p,y0,y1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
sc=float(sys.argv[4]) if len(sys.argv)>4 else 0.62
im=Image.open('/home/claude/en/trackB/b70_selvatico_read/img/%s.jpg'%p); W,H=im.size
for j,(a,b) in enumerate([(0,W//2+200),(W//2-200,W)]):
    c=im.crop((a,y0,b,min(y1,H))); c=c.resize((int(c.width*sc),int(c.height*sc)),Image.LANCZOS)
    c.save('/home/claude/en/trackB/b70_selvatico_read/crops/%s_%d_%s.jpg'%(p,y0,'ab'[j]),quality=90)
