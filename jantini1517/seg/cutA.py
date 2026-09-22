# adaptive line cropper: follows the line's ink band piece by piece
import sys, numpy as np
from PIL import Image, ImageOps; Image.MAX_IMAGE_PIXELS=None
img,tag,y0=sys.argv[1],sys.argv[2],int(sys.argv[3])
x0=int(sys.argv[4]); x1=int(sys.argv[5]); slope=float(sys.argv[6]) if len(sys.argv)>6 else -0.065
im=Image.open('img/'+img+'.png').convert('L'); a=np.array(im).astype(float)
y=y0; x=x0; i=0; out=[]
while x<x1:
  # refine: base-line band ink in window
  w=a[int(y-45):int(y+45), x:x+400]; d=(w<110).sum(1)
  if d.sum()>200:
    cy=int(y-45+np.argmax(np.convolve(d,np.ones(25),'same')))
    y=0.5*y+0.5*cy
  c=im.crop((x,int(y)-115,x+460,int(y)+60)); c=ImageOps.autocontrast(c,cutoff=1)
  c.resize((c.width*3,c.height*3),Image.LANCZOS).save(f'seg/{tag}_{i}.png'); out.append(int(y))
  x+=400; i+=1; y+=slope*400
print(out)
