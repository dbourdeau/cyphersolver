# linestrips.py img first_y last_y nlines(first..last inclusive index 1..n) x0 x1 out_prefix L,L,L... [halfh]
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
img,fy,ly,n,x0,x1,out,ls=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),sys.argv[7],sys.argv[8]
hh=int(sys.argv[9]) if len(sys.argv)>9 else 140
im=Image.open(img); sp=(ly-fy)/(n-1)
for L in ls.split(','):
    k=int(L); y=int(fy+(k-1)*sp); mid=(x0+x1)//2
    parts=[im.crop((x0,y-hh,mid+150,y+hh)),im.crop((mid-150,y-hh,x1,y+hh))]
    parts=[p.resize((1200,int(p.size[1]*1200/p.size[0])),Image.LANCZOS) for p in parts]
    s=Image.new('RGB',(1200,sum(p.size[1] for p in parts)+6),'white'); s.paste(parts[0],(0,0)); s.paste(parts[1],(0,parts[0].size[1]+6))
    s.save('%s_L%02d.jpg'%(out,k),quality=85)
