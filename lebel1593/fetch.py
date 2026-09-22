"""Fetch canvases/regions of fr.3983 (btv1b9059406b) or fr.3984 (btv1b9060633d)."""
import sys, os, time, urllib.request
ARKS={'3983':'btv1b9059406b','3984':'btv1b9060633d','3985':'btv1b90606498','esp336':'btv1b100325613'}
vol=os.environ.get('VOL','3983'); ARK=ARKS[vol]
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36','Accept':'*/*'}
REG=os.environ.get('REG','full'); W=int(os.environ.get('W','1400'))
tag=REG.replace(':','').replace(',','_')
os.makedirs(f'img{vol}',exist_ok=True)
for a in sys.argv[1:]:
    i=int(a); fn=f'img{vol}/c{i:04d}_{tag}_w{W}.jpg'
    if os.path.exists(fn) and os.path.getsize(fn)>5000: print(i,'have',flush=True); continue
    url=f'https://gallica.bnf.fr/iiif/ark:/12148/{ARK}/f{i}/{REG}/{W},/0/native.jpg'
    for t in range(6):
        try:
            d=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=240).read()
            open(fn,'wb').write(d); print(i,len(d),flush=True); break
        except Exception as e:
            print(i,'fail',str(e)[:60],flush=True); time.sleep(6*(t+1))
    time.sleep(0.3)
print('DONE',flush=True)
