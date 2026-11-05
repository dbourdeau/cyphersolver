"""Line-labelled decode: python tools/lines.py [folio]  ->  'f147v.4  [1]ja [2]i ...' (index per token, clear words count as tokens)"""
import sys
sys.path.insert(0,'tools')
from decode import load,tokens,val
def lines():
    k=load(); out=[]; fol=None; n=0; cur=[]
    for f,t,l in tokens():
        if t=='@': fol=f; n=0; cur=[]; continue
        if t=='|':
            n+=1; out.append((fol,n,cur)); cur=[]; continue
        cur.append((t,val(k,t)))
    return out
if __name__=='__main__':
    want=sys.argv[1] if len(sys.argv)>1 else None
    for fol,n,cur in lines():
        if want and fol!=want: continue
        print(f'{fol}.{n}  '+' '.join(f'{i+1}:{v}' for i,(t,v) in enumerate(cur)))
