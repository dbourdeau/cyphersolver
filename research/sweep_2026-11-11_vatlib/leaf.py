"""python leaf.py <scratch> <Shelfmark> <width> <canvas index>... [--top] : single leaves by canvas index, 3 s apart (--top = upper 40% at full width)"""
import sys,json,os,urllib.request,time
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
a=sys.argv[1:]; top='--top' in a
if top: a.remove('--top')
S,sm,w=a[0],a[1],a[2]
cv=json.load(open(f'{S}/m_{sm}.json',encoding='utf8'))['sequences'][0]['canvases']
os.makedirs(f'{S}/leaf',exist_ok=True)
for i in map(int,a[3:]):
    c=cv[i]; svc=c['images'][0]['resource']['service']['@id']
    reg=f'0,0,{c["width"]},{int(c["height"]*0.4)}' if top else 'full'
    fn=f'{S}/leaf/{sm}_{i:04d}_{c["label"]}_{w}{"t" if top else ""}.jpg'
    if not os.path.exists(fn):
        req=urllib.request.Request(f'{svc}/{reg}/{w},/0/default.jpg',headers={'User-Agent':UA,'Referer':'https://digi.vatlib.it/'})
        open(fn,'wb').write(urllib.request.urlopen(req,timeout=120).read()); time.sleep(3)
    print(fn,flush=True)
