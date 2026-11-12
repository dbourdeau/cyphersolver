"""rasheet.py bsid a b outdir [W=300] : Rigsarkivet unit images a..b as 4x4 contact sheets (plain curl, default UA)
image list: api.rigsarkivet.dk/ao/v1/billedviser/billed-reference-lister?bsid=<unit>; image: /ao/v1/images/<id>"""
import sys,json,subprocess,time,io,os
from PIL import Image,ImageDraw
def get(u):
    r=subprocess.run(['curl','-sS','-m','120',u],capture_output=True)
    if r.returncode: raise RuntimeError(r.stderr.decode()[:200])
    return r.stdout
b,a,z,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]; W=int(sys.argv[5]) if len(sys.argv)>5 else 300
os.makedirs(out,exist_ok=True)
ids=[g.split(',')[1] for g in json.loads(get('https://api.rigsarkivet.dk/ao/v1/billedviser/billed-reference-lister?bsid=%s'%b))['SA_GUIDs']]
print('images',len(ids),flush=True); z=min(z,len(ids)); lg=open(os.path.join(out,'ids.tsv'),'a')
for s in range(a,z+1,16):
    ims=[]
    for n in range(s,min(s+16,z+1)):
        try:
            im=Image.open(io.BytesIO(get('https://api.rigsarkivet.dk/ao/v1/images/%s'%ids[n-1]))); im.draft('L',(W*2,W*2)); im=im.convert('L')
            im=im.resize((W,int(im.height*W/im.width)))
        except Exception as e: print('fail',n,e,flush=True); continue
        d=ImageDraw.Draw(im); d.rectangle([0,0,60,16],fill=255); d.text((3,3),str(n),fill=0); ims.append(im)
        lg.write('%s\t%d\t%s\n'%(b,n,ids[n-1])); lg.flush(); time.sleep(0.7)
    if not ims: continue
    h=max(i.height for i in ims); S=Image.new('L',(4*W,((len(ims)+3)//4)*h),255)
    for k,im in enumerate(ims): S.paste(im,((k%4)*W,(k//4)*h))
    fn=os.path.join(out,'%s_%04d.jpg'%(b,s)); S.save(fn,quality=70); print(fn,flush=True)
