# Gallery of every q-form: tail and neighbours. No value printed; left-to-right, line by line.
import json
from PIL import Image, ImageDraw, ImageEnhance
Q=json.load(open('work/qpos.json'))
ims={p:ImageEnhance.Contrast(Image.open(f'scans/{p}_full.jpg')).enhance(1.2) for p in ('f76r','f76v','f77r')}
CW,CH=310,235;NC=4;NR=5;SC=1.0
per=NC*NR
for k in range(0,len(Q),per):
    S=Image.new('RGB',(NC*CW,NR*(CH+16)),'white');d=ImageDraw.Draw(S)
    for n,q in enumerate(Q[k:k+per]):
        r,c=n//NC,n%NC
        x0=q['x']-235;y0=q['y']-40
        cr=ims[q['p']].crop((x0,y0,x0+CW-6,y0+CH))
        S.paste(cr,(c*CW,r*(CH+16)+14))
        d.line((c*CW+235,r*(CH+16)+14,c*CW+235,r*(CH+16)+24),fill='red',width=3)
        d.text((c*CW+3,r*(CH+16)+1),f"{k+n} {q['p'][1:]}.{q['l']} {q['ctx']}",fill='blue')
    S.save(f'scans/t/qg_{k//per:02d}.png')
print(len(Q)//per+1)
