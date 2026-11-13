# sheet.py dFFF.tsv imgdir out_prefix start count cols : contact sheets of ranked pages (400 px wide), label = pos
import sys,os
from PIL import Image,ImageDraw,ImageOps
tsv,imgdir,outp,start,count=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5])
cols=int(sys.argv[6]) if len(sys.argv)>6 else 4
rows=[l.split('\t') for l in open(tsv)]
rows=[(r[0],int(r[1])) for r in rows if len(r)>=3 and int(r[1])>=0]
rows.sort(key=lambda x:-x[1])
sel=rows[start:start+count]
W=400
ims=[]
for f,k in sel:
    im=Image.open(os.path.join(imgdir,f)).convert('L'); im=ImageOps.autocontrast(im,cutoff=1)
    h=int(im.height*W/im.width); im=im.resize((W,h)).convert('RGB')
    d=ImageDraw.Draw(im); d.rectangle([0,0,110,16],fill='white'); d.text((3,2),'%d k=%d'%(int(f[1:8]),k),fill='red'); ims.append(im)
H=max(i.height for i in ims)
n=(len(ims)+cols-1)//cols
S=Image.new('RGB',(W*cols,H*n),'white')
for j,i in enumerate(ims): S.paste(i,((j%cols)*W,(j//cols)*H))
S.save(outp,quality=80); print(outp,S.size)
