import sys
from PIL import Image, ImageOps; Image.MAX_IMAGE_PIXELS=None
f,y0,y1,x0,x1,out=sys.argv[1],*map(int,sys.argv[2:6]),sys.argv[6]
im=Image.open(f).convert('L').crop((x0,y0,x1,y1)); im=ImageOps.autocontrast(im,cutoff=1)
im.resize((im.width*2,im.height*2),Image.LANCZOS).save(out)
