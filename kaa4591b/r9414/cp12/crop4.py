# P4 per-line crops, 4 bands at 2x. Line centres tracked per band: each band's centre for line k = nearest own
# profile peak to (its centre for line k-1 + band-a pitch), so the half-line drift mid-page is followed.
import sys, numpy as np
from PIL import Image, ImageOps, ImageDraw
im=Image.open('../img/IMG_R9414_I44519_P4.jpg').convert('L').rotate(180)
a=np.asarray(im).astype(float); Q=[600,1290,1970,2650,3330]
def peaks(x0,x1):
    band=a[180:4540,x0:x1]; thr=np.percentile(band,6)+15
    s=np.convolve((band<thr).sum(1).astype(float),np.ones(31)/31,'same')
    c=[i for i in range(45,len(s)-45) if s[i]==s[i-45:i+46].max() and s[i]>0.15*s.max()]
    d=[]
    for i in c:
        if not d or i-d[-1]>40: d.append(i)
    return [180+i for i in d]
P=[peaks(Q[b],Q[b+1]) for b in range(4)]
A=P[0][:40]+[P[0][39]+103]
C=[[P[b][0] for b in range(4)]]
for k in range(1,41):
    row=[]
    for b in range(4):
        e=C[-1][b]+(A[k]-A[k-1]); near=min(P[b],key=lambda p:abs(p-e))
        row.append(near if abs(near-e)<35 else e)
    C.append(row)
FIX={}  # manual overrides line:(b,y)
for k in range(41):
    strips=[]
    for b in range(4):
        c=C[k][b]
        s=ImageOps.autocontrast(im.crop((Q[b]-(40 if b else 0),c-80,Q[b+1]+40,c+70)),cutoff=1).convert('RGB')
        s=s.resize((s.width*2,s.height*2))
        dr=ImageDraw.Draw(s); dr.rectangle((0,0,50,20),fill='white'); dr.text((4,4),f'{k+1:02d}{"abcd"[b]}',fill='red')
        strips.append(s)
    W=max(s.width for s in strips); out=Image.new('RGB',(W,sum(s.height for s in strips)+10),'white'); y=0
    for s in strips: out.paste(s,(0,y)); y+=s.height+5
    out.save(f'cp12/P4_{k+1:02d}.png')
for k in range(41): print(k+1,C[k])
