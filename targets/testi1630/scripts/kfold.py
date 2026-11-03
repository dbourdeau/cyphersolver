# kfold.py : same-hand second pass. Each line is read by a classifier trained only on the OTHER lines of that page (3 folds), no language model.
# Disagreements with the eye pass are listed and cropped. Also scores the blind c. 13r read against c. 15, with a shuffled-table control.
import sys,json,random,numpy as np
from PIL import Image,ImageDraw,ImageFont
sys.argv=[sys.argv[0]]
import importlib.util as iu
sp=iu.spec_from_file_location('o','scripts/ocr_page.py'); o=iu.module_from_spec(sp); sp.loader.exec_module(o)
PAGES={'c23':('scans/work/c23_block.jpg',[124,410,694,972,1261,1540,1822,2105,2391],'scans/work/c23_passA.txt'),
       'c13':('scans/work/c13r_block.jpg',[183,440,668,912,1133,1371,1601,1835],'scans/work/c13_passA.txt')}
font=ImageFont.truetype('arial.ttf',20)
res={}
for page,(blk,ys,pf) in PAGES.items():
    ink=o.load(blk); im=Image.open(blk).convert('RGB'); P=[l.split() for l in open(pf,encoding='utf8') if l.strip()]
    D=[]
    for y,seq in zip(ys,P):
        B=o.line_boxes(ink,y); D.append((seq,B,[o.vec(ink,b[:4]) for b in B]))
    # strict one-to-one training pairs from lines
    n=len(D); tot=ok=0; mism=[]; read=[]
    for li in range(n):
        tr=[d for k,d in enumerate(D) if k%3!=li%3]
        T=json.load(open('scans/work/c23_tpl.json')); ink0=o.load('scans/work/c23_block.jpg')
        X=np.array([o.vec(ink0,b) for bs in T.values() for b in bs]); Y=np.array([l for l,bs in T.items() for b in bs])
        if page=='c23':  # do not seed c. 23r from its own crops: start from c. 13r eye labels
            X0=[];Y0=[]
            for seq,B,V in [ (l,None,None) for l in [] ]: pass
        for r in range(3):
            XX=[];YY=[]
            for seq,B,V in tr:
                lab=[o.classify(X,Y,v) for v in V]
                for i,j in o.nw(seq,lab):
                    if seq[i]==lab[j]: XX.append(V[j]);YY.append(seq[i])
            X=np.array(XX);Y=np.array(YY)
        seq,B,V=D[li]; lab=[o.classify(X,Y,v) for v in V]; read.append(lab)
        for i,j in o.nw(seq,lab):
            tot+=1; ok+=seq[i]==lab[j]
            if seq[i]!=lab[j]: mism.append((li+1,i+1,seq[i],lab[j],B[j][:4]))
    print(page,'kfold aligned',tot,'agree',ok,round(ok/tot,4),'disagreements',len(mism))
    res[page]=read
    # disagreement sheet
    cols=8; W=180;H=170; rows=(len(mism)+cols-1)//cols
    C=Image.new('RGB',(cols*W,rows*H),'white'); d=ImageDraw.Draw(C)
    for k,(li,i,a,b,bx) in enumerate(mism[:cols*12]):
        x0,y0,x1,y1=bx; cx=(x0+x1)//2; cy=(y0+y1)//2
        c=im.crop((cx-70,cy-65,cx+70,cy+65)).resize((168,156)); xx=(k%cols)*W; yy=(k//cols)*H; C.paste(c,(xx,yy+14)); d.text((xx+2,yy-2),f'{li}.{i} {a}|{b}',fill=(200,0,0),font=font)
    C=C.crop((0,0,cols*W,min(rows,12)*H)); C.save(f'scans/work/{page}_dis.jpg',quality=88)
json.dump(res,open('scans/work/kfold.json','w'))
KEY=o.KEY
clear=''.join(c for c in open('scans/work/clear_c15_heldout.txt',encoding='utf8').read() if c.isalpha()).replace('v','u')
def sw(a,b):
    n,m=len(a),len(b); prev=np.zeros(m+1,int); best=0
    for i in range(1,n+1):
        cur=np.zeros(m+1,int)
        for j in range(1,m+1):
            cur[j]=max(0,prev[j-1]+(2 if a[i-1]==b[j-1] else -1),prev[j]-1,cur[j-1]-1)
        best=max(best,cur.max()); prev=cur
    return int(best)
def globalm(a,b):
    a=list(a);b=list(b); n,m=len(a),len(b); D=np.zeros((n+1,m+1),int)
    for i in range(1,n+1):
        for j in range(1,m+1): D[i,j]=max(D[i-1,j-1]+(a[i-1]==b[j-1]),D[i-1,j],D[i,j-1])
    return int(D[n,m])
# blind c13: letters after dropping the plain text at line ends is impossible without looking, so use the k-fold read of the whole line and LCS against the clear text
for nm,lines in (('kfold same-hand',res['c13']),('other-hand blind',json.load(open('scans/work/blind.json'))['c13'])):
    s=''.join(KEY.get(l,'?').replace('v','u') for q in lines for l in q)
    lcs=globalm(s,clear); print(nm,'machine signs',len(s),'clear',len(clear),'LCS',lcs,round(lcs/len(clear),4))
    rng=random.Random(2); ks=list(KEY); vals=[KEY[k].replace('v','u') for k in ks]; R=[]
    for _ in range(100):
        v=vals[:]; rng.shuffle(v); k2=dict(zip(ks,v)); t=''.join(k2.get(l,'?') for q in lines for l in q); R.append(globalm(t,clear)/len(clear))
    print('  shuffled table control mean',round(np.mean(R),4),'max',round(max(R),4))
