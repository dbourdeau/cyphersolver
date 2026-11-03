# usage: python e1570/fetch_tiles.py NAME IIIF_BASE x0 y0 x1 y1 : native-size region, tile by tile, 1 s apart; stitched to scans/e1570/NAME_full.jpg. Scans stay out of git.
import sys,time,io,urllib.request,urllib.error
from PIL import Image
n,s=sys.argv[1],sys.argv[2]; x0,y0,x1,y1=(int(a) for a in sys.argv[3:7])
tw,th=1400,680
canvas=Image.new('RGB',(x1-x0,y1-y0),'white')
y=y0
while y<y1:
    x=x0
    while x<x1:
        w=min(tw,x1-x); h=min(th,y1-y)
        u=f"{s}/{x},{y},{w},{h}/max/0/default.jpg"
        b=None
        for attempt in (1,2):
            try:
                b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'WAINUT-research'}),timeout=90).read(); break
            except urllib.error.HTTPError as e:
                print('HTTP',e.code,u)
                if e.code==429: sys.exit('429 stop')
                time.sleep(2)
        if b:
            t=Image.open(io.BytesIO(b)).convert('RGB')
            if t.size!=(w,h): print('size',t.size,(w,h)); t=t.resize((w,h))
            canvas.paste(t,(x-x0,y-y0))
        x+=tw; time.sleep(1)
    y+=th
canvas.save(f'scans/e1570/{n}_full.jpg',quality=93); print(n,canvas.size)
