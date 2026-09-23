import sys
from PIL import Image
p,y0,y1,name=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
im=Image.open(f'img/p{p}.jpg'); t=Image.open(f'img/s{p}.jpg'); s=im.size[0]/t.size[0]
x0=float(sys.argv[5]) if len(sys.argv)>5 else 160; x1=float(sys.argv[6]) if len(sys.argv)>6 else 1150
segs=[(x0,x0+(x1-x0)*0.4),(x0+(x1-x0)*0.3,x0+(x1-x0)*0.7),(x0+(x1-x0)*0.6,x1)]
for i,(a,b) in enumerate(segs):
  im.crop((int(a*s),int(y0*s),int(b*s),int(y1*s))).save(f'img/{name}_{i}.jpg',quality=88)
