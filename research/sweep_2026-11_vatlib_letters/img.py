"""python img.py <Shelfmark> <folio-label> [<folio-label>...] [--w 1600] : save IIIF images by canvas label"""
import sys,json,os,urllib.request,time
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0'
args=sys.argv[1:]; w='1600'
if '--w' in args: k=args.index('--w'); w=args[k+1]; del args[k:k+2]
sm=args[0]; labels=args[1:]
mp=f'm_{sm}.json'
if not os.path.exists(mp):
    req=urllib.request.Request(f'https://digi.vatlib.it/iiif/MSS_{sm}/manifest.json',headers={'User-Agent':UA})
    open(mp,'wb').write(urllib.request.urlopen(req,timeout=90).read()); time.sleep(1)
m=json.load(open(mp,encoding='utf8'))
cv=m['sequences'][0]['canvases']
lab={c['label']:c for c in cv}
if labels==['list']:
    print(len(cv),' '.join(c['label'] for c in cv)); sys.exit()
os.makedirs('img',exist_ok=True)
for L in labels:
    c=lab.get(L)
    if not c: print('no canvas',L); continue
    svc=c['images'][0]['resource']['service']['@id']
    u=f'{svc}/full/{w},/0/default.jpg'
    fn=f'img/{sm}_{L}_{w}.jpg'
    req=urllib.request.Request(u,headers={'User-Agent':UA})
    open(fn,'wb').write(urllib.request.urlopen(req,timeout=120).read()); time.sleep(1)
    print(fn)
