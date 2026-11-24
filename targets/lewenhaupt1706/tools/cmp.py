"""compare deux suites de groupes (copies A et B). usage: cmp.py "fA1 fA2 ..." "fB1 ..." """
import sys, re, difflib
def toks(fs):
    t=[]
    for f in fs.split():
        for line in open(f,encoding='utf-8'):
            if line.startswith('#'): continue
            line=re.sub(r'\{[^}]*\}',' {P} ',re.sub(r'\[[^\]]*\]',' ',line.split('#')[0]))
            for m in re.finditer(r'\{P\}|\d+\??',line): t.append((m.group(0),f.split('/')[-1]))
    return t
A=toks(sys.argv[1]); B=toks(sys.argv[2])
a=[x[0].rstrip('?') for x in A]; b=[x[0].rstrip('?') for x in B]
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
print(len(a),len(b))
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op!='equal': print(op,'A',i1,A[i1:i2],'| B',j1,B[j1:j2],'| ctx',a[max(0,i1-3):i1])
