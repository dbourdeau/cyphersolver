"""Independent decoder for szembek1689: reads only key.tsv; tokens from runs.tsv col 2; compares with col 3 gloss."""
import sys,re
R=sys.argv[1]
key={}
for l in open(R+'/key.tsv'):
    if l.startswith('#') or not l.strip(): continue
    f=l.rstrip('\n').split('\t'); key[f[0]]=f[1]
n=same=0; diffs=[]; signs=0; unk=[]
for l in open(R+'/runs.tsv'):
    if l.startswith('#') or not l.strip(): continue
    f=l.rstrip('\n').split('\t'); fol,toks,gl=f[0],f[1],f[2]; note=f[3] if len(f)>3 else ''
    out=''
    for t in toks.split():
        if re.fullmatch(r'\d\d',t): out+=key.get(t,'?'); signs+=1; 
        elif re.fullmatch(r'\d{3}',t): out+='['+t+']'
        elif re.fullmatch(r'\d\??',t) or '?' in t: out+='{'+t+'}'; unk.append(t)
        else: out+=t
        if re.fullmatch(r'\d\d',t) and t not in key: unk.append(t)
    n+=1
    if out.lower()==gl.lower(): same+=1
    else: diffs.append((fol,toks,out,gl,note))
print('runs',n,'identical',same,'two-digit signs',signs,'unkeyed',unk)
for d in diffs: print(' | '.join(d))
