# each cipher line paired with (gloss interline above + gloss interline below); skips allowed.
import sys, math, json, collections
sys.path.insert(0,__file__.rsplit('/',1)[0])
from parse import load, norm
import em2
def pairs_window(path):
    blocks=load(path); pairs=[]
    for b in blocks:
        seq=[(t,v) for t,v in b['lines'] if t in 'CG']
        for k,(t,v) in enumerate(seq):
            if t!='C': continue
            up='' ; dn=''
            j=k-1
            while j>=0 and seq[j][0]=='G': up=norm(seq[j][1])+up; j-=1
            j=k+1
            while j<len(seq) and seq[j][0]=='G': dn+=norm(seq[j][1]); j+=1
            pairs.append({'id':'%s:%d'%(b['id'],k),'C':v,'G':up+dn,'up':up,'dn':dn})
    return pairs
if __name__=='__main__':
    P=pairs_window(sys.argv[1])
    em2.LENP.update({1:0.12,2:0.3,3:0.3,4:0.15,5:0.07,6:0.04,7:0.02})
    E={}
    for stage,(sc,ss,it) in enumerate([(0.3,0.3,10),(0.1,0.1,10),(0.05,0.05,15)]):
        E,counts,LL=em2.run(P,iters=it,skipc=math.log(sc),skips=math.log(ss),E=E,verbose=False)
        print('stage',stage,'LL',round(LL,1),flush=True)
    json.dump(E,open(sys.argv[2],'w'))
    for c,d in sorted(counts.items(),key=lambda x:-sum(x[1].values()))[:80]:
        tt=sum(d.values()); top=sorted(d.items(),key=lambda x:-x[1])[:4]
        print(c,round(tt,1),' '.join('%s:%.2f'%(t,v/tt) for t,v in top))
