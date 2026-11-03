# Large straightened crops of doubtful q-forms, page coordinates by hand.
import sys
from PIL import Image, ImageDraw
src=open('scripts/strips_f.py').read().split("sheets('f76r'")[0]
exec(src)
LINES['f77r']=LINES['f77r']+[(2975,2925),(3100,3050),(3215,3160),(3345,3285)]
def strip(p,ln,x0,x1,top=55,h=215,sc=2.0):
    im=Image.open(f'scans/{p}_full.jpg'); yl,yr=LINES[p][ln-1]
    o=Image.new('RGB',(x1-x0,h),'white')
    for x in range(x0,x1,8):
        y=yl+(yr-yl)*(x+4-LX)/(RX-LX)
        o.paste(im.crop((x,int(y-top),x+8,int(y-top)+h)),(x-x0,0))
    return o.resize((int((x1-x0)*sc),int(h*sc)),Image.LANCZOS)
J=[('272-274',8,880,1300),('281',9,760,1150),('283',9,1420,1760),('301',12,2120,2480),('313',14,1520,1880),('318',15,2520,2880),('326',16,2150,2500),('334',17,2620,2980)]
rows=[]
for t,ln,a,b in J: rows.append((t,strip('f77r',ln,a,b)))
for s in range(0,len(rows),3):
    ch=rows[s:s+3];W=max(r.width for _,r in ch)+40;H=sum(r.height+6 for _,r in ch)
    S=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(S);y=0
    for t,r in ch:
        S.paste(r,(40,y));d.text((2,y+6),t,fill='red');y+=r.height+6
    S.save(f'scans/t/zoom_{s//3}.png')
print(len(rows))
