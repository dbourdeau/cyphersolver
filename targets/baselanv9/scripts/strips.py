"""strips.py <canvas> [y0 y1 step]: cut a 2000-px page into horizontal strips work/strips/cNNN_sK.jpg"""
import sys, glob, os
from PIL import Image
D='/home/claude/keyless/round40c/basel_anv9/'
c=int(sys.argv[1]); f=glob.glob(D+'img/p2000/c%03d_*.jpg'%c)[0]
im=Image.open(f); W,H=im.size
y0=int(sys.argv[2]) if len(sys.argv)>2 else 0; y1=int(sys.argv[3]) if len(sys.argv)>3 else H
step=int(sys.argv[4]) if len(sys.argv)>4 else 420
os.makedirs(D+'work/strips',exist_ok=True)
k=0; y=y0
while y<y1:
    im.crop((0,y,W,min(y+step+60,H))).save(D+'work/strips/c%03d_s%d.jpg'%(c,k)); print('c%03d_s%d'%(c,k),y,min(y+step+60,H)); k+=1; y+=step
