import sys
from PIL import Image
n,x0,y0,x1,y1,scale,out=sys.argv[1],*map(int,sys.argv[2:6]),float(sys.argv[6]),sys.argv[7]
im=Image.open('/home/claude/en/trackB/b198_magdeburg_blind/img/%s.jpg'%n).crop((x0,y0,x1,y1))
im=im.resize((int(im.width*scale),int(im.height*scale)),Image.LANCZOS)
im.save('/home/claude/en/trackB/b198_magdeburg_blind/crops/'+out)
print(im.size)
