# P2 per-line crops (adapted from crop4p3.py): image rotated 180, 4 bands at 2x, line centres tracked per band
# (nearest own profile peak to previous centre + band-a pitch) to follow the drift. Out: cp12/p2h/P2_NN.png
import sys, numpy as np
from PIL import Image, ImageOps, ImageDraw
im=Image.open('../img/IMG_R9414_I44519_P2.jpg').convert('L').rotate(180)
a=np.asarray(im).astype(float); Q=[720,1360,2000,2640,3290]; Y0,Y1=430,4500; N=37
def peaks(x0,x1):
    band=a[Y0:Y1,x0:x1]; thr=np.percentile(band,6)+15
    s=np.convolve((band<thr).sum(1).astype(float),np.ones(31)/31,'same')
    c=[i for i in range(45,len(s)-45) if s[i]==s[i-45:i+46].max() and s[i]>0.15*s.max()]
    d=[]
    for i in c:
        if not d or i-d[-1]>40: d.append(i)
    return [Y0+i for i in d]
P=[peaks(Q[b],Q[b+1]) for b in range(4)]
for b in range(4): print('band',b,len(P[b]),P[b][:3],P[b][-2:])
pitch=(P[0][-1]-P[0][0])/(len(P[0])-1)
A=(P[0]+[P[0][-1]+pitch*j for j in range(1,8)])[:N]
C=[[P[b][0] for b in range(4)]]
for k in range(1,N):
    row=[]
    for b in range(4):
        e=C[-1][b]+(A[k]-A[k-1]); near=min(P[b],key=lambda p:abs(p-e))
        row.append(int(near if abs(near-e)<35 else e))
    C.append(row)
for k in range(N):
    strips=[]
    for b in range(4):
        c=C[k][b]
        s=ImageOps.autocontrast(im.crop((Q[b]-(40 if b else 0),c-80,Q[b+1]+40,c+70)),cutoff=1).convert('RGB')
        s=s.resize((s.width*2,s.height*2))
        dr=ImageDraw.Draw(s); dr.rectangle((0,0,50,20),fill='white'); dr.text((4,4),f'{k+1:02d}{"abcd"[b]}',fill='red')
        strips.append(s)
    W=max(s.width for s in strips); out=Image.new('RGB',(W,sum(s.height for s in strips)+10),'white'); y=0
    for s in strips: out.paste(s,(0,y)); y+=s.height+5
    out.save(f'cp12/p2h/P2_{k+1:02d}.png')
for k in range(N): print(k+1,C[k])
