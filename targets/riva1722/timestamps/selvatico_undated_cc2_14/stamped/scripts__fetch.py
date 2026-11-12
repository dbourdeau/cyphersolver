import json,sys,subprocess,io,re
from PIL import Image
man,out=sys.argv[1],sys.argv[2]
m=json.load(open(man))
T=1024
for c in m['sequences'][0]['canvases']:
    lab=c['label'].split(' - ')[-1]; W,H=c['width'],c['height']
    base=c['images'][0]['resource']['service']['@id']
    full=Image.new('RGB',(W,H),'white')
    for y in range(0,H,T):
        for x in range(0,W,T):
            w=min(T,W-x);h=min(T,H-y)
            u=f"{base}/{x},{y},{w},{h}/{w},{h}/0/default.jpg"
            for a in range(3):
                b=subprocess.run(['curl','-s','-m','60',u],capture_output=True).stdout
                try: full.paste(Image.open(io.BytesIO(b)),(x,y)); break
                except Exception as e:
                    if a==2: print('fail',u,b[:100])
    full.save(f"{out}/{lab}.jpg",quality=92); print(lab,full.size,base)
