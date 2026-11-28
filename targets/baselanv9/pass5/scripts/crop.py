# usage: crop.py canvas x0 y0 x1 y1 out [rot_deg] [maxw]   (coords in the 1/ small-view units: full = small * S)
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
D='/home/claude/keyless/round40c/basel_anv9/keyleaf/img/'
F={'107':'c107_5353326','109':'c109_5353328','111':'c111_5353330','197':'c197_5353416','198':'c198_5353417'}
c=sys.argv[1]; x0,y0,x1,y1=map(float,sys.argv[2:6]); out=sys.argv[6]
rot=float(sys.argv[7]) if len(sys.argv)>7 else 0; maxw=int(sys.argv[8]) if len(sys.argv)>8 else 1500
im=Image.open(D+F[c]+'_full.jpg')
S=im.size[0]/ (1081 if c in('107','109','111') else (1094 if c=='197' else 1100))
b=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
if rot: b=b.rotate(rot,expand=True,fillcolor='white',resample=Image.BICUBIC)
if b.size[0]>maxw: b=b.resize((maxw,int(b.size[1]*maxw/b.size[0])),Image.LANCZOS)
b.save(out,quality=88); print(out,b.size,'S=%.3f'%S)
