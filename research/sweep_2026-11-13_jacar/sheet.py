"""contact sheet of a PDF's pages -> png/<ref>_sheet.png (usage: sheet.py ref [dpi] [cols])"""
import sys, pymupdf
from PIL import Image
ref=sys.argv[1]; dpi=int(sys.argv[2]) if len(sys.argv)>2 else 45; cols=int(sys.argv[3]) if len(sys.argv)>3 else 4
d=pymupdf.open(f"pdf/{ref}.pdf"); ims=[]
for p in d:
    pm=p.get_pixmap(dpi=dpi); ims.append(Image.frombytes("RGB",(pm.width,pm.height),pm.samples))
w=max(i.width for i in ims); h=max(i.height for i in ims); rows=(len(ims)+cols-1)//cols
S=Image.new("RGB",(w*cols,h*rows),"white")
for k,i in enumerate(ims): S.paste(i,((k%cols)*w,(k//cols)*h))
S.save(f"png/{ref}_sheet.png"); print(S.size)
