# P3 per-line crops (rotated 180), fixed pitch, 3 bands, generous height; cp12/P3_NN.png
import sys
from PIL import Image, ImageOps, ImageDraw
im=Image.open('../img/IMG_R9414_I44519_P3.jpg').convert('L').rotate(180)
X=[560,1450,2340,3260]; y1,p=float(sys.argv[3]) if len(sys.argv)>3 else 180,103.4
for ln in range(int(sys.argv[1]),int(sys.argv[2])+1):
    c0=int(y1+p*(ln-1)); st=[]
    for b in range(3):
        c=c0+(0,0,35)[b]
        s=ImageOps.autocontrast(im.crop((X[b]-(40 if b else 0),c-95,X[b+1]+40,c+85)),cutoff=1).convert('RGB').resize(((X[b+1]-X[b]+80)*2,360))
        ImageDraw.Draw(s).text((4,4),f'{ln:02d}{"abc"[b]}',fill='red'); st.append(s)
    out=Image.new('RGB',(max(s.width for s in st),3*365),'white')
    for i,s in enumerate(st): out.paste(s,(0,i*365))
    out.save(f'cp12/P3_{ln:02d}.png')
