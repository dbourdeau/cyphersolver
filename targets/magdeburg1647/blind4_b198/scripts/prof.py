import sys
from PIL import Image
n,x0,x1,y0,y1=sys.argv[1],*map(int,sys.argv[2:6])
im=Image.open('/home/claude/en/trackB/b198_magdeburg_blind/img/%s.jpg'%n).convert('L').crop((x0,y0,x1,y1))
w,h=im.size; px=im.load()
for y in range(0,h,3):
    d=sum(1 for x in range(0,w,2) if px[x,y]<100)
    print(y0+y, '#'*(d//6))
