import sys
from PIL import Image, ImageOps; Image.MAX_IMAGE_PIXELS=None
img,tag,yc=sys.argv[1],sys.argv[2],int(sys.argv[3])
xs=[int(v) for v in sys.argv[4].split(',')] if len(sys.argv)>4 else [600,1300,2000]
w=int(sys.argv[5]) if len(sys.argv)>5 else 800
im=Image.open('img/'+img+'.png').convert('L')
for i,x in enumerate(xs):
  c=im.crop((x,yc-110,x+w,yc+90)); c=ImageOps.autocontrast(c,cutoff=1)
  c.resize((c.width*2,c.height*2),Image.LANCZOS).save(f'seg/{tag}_{i}.png')
