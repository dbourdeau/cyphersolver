import sys,re
key={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    g,s,t=l.rstrip('\n').split('\t'); key[g]=(s,t)
for l in open(sys.argv[2],encoding='utf-8'):
    m=re.match(r'([RrLl]\d+):\s*(.*)',l)
    if not m: continue
    out=[]
    for part in re.findall(r'"[^"]*"|\S+',m.group(2)):
        if part.startswith('"'): out.append(' «'+part.strip('"')+'» '); continue
        cut=part.endswith('~'); g=re.sub(r'[^0-9]','',part)
        if cut or not g: out.append('[~]'); continue
        if g not in key: out.append('<%s>'%g); continue
        s,t=key[g]
        out.append(s if t in 'ABF' else ('<%s>'%g if t in 'UW' else ('' if t=='N' else s.upper())))
    print(m.group(1),''.join(out))
