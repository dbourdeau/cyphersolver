# iterative refinement of a draft key on training paragraphs (token -> clear substring tallies)
import sys,collections
sys.path.insert(0,'scripts'); from common import *
T=load_trans('transcription_ind737_letter1.txt')
key=load_key(sys.argv[1] if len(sys.argv)>1 and sys.argv[1].endswith('.tsv') else 'key_frozen.tsv'); paras={'P1':['1.%02d'%i for i in range(3,18)],'P2':['1.%02d'%i for i in range(18,29)],'P3':['1.29','1.30','1.31','1.32','2.02','2.03','2.04'],'P4n':['2.05','2.06','2.07','2.08','2.09','2.10'],'P4':['2.05','2.06','2.07','2.08','2.09','2.10']}
clear={}
for ln in open('clear_panama29_R6_N23.txt',encoding='utf-8'):
    if ln[:1]=='P': k,v=ln.split(':',1); clear[k]=re.sub(r'[^a-zñç]','',re.sub(r'\[|\]','',v.lower()))
def nw(a,b):
    n,m=len(a),len(b); S=[[0]*(m+1) for _ in range(n+1)]; P=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1): S[i][0]=-i; P[i][0]=1
    for j in range(1,m+1): S[0][j]=-j; P[0][j]=2
    for i in range(1,n+1):
        ai=a[i-1]
        for j in range(1,m+1):
            s=2 if ai==b[j-1] else (0.3 if ai=='?' else -1)
            best=S[i-1][j-1]+s;p=0
            if S[i-1][j]-1>best: best=S[i-1][j]-1;p=1
            if S[i][j-1]-1>best: best=S[i][j-1]-1;p=2
            S[i][j]=best;P[i][j]=p
    i,j=n,m; amap=[None]*n
    while i>0 or j>0:
        p=P[i][j]
        if p==0: amap[i-1]=j-1; i-=1; j-=1
        elif p==1: i-=1
        else: j-=1
    return amap
def run(pk, show=False):
    toks=[t for l in paras[pk] for w in words(T[l]) for t in w]
    outs=[dec_tok(t,key) for t in toks]; s=''.join(outs); c=clear[pk]
    amap=nw(s,c); spans=[];pos=0
    for t,o in zip(toks,outs):
        idx=[amap[k] for k in range(pos,pos+len(o)) if amap[k] is not None]; spans.append((t,o,idx)); pos+=len(o)
    matches=sum(1 for k in range(len(s)) if amap[k] is not None and s[k]==c[amap[k]])
    return toks,spans,matches,len(c),s
if __name__=='__main__':
    tally=collections.defaultdict(collections.Counter)
    for pk in sys.argv[2].split(','):
        toks,spans,mt,lc,s=run(pk)
        print(pk,'matched letters',mt,'of clear',lc, round(mt/lc,3))
        # assign clear substrings between consecutive anchors
        anchors=[]
        for i,(t,o,idx) in enumerate(spans):
            if idx: anchors.append((i,min(idx),max(idx)))
        for (i1,a1,b1),(i2,a2,b2) in zip(anchors,anchors[1:]):
            pass
        for i,(t,o,idx) in enumerate(spans):
            if idx: tally[t][clear[pk][min(idx):max(idx)+1]]+=1
            else: tally[t]['']+=1
    if len(sys.argv)>3:
        for t,cn in sorted(tally.items(),key=lambda x:-sum(x[1].values())):
            print(t, key.get(t,'-'), cn.most_common(4))
