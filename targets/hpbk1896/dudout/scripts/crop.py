# crop.py ID x0 y0 x1 y1 out [maxdim]  (coords in full-res pixels)
import sys
from PIL import Image
i,x0,y0,x1,y1,out=sys.argv[1:7]; m=int(sys.argv[7]) if len(sys.argv)>7 else 1800
im=Image.open(f'IMGROOT/img/HPBK_{i}.jpg')
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c.thumbnail((m,m))
c.save('IMGROOT/v/'+out,quality=90)
print(c.size)
