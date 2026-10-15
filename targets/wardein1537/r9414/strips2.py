"""Per-line half strips on a slanted grid: centre(line, x) = y06 + (line-6)*pitch + slope*(x-x0). 4 lines per image."""
import sys
from PIL import Image, ImageOps, ImageDraw
p=int(sys.argv[1]); x0,x1=int(sys.argv[2]),int(sys.argv[3]); first=int(sys.argv[4]); y1=float(sys.argv[5]); pitch=float(sys.argv[6]); slope=float(sys.argv[7]); last=int(sys.argv[8])
rot=len(sys.argv)>9 and sys.argv[9]=='rot'
im=Image.open(f'r9414/crops/P{p}_full.jpg').convert('L')
xm=(x0+x1)//2
strips=[]
for ln in range(first,last+1):
    for h,(u,v) in enumerate([(x0,xm+60),(xm-60,x1)]):
        c=y1+(ln-first)*pitch+slope*((u+v)/2-x0)
        s=ImageOps.autocontrast(im.crop((u,int(c-62),v,int(c+48))),cutoff=1)
        s=s.resize((1900,int(s.height*1900/s.width)))
        d=ImageDraw.Draw(s); d.rectangle((0,0,60,25),fill=255); d.text((3,3),f'{ln:02d}{"LR"[h]}',fill=0)
        strips.append(s)
for j in range(0,len(strips),8):
    g=strips[j:j+8]; H=sum(s.height for s in g)
    out=Image.new('L',(1900,H),255); y=0
    for s in g: out.paste(s,(0,y)); y+=s.height
    out.save(f'r9414/crops/P{p}_t{first+j//2:02d}.png')
