import pymupdf as fitz,json,glob,re,os
from PIL import Image,ImageDraw
L={r['id']:r for r in json.load(open('list1598.json'))}
os.makedirs('strips',exist_ok=True)
ids=[]
for f in sorted(glob.glob('pdf/*.pdf')):
    rid=re.search(r'R(\d+)_',f).group(1)
    if L[rid]['record_type']!='1' or rid in [i for i,_ in ids]: continue
    ids.append((rid,f))
tiles=[]
for rid,f in ids:
    p=fitz.open(f)[0]; r=p.rect
    clip=fitz.Rect(r.x0+r.width*.08,r.y0+r.height*.18,r.x0+r.width*.62,r.y0+r.height*.30)
    pm=p.get_pixmap(dpi=110,clip=clip); pm.save('strips/t.png')
    im=Image.open('strips/t.png').convert('L'); im.thumbnail((880,300)); tiles.append((rid,im.copy()))
for k in range(0,len(tiles),10):
    S=Image.new('L',(1800,5*330),255);d=ImageDraw.Draw(S)
    for j,(rid,im) in enumerate(tiles[k:k+10]):
        x,y=(j%2)*900,(j//2)*330;S.paste(im,(x,y+22));d.text((x+4,y+4),rid,fill=0)
    S.save(f'strips/f{k//10:02d}.jpg',quality=85)
print(len(tiles))
