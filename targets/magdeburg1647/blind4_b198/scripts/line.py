import sys
from PIL import Image
n,x0,x1,pre=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
cs=[int(c) for c in sys.argv[5:]]
S=4;K=3;ov=30
im=Image.open('/home/claude/en/trackB/b198_magdeburg_blind/img/%s.jpg'%n).convert('L')
seg=(x1-x0)//K
for i,c in enumerate(cs):
    y0,y1=c-33,c+35
    parts=[im.crop((max(x0,x0+k*seg-ov),y0,min(x1,x0+(k+1)*seg+ov),y1)) for k in range(K)]
    w=max(p.width for p in parts)
    o=Image.new('L',(w*S,(y1-y0)*S*K+10*(K-1)),128)
    for k,p in enumerate(parts):
        o.paste(p.resize((p.width*S,p.height*S),Image.LANCZOS),(0,k*((y1-y0)*S+10)))
    o.save('/home/claude/en/trackB/b198_magdeburg_blind/crops/%s%02d.jpg'%(pre,i+1))
