import sys,re,difflib
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
def load(p):
    D={}
    for l in open(p,encoding='utf-8'):
        if re.match(r'^\d{4}\|',l):
            a=l.rstrip('\n').split('|',3)
            body=re.sub(r'\{[^}]*\}',' ',a[3])
            toks=[t.strip('.,') for t in body.split() if t.strip('.,')]
            D[(a[0],a[1],a[2])]=toks
    return D
if __name__=='__main__':
    A=load(sys.argv[1]);B=load(sys.argv[2])
    keys=sorted(set(A)|set(B)); nd=0;tot=0
    for k in keys:
        a=A.get(k,[]);b=B.get(k,[])
        if a!=b:
            sm=difflib.SequenceMatcher(a=a,b=b,autojunk=False)
            for op,i1,i2,j1,j2 in sm.get_opcodes():
                if op!='equal': nd+=1; print(k,op,'P1:',a[i1:i2],'P2:',b[j1:j2],' ctx P1:',' '.join(a[max(0,i1-2):i2+2]))
        tot+=len(a)
    print('lines',len(keys),'P1 groups',tot,'diff blocks',nd)
