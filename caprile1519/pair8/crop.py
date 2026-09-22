import sys
from PIL import Image, ImageOps; Image.MAX_IMAGE_PIXELS=None
p,x0,y0,x1,y1,out=sys.argv[1:7]; s=float(sys.argv[7]) if len(sys.argv)>7 else 1.5
im=Image.open('img/'+p).convert('L').crop(tuple(map(int,(x0,y0,x1,y1))))
im=ImageOps.autocontrast(im,cutoff=1); im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS); im.save('pair8/crops/'+out)
