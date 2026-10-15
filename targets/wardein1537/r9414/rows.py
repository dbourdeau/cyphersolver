"""Find text-line centres in each half of a page by dark-pixel profile; stack per-line half strips, 4 lines per image."""
import sys, numpy as np
from PIL import Image, ImageOps, ImageDraw
p=int(sys.argv[1]); x0,x1=int(sys.argv[2]),int(sys.argv[3]); ytop,ybot=int(sys.argv[4]),int(sys.argv[5])
im=Image.open(f'r9414/crops/P{p}_full.jpg').convert('L')
a=np.asarray(im).astype(float)
xm=(x0+x1)//2
def centres(u,v):
    band=a[ytop:ybot,u:v]; thr=np.percentile(band,8)
    prof=(band<thr+10).sum(1).astype(float)
    k=np.ones(25)/25; s=np.convolve(prof,k,'same')
    c=[i for i in range(30,len(s)-30) if s[i]==s[i-30:i+31].max() and s[i]>0.35*s.max()]
    out=[]
    for i in c:
        if not out or i-out[-1]>55: out.append(i)
    return [ytop+i for i in out]
L=centres(x0,xm); R=centres(xm,x1)
print(len(L),len(R)); print(L); print(R)
n=min(len(L),len(R))
strips=[]
for i in range(n):
    for (u,v,c) in [(x0,xm+40,L[i]),(xm-40,x1,R[i])]:
        s=ImageOps.autocontrast(im.crop((u,c-75,v,c+45)),cutoff=1)
        s=s.resize((1900,int(s.height*1900/s.width)))
        d=ImageDraw.Draw(s); d.text((5,5),f'{i+1}{"LR"[u!=x0]}',fill=0)
        strips.append(s)
for j in range(0,len(strips),8):
    g=strips[j:j+8]; H=sum(s.height for s in g)
    out=Image.new('L',(1900,H),255); y=0
    for s in g: out.paste(s,(0,y)); y+=s.height
    out.save(f'r9414/crops/P{p}_s{j//2+1:02d}.png')
