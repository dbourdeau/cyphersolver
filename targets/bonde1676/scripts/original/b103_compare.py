import re,sys,difflib
def blind(p):
    out=[]
    for l in open(p):
        if l.startswith('#') or not l.strip(): continue
        n,rest=l.split(' ',1)
        rest=re.sub(r'\[[^\]]*\]',' ',rest)
        for t in re.split(r'[.\s]+',rest):
            if t: out.append((int(n),t.replace('?','~')))
    return out
def b101(p):
    out=[]
    for l in open(p):
        m=re.match(r'R(\d+):(.*)',l)
        if not m: continue
        rest=re.sub(r'"[^"]*"',' ',m.group(2))
        for t in rest.split(): out.append((int(m.group(1)),t))
    return out
for pg,bf in (('323L','bonde_323L_f307v.txt'),('325L','bonde_325L_f309v.txt')):
    a=blind('tx/blind_%s_%s'%(pg,bf.split('_',2)[2])); b=b101('../b101_bonde2/tx/'+bf)
    A=[t for _,t in a]; B=[t for _,t in b]
    fa=[t for t in A if '~' not in t]; fb=[t for t in B if '~' not in t]
    print(pg,'blind tokens',len(A),'full',len(fa),'cut',len(A)-len(fa),'| b101 tokens',len(B),'full',len(fb),'cut',len(B)-len(fb))
    sm=difflib.SequenceMatcher(None,A,B,autojunk=False)
    eq=0
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': eq+=i2-i1
        else: print('  ',op,'blind',a[i1:i2],'b101',b[j1:j2])
    print('  identical aligned tokens',eq,'of blind',len(A),'/ b101',len(B))
