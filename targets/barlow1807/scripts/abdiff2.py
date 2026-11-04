"""Whole-page diff of number tokens, pass A vs pass B; each disagreement with A line number and context."""
import sys,re,difflib
def toks(text):
    out=[]
    for ln,line in enumerate([l for l in text.splitlines() if l.strip()],1):
        line=re.sub(r'^L\d+\s*','',line); line=re.sub(r'\[[^\]]*\]|\{[^}]*\}','',line)
        for t in re.findall(r'\d[\d?]*|[A-Za-z]+',line): out.append((t,ln))
    return out
for p in sys.argv[1].split(','):
    a=toks(open(f'trans_raw/p{p}_A.txt',encoding='utf8').read()); b=toks(open(f'trans_raw/p{p}_B.txt',encoding='utf8').read())
    sm=difflib.SequenceMatcher(None,[x[0] for x in a],[x[0] for x in b],autojunk=False)
    print('== page',p)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        ln=a[i1][1] if i1<len(a) else a[-1][1]
        ctx=' '.join(x[0] for x in a[max(0,i1-3):i1])
        print(f' L{ln:02d} ...{ctx} [A:{" ".join(x[0] for x in a[i1:i2])} | B:{" ".join(x[0] for x in b[j1:j2])}]')
