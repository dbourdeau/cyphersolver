import sys
from PIL import Image, ImageOps
rec,p,y0,step,n,x0,x1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7])
per=int(sys.argv[8]) if len(sys.argv)>8 else 3
im=Image.open(f'{rec}/crops/P{p}_full.jpg').convert('L')
xm=(x0+x1)//2
for k in range(0,n,per):
    a=y0+k*step-110; b=y0+(k+per)*step+40
    for h,(u,v) in enumerate([(x0,xm+60),(xm-60,x1)]):
        c=ImageOps.autocontrast(im.crop((u,a,v,b)),cutoff=1)
        w=1900; c=c.resize((w,int(c.height*w/c.width)))
        c.save(f'{rec}/crops/P{p}_H{k+1:02d}{"ab"[h]}.png')
