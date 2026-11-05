"""Three-row crop around entries of table 274: python tools/cell3.py out.png n n n ..."""
import sys
sys.path.insert(0,'tools')
from cell import GEOM
from PIL import Image
def crop3(n, scale=9, sheet='274'):
    g = GEOM[sheet]; im = Image.open(g['f'])
    b=(n-1)//100; c=(n-1)%10; r=((n-1)%100)//10
    x0,x1=g['x'][c],g['x'][c+1]; y0,y1=g['y'][b],g['y'][b+1]; h=(y1-y0)/10.0
    ya=int(y0+(r-0.9)*h); yb=int(y0+(r+1.9)*h)
    return im.crop((x0,max(ya,0),x1,yb)).resize((int((x1-x0)*scale),int((yb-max(ya,0))*scale)),Image.LANCZOS)
if __name__=='__main__':
    ss=[crop3(int(a)) for a in sys.argv[2:]]
    W=max(s.width for s in ss);H=sum(s.height for s in ss)+8*len(ss)
    m=Image.new('L',(W,H),90);y=0
    for s in ss: m.paste(s,(0,y)); y+=s.height+8
    m.save(sys.argv[1]);print(m.size)
