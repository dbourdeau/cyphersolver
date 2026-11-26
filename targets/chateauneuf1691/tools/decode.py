import sys,json,re
key=json.load(open(sys.argv[1])); src=sys.argv[2]
for l in open(src,encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('# LETTER'): print('\n'+l); continue
    if not re.match(r'^\d{4}\|',l): continue
    a=l.split('|',3); out=[]
    for part in re.split(r'(\{[^}]*\})',a[3]):
        if part.startswith('{'): out.append(part); continue
        for t in part.split():
            m=re.match(r'^(\d+)',t)
            if not m or '###' in t: out.append('‹?›'); continue
            v=key.get(m.group(1)); out.append(v.upper() if v else '‹%s›'%m.group(1))
    print(a[0],a[1],a[2],' '.join(out))
