import sys
from PIL import Image, ImageOps
rec,p,y0,y1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
x0=int(sys.argv[5]) if len(sys.argv)>5 else 500; x1=int(sys.argv[6]) if len(sys.argv)>6 else 3400
im=Image.open(f'{rec}/crops/P{p}_full.jpg').crop((x0,y0,x1,y1))
im=ImageOps.autocontrast(im.convert('L'),cutoff=1)
w=1900; im=im.resize((w,int(im.height*w/im.width)))
im.save(f'{rec}/crops/P{p}_{y0}_{x0}.png'); print(f'{rec}/crops/P{p}_{y0}_{x0}.png')
