import sys,subprocess,io,time
from PIL import Image
base,W,H,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
T=1024;full=Image.new('RGB',(W,H),'white');fails=0
for y in range(0,H,T):
  for x in range(0,W,T):
    w=min(T,W-x);h=min(T,H-y)
    u=f"{base}/{x},{y},{w},{h}/{w},{h}/0/default.jpg"
    ok=False
    for a in range(3):
      b=subprocess.run(['curl','-sS','-m','60',u],capture_output=True).stdout
      try: full.paste(Image.open(io.BytesIO(b)),(x,y));ok=True;break
      except Exception as e: print('fail',a,u,b[:80]);time.sleep(3)
    if not ok: fails+=1
    time.sleep(0.5)
full.save(out,quality=93);print(out,full.size,'failed tiles',fails)
