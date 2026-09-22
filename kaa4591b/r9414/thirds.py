"""Line-third crops for re-transcription v2. Per band, a comb fit (y0,pitch) then +-15 px snap.
args: page x0 x1 yguess first last [rot]   (yguess = rough centre of line `first` at left)"""
import sys, numpy as np
from PIL import Image, ImageOps, ImageDraw
p=int(sys.argv[1]); x0,x1=int(sys.argv[2]),int(sys.argv[3]); yg=float(sys.argv[4]); first,last=int(sys.argv[5]),int(sys.argv[6])
im=Image.open(f'../img/IMG_R9414_I44519_P{p}.jpg').convert('L')
if len(sys.argv)>7: im=im.rotate(180)
a=np.asarray(im).astype(float); n=last-first+1
w=(x1-x0)//3; bands=[(x0+i*w-(50 if i else 0), x0+(i+1)*w+50) for i in range(3)]
strips=[]; fits=[]
for b,(u,v) in enumerate(bands):
    band=a[:,u:v]; thr=np.percentile(band[int(yg):int(yg+n*110)],6)+12
    prof=np.convolve((band<thr).sum(1).astype(float),np.ones(15)/15,'same')
    best=None
    for pitch in np.arange(95,115,0.5):
        for y0 in range(int(yg-90),int(yg+90)):
            ys=(y0+np.arange(n)*pitch).astype(int)
            if ys[-1]>=len(prof): continue
            s=prof[ys].sum()
            if best is None or s>best[0]: best=(s,y0,pitch)
    fits.append(best[1:])
if len(sys.argv)>8 or True:
    import os
    if os.environ.get('FITS'): fits=[tuple(map(float,f.split(':'))) for f in os.environ['FITS'].split(',')]
print(fits)
for i in range(n):
    for b,(u,v) in enumerate(bands):
        y0,pitch=fits[b]; g=int(y0+i*pitch)
        c=g
        s=ImageOps.autocontrast(im.crop((u,c-70,v,c+50)),cutoff=1)
        s=s.resize((1900,int(s.height*1900/s.width)))
        d=ImageDraw.Draw(s); d.rectangle((0,0,55,22),fill=255); d.text((3,3),f'{first+i:02d}{"abc"[b]}',fill=0)
        strips.append(s)
for j in range(0,len(strips),6):
    g=strips[j:j+6]; H=sum(s.height for s in g)
    out=Image.new('L',(1900,H),255); y=0
    for s in g: out.paste(s,(0,y)); y+=s.height
    out.save(f'crops2/P{p}_{first+j//3:02d}.png')
