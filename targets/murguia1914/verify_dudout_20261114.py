import sys,re
R=sys.argv[1]
key={}
for l in open(R+'/key.tsv'):
    f=l.rstrip('\n').split('\t')
    if f[0].isdigit(): key[f[0]]=f[1]
pub={}
for l in open(R+'/decryption_LXVIII-1.14.1943.1.txt'):
    if re.match(r'S\d',l): s,t=l.split('\t')[:2]; pub[s]=t.strip()
n=0;bad=0
for l in open(R+'/transcription_LXVIII-1.14.1943.1.txt'):
    if not re.match(r'S\d',l): continue
    s,rest=l.rstrip('\n').split('\t'); g=rest.split('|')[1].strip().split('-')
    out=''
    for x in g:
        n+=1; v=key.get(x)
        if v is None or v=='?': out+='['+x+']'
        elif len(v)>2 and v not in ('rr','ll'): out+=v.upper()
        else: out+=v
    ok= out==pub[s]
    if not ok: bad+=1; print(s,'MINE',out,'PUB',pub[s])
print('segments',len(pub),'groups',n,'differing segments',bad)
