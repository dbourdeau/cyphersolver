"""contact sheet of a range of page numbers: sheetr.py <dir> first last [cols=6] [tw=330]"""
import sys, os
from PIL import Image, ImageDraw
d=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); cols=int(sys.argv[4]) if len(sys.argv)>4 else 6; tw=int(sys.argv[5]) if len(sys.argv)>5 else 330
fs=[(i,f'{d}/p{i:04d}.png') for i in range(a,b+1) if os.path.exists(f'{d}/p{i:04d}.png')]
ims=[]
for i,f in fs:
    im=Image.open(f).convert('RGB'); im=im.resize((tw,int(im.height*tw/im.width))); ImageDraw.Draw(im).text((4,4),str(i),fill=(255,0,0)); ims.append(im)
rows=(len(ims)+cols-1)//cols; h=ims[0].height; sh=Image.new('RGB',(cols*tw,rows*h),'white')
for j,im in enumerate(ims): sh.paste(im,((j%cols)*tw,(j//cols)*h))
fn=f'{d}/s_{a:04d}_{b:04d}.jpg'; sh.save(fn,quality=80); print(fn,len(ims),sh.size)
