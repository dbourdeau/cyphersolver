"""python sheet.py <scratch> <Shelfmark> [--step N] [--w 280] [--from i] [--to j] : thumbnails of every Nth canvas, 2 s apart,
then contact sheets (6x5, labelled) in <scratch>/sheets/. Needs the manifest fetched by man.py."""
import sys,json,os,urllib.request,time,urllib.error
from PIL import Image,ImageDraw
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
a=sys.argv[1:]
def opt(n,d):
    if n in a:
        k=a.index(n); v=a[k+1]; del a[k:k+2]; return int(v)
    return d
step=opt('--step',1); w=opt('--w',280); i0=opt('--from',0); i1=opt('--to',10**6)
S,sm=a[0],a[1]
cv=json.load(open(f'{S}/m_{sm}.json',encoding='utf8'))['sequences'][0]['canvases']
os.makedirs(f'{S}/th/{sm}',exist_ok=True); os.makedirs(f'{S}/sheets',exist_ok=True)
sel=[(i,c) for i,c in enumerate(cv) if i0<=i<i1 and (i-i0)%step==0]
got=[]
for i,c in sel:
    fn=f'{S}/th/{sm}/{i:04d}.jpg'
    if not os.path.exists(fn):
        svc=c['images'][0]['resource']['service']['@id']
        req=urllib.request.Request(f'{svc}/full/{w},/0/default.jpg',headers={'User-Agent':UA,'Referer':'https://digi.vatlib.it/'})
        try: open(fn,'wb').write(urllib.request.urlopen(req,timeout=120).read())
        except urllib.error.HTTPError as e:
            print('HTTP',e.code,i,flush=True)
            if e.code in(429,403): break
            continue
        except Exception as e:
            print('ERR',i,e,flush=True); time.sleep(5); continue
        time.sleep(2)
    got.append((i,c['label'],fn))
per=30; cols=6
for k in range(0,len(got),per):
    ch=got[k:k+per]; _a=Image.open(ch[0][2]); H=int(w*(0.85 if _a.width>_a.height else 1.45))+16
    sh=Image.new('RGB',(cols*w,((len(ch)+cols-1)//cols)*H),'white'); d=ImageDraw.Draw(sh)
    for n,(i,lab,fn) in enumerate(ch):
        try: im=Image.open(fn).convert('RGB')
        except Exception: continue
        im.thumbnail((w,H-16)); x=(n%cols)*w; y=(n//cols)*H
        sh.paste(im,(x,y+16)); d.text((x+3,y+2),f'{i} {lab}',fill='red')
    out=f'{S}/sheets/{sm}_{ch[0][0]:04d}.jpg'; sh.save(out,quality=80); print(out,flush=True)
