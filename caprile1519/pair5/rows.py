import sys
from PIL import Image, ImageOps; Image.MAX_IMAGE_PIXELS=None
p=sys.argv[1]; x0,x1=int(sys.argv[2]),int(sys.argv[3]); ys=[int(v) for v in sys.argv[4].split(',')]; out=sys.argv[5]; s=2.6
im=Image.open('img/IMG_R1131_I57%s.png'%p).convert('L')
strips=[]
for y in ys:
  c=ImageOps.autocontrast(im.crop((x0,y-55,x1,y+22)),cutoff=1)
  strips.append(c.resize((int((x1-x0)*s),int(77*s)),Image.LANCZOS))
W=Image.new('L',(strips[0].width,sum(t.height+12 for t in strips)),0)
yy=0
for t in strips: W.paste(t,(0,yy)); yy+=t.height+12
W.save('pair5/crops/'+out)
