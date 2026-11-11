"""python mksheet.py <scratch> <Shelfmark> <from> <to> : contact sheet from thumbnails already fetched by sheet.py"""
import sys,json,os
from PIL import Image,ImageDraw
S,sm,a,b=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
cv=json.load(open(f'{S}/m_{sm}.json',encoding='utf8'))['sequences'][0]['canvases']
fs=[(i,f'{S}/th/{sm}/{i:04d}.jpg') for i in range(a,b) if os.path.exists(f'{S}/th/{sm}/{i:04d}.jpg')]
w=280;H=int(w*1.45)+16;cols=6
sh=Image.new('RGB',(cols*w,((len(fs)+cols-1)//cols)*H),'white'); d=ImageDraw.Draw(sh)
for n,(i,fn) in enumerate(fs):
    im=Image.open(fn).convert('RGB'); im.thumbnail((w,H-16)); x=(n%cols)*w; y=(n//cols)*H
    sh.paste(im,(x,y+16)); d.text((x+3,y+2),f'{i} {cv[i]["label"]}',fill='red')
os.makedirs(f'{S}/sheets',exist_ok=True); out=f'{S}/sheets/{sm}_{a:04d}x.jpg'; sh.save(out,quality=80); print(out)
