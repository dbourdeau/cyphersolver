"""control_tiles.py <lookups.tsv> <outprefix> : one 3-line crop per control lookup, labelled by a random code only.
Line index = detector index on the column-b line grid (index 0 is normally the running head)."""
import sys,glob,os,csv,random
sys.path.insert(0,os.path.dirname(__file__))
from imglines import analyse
from PIL import Image,ImageDraw,ImageFont
import os
R=os.environ.get('ENTICK_DIR', 'sources/raw/entick_dictionary/')
dirs={'1776':R+'bim_eighteenth-century_the-new-spelling-diction_entick-john_1776/pages','1772':R+'bim_eighteenth-century_the-new-spelling-diction_entick-john_1772/pages'}
rows=list(csv.DictReader(open(sys.argv[1]),delimiter='\t'))
random.seed(42); codes=random.sample(range(100,1000),len(rows))
font=ImageFont.load_default(size=28)
key=open(sys.argv[2]+'_key.tsv','w'); key.write('code\tid\tgroup\tarm\tedition\tpage\tcol\tline\n')
tiles=[]
order=list(range(len(rows))); random.shuffle(order)
for k in order:
    r=rows[k]; p=int(r['page']); c=r['col']; n=int(r['line'])
    f=glob.glob(os.path.join(dirs[r['edition']],f"p{p:03d}_*.jpg"))
    key.write(f"{codes[k]}\t{r['id']}\t{r['group']}\t{r['arm']}\t{r['edition']}\t{p}\t{c}\t{n}\n")
    if not f: tiles.append((codes[k],None)); continue
    im=Image.open(f[0]).convert('L'); sc=1600/im.size[0]; sm=im.resize((1600,int(im.size[1]*sc)))
    try:
        a=analyse(f[0]); dv=a['divider']; bx1=a['cols']['b']['x'][1]; colw=bx1-dv; L=a['cols']['b']['lines']
        if colw<400 or colw>900 or len(L)<30: raise Exception
    except Exception:
        tiles.append((codes[k],None)); continue
    x0,x1=(max(0,int(dv-colw*1.1)),dv) if c=='a' else (dv,min(1600,int(dv+colw*1.02)))
    n=min(n,len(L)-1)
    ya=L[max(0,n-1)][0]-4; yb=L[min(len(L)-1,n+1)][1]+4
    cr=sm.crop((x0,ya,x1,yb)).convert('RGB'); lab=Image.new('RGB',(cr.size[0]+110,cr.size[1]),'white'); lab.paste(cr,(110,0))
    d=ImageDraw.Draw(lab); d.text((4,cr.size[1]//2-14),str(codes[k]),fill=(200,0,0),font=font)
    ym=(L[n][0]+L[n][1])//2-ya; d.line((105,ym,110+cr.size[0],ym),fill=(255,0,0),width=1)
    tiles.append((codes[k],lab))
miss=[c for c,t in tiles if t is None]; print('missing',miss)
T=[t for c,t in tiles if t is not None]
for i in range(0,len(T),14):
    g=T[i:i+14]; W=max(t.size[0] for t in g); H=sum(t.size[1]+6 for t in g)
    big=Image.new('RGB',(W,H),'gray'); y=0
    for t in g: big.paste(t,(0,y)); y+=t.size[1]+6
    big.save(f"{sys.argv[2]}_{i//14:02d}.jpg",quality=80); print(f"{sys.argv[2]}_{i//14:02d}.jpg",big.size)
