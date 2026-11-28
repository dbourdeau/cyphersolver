# planche-contact : chaque cadre, marge 30 px, cadre rouge, x3 ; lots de 12 vignettes. PIL (déclaré).
import sys, os
from PIL import Image, ImageDraw, ImageOps
HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'boxes.py')).read())
IMGD='/Volumes/SPOF_2/Archives-Veille-cyber/planches-pistes-2511/champagne1590/images/'
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
keys=sys.argv[2].split(',') if len(sys.argv)>2 else list(C)
I={}; tiles=[]
for k in keys:
    s,x0,y0,x1,y1=C[k]
    if s not in I: I[s]=Image.open(IMGD+s+'.png').convert('L')
    P=30; c=ImageOps.autocontrast(I[s].crop((x0-P,y0-P,x1+P,y1+P)),cutoff=1).convert('RGB')
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS); d=ImageDraw.Draw(c)
    d.rectangle([(P-2)*3,(P-2)*3,(x1-x0+P+2)*3,(y1-y0+P+2)*3],outline=(220,0,0),width=2)
    t=Image.new('RGB',(c.width,c.height+22),'white'); t.paste(c,(0,22)); ImageDraw.Draw(t).text((4,4),k,fill=(0,0,0)); tiles.append(t)
for n in range(0,len(tiles),8):
    g=tiles[n:n+8]; W=sum(t.width+6 for t in g); H=max(t.height for t in g)
    S=Image.new('RGB',(W,H),(150,150,150)); x=0
    for t in g: S.paste(t,(x,0)); x+=t.width+6
    if S.width>1800: S=S.resize((1800,int(S.height*1800/S.width)))
    S.save(os.path.join(OUT,'contact_%02d.jpg'%(n//8)),quality=85)
print(len(tiles))
