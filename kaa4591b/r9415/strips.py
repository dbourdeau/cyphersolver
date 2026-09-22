import sys
from PIL import Image, ImageOps
rec,p,y0,step,n=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
x0=int(sys.argv[6]); x1=int(sys.argv[7]); per=int(sys.argv[8]) if len(sys.argv)>8 else 3
im=Image.open(f'{rec}/crops/P{p}_full.jpg').convert('L')
for k in range(0,n,per):
    a=y0+k*step-110; b=y0+(k+per)*step+40
    c=ImageOps.autocontrast(im.crop((x0,a,x1,b)),cutoff=1)
    w=1900; c=c.resize((w,int(c.height*w/c.width)))
    c.save(f'{rec}/crops/P{p}_L{k+1:02d}.png')
