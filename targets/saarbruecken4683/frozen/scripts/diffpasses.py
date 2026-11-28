import sys,re,difflib
def load(p):
    L={}
    for l in open(p,encoding='utf-8'):
        m=re.match(r'(29\d[rv]) L(\d+) \| (.*)',l.strip())
        if m: L[(m.group(1),int(m.group(2)))]=m.group(3)
    return L
def nums(s):
    s=re.sub(r'\{[^}]*\}',' W ',s); s=re.sub(r'\[[^\]]*\]',' ',s)
    return [t for t in s.split() if re.match(r'^(\d+\??|\?\?|W)$',t)]
A=load(sys.argv[1]);B=load(sys.argv[2])
nd=0
for k in sorted(set(A)|set(B)):
    a=nums(A.get(k,''));b=nums(B.get(k,''))
    aa=[x.rstrip('?') for x in a if x!='W'];bb=[x.rstrip('?') for x in b if x!='W']
    if aa!=bb:
        nd+=1; print(k[0],k[1],'\n A:',' '.join(a),'\n B:',' '.join(b))
print('lignes en désaccord',nd)
