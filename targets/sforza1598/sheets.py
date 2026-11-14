import fitz,json,os,glob,re
from PIL import Image
L={r['id']:r for r in json.load(open('list1598.json'))}
os.makedirs('png',exist_ok=True);os.makedirs('sheets',exist_ok=True)
items=[]
for f in sorted(glob.glob('pdf/*.pdf')):
    rid=re.search(r'R(\d+)_',f).group(1)
    if L[rid]['record_type']!='1': continue
    d=fitz.open(f)
    for p in range(len(d)):
        out=f'png/{os.path.basename(f)[:-4]}_{p}.png'
        if not os.path.exists(out): d[p].get_pixmap(dpi=60).save(out)
        items.append((rid,out))
W,H,C=300,400,6
for k in range(0,len(items),24):
    S=Image.new('RGB',(W*C,H*4),'white')
    for j,(rid,out) in enumerate(items[k:k+24]):
        im=Image.open(out);im.thumbnail((W-6,H-20));S.paste(im,((j%C)*W,(j//C)*H+18))
        from PIL import ImageDraw;ImageDraw.Draw(S).text(((j%C)*W+4,(j//C)*H+2),rid+' '+out[-6:-4],fill='red')
    S.save(f'sheets/s{k//24:02d}.jpg',quality=80)
print(len(items))
