"""Mechanical decode of a transcription with Harumi-Matsuba's key.tsv (Daniel's target key for f. 120).
Single letters lower case, word signs =WORD, polyphones (a|b), unvalued [?name]."""
import re, sys
key={}
for l in open(sys.argv[1],encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)<2 or p[0].startswith('# '): continue
    key[p[0]]=p[1]
for raw in open(sys.argv[2],encoding='utf-8'):
    m=re.match(r'^(\w\d\d)( [R-])?:\s*(.*)$',raw.rstrip('\n'))
    if not m: continue
    out=[]; toks=m.group(3).split(); i=0
    while i<len(toks):
        t=toks[i]
        if t.startswith('^('):
            j=i
            while not toks[j].endswith(')'): j+=1
            i=j+1; continue
        if t.startswith('{') or t=='//' and False: i+=1; continue
        v=key.get(t.rstrip('?'))
        if v is None or v=='?': out.append('[?'+t+']')
        elif '|' in v: out.append('('+v+')')
        elif len(v)==1: out.append(v)
        else: out.append('='+v.upper())
        i+=1
    print(m.group(1), ' '.join(out))
