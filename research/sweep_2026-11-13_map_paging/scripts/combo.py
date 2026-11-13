# combo.py FFF nk n2 : contact sheet of top nk pages by det.py k plus top n2 by det2 run score (not already in), 4 cols
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
import det2
from PIL import Image,ImageDraw,ImageOps
B='/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/map'
f=sys.argv[1]; nk=int(sys.argv[2]); n2=int(sys.argv[3]); skip=int(sys.argv[4]) if len(sys.argv)>4 else 0
d=B+'/n'+f
rows=[l.split('\t') for l in open(B+'/d'+f+'.tsv')]
rows=[(r[0],int(r[1])) for r in rows if len(r)>=3 and int(r[1])>=0]
rows.sort(key=lambda x:-x[1])
sel=[x[0] for x in rows[skip:skip+nk]]
cache=B+'/d2_'+f+'.tsv'
if os.path.exists(cache): r2={l.split('\t')[0]:int(l.split('\t')[1]) for l in open(cache)}
else:
    r2={}
    for x in sorted(os.listdir(d)):
        try: r2[x]=det2.feat(os.path.join(d,x))[0]
        except Exception: r2[x]=-1
    open(cache,'w').write(''.join('%s\t%d\n'%kv for kv in r2.items()))
add=[x for x,_ in sorted(r2.items(),key=lambda kv:-kv[1]) if x not in sel][:n2]
sel+=add
W=400;ims=[]
k1=dict(rows)
for x in sel:
    im=Image.open(os.path.join(d,x)).convert('L'); im=ImageOps.autocontrast(im,cutoff=1)
    h=int(im.height*W/im.width); im=im.resize((W,h)).convert('RGB')
    dr=ImageDraw.Draw(im); dr.rectangle([0,0,170,16],fill='white'); dr.text((3,2),'%d k=%d r=%d'%(int(x[1:8]),k1.get(x,-1),r2.get(x,-1)),fill='red'); ims.append(im)
H=max(i.height for i in ims); cols=4; n=(len(ims)+cols-1)//cols
S=Image.new('RGB',(W*cols,H*n),'white')
for j,i in enumerate(ims): S.paste(i,((j%cols)*W,(j//cols)*H))
out=B+'/combo_%s_%d.jpg'%(f,skip); S.save(out,quality=78); print(out,S.size)
