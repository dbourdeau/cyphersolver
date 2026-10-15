import sys
from PIL import Image, ImageOps
im=Image.open('../img/IMG_R9414_I44519_P3.jpg').convert('L').rotate(180)
x0,x1,y0,y1=map(int,sys.argv[1:5]); f=float(sys.argv[5]) if len(sys.argv)>5 else 3
s=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=1); s=s.resize((int(s.width*f),int(s.height*f)))
s.save(sys.argv[6] if len(sys.argv)>6 else 'C:/Users/dbour/AppData/Local/Temp/claude/c--Users-dbour-cypher/f343e5cc-af72-48cf-88e3-6bce625167be/scratchpad/z.png')
