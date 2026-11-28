# pcrop.py img out x0 y0 x1 y1 [scale]  pixel box
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
im=Image.open(sys.argv[1]); x0,y0,x1,y1=map(int,sys.argv[3:7]); sc=float(sys.argv[7]) if len(sys.argv)>7 else 0.6
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.size[0]*sc),int(c.size[1]*sc)),Image.LANCZOS); c.save(sys.argv[2],quality=88)
