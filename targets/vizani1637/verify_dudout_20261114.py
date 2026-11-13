import json,sys,re,unicodedata
R=sys.argv[1]
k=json.load(open(R+'/key.json'))
inv={}
for v,signs in k['key']:
    for s in signs: inv[s]=v.split(' / ')[0]
signs=sorted(inv,key=len,reverse=True)
def seg(w):
    out=[];i=0
    while i<len(w):
        for s in signs:
            if w.startswith(s,i): out.append(s); i+=len(s); break
        else:
            m=re.match(r'\d+',w[i:])
            if m: out.append(m.group()); i+=len(m.group())
            else: out.append('<'+w[i]+'>'); i+=1
    return out
n=agree=0;nsig=0;rows=[]
for l in open(R+'/cipher_words.tsv'):
    if l.startswith('#') or not l.strip(): continue
    f=l.rstrip('\n').split('\t'); w,p=f[0],f[1]; flag=f[2] if len(f)>2 else ''
    s=seg(w); 
    dec=''.join(inv.get(x,'['+x+']' if x.isdigit() else x) for x in s)
    nsig+=sum(1 for x in s if not x.isdigit())
    pn=re.sub(r"[^a-z\[\]0-9?]","",p.lower().replace('é','e').replace('è','e').replace('v','u'))
    ok= dec==pn
    n+=1; agree+=ok
    if not ok: rows.append((w,' '.join(s),dec,p,flag))
print('words',n,'agree',agree,'signs',nsig)
for r in rows: print(' | '.join(r))
