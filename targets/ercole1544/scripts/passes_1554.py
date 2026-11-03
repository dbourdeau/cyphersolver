# usage, from the target folder: python scripts/passes_1554.py : per page, signs in pass 1 and pass 2, edit distance over the sign sequence, line by line
import re,glob,os
tok=lambda b: re.findall(r'L\^\w+|\d+|\?|[A-Za-z]',b)
def load(f):
    d={}
    for l in open(f,encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        a,_,b=l.strip().partition(' '); d[a]=tok(b)
    return d
def ed(a,b):
    p=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        c=[i]
        for j,y in enumerate(b,1):
            c.append(min(p[j]+1,c[-1]+1,p[j-1]+(x!=y)))
        p=c
    return p[-1]
T=D=0
for f in sorted(glob.glob('validation/1554_pass2/*.txt')):
    n=os.path.basename(f)
    a=load('validation/1554_pass1/'+n); b=load(f)
    t=d=0
    for k in sorted(set(a)|set(b)):
        e=ed(a.get(k,[]),b.get(k,[])); s=max(len(a.get(k,[])),len(b.get(k,[])))
        t+=s; d+=e
    print(n,t,'signs',d,f'differ {100*d/t:.1f}%'); T+=t; D+=d
print('all',T,D,f'{100*D/T:.1f}%')
