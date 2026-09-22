import sys
from PIL import Image, ImageDraw
i,side=sys.argv[1],sys.argv[2]
im=Image.open(f'img/{i}.jpg').resize((800,491))
c=im.crop((0,0,420,491) if side=='L' else (380,0,800,491)).resize((840,982))
d=ImageDraw.Draw(c)
for y in range(0,491,20):
    d.line((0,y*2,15,y*2),fill='red'); d.text((17,y*2-5),str(y),fill='red')
c.save(f'sheets/h_{i}{side}.jpg')
