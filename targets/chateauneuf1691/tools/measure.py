import sys,json,random
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from common import *
def lev(a,b):
    prev=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        cur=[i]+[0]*len(b)
        for j,cb in enumerate(b,1):
            cur[j]=min(prev[j]+1,cur[j-1]+1,prev[j-1]+(ca!=cb))
        prev=cur
    return prev[-1]
def score(key,nums,ref):
    dec=''.join(('?' if (n is None or str(n) not in key) else key[str(n)]) for n in nums)
    d=norm(dec.replace('?','#'),True) if False else None
    # keep '?' as a non-matching char
    import unicodedata
    out=[]
    for n in nums:
        if n is None or str(n) not in key: out.append('#')
        else: out.append(norm(key[str(n)],True))
    dec=''.join(out)
    return 1-lev(dec,ref)/len(ref), dec
if __name__=='__main__':
    key=json.load(open(sys.argv[1])); path=sys.argv[2]
    rows=read_gloss(path); nums=[]; ref=''
    for img,side,ln,kind,txt in rows:
        if kind=='G' and not txt.strip().startswith('(none)'): ref+=txt
        if kind=='N': nums+= [t for t in tok_numbers(txt) if t!='BRK']
    ref=norm(ref,True)
    s,dec=score(key,nums,ref)
    print('groups',len(nums),'ref letters',len(ref)); print('SCORE',round(s,4))
    vals=[key[k] for k in sorted(key,key=int)]; ks=sorted(key,key=int); C=[]
    for k in range(200):
        r=random.Random(1691+k); v=vals[:]; r.shuffle(v)
        C.append(score(dict(zip(ks,v)),nums,ref)[0])
    print('controls max',round(max(C),4),'mean',round(sum(C)/len(C),4))
    print('PASS' if (s>=0.85 and s>=max(C)+0.30) else 'FAIL')
    print('DEC',dec); print('REF',ref)
