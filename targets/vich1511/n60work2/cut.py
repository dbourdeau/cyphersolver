from PIL import Image, ImageOps, ImageDraw
S=4
for p in range(7,16):
    im=ImageOps.autocontrast(Image.open(f'img/n60_{p}.jpg').convert('L'),cutoff=1); W=im.width
    k=0
    for y in range(150,1540,115):
        rows=[]
        for (x0,x1) in ((110,W//2+30),(W//2-30,W-20)):
            c=im.crop((x0,y,x1,y+130)).resize(((x1-x0)*S,130*S),Image.LANCZOS)
            ImageDraw.Draw(c).text((4,4),f'p{p} y{y}',fill=0); rows.append(c)
        out=Image.new('L',(max(r.width for r in rows),sum(r.height+8 for r in rows)),255); yy=0
        for r in rows: out.paste(r,(0,yy)); yy+=r.height+8
        out.save(f'n60work2/s/p{p:02d}_{k:02d}.png'); k+=1
