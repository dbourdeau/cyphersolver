import sys,json,re
key=json.load(open(sys.argv[1]))
tot=unk=0
for line in open(sys.argv[2],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip() or line.startswith('#'): print(line); continue
    tag,_,body=line.partition('|')
    out=[]
    for tok in body.split():
        if tok.startswith('['):   # clear text in brackets
            out.append(' '+tok.strip('[]').replace('_',' ')+' '); continue
        doubt=tok.endswith('?'); t=tok.rstrip('?')
        tot+=1
        if t in key['num']: p=key['num'][t]
        elif re.fullmatch(r'[A-Za-z]\d',t) and t[0] in key['base'] and t[1] in key['vowel']: p=key['base'][t[0]]+key['vowel'][t[1]]
        elif t in key['bare']: p=key['bare'][t]
        else: p='<'+t+'>'; unk+=1
        out.append(p+('?' if doubt else ''))
    print(tag+'|'+'-'.join(out))
print(f"# tokens {tot} unknown-by-key {unk} decoded {100*(tot-unk)/max(tot,1):.1f}%",file=sys.stderr)
