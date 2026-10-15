# zc: enlarge part of a band of a line crop. python cp12/zc.py crop.png band(a-d) x0 x1 out [scale]
import sys
from PIL import Image
f,b,x0,x1,out=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
sc=float(sys.argv[6]) if len(sys.argv)>6 else 2
im=Image.open(f); h=(im.height+5)//4  # 4 bands + gaps
i='abcd'.index(b); y0=i*(h); c=im.crop((x0,y0,x1,y0+h-5))
c.resize((int(c.width*sc),int(c.height*sc)),Image.LANCZOS).save(out)
