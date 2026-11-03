# Sheets for reading each q-form by its tail: straightened lines, 1.5x, no labels but the line number.
import sys
from PIL import Image, ImageDraw, ImageEnhance
src=open('scripts/strips_f.py').read().split("sheets('f76r'")[0]
exec(src)
LINES['f77r']=LINES['f77r']+[(2975,2925),(3100,3050),(3215,3160),(3345,3285)]
XR={'f76r':(380,3170),'f76v':(330,3130),'f77r':(250,3170)}
SEG=3;H=205;TOP=45;SC=1.25;PER=5
def band2(im,yl,yr,x0,x1):
    W=x1-x0; out=Image.new('RGB',(W,H),'white')
    for x in range(x0,x1,16):
        y=yl+(yr-yl)*(x+8-LX)/(RX-LX)
        out.paste(im.crop((x,int(y-TOP),x+16,int(y-TOP)+H)),(x-x0,0))
    return out
for p in LINES:
    im=ImageEnhance.Contrast(Image.open(f'scans/{p}_full.jpg')).enhance(1.25)
    x0,x1=XR[p]; w=(x1-x0)//SEG
    items=[]
    for i,(a,b) in enumerate(LINES[p]):
        for s in range(SEG):
            items.append((i+1,s,a,b,x0+s*w,x0+(s+1)*w+50))
    n=0
    for k in range(0,len(items),PER):
        ch=items[k:k+PER]; hh=int(H*SC)
        S=Image.new('RGB',(int((w+50)*SC)+50,len(ch)*(hh+6)),'white'); d=ImageDraw.Draw(S)
        for r,(ln,s,a,b,xa,xb) in enumerate(ch):
            B=band2(im,a,b,xa,xb); B=B.resize((int(B.width*SC),hh),Image.LANCZOS)
            S.paste(B,(48,r*(hh+6))); d.text((2,r*(hh+6)+30),f'{ln:02d}{"abc"[s]}',fill='red')
            d.line((48+int(w*SC),r*(hh+6),48+int(w*SC),r*(hh+6)+12),fill='red',width=2)
        S.save(f'scans/t/{p}_{n:02d}.png'); n+=1
    print(p,n,S.size)
