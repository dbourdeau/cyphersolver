"""Monotone DP alignment of system A cipher groups to a contemporary clear, with a partial key.
Each group >=100: known value -> must match clear exactly (cost 0) or 'error' (any 0-5 letters, cost E);
known null ('') -> emits nothing (cost 0) or 1-4 letters (cost E); unknown group -> 0-6 letters (cost U);
clear letters may be skipped (cost S each). Free end in the clear.
usage: align_learn.py key.json out.json cipher1 clear1 [cipher2 clear2 ...]"""
import json,sys,re,unicodedata
import numpy as np
E,U,S=2.5,1.0,1.0; MAXL=8
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); return re.sub(r'[^a-z]','',s)
def load_cipher(p):
    out=[]
    for l in open(p,encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        lab,_,b=l.strip().partition(' ')
        if lab.endswith('T') or lab.endswith('G'): continue
        for g in re.split(r'[\s.|]+',b):
            v=re.sub(r'[^0-9]','',g.split('/')[0])
            if v and int(v)>=100: out.append((lab,str(int(v)),'?' in g))
    return out
def load_clear(p):
    out=[]
    for l in open(p,encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        t=l
        m=re.match(r'^\S+\s',l)
        if m and re.search(r'\d',m.group(0)): t=l[m.end():]
        t=re.sub(r'\[del:[^\]]*\]','',t); t=re.sub(r'\[ins:([^\]]*)\]',r'\1',t); t=t.replace('[?]','')
        out.append(t)
    return norm(' '.join(out))
def align(groups,clear,K):
    n,m=len(groups),len(clear); INF=1e9
    D=np.full((n+1,m+1),INF); D[0,0]=0
    BL=np.zeros((n+1,m+1),np.int8); BT=np.zeros((n+1,m+1),np.int8) # BT: 0 skip,1 exact,2 err/unk
    ca=np.frombuffer(clear.encode(),dtype=np.uint8)
    for i in range(n+1):
        # skip transitions within row i: D[i][j]=min(D[i][j], D[i][j-1]+S)
        row=D[i]; idx=np.arange(m+1)
        cm=np.minimum.accumulate(row-S*idx)+S*idx
        better=cm<row-1e-12
        # backtrack for skip: mark type 0
        BT[i][better]=0; D[i]=np.minimum(row,cm)
        if i==n: break
        g=groups[i][1]; v=K.get(g); cur=D[i]
        if v:  # known non-empty
            L=len(v); vb=np.frombuffer(v.encode(),dtype=np.uint8)
            if L<=m:
                ok=np.ones(m-L+1,bool)
                for k in range(L): ok&=(ca[k:m-L+1+k]==vb[k])
                cand=np.where(ok,cur[:m-L+1],INF)
                tgt=D[i+1,L:]; b=cand<tgt; tgt[b]=cand[b]; BL[i+1,L:][b]=L; BT[i+1,L:][b]=1
            cost=E; Ls=range(0,MAXL)
        elif v=='':
            cand=cur.copy(); tgt=D[i+1]; b=cand<tgt; tgt[b]=cand[b]; BL[i+1][b]=0; BT[i+1][b]=1
            cost=E; Ls=range(1,5)
        else:
            cost=U; Ls=range(0,MAXL+1)
        for L in Ls:
            cand=cur[:m+1-L]+cost+0.01*L; tgt=D[i+1,L:]; b=cand<tgt-1e-12
            tgt[b]=cand[b]; BL[i+1,L:][b]=L; BT[i+1,L:][b]=2
    # free end
    j=int(np.argmin(D[n])); i=n; path=[]
    while i>0 or j>0:
        t=BT[i][j]
        if t==0:
            j-=1; continue
        L=int(BL[i][j]); path.append((i-1,clear[j-L:j],int(t))); i-=1; j-=L
    return path[::-1],float(D[n].min())
if __name__=='__main__':
    K={k:(v[0] if v else '') for k,v in json.load(open(sys.argv[1])).items()}
    res=[]
    for a in range(3,len(sys.argv),2):
        gr=load_cipher(sys.argv[a]); cl=load_clear(sys.argv[a+1])
        path,c=align(gr,cl,K)
        print(sys.argv[a],len(gr),'groups',len(cl),'letters cost',round(c,1),file=sys.stderr)
        for (gi,s,t) in path:
            lab,g,q=gr[gi]
            res.append({'src':sys.argv[a],'lab':lab,'i':gi,'g':g,'q':q,'emit':s,'type':t,'known':K.get(g)})
    json.dump(res,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
