import sys
from PIL import Image, ImageOps
f,tag,y0,pitch,n,xl,xr=sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7])
im=Image.open(f).convert('L'); s=im.size[1]/1467
xm=(xl+xr)/2
for i in range(0,n,2):
  top=y0+i*pitch-0.6*pitch; bot=y0+(i+1)*pitch+0.55*pitch
  for j,(a,b) in enumerate([(xl,xm+25),(xm-25,xr)]):
    c=im.crop((int(a*s),int(top*s),int(b*s),int(bot*s)))
    c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((1600,int(1600*c.size[1]/c.size[0])))
    c.save(f'r9411/c/{tag}_L{i+1:02d}{"ab"[j]}.png')
