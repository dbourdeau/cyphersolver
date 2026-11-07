"""python samp.py SM n_samples [w] : save evenly spaced canvases at width w, then montage"""
import sys,json,os,urllib.request,time
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0'
sm=sys.argv[1]; n=int(sys.argv[2]); w=sys.argv[3] if len(sys.argv)>3 else '700'
mp=f'm_{sm}.json'
if not os.path.exists(mp):
    req=urllib.request.Request(f'https://digi.vatlib.it/iiif/MSS_{sm}/manifest.json',headers={'User-Agent':UA})
    open(mp,'wb').write(urllib.request.urlopen(req,timeout=90).read()); time.sleep(3)
cv=json.load(open(mp,encoding='utf8'))['sequences'][0]['canvases']
N=len(cv)
idx=[int(N*(k+0.5)/n) for k in range(n)] if len(sys.argv)<=4 else [int(x) for x in sys.argv[4].split(',')]
os.makedirs('img',exist_ok=True); out=[]
for i in idx:
    c=cv[i]; svc=c['images'][0]['resource']['service']['@id']
    fn=f'img/{sm}_{i}_{w}.jpg'
    if not os.path.exists(fn):
        for t in range(3):
            try:
                open(fn,'wb').write(urllib.request.urlopen(urllib.request.Request(f'{svc}/full/{w},/0/default.jpg',headers={'User-Agent':UA}),timeout=120).read()); break
            except Exception as e: print('ERR',e); time.sleep(10)
        time.sleep(2)
    out.append(fn); print(i,c['label'],fn)
try:
    from PIL import Image
    ims=[Image.open(f) for f in out if os.path.exists(f)]
    cols=min(3,len(ims)); rows=(len(ims)+cols-1)//cols
    W=max(i.width for i in ims);H=max(i.height for i in ims)
    sheet=Image.new('RGB',(cols*W,rows*H),'white')
    for k,im in enumerate(ims): sheet.paste(im,((k%cols)*W,(k//cols)*H))
    sheet.save(f'img/sheet_{sm}.jpg',quality=80); print('sheet',sheet.size)
except Exception as e: print('nosheet',e)
