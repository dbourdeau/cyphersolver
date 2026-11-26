import re
W='/home/claude/keyless/ostermann1737/'
MN="V b W U C w + y 8 4 2 3 5 9 v T a p n r F D A G e l q Y o x X L Z".split()
LAB={'S%02d'%(i+1):m for i,m in enumerate(MN)}
def load(lines=None, keepq=True):
    out=[]
    for l in open(W+'TRANSCRIPTION.tsv').read().split('\n')[1:]:
        if not l: continue
        p,ln,t=l.split('\t'); ln=int(ln)
        if lines and ln not in lines: continue
        t=re.sub(r'\{[^}]*\}','',t)
        words=[]
        for g in t.split('|'):
            w=[]
            for k in g.split():
                if k=='[...]': w.append('?')
                else: w.append(LAB[k.rstrip('?')])
            if w: words.append(w)
        out.append((ln,words))
    return out
TRAIN=set(range(1,17)); HELD={17,18,19,20}
