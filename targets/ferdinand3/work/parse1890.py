import re,collections
src=open('../decode/DOC_R1890_D3604_3604.txt',encoding='utf8').read()
lines=[l for l in src.splitlines() if l and not l.startswith('#')]
toks=[]
for l in lines:
    if l.startswith('<CLEARTEXT'): 
        if toks and toks[-1]!='|': toks.append('|')
        continue
    l=re.sub(r'<CLEARTEXT[^>]*>',' | ',l)
    for g in re.split(r'\s{2,}',l.strip()):
        g=g.replace(' ','').strip()
        if g: toks.append(g)
    toks.append('/')
if __name__=='__main__':
    print(' '.join(toks))
    c=collections.Counter(t for t in toks if t not in '|/')
    print(sum(c.values()),len(c)); print(c.most_common())
