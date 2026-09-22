"""One image per line: three thirds, each a 230 px tall window, ~1.8x, red ticks at the expected line centre.
args: page x0 x1 first last y_first_a:pitch_a,y_first_b:pitch_b,y_first_c:pitch_c [rot]"""
import sys
from PIL import Image, ImageOps, ImageDraw
p=int(sys.argv[1]); x0,x1=int(sys.argv[2]),int(sys.argv[3]); first,last=int(sys.argv[4]),int(sys.argv[5])
fits=[tuple(map(float,f.split(':'))) for f in sys.argv[6].split(',')]
import os; im=Image.open(os.environ.get('SRC') or f'../img/IMG_R9414_I44519_P{p}.jpg').convert('L')
if len(sys.argv)>7: im=im.rotate(180)
w=(x1-x0)//3; bands=[(x0+i*w-(50 if i else 0), x0+(i+1)*w+50) for i in range(3)]
for ln in range(first,last+1):
    strips=[]
    for b,(u,v) in enumerate(bands):
        y0,pitch=fits[b]; c=int(y0+(ln-first)*pitch)
        s=ImageOps.autocontrast(im.crop((u,c-120,v,c+110)),cutoff=1).convert('RGB')
        s=s.resize((1900,int(s.height*1900/s.width)))
        d=ImageDraw.Draw(s); yc=int(120*1900/(v-u))
        d.rectangle((0,yc-4,30,yc+4),fill=(255,0,0)); d.rectangle((1870,yc-4,1900,yc+4),fill=(255,0,0))
        d.rectangle((30,0,90,22),fill=(255,255,255)); d.text((33,3),f'{ln:02d}{"abc"[b]}',fill=(0,0,0))
        strips.append(s)
    H=sum(s.height for s in strips); out=Image.new('RGB',(1900,H),'white'); y=0
    for s in strips: out.paste(s,(0,y)); y+=s.height+0
    out.save(f'crops2/L{p}_{ln:02d}.png')
