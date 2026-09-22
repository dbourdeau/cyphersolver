import sys
from PIL import Image, ImageOps
# zl.py page line xfrac0 xfrac1 [y0 step]  -> 3x crop of one line
p,n,f0,f1=int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])
y0=int(sys.argv[5]) if len(sys.argv)>5 else 180; st=float(sys.argv[6]) if len(sys.argv)>6 else 132
im=Image.open(f'C:/Users/dbour/cypher/kaa4591b/r9415/crops/P{p}_full.jpg').convert('L')
y=y0+st*(n-1); W=im.width
c=im.crop((int(f0*W),int(y-95),int(f1*W),int(y+85)))
c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((c.width*3//2,c.height*3//2))
out=f'C:/Users/dbour/AppData/Local/Temp/claude/z/P{p}_{n}_{int(f0*100)}.png'; c.save(out); print(out,c.size)
