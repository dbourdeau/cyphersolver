import re,sys,json
sys.path.insert(0,'work')
k=json.load(open(sys.argv[1]))
want=sys.argv[2:]
CODE={'b u r':'TT','b o r':'SS','b a r':'RR','m u r':'LL','F r':'CC','Q u a n':'<QUAN>','u l i r':'<ULIR>','i m a':'<IMA>','s e d':'<SED>','L u s':'<LUS>'}
stream=[];lab=[]
for f in ['c15r','c15v','c16r']:
    for ln in open(f'cc15_16/transcription_{f}_pass2.txt',encoding='utf8'):
        if ln.startswith('#') or ' ' not in ln.strip():continue
        l,rest=ln.split(' ',1)
        rest=re.sub(r'\[[^\]]*\]',' ~ ',rest)
        o=[]
        for x in rest.split():
            if x in('_8','_9'):
                if o:o.pop()
                continue
            o.append(x)
        s=' '+' '.join(o)+' '
        s=s.replace(' e r ',' ER ')
        for c,v in CODE.items():s=s.replace(' '+c+' ',' '+v+' ')
        for x in s.split():stream.append(x);lab.append(l)
def p(x):
    if x=='~':return '/'
    if x in CODE.values():return x
    return k.get(x,'?'+x+'?')
for w in want:
    print('==',w,k.get(w))
    for i,x in enumerate(stream):
        if x==w:
            a=''.join(p(y) for y in stream[max(0,i-7):i]);b=''.join(p(y) for y in stream[i+1:i+8])
            print(f'  {lab[i]:4} {a:>16} [{w}] {b}')
