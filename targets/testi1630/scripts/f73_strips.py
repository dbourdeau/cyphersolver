# f73_strips.py : cut the cipher blocks of cc. 73v-74r into numbered strips for the key-free reader
import numpy as np,json,sys,os
from PIL import Image,ImageDraw,ImageFont
from scipy.ndimage import uniform_filter
F=ImageFont.truetype('arial.ttf',22)
def ink(im):
    a=np.asarray(im.convert('L')).astype(np.float32); return ((uniform_filter(a,151)-a)>30).astype(np.uint8)
WIDE=1500;SCALE=0.72;SRCW=int(WIDE/SCALE);ROWH=int(300*SCALE)+34;PER=7
Image.MAX_IMAGE_PIXELS=None
pages={'c73v':['scans/F/c73v_c.jpg','scans/F/c73v_d.jpg'],'c74r':['scans/F/c74r_a.jpg','scans/F/c74r_b.jpg','scans/F/c74r_c.jpg']}
idx={}
for p,fs in pages.items():
    ims=[Image.open(f).convert('RGB') for f in fs]; rows=[];ln=0
    for b,im in enumerate(ims):
        k=ink(im); k[:, :250]=0; k[:, 4950:]=0
        pr=np.convolve(k.sum(1).astype(float),np.ones(101)/101,'same')
        M=[];order=np.argsort(-pr)
        for y in order:
            if pr[y]<pr.max()*0.07: break
            if all(abs(y-m)>170 for m in M): M.append(int(y))
        M=[(m-1,m+1) for m in sorted(M)]
        print(p,b,'lines',[(a,e) for a,e in M])
        for a,e in M:
            ln+=1; cy=(a+e)//2; y0,y1=max(0,cy-150),min(im.height,cy+150)
            col=np.convolve(k[y0:y1].sum(0).astype(float),np.ones(9)/9,'same'); nz=np.where(col>0.5)[0]
            x0=max(0,int(nz[0])-40); xe=min(im.width,int(nz[-1])+40); parts=[]; x=x0
            while x<xe:
                if xe-x<=SRCW: parts.append((x,xe)); break
                A=x+int(SRCW*.82); B=x+SRCW; c=A+int(np.argmin(col[A:B])); parts.append((x,c)); x=c
            for i,(u,v) in enumerate(parts,1): rows.append((b,ln,i,len(parts),u,v,y0,y1))
    s=0;sheets=[]
    while s<len(rows):
        ch=rows[s:s+PER]; S=Image.new('RGB',(WIDE+10,len(ch)*ROWH+6),'white'); d=ImageDraw.Draw(S)
        for r,(b,n,i,t,u,v,y0,y1) in enumerate(ch):
            c=ims[b].crop((u,y0,v,y1)); c=c.resize((int(c.width*SCALE),int(c.height*SCALE)),Image.LANCZOS)
            d.text((6,r*ROWH+4),f'{p} line {n} part {i} of {t}',fill=(0,0,200),font=F); S.paste(c,(4,r*ROWH+30))
        fn=f'scans/blind/{p}_{len(sheets)+1:02d}.jpg'; S.save(fn,quality=90); sheets.append(fn); s+=PER
    idx[p]=dict(rows=rows,sheets=sheets); print(p,len(rows),'rows',sheets)
json.dump(idx,open('scans/blind/index_f73.json','w'))
