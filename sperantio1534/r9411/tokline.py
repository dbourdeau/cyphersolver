import re,sys
key=dict(kv.split('=',1) for kv in open(sys.argv[1],encoding='utf8').readline().split())
dflt={'n':'b/o','4':'e/i','E':'d/c'}
for l in open(sys.argv[2],encoding='utf8'):
    m=re.match(r'(\d+) (.*)',l)
    if m and m.group(1) in sys.argv[3].split(','):
        print(m.group(1),' '.join(f"{t}:{key.get(t,dflt.get(t,'?'))}" for t in m.group(2).split() if not t.startswith('{')))
