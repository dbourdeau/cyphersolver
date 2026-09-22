import re,sys
KEY={}
for kv in open(sys.argv[2],encoding='utf8').read().split():
    k,v=kv.split('=',1) if not kv.startswith('==') else ('=',kv[2:])
    KEY[k]=v
show=len(sys.argv)>3
for l in open(sys.argv[1],encoding='utf8'):
    if l.startswith('=='): print(l.strip()); continue
    m=re.match(r'(\d\d) (.*)',l)
    if not m: continue
    s=re.sub(r'\{[^}]*\}','',m.group(2)).replace('o/','0')
    out=re.sub(r'(\[[^\]]*\])|([^\[\]]+)',lambda x:x.group(1) or ''.join(KEY.get(c,'?') for c in x.group(2)),s)
    print(m.group(1),out)
    if show: print('  ',s)
