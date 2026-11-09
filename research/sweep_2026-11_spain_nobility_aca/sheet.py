"""python sheet.py <id> <n_first> <n_last> : fetch images, write contact sheet (4 per row, 400px wide) in scratchpad"""
import fetch,tempfile,os,re,sys
from PIL import Image
i=sys.argv[1]; a,b=int(sys.argv[2]),int(sys.argv[3])
jar=tempfile.mktemp(); sh=os.path.join(fetch.SCR,'show_%s.html'%i)
fetch.curl(fetch.B+'catalogo/show/'+i,sh,jar)
db=re.search(r'dbCode=(\d+)',open(sh,encoding='utf-8',errors='replace').read()).group(1)
ims=[]
for k in range(a,b+1):
    out=os.path.join(fetch.SCR,'%s_%d.jpg'%(i,k))
    if not (os.path.exists(out) and os.path.getsize(out)>1000):
        u=fetch.B+'ViewImage.do?accion=42&txt_descarga=1&dbCode=%s&txt_id_imagen=%d&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0'%(db,k)
        fetch.curl(u,out,jar)
    try: ims.append((k,Image.open(out).convert('L')))
    except Exception as e: print('bad',k)
W=420
per=3
sheets=[]
for s in range(0,len(ims),6):
    grp=ims[s:s+6]; th=[]
    for k,im in grp:
        r=W/im.width; th.append(im.resize((W,int(im.height*r))))
    H=max(t.height for t in th)
    sheet=Image.new('L',(W*3,H*2),255)
    for n,t in enumerate(th): sheet.paste(t,((n%3)*W,(n//3)*H))
    p=os.path.join(fetch.SCR,'sheet_%s_%d.png'%(i,grp[0][0])); sheet.save(p); print(p,[k for k,_ in grp])
