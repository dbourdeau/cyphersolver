import sys, numpy as np
from PIL import Image, ImageOps, ImageDraw
p=int(sys.argv[1]); x0,x1=int(sys.argv[2]),int(sys.argv[3]); y0,y1=int(sys.argv[4]),int(sys.argv[5]); rot=sys.argv[6]=='r'
lines=list(map(int,sys.argv[7].split(':'))); first=lines[0]
im=Image.open(f'../img/IMG_R9414_I44519_P{p}.jpg').convert('L')
if rot: im=im.rotate(180)
a=np.asarray(im).astype(float); w=(x1-x0)//3
P=[]
for b in range(3):
    band=a[y0:y1,x0+b*w:x0+(b+1)*w]; thr=np.percentile(band,6)+15
    s=np.convolve((band<thr).sum(1).astype(float),np.ones(31)/31,'same')
    c=[i for i in range(45,len(s)-45) if s[i]==s[i-45:i+46].max() and s[i]>0.25*s.max()]
    d=[]
    for i in c:
        if not d or i-d[-1]>40: d.append(i)
    P.append([y0+i for i in d])
S=3; H=int(sys.argv[8]) if len(sys.argv)>8 else 85
for k,ln in enumerate(range(lines[0],lines[1]+1)):
    strips=[]
    for b in range(3):
        c=P[b][k]; u=x0+b*w-(40 if b else 0); v=x0+(b+1)*w+40
        s=ImageOps.autocontrast(im.crop((u,c-H,v,c+H-15)),cutoff=1).convert('RGB')
        s=s.resize((s.width*S//2*2//2, s.height*S))
        dr=ImageDraw.Draw(s); dr.rectangle((0,0,70,24),fill='white'); dr.text((4,4),f'{ln:02d}{"abc"[b]}',fill='red')
        strips.append(s)
    W=max(s.width for s in strips); out=Image.new('RGB',(W,sum(s.height for s in strips)+10),'white'); y=0
    for s in strips: out.paste(s,(0,y)); y+=s.height+5
    out.save(f'cp12/P{p}_{ln:02d}.png')
print([len(x) for x in P])
