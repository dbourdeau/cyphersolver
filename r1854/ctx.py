import sys
key=dict(l.strip().rsplit('=',1) for l in open(sys.argv[1],encoding='utf-8') if '=' in l)
toks=[t for l in open(sys.argv[2],encoding='utf-8') if l.startswith('L') for t in l.split(':',1)[1].split()]
for s in sys.argv[3:]:
    print('==',s,key.get(s))
    for i,t in enumerate(toks):
        if t==s:
            f=lambda y: '|' if y=='_' else ('' if key.get(y)=='_' else key.get(y,'?'))
            print('  ',''.join(f(y) for y in toks[max(0,i-8):i]),'['+key.get(s,'?')+']',''.join(f(y) for y in toks[i+1:i+9]))
