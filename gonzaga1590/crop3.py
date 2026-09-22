import sys
from PIL import Image, ImageOps
f,tag=sys.argv[1],sys.argv[2]; ys=[int(v) for v in sys.argv[3].split(',')]; x0=int(sys.argv[4]); x1=int(sys.argv[5])
im=ImageOps.grayscale(Image.open(f))
n=int(sys.argv[6]) if len(sys.argv)>6 else 4; step=(x1-x0)//n
for i,y in enumerate(ys):
    for j in range(n):
        a=max(0,x0+j*step-40); b=min(im.width,x0+(j+1)*step+40)
        c=im.crop((a,y-80,b,y+80)); c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'{tag}{i}{j}.png')
