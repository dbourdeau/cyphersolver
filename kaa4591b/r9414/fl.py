import sys
from PIL import Image, ImageOps
p=int(sys.argv[1]); y0=int(sys.argv[2]); step=float(sys.argv[3]); n=int(sys.argv[4]); x0,x1=int(sys.argv[5]),int(sys.argv[6])
im=Image.open(f'r9414/crops/P{p}_full.jpg').convert('L')
for k in range(0,n,2):
    a=int(y0+k*step-65); b=int(y0+(k+2)*step+5)
    c=ImageOps.autocontrast(im.crop((x0,a,x1,b)),cutoff=1)
    c=c.resize((1900,int(c.height*1900/c.width))); c.save(f'r9414/crops/P{p}_f{k:02d}.png')
