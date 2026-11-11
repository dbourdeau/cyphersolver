"""Build N-up contact sheets from a folder of page images: python3 sheets.py DIR [cols rows tilewidth]"""
import sys,os,glob
from PIL import Image
d=sys.argv[1]; C=int(sys.argv[2]) if len(sys.argv)>2 else 6; R=int(sys.argv[3]) if len(sys.argv)>3 else 3; W=int(sys.argv[4]) if len(sys.argv)>4 else 300
H=int(W*1.4); ims=sorted(f for f in glob.glob(os.path.join(d,'[0-9]*.jpg')))
for f in glob.glob(os.path.join(d,'sheet_*.jpg')): os.remove(f)
for s in range(0,len(ims),C*R):
    sh=Image.new('RGB',(W*C,H*R),'white')
    for k,f in enumerate(ims[s:s+C*R]):
        try: im=Image.open(f).convert('RGB')
        except Exception: continue
        im.thumbnail((W,H)); sh.paste(im,((k%C)*W,(k//C)*H))
    sh.save(os.path.join(d,'sheet_%s.jpg'%os.path.basename(ims[s])[:-4]),quality=60)
print(len(ims),'images')
