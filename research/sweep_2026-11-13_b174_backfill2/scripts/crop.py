# crop.py img y0 y1 out [x0 x1] : fractional crop of a scratch image, kept native size (for viewing only)
import sys
from PIL import Image
im=Image.open(sys.argv[1]); w,h=im.size; y0,y1=float(sys.argv[2]),float(sys.argv[3])
x0,x1=(float(sys.argv[5]),float(sys.argv[6])) if len(sys.argv)>6 else (0,1)
im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h))).save(sys.argv[4],quality=85); print(im.size)
