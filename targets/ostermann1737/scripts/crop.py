import sys
from PIL import Image, ImageOps, ImageFilter
im=Image.open('/home/claude/keyless/ostermann1737/img/thumbphp.jpg').convert('L')
ys=[228,274,318,363,408,452,497,541,585,629,672,716,760,805,850,895,940,985]
for n,y in enumerate(ys,1):
    for h,(x0,x1) in enumerate([(40,400),(340,700)]):
        c=im.crop((x0,y-30,x1,y+30)); c=ImageOps.autocontrast(c,cutoff=1)
        c=c.resize((c.width*4,c.height*4),Image.LANCZOS)
        c.save('/home/claude/keyless/ostermann1737/crops/L%02d%s.png'%(n,'ab'[h]))
# stacked sheets of 3 lines
for k in range(0,18,3):
    for h in 'ab':
        ims=[Image.open('/home/claude/keyless/ostermann1737/crops/L%02d%s.png'%(n,h)) for n in range(k+1,k+4)]
        sh=Image.new('L',(ims[0].width,sum(i.height for i in ims)+20),255); yy=0
        for i in ims: sh.paste(i,(0,yy)); yy+=i.height+10
        sh.save('/home/claude/keyless/ostermann1737/crops/S%02d%s.png'%(k//3+1,h))
