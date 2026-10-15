import sys
from PIL import Image, ImageOps
p,y0,n=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[4]); step=float(sys.argv[3]); x0,x1=int(sys.argv[5]),int(sys.argv[6])
im=Image.open(f'r9414/crops/P{p}_full.jpg').convert('L')
xm=(x0+x1)//2
for k in range(0,n,3):
    a=int(y0+k*step-70); b=int(y0+(k+3)*step+10)
    for h,(u,v) in enumerate([(x0,xm+50),(xm-50,x1)]):
        c=ImageOps.autocontrast(im.crop((u,a,v,b)),cutoff=1)
        c=c.resize((1900,int(c.height*1900/c.width))); c.save(f'r9414/crops/P{p}_g{k+1:02d}{"ab"[h]}.png')
