"""List every A/B disagreement with leaf, B line_y and sign index within that B line, plus context."""
import difflib, re
def load(fn):
    return [l.rstrip('\n').split('\t') for l in open(fn) if not l.startswith('#') and not l.startswith('leaf') and len(l.split('\t'))>=5]
def toks(s):
    s=re.sub(r'\[([^/\]]+)/[^\]]*\]',r'\1',s); return [t for t in s.split() if t]
A=load('passA_forward.tsv'); B=[r for r in load('passB_backward.tsv') if not r[2].startswith('x') and r[0] not in('19r','62r')][::-1]
leaves=[]
for r in A:
    if r[0] not in leaves: leaves.append(r[0])
n=0
for lf in leaves:
    a=[r for r in A if r[0]==lf]; b=sorted([r for r in B if r[0]==lf],key=lambda r:(float(r[1]),r[2].replace('(cont.)','0')))
    sa=[t for r in a for t in toks(r[4])]
    sb=[];pos=[]
    for r in b:
        for i,t in enumerate(toks(r[4])): sb.append(t); pos.append((r[1],r[2],i+1))
    sm=difflib.SequenceMatcher(None,sa,sb,autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        n+=1
        p=pos[j1] if j1<len(pos) else pos[-1]
        print(f"{n}\t{lf}\t{p[0]}\t{p[1]}\tsign{p[2]}\t{op}\tA={' '.join(sa[i1:i2]) or '-'}\tB={' '.join(sb[j1:j2]) or '-'}\tctxB={' '.join(sb[max(0,j1-3):j1])}|{' '.join(sb[j2:j2+3])}")
