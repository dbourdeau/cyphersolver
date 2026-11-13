import sys
from PIL import Image
n,x0,x1,y0,y1,out=sys.argv[1],*map(int,sys.argv[2:6]),sys.argv[6]
S=3
im=Image.open('/home/claude/en/trackB/b198_magdeburg_blind/img/%s.jpg'%n)
mid=(x0+x1)//2; ov=40
a=im.crop((x0,y0,mid+ov,y1)); b=im.crop((mid-ov,y0,x1,y1))
w=max(a.width,b.width)
o=Image.new('L',(w*S,(y1-y0)*S*2+12),128)
o.paste(a.convert('L').resize((a.width*S,a.height*S),Image.LANCZOS),(0,0))
o.paste(b.convert('L').resize((b.width*S,b.height*S),Image.LANCZOS),(0,(y1-y0)*S+12))
o.save('/home/claude/en/trackB/b198_magdeburg_blind/crops/'+out)
