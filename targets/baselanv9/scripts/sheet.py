"""Contact sheet: sheet.py out.jpg width_per_thumb canvas1 canvas2 ...  (reads img/p2000/cNNN_*.jpg)"""
import sys, glob
from PIL import Image, ImageDraw
D='/home/claude/keyless/round40c/basel_anv9/img/p2000/'
out=sys.argv[1]; w=int(sys.argv[2]); cs=[int(x) for x in sys.argv[3:]]
ims=[]
for c in cs:
    f=glob.glob(D+'c%03d_*.jpg'%c)
    if not f: continue
    im=Image.open(f[0]).convert('RGB'); h=int(im.size[1]*w/im.size[0]); im=im.resize((w,h))
    d=ImageDraw.Draw(im); d.rectangle([0,0,60,22],fill='yellow'); d.text((3,3),'c%d'%c,fill='black'); ims.append(im)
H=max(i.size[1] for i in ims); S=Image.new('RGB',(w*len(ims)+5*(len(ims)-1),H),'white')
x=0
for i in ims: S.paste(i,(x,0)); x+=w+5
S.save(out,quality=85); print(out,S.size)
