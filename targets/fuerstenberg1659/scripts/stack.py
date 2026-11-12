import sys
from PIL import Image, ImageDraw
base=sys.argv[1]; out=sys.argv[2]; names=sys.argv[3:]
ims=[Image.open(base+'/work/crops/'+n) for n in names]
W=max(i.width for i in ims); H=sum(i.height+20 for i in ims)
c=Image.new('RGB',(W,H),'white'); y=0
d=ImageDraw.Draw(c)
for n,i in zip(names,ims):
    c.paste(i,(0,y)); y+=i.height; d.rectangle([0,y,W,y+20],fill='red'); y+=20
c.save(base+'/work/crops/'+out)
