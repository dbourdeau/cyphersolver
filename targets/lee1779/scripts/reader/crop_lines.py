"""crop_lines.py <table.tsv> <words.tsv> <pages_dir> <page_offset(leaf=page-off)> <out.jpg> <group> [<group>...]
For each group (e.g. 243a17) crop column lines n-3..n+3 from the page image, label each row with the
line number computed from the OCR grid, and stack crops into one image."""
import sys,csv,glob,os
from PIL import Image,ImageDraw,ImageFont
csv.field_size_limit(10**8)
table,words,pdir,off,out=sys.argv[1:6]; off=int(off); groups=sys.argv[6:]
rows={}
for r in csv.reader(open(table,encoding='utf8'),delimiter='\t'):
    rows.setdefault(int(r[0]),[]).append((r[2],int(r[3]),int(r[4])))
dims={}; xs={}
for l in open(words,encoding='utf8'):
    f=l.split('\t'); leaf=int(f[0])
    if leaf not in dims: dims[leaf]=(int(f[5]),int(f[6]))
font=ImageFont.load_default(size=40)
tiles=[]
for g in groups:
    p=int(g[:3]); c=g[3]; n=int(g[4:6]); leaf=p-off
    fl=glob.glob(os.path.join(pdir,f"p{p:03d}_*.jpg"))
    if not fl or leaf not in rows: tiles.append(None); continue
    im=Image.open(fl[0]).convert('L'); W,H=dims[leaf]; s=im.size[0]/W
    R=[(ln,y) for cc,ln,y in rows[leaf] if cc==c]
    # fit y = y1 + (ln-1)*pitch from rows
    import statistics as st
    pts=sorted(R); 
    if len(pts)<5: tiles.append(None); continue
    pitch=st.median([(b[1]-a[1])/(b[0]-a[0]) for a,b in zip(pts,pts[1:]) if b[0]!=a[0]])
    y1=st.median([y-(ln-1)*pitch for ln,y in pts])
    # column x-range: from rows' words — approximate with half page
    allx=[ (cc) for cc,_,_ in rows[leaf]]
    x0= 0 if c=='a' else int(im.size[0]*0.47); x1=int(im.size[0]*0.56) if c=='a' else im.size[0]
    ya=int((y1+(n-4.5)*pitch)*s); yb=int((y1+(n+2.5)*pitch)*s)
    cr=im.crop((x0,max(0,ya),x1,min(im.size[1],yb))).convert('RGB')
    lab=Image.new("RGB",(cr.size[0]+330,cr.size[1]),"white"); lab.paste(cr,(330,0)); d=ImageDraw.Draw(lab)
    for k in range(n-3,n+3):
        yy=int(((y1+(k-1)*pitch)*s)-ya)
        d.text((5,yy-20),f"{g} L{k}" if k==n else f"   L{k}",fill=(255,0,0) if k==n else (0,0,255),font=font)
    tiles.append(lab)
tiles=[t for t in tiles if t]
if not tiles: sys.exit('none')
w=max(t.size[0] for t in tiles); h=sum(t.size[1]+6 for t in tiles)
big=Image.new('RGB',(w,h),'gray'); y=0
for t in tiles: big.paste(t,(0,y)); y+=t.size[1]+6
sc=min(1.0,1100/w); big=big.resize((int(w*sc),int(h*sc)))
big.save(out,quality=85)
