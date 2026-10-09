"""zoomx.py PAGE LINE F0 F1 [Z]: like zoom.py, with autocontrast + unsharp mask + light threshold -> img/zoomx.png"""
import json,sys
from PIL import Image,ImageOps,ImageFilter
d=json.load(open('raince_tokens.json')); page,ln=sys.argv[1],int(sys.argv[2]); f0,f1=float(sys.argv[3]),float(sys.argv[4])
Z=float(sys.argv[5]) if len(sys.argv)>5 else 2.5
r=d['regions'][page]; toks=[t for t in d['tokens'] if t['page']==page]
x0=r['x0']+min(t['x0'] for t in toks)-25; x1=r['x0']+max(t['x1'] for t in toks)+25; W=x1-x0
y=int(r['y0']+r['lines'][ln-1]); p=r['pitch']
im=Image.open(r['img']).convert('L').crop((int(x0+f0*W),int(y-p*0.75),int(x0+f1*W),int(y+p*0.5)))
im=ImageOps.autocontrast(im,cutoff=2).filter(ImageFilter.UnsharpMask(3,200,2))
im=im.point(lambda v:0 if v<150 else (255 if v>215 else v))
im=im.resize((int(im.width*Z),int(im.height*Z)),Image.LANCZOS)
# token ticks
from PIL import ImageDraw
dr=ImageDraw.Draw(im)
row=sorted([t for t in toks if t['line']==ln-1],key=lambda t:t['x0'])
for i,t in enumerate(row,1):
    cx=(r['x0']+(t['x0']+t['x1'])/2-(x0+f0*W))*Z
    if 0<cx<im.width: dr.text((cx-6,im.height-14),str(i),fill=0)
im.save('img/zoomx.png'); print(im.size)
