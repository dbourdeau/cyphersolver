import sys,subprocess,io,os
from PIL import Image
base,W,H,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
T=1024;full=Image.new('RGB',(W,H),'white')
for y in range(0,H,T):
  for x in range(0,W,T):
    w=min(T,W-x);h=min(T,H-y)
    u=f"{base}/{x},{y},{w},{h}/{w},{h}/0/default.jpg"
    b=subprocess.run(['curl','-s','-m','60',u],capture_output=True).stdout
    try: full.paste(Image.open(io.BytesIO(b)),(x,y))
    except Exception as e: print('fail',u,b[:120])
full.save(out,quality=92);print(out,full.size)
