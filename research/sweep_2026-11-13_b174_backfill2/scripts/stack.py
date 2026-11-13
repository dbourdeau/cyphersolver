# stack.py out dir pos:y0:y1 ... : stack fractional horizontal bands (native width) from scratch pages, labelled
import sys,os
from PIL import Image,ImageDraw
out,d=sys.argv[1],sys.argv[2]; bands=[]
for t in sys.argv[3:]:
    p,y0,y1=t.split(':'); im=Image.open(os.path.join(d,'q%07d.jpg'%int(p))).convert('RGB'); w,h=im.size
    b=im.crop((0,int(float(y0)*h),w,int(float(y1)*h))); dr=ImageDraw.Draw(b); dr.rectangle([0,0,110,18],fill='white'); dr.text((3,3),t,fill='red'); bands.append(b)
W=max(b.width for b in bands); S=Image.new('RGB',(W,sum(b.height for b in bands)),'white'); y=0
for b in bands: S.paste(b,(0,y)); y+=b.height
S.save(out,quality=80); print(S.size)
