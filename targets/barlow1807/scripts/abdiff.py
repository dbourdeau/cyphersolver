"""Line-by-line comparison of pass A and pass B for one page; prints numbered lines with differing tokens flagged."""
import sys,re,difflib
def toks(line):
    line=re.sub(r'^L\d+\s*','',line)
    return re.findall(r'\d[\d?]*|[A-Za-z]+|\[[^\]]*\]|\{[^}]*\}|\.',line)
p=sys.argv[1]
A=[l for l in open(f'trans_raw/p{p}_A.txt',encoding='utf8').read().splitlines() if l.strip()]
B=[l for l in open(f'trans_raw/p{p}_B.txt',encoding='utf8').read().splitlines() if l.strip()]
print(f'== page {p}: A {len(A)} lines, B {len(B)} lines')
for i in range(max(len(A),len(B))):
    a=toks(A[i]) if i<len(A) else []; b=toks(B[i]) if i<len(B) else []
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False); out=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': out.append(' '.join(a[i1:i2]))
        else: out.append('{A:'+' '.join(a[i1:i2])+' | B:'+' '.join(b[j1:j2])+'}')
    print(f'{i+1:02d}',' '.join(out))
