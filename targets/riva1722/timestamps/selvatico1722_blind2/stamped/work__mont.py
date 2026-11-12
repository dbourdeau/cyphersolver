import sys
from PIL import Image
# args: out page x0 y0 x1 y1 [page x0 y0 x1 y1 ...]
out=sys.argv[1]; a=sys.argv[2:]; ims=[]
cache={}
for i in range(0,len(a),5):
    p=a[i]; b=tuple(int(v) for v in a[i+1:i+5])
    if p not in cache: cache[p]=Image.open('/home/claude/en/trackB/b70_selvatico_read/img/%s.jpg'%p)
    ims.append(cache[p].crop(b))
W=max(i.width for i in ims); H=sum(i.height+8 for i in ims)
m=Image.new('RGB',(W,H),'red'); y=0
for i in ims: m.paste(i,(0,y)); y+=i.height+8
sc=min(1.0,1950/W)
m=m.resize((int(W*sc),int(H*sc)),Image.LANCZOS); m.save(out,quality=88); print(out,m.size)
