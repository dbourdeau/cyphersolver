# grid.py out cols scale img1 img2 ...
import sys
from PIL import Image
out=sys.argv[1]; cols=int(sys.argv[2]); sc=float(sys.argv[3]); ims=[Image.open(f) for f in sys.argv[4:]]
ims=[i.resize((int(i.size[0]*sc),int(i.size[1]*sc)),Image.LANCZOS) for i in ims]
W=max(i.size[0] for i in ims)+10; H=max(i.size[1] for i in ims)+10
rows=(len(ims)+cols-1)//cols
s=Image.new('RGB',(W*cols,H*rows),'white')
for k,i in enumerate(ims): s.paste(i,((k%cols)*W,(k//cols)*H))
s.save(out,quality=88); print(out,s.size)
