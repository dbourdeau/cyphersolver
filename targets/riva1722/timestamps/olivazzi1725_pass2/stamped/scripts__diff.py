import sys,difflib,importlib.util
spec=importlib.util.spec_from_file_location('dec','/home/claude/en/trackB/b70_selvatico_read/scripts/dec.py');dec=importlib.util.module_from_spec(spec);spec.loader.exec_module(dec)
def load(p):
    return {lid:[(o['canon'] or o['val'],o['raw'],o['val']) for k,o in items if k=='unit'] for lid,items in dec.run(sys.argv[1],p)}
A=load(sys.argv[2]);B=load(sys.argv[3]);n=0
for lid,a in A.items():
    b=B.get(lid,[])
    sm=difflib.SequenceMatcher(None,[x[0] for x in a],[x[0] for x in b],autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal':
            n+=1; print(n,lid,op,'B idx',i1+1,[x[1]+'='+x[2] for x in a[i1:i2]],'| A',[x[1]+'='+x[2] for x in b[j1:j2]])
