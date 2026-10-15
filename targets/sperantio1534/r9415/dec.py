import re,sys
KEY=dict(kv.split('=') for kv in open(sys.argv[2],encoding='utf8').read().split(','))
for l in open(sys.argv[1],encoding='utf8'):
    m=re.match(r'(\d\d) (.*)',l)
    if l.startswith('=='): print(l.strip()); continue
    if not m: continue
    s=m.group(2)
    out=re.sub(r'(\[[^\]]*\])|([^\[\]]+)',lambda x:x.group(1) or ''.join(KEY.get(c,'?') for c in x.group(2)),s)
    print(m.group(1),out)
    if len(sys.argv)>3: print('   ',re.sub(r'\[[^\]]*\]','|',s))
