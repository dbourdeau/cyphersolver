import sys
from PIL import Image
p,y0,y1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
x0=int(sys.argv[4]) if len(sys.argv)>4 else 0; x1=int(sys.argv[5]) if len(sys.argv)>5 else 3468
w=int(sys.argv[6]) if len(sys.argv)>6 else 2000
im=Image.open(f'_{p}_rot.png').crop((x0,y0,x1,y1))
im=im.resize((w,int(w*(y1-y0)/(x1-x0))))
im.save('_c/c.png')
