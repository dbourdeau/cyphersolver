import sys
from PIL import Image, ImageOps
p,y0,y1,x0,x1=map(int,sys.argv[1:6]); tag=sys.argv[6] if len(sys.argv)>6 else ''
im=Image.open(f'r9414/crops/P{p}_full.jpg').convert('L').crop((x0,y0,x1,y1))
im=ImageOps.autocontrast(im,cutoff=1); w=1900; im=im.resize((w,int(im.height*w/im.width)))
fn=f'r9414/crops/P{p}_{y0}_{x0}{tag}.png'; im.save(fn); print(fn)
