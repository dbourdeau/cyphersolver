# one line, K segments each saved as own file at scale S
import sys
from PIL import Image
n,x0,x1,c,pre=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
slope=float(sys.argv[6]) if len(sys.argv)>6 else 0.0
S=5;K=int(sys.argv[7]) if len(sys.argv)>7 else 2;ov=25
im=Image.open('/home/claude/en/trackB/b198_magdeburg_blind/img/%s.jpg'%n).convert('L')
seg=(x1-x0)//K
parts=[]
for k in range(K):
    a=max(x0,x0+k*seg-ov); b=min(x1,x0+(k+1)*seg+ov)
    cc=c+int(slope*((a+b)/2-x0))
    p=im.crop((a,cc-30,b,cc+32)); parts.append(p.resize((p.width*S,p.height*S),Image.LANCZOS))
w=max(p.width for p in parts)
o=Image.new('L',(w,sum(p.height for p in parts)+10),128)
y=0
for p in parts:
    o.paste(p,(0,y)); y+=p.height+10
o.save('/home/claude/en/trackB/b198_magdeburg_blind/crops/%s.jpg'%pre)
