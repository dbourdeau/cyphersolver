# strip.py out dir W pos ... : side-by-side reduced pages from scratch (for identifying signer/date)
import sys,os
from PIL import Image,ImageDraw
out,d,W=sys.argv[1],sys.argv[2],int(sys.argv[3]); ims=[]
for p in sys.argv[4:]:
    i=Image.open(os.path.join(d,'q%07d.jpg'%int(p))).convert('RGB'); i=i.resize((W,int(i.height*W/i.width)))
    ImageDraw.Draw(i).text((4,4),p,fill='red'); ims.append(i)
S=Image.new('RGB',(W*len(ims),max(i.height for i in ims)),'white')
for k,i in enumerate(ims): S.paste(i,(k*W,0))
S.save(out,quality=75)
