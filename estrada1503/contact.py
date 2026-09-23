import sys,glob,re
from PIL import Image
d=sys.argv[1]; fs=sorted(glob.glob(d+'/p*.jpg'),key=lambda f:int(re.findall(r'p(\d+)',f)[-1]))
ims=[]
for f in fs:
    try: ims.append(Image.open(f).convert('L').resize((490,680)))
    except Exception: ims.append(Image.new('L',(490,680),0))
c=4; W=Image.new('L',(490*c,680*((len(ims)+c-1)//c)),255)
for k,im in enumerate(ims): W.paste(im,((k%c)*490,(k//c)*680))
W.save(d+'/contact.png'); print(len(ims))
