"""grid.py out.jpg thumb_w per_row c1 c2: grid of canvases c1..c2 (img/p2000), labelled."""
import sys, glob
from PIL import Image, ImageDraw
D='/home/claude/keyless/round40c/basel_anv9/img/p2000/'
out=sys.argv[1]; w=int(sys.argv[2]); per=int(sys.argv[3]); a,b=int(sys.argv[4]),int(sys.argv[5])
ims=[]
for c in range(a,b+1):
    f=glob.glob(D+'c%03d_*.jpg'%c)
    if not f: continue
    im=Image.open(f[0]).convert('RGB'); h=int(im.size[1]*w/im.size[0]); im=im.resize((w,h))
    d=ImageDraw.Draw(im); d.rectangle([0,0,34,14],fill='yellow'); d.text((2,2),str(c),fill='black'); ims.append(im)
H=max(i.size[1] for i in ims); rows=(len(ims)+per-1)//per
S=Image.new('RGB',(per*(w+3),rows*(H+3)),'white')
for k,i in enumerate(ims): S.paste(i,((k%per)*(w+3),(k//per)*(H+3)))
S.save(out,quality=80); print(out,S.size,len(ims))
