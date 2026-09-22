import sys, numpy as np
from PIL import Image, ImageFilter; Image.MAX_IMAGE_PIXELS=None
p,x0,y0,x1,y1,s,out=sys.argv[1:]
x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); s=float(s)
im=Image.open('img/IMG_R1131_I57%s.png'%p).convert('RGB').crop((x0-40,y0-40,x1+40,y1+40))
a=np.asarray(im).astype(float)
g=a[:,:,2]*0.7+a[:,:,1]*0.3   # blue channel: ink dark, stain light
G=Image.fromarray(g.astype('uint8'))
bg=np.asarray(G.filter(ImageFilter.GaussianBlur(12))).astype(float)
d=np.clip(bg-g,0,None)
d=d/np.percentile(d,99.5); d=np.clip(1-d,0,1)*255
o=Image.fromarray(d.astype('uint8')).crop((40,40,40+x1-x0,40+y1-y0))
o.resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS).save('pair5/crops/'+out)
