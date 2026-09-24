import re,sys,glob
key={}
for f in sorted(glob.glob('key1743/decode_*.tsv')):
    for line in open(f,encoding='utf-8'):
        p=line.rstrip('\n').split('\t')
        if len(p)>=2 and p[0].strip().isdigit(): key[int(p[0])]=p[1].strip()
src=sys.argv[1] if len(sys.argv)>1 else 'cipher1743_feb26.txt'
for line in open(src,encoding='utf-8'):
    line=line.rstrip()
    if not line or line.startswith('#'): print(line); continue
    toks=[t for t in re.split(r'[.\s]+',line) if t]
    out=[]
    for t in toks:
        if t.isdigit(): out.append(key.get(int(t),'<%s>'%t) or '<%s:blank>'%t)
        else: out.append('<%s>'%t)
    print(line); print('   ', ' | '.join(out))
