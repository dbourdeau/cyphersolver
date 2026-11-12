# usage: python3 -I asfmap.py out.jpg W filza:pos [filza:pos ...]  (plain curl, IIIF)
import sys,subprocess,io,time
from PIL import Image,ImageDraw
out,W=sys.argv[1],int(sys.argv[2]); ims=[]
for t in sys.argv[3:]:
    f,p=t.split(':')
    u='https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001%05d/A%07d.ptif/full/%d,/0/default.jpg'%(int(f),int(p),W)
    r=subprocess.run(['curl','-sS','-m','90',u],capture_output=True)
    try: im=Image.open(io.BytesIO(r.stdout)).convert('RGB')
    except Exception as e: print('FAIL',t,u,r.stdout[:100]); continue
    d=ImageDraw.Draw(im); d.rectangle([0,0,150,22],fill='white'); d.text((4,5),t,fill='red'); ims.append(im); print('ok',t,im.size,u); time.sleep(1)
h=max(i.height for i in ims); S=Image.new('RGB',(W*len(ims),h),'white')
for k,i in enumerate(ims): S.paste(i,(k*W,0))
S.save(out,quality=80)
