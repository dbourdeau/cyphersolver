import json,sys,re
K=json.load(open(sys.argv[1]))
for line in open(sys.argv[2]):
    line=line.rstrip('\n')
    m=re.match(r'^(\S+?)([TGC]?)\s(.*)$',line)
    if not m or line.startswith('#'): continue
    lid,tag,rest=m.groups()
    if tag in('T',):continue
    if tag=='G': print(lid,'G',rest);continue
    out=[]
    for g in rest.split():
        if g=='|': out.append('|');continue
        v=re.sub(r'[^0-9]','',g)
        if not v: continue
        if int(v)<100: out.append('.');continue
        k=K.get(v) or K.get(str(int(v)))
        out.append(k[0] if k and k[0] else '‹%s›'%v)
    print(lid,'D',' '.join(out))
