import sys
from PIL import Image
n,x0,x1,y0,y1=sys.argv[1],*map(int,sys.argv[2:6])
im=Image.open('/home/claude/en/trackB/b198_magdeburg_blind/img/%s.jpg'%n).convert('L').crop((x0,y0,x1,y1))
w,h=im.size; px=im.load()
d=[sum(1 for x in range(0,w,2) if px[x,y]<100) for y in range(h)]
sm=[sum(d[max(0,y-4):y+5])/9 for y in range(h)]
pk=[y0+y for y in range(13,h-13) if sm[y]==max(sm[y-12:y+13]) and sm[y]>40]
print(pk)
