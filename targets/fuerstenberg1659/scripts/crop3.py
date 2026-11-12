import sys
from PIL import Image
base=sys.argv[1]; img=sys.argv[2]; name=sys.argv[3]; box=[int(v) for v in sys.argv[4].split(',')]; z=int(sys.argv[5]) if len(sys.argv)>5 else 2
s=2550/2184
im=Image.open(base+'/scans/'+img)
b=[int(v*s) for v in box]
r=im.crop(b); r=r.resize((r.width*z,r.height*z)); r.save(base+'/work/crops/'+name)
