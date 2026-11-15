"""Pair pass A and pass B segments leaf by leaf in reading order and align signs (difflib). Output: per segment, both readings and the differing positions."""
import csv, difflib, sys, collections
def load(fn):
    rows=[]
    for l in open(fn):
        if l.startswith('#') or l.startswith('leaf'): continue
        f=l.rstrip('\n').split('\t')
        if len(f)<5: continue
        rows.append(f)
    return rows
def toks(s):
    out=[]; i=0
    s=s.replace('[','<').replace(']','>')
    parts=[]; buf=''
    j=0
    while j<len(s):
        c=s[j]
        if c=='<':
            k=s.index('>',j); parts.append(s[j+1:k].split('/')[0]); j=k+1
        elif c==' ': j+=1
        else:
            # read token until space
            k=j
            while k<len(s) and s[k] not in ' <': k+=1
            parts.append(s[j:k]); j=k
    return [p for p in parts if p and not p.startswith('struck')]
A=load('passA_forward.tsv'); B=load('passB_backward.tsv')
B=[r for r in B if not r[2].startswith('x') and r[0] not in ('19r','62r')]
B=B[::-1]
# B is backward by leaf and by line, but within a line runs were listed in reverse order too; sort within leaf by line_y then run label
def key(r): 
    order='0123456789'
    return (float(r[1]), r[2])
leaves=[]
for r in A:
    if r[0] not in leaves: leaves.append(r[0])
out=[]
for lf in leaves:
    a=[r for r in A if r[0]==lf]; b=sorted([r for r in B if r[0]==lf], key=lambda r:(float(r[1]),r[2].replace('(cont.)','0').replace('(cont)','0')))
    sa=[t for r in a for t in toks(r[4])]; sb=[t for r in b for t in toks(r[4])]
    sm=difflib.SequenceMatcher(None,sa,sb,autojunk=False)
    agree=sum(bl.size for bl in sm.get_matching_blocks())
    out.append((lf,len(sa),len(sb),agree))
    print(f'== {lf}: A {len(sa)} signs, B {len(sb)} signs, matched {agree}')
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal': print(f'   {op:7s} A[{i1}:{i2}]={" ".join(sa[i1:i2])!r:30s} B[{j1}:{j2}]={" ".join(sb[j1:j2])!r}   ctxA ...{" ".join(sa[max(0,i1-4):i1])} | {" ".join(sa[i2:i2+3])}')
tA=sum(o[1] for o in out); tB=sum(o[2] for o in out); m=sum(o[3] for o in out)
print('TOTAL A',tA,'B',tB,'matched',m, 'agreement %.1f%% of B'%(100*m/tB))
