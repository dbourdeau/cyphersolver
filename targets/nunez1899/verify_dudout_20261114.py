import sys,re
R=sys.argv[1]
key={}
for l in open(R+'/key.tsv'):
    if l.startswith('#') or l.startswith('code\t') or not l.strip(): continue
    f=l.rstrip('\n').split('\t'); key[f[0]]=(f[1],f[2] if len(f)>2 else '')
pub={l.split(' ',1)[0]:l.split(' ',1)[1].strip() for l in open(R+'/decryption_9926.txt') if re.match(r'L\d\d ',l)}
tr={l.split(' ',1)[0]:l.split(' ',1)[1].strip() for l in open(R+'/transcription_9926.txt') if re.match(r'L\d\d ',l)}
nw=nc=bad=0; holes=0
for L,t in tr.items():
    out=[]
    ws=t.split(); i=0
    while i<len(ws):
        w=ws[i]; i+=1; nw+=1
        if i<len(ws) and w+' '+ws[i] in key: w=w+' '+ws[i]; i+=1; nw+=1
        if w in key:
            nc+=1; v,b=key[w]
            if b=='hole' or not v: out.append('[...]'); holes+=1
            else: out.append(v.upper())
        else: out.append(w)
    o=' '.join(out)
    if o!=pub.get(L): bad+=1; print(L,'MINE',o,'| PUB',pub.get(L))
from collections import Counter
print('lines',len(tr),'words',nw,'code words',nc,'holes',holes,'differing lines',bad)
print(Counter(b for v,b in key.values()))
