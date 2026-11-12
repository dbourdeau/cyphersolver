import sys,re,difflib
def norm(path,ours):
    out={}
    for l in open(path):
        if l.startswith('#') or not l.strip(): continue
        lab,body=l.split(' ',1)
        if ours:
            body=re.sub(r'\[([^/\]]+)/[^\]]*\]',r'\1',body).replace('^','')
            toks=re.findall(r'<[^>]+>|.',body.strip()); toks=[t.strip('<>') for t in toks if t.strip()]
        else:
            toks=[]
            for w in body.split():
                if re.fullmatch(r'\d+|L\^.*',w): toks.append(w)
                else: toks+=list(w)
        out[lab]=toks
    return out
a=norm(sys.argv[1],True); b=norm(sys.argv[2],False)
tot=agree=0; diffs=[]
for lab in a:
    x,y=a[lab],b.get(lab,[])
    sm=difflib.SequenceMatcher(None,x,y,autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        n=max(i2-i1,j2-j1); tot+=n
        if op=='equal': agree+=n
        else: diffs.append((lab,op,''.join(x[i1:i2]) if all(len(t)==1 for t in x[i1:i2]) else ' '.join(x[i1:i2]),' '.join(y[j1:j2])))
print(f'aligned positions {tot}, agree {agree} ({agree/tot:.1%}), differ {tot-agree}')
for d in diffs: print(*d,sep='\t')
