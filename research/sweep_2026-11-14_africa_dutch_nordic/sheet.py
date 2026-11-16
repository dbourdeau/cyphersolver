"""contact sheets: sheet.py DIR FIRST LAST [cols=6] [tile=330]  (files pNNNN.jpg) -> DIR/sheet_FIRST_LAST.jpg, tiles labelled with scan numbers"""
import sys,os
from PIL import Image,ImageDraw
d=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); cols=int(sys.argv[4]) if len(sys.argv)>4 else 6; tw=int(sys.argv[5]) if len(sys.argv)>5 else 330
fs=[(n,f'{d}/p{n:04d}.jpg') for n in range(a,b+1) if os.path.exists(f'{d}/p{n:04d}.jpg')]
ims=[]
for n,f in fs:
    im=Image.open(f).convert('RGB'); im=im.resize((tw,int(im.height*tw/im.width))); ImageDraw.Draw(im).text((4,2),str(n),fill=(255,0,0)); ims.append(im)
h=max(i.height for i in ims); rows=(len(ims)+cols-1)//cols
sh=Image.new('RGB',(cols*tw,rows*h),'white')
for j,im in enumerate(ims): sh.paste(im,((j%cols)*tw,(j//cols)*h))
fn=f'{d}/sheet_{a}_{b}.jpg'; sh.save(fn,quality=80); print(fn,len(ims),sh.size)
