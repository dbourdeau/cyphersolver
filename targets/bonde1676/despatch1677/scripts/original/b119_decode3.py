import sys,re
# decode3.py key file : tiers A/B/F/P = frozen letter values (lowercase); C = weak EM guess (UPPER); W/U/unknown = <n>; cut = [~]
key={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    g,s,t=l.rstrip('\n').split('\t'); key[g]=(s,t)
for l in open(sys.argv[2],encoding='utf-8'):
    m=re.match(r'(R\d+):\s*(.*)',l)
    if not m: continue
    out=[]
    for part in re.findall(r'"[^"]*"|\S+',m.group(2)):
        if part.startswith('"'): out.append(' «'+part.strip('"')+'» '); continue
        if part.endswith('~'): out.append('[~]'); continue
        if part not in key: out.append('<%s>'%part); continue
        s,t=key[part]
        out.append(s if t in 'ABFPQTGH' else (s.upper() if t=='C' else '<%s>'%part))
    print(m.group(1),''.join(out))
