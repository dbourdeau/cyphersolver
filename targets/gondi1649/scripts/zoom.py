"""Zoom sheet: crop windows around sign positions (estimated from sign index along the inked extent of the line band).
usage: zoom.py IMG OUT LINE:INDEX:N ...   (N = signs in the pass-1 line)"""
import sys, numpy as np
from PIL import Image, ImageDraw, ImageOps
C=[100,335,600,875,1120,1395,1690,1960,2190,2460,2790,3045,3300,3575]
im=Image.open(sys.argv[1]).convert('L'); a=np.asarray(im)
rows=[]
for spec in sys.argv[3:]:
    L,i,n=map(int,spec.split(':')); c=C[L]
    band=a[c-60:c+60]; cols=np.where((band<110).sum(0)>3)[0]
    x0,x1=cols.min(),cols.max(); x=int(x0+(i+0.5)/n*(x1-x0))
    r=im.crop((max(0,x-520),c-95,x+520,c+95)); r=ImageOps.autocontrast(r,cutoff=1).resize((780,143)).convert('RGB')
    d=ImageDraw.Draw(r); d.rectangle([0,0,110,22],fill='yellow'); d.text((4,4),f"L{L:02d}@{i}",fill='black')
    rows.append(r)
o=Image.new('RGB',(780*2+10,((len(rows)+1)//2)*148),'blue')
for k,r in enumerate(rows): o.paste(r,((k%2)*790,(k//2)*148))
o.save(sys.argv[2]); print(o.size)
