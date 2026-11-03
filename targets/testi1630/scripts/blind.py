# blind.py : language-free cross-validated read. Classifier for page P is trained only on OTHER pages. Used as the second transcription pass
# for c. 23r and as the blind held-out read of c. 13r. No plaintext of the tested page enters.
import sys,json,numpy as np
sys.argv=[sys.argv[0]]
import importlib.util as iu
sp=iu.spec_from_file_location('o','scripts/ocr_page.py'); o=iu.module_from_spec(sp); sp.loader.exec_module(o)
PAGES={'c23':('scans/work/c23_block.jpg',[124,410,694,972,1261,1540,1822,2105,2391],'scans/work/c23_passA.txt'),
       'c13':('scans/work/c13r_block.jpg',[183,440,668,912,1133,1371,1601,1835],'scans/work/c13_passA.txt'),
       'c7r':('scans/work/c7r_block.jpg',json.load(open('scans/work/c7r_lines.json'))[2:17],'scans/work/c7r_passA.txt')}
def build(exclude):
    T=json.load(open('scans/work/c23_tpl.json')); ink0=o.load('scans/work/c23_block.jpg')
    data=[]
    for k,(blk,ys,pf) in PAGES.items():
        if k==exclude: continue
        ink=o.load(blk); P=[l.split() for l in open(pf,encoding='utf8') if l.strip()]
        for y,seq in zip(ys,P):
            B=[b for b in o.line_boxes(ink,y) if b[4]=='w']; data.append((seq,[o.vec(ink,b[:4]) for b in B]))
    if exclude=='c23':
        # seed templates come from c. 23r, so seed from the c. 7r eye read instead, by position in clean lines
        X=[];Y=[]
        for seq,V in data:
            if abs(len(seq)-len(V))<=1:
                for s,v in zip(seq,V): X.append(v);Y.append(s)
        X=np.array(X);Y=np.array(Y)
    else:
        X=[];Y=[]
        for l,bs in T.items():
            for b in bs: X.append(o.vec(ink0,b));Y.append(l)
        X=np.array(X);Y=np.array(Y)
    for r in range(3):
        XX=[];YY=[]
        for seq,V in data:
            lab=[o.classify(X,Y,v) for v in V]; A=o.nw(seq,lab)
            for i,j in A:
                if seq[i]==lab[j]: XX.append(V[j]);YY.append(seq[i])
        X=np.array(XX);Y=np.array(YY)
    return X,Y
out={}
for page in ('c23','c13'):
    X,Y=build(page); blk,ys,pf=PAGES[page]; ink=o.load(blk); P=[l.split() for l in open(pf,encoding='utf8') if l.strip()]
    tot=ok=0; lines=[]; mism=[]
    for li,(y,seq) in enumerate(zip(ys,P),1):
        B=o.line_boxes(ink,y); lab=[o.classify(X,Y,o.vec(ink,b[:4])) for b in B]; A=o.nw(seq,lab); lines.append(lab)
        for i,j in A:
            tot+=1; ok+=seq[i]==lab[j]
            if seq[i]!=lab[j]: mism.append((li,i+1,seq[i],lab[j]))
    print(page,'trainsize',len(Y),'aligned',tot,'agree',ok,round(ok/tot,4)); print(' mismatches',mism)
    print(' letters:',' / '.join(''.join(o.KEY.get(l,'?') for l in q) for q in lines))
    out[page]=lines
json.dump(out,open('scans/work/blind.json','w'))
