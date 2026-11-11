"""python combo.py <scratch> <out name> <Shelfmark>... : stack the sample sheets of several volumes into one image, trimmed of blank rows"""
import sys,glob
from PIL import Image,ImageDraw,ImageChops
S,out=sys.argv[1],sys.argv[2]; ims=[]
for sm in sys.argv[3:]:
    for f in sorted(glob.glob(f'{S}/sheets/{sm}_0*.jpg')):
        if f.endswith('x.jpg'): continue
        im=Image.open(f).convert('RGB'); bb=ImageChops.invert(im.convert('L')).point(lambda p:255 if p>40 else 0).getbbox()
        if bb: im=im.crop((0,0,im.width,bb[3]))
        lab=Image.new('RGB',(im.width,22),'yellow'); ImageDraw.Draw(lab).text((4,4),sm,fill='black'); ims+=[lab,im]
sh=Image.new('RGB',(max(i.width for i in ims),sum(i.height for i in ims)),'white'); y=0
for i in ims: sh.paste(i,(0,y)); y+=i.height
sh.save(f'{S}/sheets/{out}.jpg',quality=78); print(sh.size)
