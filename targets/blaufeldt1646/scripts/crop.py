"""crop.py SRC OUT x0 y0 x1 y1 [scale] [contrast]  -- crop a region from a frame, upscale, optional autocontrast"""
import sys
from PIL import Image, ImageOps
src,out=sys.argv[1],sys.argv[2]
x0,y0,x1,y1=map(int,sys.argv[3:7])
s=float(sys.argv[7]) if len(sys.argv)>7 else 2
im=Image.open(src).convert('L').crop((x0,y0,x1,y1))
im=ImageOps.autocontrast(im,cutoff=1)
im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
im.save(out)
