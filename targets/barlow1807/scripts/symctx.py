import sys,collections
sys.path.insert(0,'scripts'); from parse import words
key=dict(l.split('=') for l in open(sys.argv[1]).read().split())
ctx=collections.defaultdict(list)
for p in sys.argv[2].split(','):
    for k,v in words(open(f'trans_final/p{p}.txt',encoding='utf8').read()):
        if k=='C':
            for i,t in enumerate(v):
                d=''.join((key.get(x,'?').upper() if j==i else key.get(x,'?')) for j,x in enumerate(v))
                ctx[t].append(d)
for t in sorted(ctx,key=lambda x:(len(x),x)):
    print(t,key.get(t,'?'),len(ctx[t]),' '.join(ctx[t][:14]))
