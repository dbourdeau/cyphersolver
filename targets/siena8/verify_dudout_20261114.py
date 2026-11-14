import json,sys,re
R=sys.argv[1]
k=json.load(open(R+'/key.json'))
key={}
for lab,v in k.items():
    code=lab.split(' (')[0]
    key[code]=v if isinstance(v,str) else '/'.join(v)
toks=open(R+'/transcripts/no08.tok').read().split('\n')
pub=[l.split('cipher:')[1].strip() for l in open(R+'/texts/no08_decryption.txt') if 'cipher:' in l]
n=0
for line,p in zip([t for t in toks if t.strip()],pub):
    out=''
    for t in line.split():
        n+=1; v=key.get(t,'?')
        out+= '['+v+']' if len(v)>3 and '/' not in v else (v.split('/')[0] if t!='9' else '{'+v+'}')
    cmp=re.sub(r'\{u/v/b\}','u',out)
    print(len(line.split()),cmp==p.replace('[duca di Milano]','[duca di Milano]') or (cmp.lower()==p.lower()),'\n mine:',out,'\n pub :',p)
print('signs',n,'distinct',len(set(' '.join(toks).split())))
