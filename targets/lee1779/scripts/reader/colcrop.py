"""colcrop.py <pages_dir> <outprefix> <per> spec... (spec = 052b:35) crude column crops, full height, 4 per image."""
import sys,glob,os
sys.path.insert(0,os.path.dirname(__file__))
from PIL import Image,ImageDraw,ImageFont
from imglines import analyse
pdir,outp,per=sys.argv[1],sys.argv[2],int(sys.argv[3]); font=ImageFont.load_default(size=26)
tiles=[]
for sp in sys.argv[4:]:
    pc,ls=sp.split(':'); p=int(pc[:-1]); c=pc[-1]
    f=glob.glob(os.path.join(pdir,f"p{p:03d}_*.jpg"))[0]
    im=Image.open(f).convert('L'); W,H=im.size; sc=1600/W; sm=im.resize((1600,int(H*sc)))
    try:
        r=analyse(f); dv=r['divider']; bx1=r['cols']['b']['x'][1]; colw=bx1-dv
        if colw<400 or colw>900: raise Exception
    except Exception:
        dv=800; colw=650
    x0,x1=(max(0,int(dv-colw*1.12)),dv+5) if c=='a' else (dv-5,min(1600,int(dv+colw*1.02)))
    cr=sm.crop((x0,0,x1,sm.size[1])).convert('RGB')
    cr=cr.resize((int(cr.size[0]*0.85),int(cr.size[1]*0.85)))
    lab=Image.new('RGB',(cr.size[0],cr.size[1]+34),'white'); lab.paste(cr,(0,34)); ImageDraw.Draw(lab).text((4,2),f"p{p}{c} want {ls}",fill=(0,120,0),font=font)
    tiles.append(lab)
for i in range(0,len(tiles),per):
    g=tiles[i:i+per]; Wt=sum(t.size[0]+10 for t in g); Ht=max(t.size[1] for t in g)
    big=Image.new('RGB',(Wt,Ht),'gray'); x=0
    for t in g: big.paste(t,(x,0)); x+=t.size[0]+10
    big.save(f"{outp}_{i//per:02d}.jpg",quality=82); print(f"{outp}_{i//per:02d}.jpg",big.size)
