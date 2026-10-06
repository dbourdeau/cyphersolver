# zoom.py page line [x-half] : crop one line of a rotated R1072 page at full resolution
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
f,ln=sys.argv[1],int(sys.argv[2]); top=float(sys.argv[3]) if len(sys.argv)>3 else 780; step=float(sys.argv[4]) if len(sys.argv)>4 else 152
rot=int(sys.argv[5]) if len(sys.argv)>5 else -90
im=Image.open(f).convert('L').rotate(rot,expand=True); im=ImageOps.autocontrast(im,cutoff=1)
y=int(top+(ln-3)*step)-40
a=im.crop((380,y,1900,y+230)); b=im.crop((1860,y,3420,y+230))
out=Image.new('L',(1560,460),255); out.paste(a,(0,0)); out.paste(b,(0,230)); out.save('sm2/zl.jpg')
