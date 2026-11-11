"""Contact sheets for an Arcinsys unit: python3 arc_sheet.py <first full-image URL with {n}> <fmt e.g. %04d> <start> OUTDIR [step] [width] [maxn]
Finds the last image by HEAD probing, fetches every step-th full image, builds 12-up sheets."""
import sys,os,time,urllib.request
from PIL import Image
tpl,fmt,start,out=sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4]
step=int(sys.argv[5]) if len(sys.argv)>5 else 1; W=int(sys.argv[6]) if len(sys.argv)>6 else 420
def url(n): return tpl.replace('{n}',fmt%n)
def ok(n):
    req=urllib.request.Request(url(n),method='HEAD',headers={'User-Agent':'Mozilla/5.0 Chrome/126'})
    try: urllib.request.urlopen(req,timeout=30); return True
    except Exception: return False
if len(sys.argv)>7: last=int(sys.argv[7])
else:
    lo,hi=start,start+1
    while ok(hi): lo,hi=hi,hi*2+1; time.sleep(.3)
    while hi-lo>1:
        m=(lo+hi)//2
        if ok(m): lo=m
        else: hi=m
        time.sleep(.3)
    last=lo
print('last',last)
os.makedirs(out,exist_ok=True); ims=[]
for n in range(start,last+1,step):
    fn=os.path.join(out,'%04d.jpg'%n)
    if not os.path.exists(fn):
        try: open(fn,'wb').write(urllib.request.urlopen(urllib.request.Request(url(n),headers={'User-Agent':'Mozilla/5.0 Chrome/126'}),timeout=90).read())
        except Exception as e: print('fail',n,e); continue
        time.sleep(1)
    ims.append(fn)
H=int(W*1.45)
for s in range(0,len(ims),12):
    sheet=Image.new('RGB',(W*4,H*3),'white')
    for k,f in enumerate(ims[s:s+12]):
        try: im=Image.open(f).convert('RGB')
        except Exception: continue
        im.thumbnail((W,H)); sheet.paste(im,((k%4)*W,(k//4)*H))
    sheet.save(os.path.join(out,'sheet_%03d_from%s.jpg'%(s//12,os.path.basename(ims[s])[:4])),quality=70)
print(len(ims),'images')
