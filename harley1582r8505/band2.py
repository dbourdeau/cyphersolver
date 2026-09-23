import sys
from PIL import Image
p,y0,y1,name=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
im=Image.open(f'img/p{p}.jpg'); t=Image.open(f'img/s{p}.jpg'); s=im.size[0]/t.size[0]
for i,(a,b) in enumerate([(265,810),(790,1325)]):
  im.crop((int(a*s),int(y0*s),int(b*s),int(y1*s))).save(f'img/{name}_{i}.jpg',quality=88)
