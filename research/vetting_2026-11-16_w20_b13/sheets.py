import sys,os
from PIL import Image, ImageDraw
src,out,per,cols,w=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
os.makedirs(out,exist_ok=True)
fs=sorted(f for f in os.listdir(src) if f.endswith('.jpg'))
for k in range(0,len(fs),per):
    ims=[Image.open(os.path.join(src,f)).convert('L') for f in fs[k:k+per]]
    ims=[im.resize((w,int(im.height*w/im.width))) for im in ims]
    h=max(im.height for im in ims); rows=(len(ims)+cols-1)//cols
    S=Image.new('L',(cols*w,rows*h),255); d=ImageDraw.Draw(S)
    for j,im in enumerate(ims):
        x,y=(j%cols)*w,(j//cols)*h; S.paste(im,(x,y)); d.text((x+10,y+10),fs[k+j],fill=0)
    S.save(os.path.join(out,f'sheet_{fs[k][:3]}.jpg'),quality=80)
print('ok')
