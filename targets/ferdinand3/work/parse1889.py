import re,collections,sys
src=open('../decode/DOC_R1889_D3605_3605.txt',encoding='utf8').read()
lines=[l for l in src.splitlines() if l and not l.startswith('#')]
toks=[];odd=[]
for l in lines:
    l=re.sub(r'<CLEARTEXT[^>]*>',' | ',l)
    for g in re.split(r'\s{2,}',l.strip()):
        g=g.strip()
        if not g: continue
        if g=='|': toks.append('|'); continue
        chars=g.split(' ')
        buf=''
        out=[]
        for c in chars:
            if c.isdigit() or c.rstrip('?').isdigit():
                buf+=c.rstrip('?')
            else:
                if buf: out.append(buf); buf=''
                out.append(c)
        if buf: out.append(buf)
        for o in out:
            if o.isdigit() and len(o)>2: odd.append(o)
            toks.append(o)
print(' '.join(toks))
c=collections.Counter(t for t in toks if t not in '|.')
print(len([t for t in toks if t not in '|.;:-=()']), len(c))
print(c.most_common())
print('odd',odd)
