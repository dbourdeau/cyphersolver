import sys; sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from common import *
def passages(path):
    rows=read_gloss(path)
    lines=[]; g=None
    for img,side,ln,kind,txt in rows:
        if kind=='G': g=txt
        elif kind=='N':
            lines.append(((img,side,ln), '' if (g is None or g.strip().startswith('(none)')) else g, txt)); g=None
    # build passages: break where a brace occurs inside/at ends
    P=[]; cur_n=[]; cur_g=''; refs=[]
    def flush():
        nonlocal cur_n,cur_g,refs
        if cur_n: P.append((refs,cur_n,cur_g))
        cur_n=[];cur_g='';refs=[]
    for ref,g,n in lines:
        toks=tok_numbers(n)
        starts_brk = toks and toks[0]=='BRK'
        if starts_brk: flush()
        refs.append(ref); cur_g+=' '+g
        for t in toks:
            if t=='BRK': continue
            cur_n.append(t)
        if toks and toks[-1]=='BRK': flush()
    flush()
    return P
if __name__=='__main__':
    P=passages(sys.argv[1])
    for refs,n,g in P: print(refs[0],len(n),len(norm(g)),g[:80])
