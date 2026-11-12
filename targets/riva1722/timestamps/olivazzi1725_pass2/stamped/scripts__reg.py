import sys
from PIL import Image
# reg.py page out scale x,y,w,h [x,y,w,h ...]  -> stacked
page,out,sc=sys.argv[1],sys.argv[2],float(sys.argv[3])
im=Image.open(f'img/{page}_full.jpg')
parts=[]
for a in sys.argv[4:]:
    x,y,w,h=map(int,a.split(','))
    c=im.crop((x,y,x+w,y+h))
    if sc!=1: c=c.resize((int(w*sc),int(h*sc)),Image.LANCZOS)
    parts.append(c)
W=max(p.width for p in parts);H=sum(p.height for p in parts)+8*(len(parts)-1)
o=Image.new('RGB',(W,H),'white');y=0
for p in parts: o.paste(p,(0,y));y+=p.height+8
o.save(out,quality=92)
