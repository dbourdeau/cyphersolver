import re,sys,collections,json
P='/home/claude/siblings/gerlach1252/p124_137/'
# decode rows
rows={}
for l in open(P+'BLIND_all.tsv',encoding='utf-8'):
    f=l.rstrip('\n').split('\t')
    if f[0]=='page':continue
    rows[(f[0],f[1])]=f[2]
key={}
for l in open(P+'key_frozen.tsv',encoding='utf-8'):
    if l.startswith('#') or l.startswith('letter') or not l.strip():continue
    f=l.rstrip('\n').split('\t');key[f[1]]=f[0]
def labs(toks):
    out=[]
    for t in re.findall(r"\{[^}]*\}|\[[^\]]*\]|\S+",toks):
        if t in {',','=','.',';',':'} or t.startswith('{'):continue
        if t=='#' or t.startswith('['): out.append(('#',None));continue
        q=t.endswith('?');lab=t.rstrip('?')
        out.append((lab,key.get(lab)))
    return out
J=[]
for l in open(P+'judge/judge.tsv',encoding='utf-8'):
    f=l.rstrip('\n').split('\t')
    if f[0]=='page':continue
    J.append(f)
stat=collections.defaultdict(lambda:[0,0,0])
errs=[]
bad=0
for f in J:
    pg,ln,rd=f[0],f[1],f[2]
    toks=rows[(pg,ln)]
    L=labs(toks)
    # judge units
    units=[]
    i=0
    while i<len(rd):
        c=rd[i]
        if c=='[':
            j=rd.index(']',i);units.append(('E',rd[i+1:j]));i=j+1
        elif c=='{':
            j=rd.index('}',i);units.append(('N',rd[i+1:j]));i=j+1
        elif c.isalpha():units.append(('S',c));i+=1
        elif c in '#_':units.append(('N',c));i+=1
        else:i+=1
    # expand multi-letter units of one bracket? each bracket one letter usually
    if len(units)!=len(L):
        bad+=1;print('MISMATCH',pg,ln,len(units),len(L),rd,'|',toks,file=sys.stderr);continue
    words=re.sub(r'\[|\]|\{|\}','',rd)
    for (k,v),(lab,let) in zip(units,L):
        stat[lab][{'S':0,'E':1,'N':2}[k]]+=1
        if k=='E':errs.append((pg,ln,lab,let,v,rd))
print('mismatch rows',bad,file=sys.stderr)
for lab,(s,e,n) in sorted(stat.items(),key=lambda x:-x[1][1]):
    print(f"{lab}\t{key.get(lab)}\tS{s}\tE{e}\tN{n}")
json.dump(errs,open('errs.json','w'))
