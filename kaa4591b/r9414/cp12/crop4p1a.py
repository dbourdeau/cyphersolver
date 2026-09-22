# P1 per-line crops l.6-18 (makes cp12/p1a/) (upright), 4 bands at 2x, drift-following as crop4p3.py
import sys, numpy as np
from PIL import Image, ImageOps, ImageDraw
im=Image.open('../img/IMG_R9414_I44519_P1.jpg').convert('L')
a=np.asarray(im).astype(float); Q=[500,1230,1960,2690,3420]; Y0,Y1=820,2400
def peaks(x0,x1):
    band=a[Y0:Y1,x0:x1]; thr=np.percentile(band,6)+15
    s=np.convolve((band<thr).sum(1).astype(float),np.ones(31)/31,'same')
    c=[i for i in range(45,len(s)-45) if s[i]==s[i-45:i+46].max() and s[i]>0.15*s.max()]
    d=[]
    for i in c:
        if not d or i-d[-1]>40: d.append(i)
    return [Y0+i for i in d]
P=[peaks(Q[b],Q[b+1]) for b in range(4)]
print(P)
y19=int(sys.argv[1]) if len(sys.argv)>1 else 958
A=[p for p in P[0] if p>=y19-50]
OFF=[0,-13,-43,-77]  # upward slope: line rises ~1 line across the page
C=[[ (lambda e:(min(P[b],key=lambda p:abs(p-e)) if min(abs(p-e) for p in P[b])<30 else e))(A[0]+OFF[b]) for b in range(4)]]
for k in range(1,13):
    row=[]
    pitch=(A[k]-A[k-1]) if k<len(A) and 70<A[k]-A[k-1]<130 else 97
    for b in range(4):
        e=C[-1][b]+pitch; near=min(P[b],key=lambda p:abs(p-e))
        row.append(near if abs(near-e)<35 else e)
    C.append(row)
for k in range(13):
    strips=[]
    for b in range(4):
        c=C[k][b]
        s=ImageOps.autocontrast(im.crop((Q[b]-(40 if b else 0),c-80,Q[b+1]+40,c+70)),cutoff=1).convert('RGB')
        s=s.resize((s.width*2,s.height*2))
        dr=ImageDraw.Draw(s); dr.rectangle((0,0,50,20),fill='white'); dr.text((4,4),f'{k+6:02d}{"abcd"[b]}',fill='red')
        strips.append(s)
    W=max(s.width for s in strips); out=Image.new('RGB',(W,sum(s.height for s in strips)+10),'white'); y=0
    for s in strips: out.paste(s,(0,y)); y+=s.height+5
    out.save(f'cp12/p1a/P1_{k+6:02d}.png')
for k in range(13): print(k+6,C[k])
