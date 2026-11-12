import sys,difflib,re
def mine(fn,prefix):
    out=[]
    for l in open(fn):
        if l.startswith(prefix):
            toks=l.split('|')[-1].strip().split('.')
            out+= [t.rstrip('?') for t in toks]
    return out
def b119(fn):
    out=[]
    for l in open(fn):
        if l.startswith('R'):
            out+=re.findall(r'(?<![\w"])\d+(?![\w"])',re.sub(r'"[^"]*"','',l.split(':',1)[1]))
    return out
def zob(fn):
    out=[]
    for l in open(fn):
        if l.startswith('w'):
            p=[x.strip() for x in l.split('|')]
            toks=[p[2]]+p[3].split('.')
            out+= [t.replace('{','').replace('}','').rstrip('?') for t in toks]
    return out
mode=sys.argv[1]
if mode=='A':
    a=mine('tx/bonde_489R_blind2.txt','R'); b=b119('/home/claude/en/trackB/b119_bonde_nov1677/tx/b119_489R.txt')
else:
    a=mine('tx/zobel_1629-09-20_blind2.txt','W'); b=zob('/home/claude/en/trackB/b106_dk_small/tx/zobel_1629-09-20.txt')
print('blind tokens',len(a),'first tokens',len(b))
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
eq=0
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=='equal': eq+=i2-i1
    else: print(op,'blind[%d:%d]'%(i1,i2),a[i1:i2],'first[%d:%d]'%(j1,j2),b[j1:j2])
print('equal positions',eq)
