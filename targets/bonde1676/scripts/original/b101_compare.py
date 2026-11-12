import sys,re,difflib
def load(p):
    d={}
    for l in open(p,encoding='utf-8'):
        m=re.match(r'R(\d+):\s*(.*)',l)
        if m: d[int(m.group(1))]=[x for x in re.findall(r'"[^"]*"|\S+',m.group(2)) if not x.startswith('"')]
    return d
a=load(sys.argv[1]); b=load(sys.argv[2])
tot=eq=cutc=diff=0
for k in sorted(set(a)|set(b)):
    A=a.get(k,[]); B=b.get(k,[])
    sm=difflib.SequenceMatcher(None,A,B,autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': eq+=i2-i1; tot+=i2-i1
        else:
            n=max(i2-i1,j2-j1)
            for q in range(n):
                x=A[i1+q] if i1+q<i2 else '-'; y=B[j1+q] if j1+q<j2 else '-'
                tot+=1
                if ('~' in x or '~' in y) and (x=='-' or y=='-' or y.rstrip('~').startswith(x.rstrip('~')) or x.rstrip('~').startswith(y.rstrip('~'))): cutc+=1; print('  R%d cut-compatible: %s | %s'%(k,x,y))
                else: diff+=1; print('  R%d DIFFER: %s | %s'%(k,x,y))
print('lines',len(set(a)|set(b)),'token positions',tot,'identical',eq,'cut-compatible',cutc,'differ',diff)
print('identical %d/%d = %.2f%%; identical+cut-compatible %d/%d = %.2f%%'%(eq,tot,100*eq/tot,eq+cutc,tot,100*(eq+cutc)/tot))
