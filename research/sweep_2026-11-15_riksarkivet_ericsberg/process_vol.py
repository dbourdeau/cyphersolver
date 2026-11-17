"""python process_vol.py <man> <n> <stride> : fetch every stride-th image at 1200 px, digitscan it, keep 300 px tiles for contact sheets,
keep full images only for flagged ones (strict>=20 or relaxed>=25). ~1 request/s. Resumable (scan/<man>.tsv)."""
import os,sys,time,io
import numpy as np, cv2
from PIL import Image
from rik_common import img, grid, SP
import digitscan
man,n,stride=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
os.makedirs(f'{SP}/scan',exist_ok=True);os.makedirs(f'{SP}/flag/{man}',exist_ok=True);os.makedirs(f'{SP}/thumb/{man}',exist_ok=True)
tsv=f'{SP}/scan/{man}.tsv'
done=set()
if os.path.exists(tsv):
    done={int(l.split('\t')[0]) for l in open(tsv)}
import requests
from rik_common import H
rr=requests.get(f'https://lbiiif.riksarkivet.se/arkis!{man}_00001/full/300,/0/default.jpg',headers=H,timeout=60)
if rr.status_code!=200:
    print('BLOCKED',man,rr.status_code);open(f'{SP}/blocked.txt','a').write(man+' '+str(rr.status_code)+chr(10));sys.exit()
fh=open(tsv,'a')
for i in range(1,n+1,stride):
    if i in done:continue
    im=img(man,i,1200)
    a=np.array(im)
    if a.mean()>253 and a.std()<2:
        fh.write(f'{i}\t-1\t-1\t-1\n');fh.flush();continue   # failed fetch
    p=f'{SP}/flag/{man}/{i}.jpg'
    im.save(p,quality=80)
    s=digitscan.features(p)
    strict,lon,rel=s if s else (0,0,0)
    fh.write(f'{i}\t{strict}\t{lon}\t{rel}\n');fh.flush()
    t=im.resize((420,max(1,int(im.size[1]*420/im.size[0]))))
    t.save(f'{SP}/thumb/{man}/{i}.jpg',quality=70)
    if not(strict>=20 or rel>=25):os.remove(p)
    time.sleep(0.7)
print('done',man)
