import subprocess,sys
from PIL import Image
def crop(b,W,name,x0,y0,x1,y1,out=1800):
    s=W/1200
    X0,Y0,X1,Y1=[int(v*s) for v in (x0,y0,x1,y1)]
    w=X1-X0
    subprocess.run(['curl','-sL','-o',f'crops/{name}.tmp',f'{b}/{X0},{Y0},{w},{Y1-Y0}/{min(w,1700)},/0/default.jpg'])
    im=Image.open(f'crops/{name}.tmp'); im=im.resize((out,int(im.size[1]*out/im.size[0])),Image.LANCZOS)
    im.save(f'crops/{name}.jpg'); return im.size
