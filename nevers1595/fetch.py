"""Fetch canvases/regions of BnF fr. 3993 (ark btv1b9059229n)."""
import sys, os, urllib.request, time
ARK='btv1b9059229n'
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}
REG=os.environ.get('REG','full'); W=int(os.environ.get('W','1200'))
tag=REG.replace(':','').replace(',','_')
os.makedirs('img',exist_ok=True)
for a in sys.argv[1:]:
    i=int(a); fn=f'img/c{i:04d}_{tag}_w{W}.jpg'
    if os.path.exists(fn) and os.path.getsize(fn)>5000: print(i,'have'); continue
    url=f'https://gallica.bnf.fr/iiif/ark:/12148/{ARK}/f{i}/{REG}/{W},/0/native.jpg'
    for t in range(5):
        try:
            d=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=240).read()
            open(fn,'wb').write(d); print(i,len(d)); break
        except Exception as e:
            print(i,'fail',str(e)[:60]); time.sleep(5*(t+1))
    time.sleep(0.25)
print('DONE')
