"""Make unwrap sheets: for each page in work/circles_raw.txt, unwrap each circle (band 590-880 px, start -10 deg,
3 rows, scale 0.6) and stack three circles per sheet with a label. Output work/unwrap/<canvas>_<k>.jpg."""
import subprocess, os, glob
from PIL import Image, ImageDraw
os.makedirs('work/unwrap',exist_ok=True)
cur=None; pages={}
for ln in open('work/circles_raw.txt'):
    if ln.startswith('=='): cur=int(ln.split('c')[1]); pages[cur]=[]; continue
    x,y,a,b,acc=ln.split(); pages[cur].append((int(x),int(y)))
for c,cs in pages.items():
    f=glob.glob('img/c%03d_*_full.jpg'%c)[0]
    ims=[]
    for k,(x,y) in enumerate(cs):
        o='work/unwrap/c%03d_p%d.jpg'%(c,k+1)
        subprocess.run(['python3','-I','scripts/unwrap2.py',f,o,str(x),str(y),'590','880','-10','3','0.6'],check=True,capture_output=True)
        ims.append((k+1,Image.open(o)))
    for g in range(0,len(ims),3):
        grp=ims[g:g+3]; W=max(i.size[0] for _,i in grp); H=sum(i.size[1]+30 for _,i in grp)
        s=Image.new('L',(W,H),255); d=ImageDraw.Draw(s); yy=0
        for k,i in grp:
            d.text((5,yy+5),'c%03d circle %d'%(c,k),fill=0); s.paste(i,(0,yy+30)); yy+=i.size[1]+30
        s.save('work/unwrap/sheet_c%03d_%d.jpg'%(c,g//3+1),quality=90)
print('ok')
