import sys
from PIL import Image, ImageOps; Image.MAX_IMAGE_PIXELS=None
img,tag,yc=sys.argv[1],sys.argv[2],int(sys.argv[3])
x0=int(sys.argv[4]); x1=int(sys.argv[5]); slope=float(sys.argv[6]) if len(sys.argv)>6 else 0
im=Image.open('img/'+img+'.png').convert('L')
tiles=[]
x=x0;i=0
while x<x1:
  y=int(yc+slope*(x-x0))
  c=im.crop((x,y-105,x+460,y+65)); c=ImageOps.autocontrast(c,cutoff=1)
  c.resize((c.width*3//1,c.height*3//1),Image.LANCZOS).save(f'seg/{tag}_{i}.png'); x+=400;i+=1
print(i)
