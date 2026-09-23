import sys,json
from PIL import Image
# zz.py line x0 x1 [scale]  : page-2 crop of one line between x0,x1 using thirds interpolation
ln=int(sys.argv[1]); x0=int(sys.argv[2]); x1=int(sys.argv[3]); sc=float(sys.argv[4]) if len(sys.argv)>4 else 2
im=Image.open('p16171_P2.png').convert('L'); T=json.load(open('p2_thirds.json'))
pts=[(900,T['900'][ln-1]),(1650,T['1650'][ln-1]),(2450,T['2450'][ln-1])]
def y(x):
    if x<=pts[0][0]: (a,ya),(b,yb)=pts[0],pts[1]
    elif x<=pts[1][0]: (a,ya),(b,yb)=pts[0],pts[1]
    else: (a,ya),(b,yb)=pts[1],pts[2]
    return ya+(yb-ya)*(x-a)/(b-a)
yc=int((y(x0)+y(x1))/2)
c=im.crop((x0,yc-70,x1,yc+70)); c=c.resize((int(c.size[0]*sc),int(c.size[1]*sc))); c.save('zz.png')
