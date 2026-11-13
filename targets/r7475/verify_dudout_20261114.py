"""Independent decoder for r7475: majority letter per number from R7475_key.tsv only; cipher lines from R7475.txt;
compares with the gloss lines (letters only, clear Latin words and notes removed) by sequence alignment."""
import sys,re,difflib,collections,unicodedata
R=sys.argv[1]
key={}
for l in open(R+'/R7475_key.tsv'):
    f=l.rstrip('\n').split('\t')
    if not f[0].isdigit(): continue
    key[f[0]]=f[1].split('/')[0] if f[0]!='600' else '#'
lines=open(R+'/R7475.txt').read().split('\n')
pairs=[];cur=None
for l in lines:
    m=re.match(r'\s*(L\d+) C: (.*)',l)
    if m: cur=[m.group(1),m.group(2)]; continue
    m=re.match(r'\s*G: (.*)',l)
    if m and cur: pairs.append((cur[0],cur[1],m.group(1))); cur=None
def norm(s):
    s=s.lower().replace('ł','l').replace('ę','e').replace('ą','a').replace('ż','z').replace('ź','z').replace('ś','s').replace('ć','c').replace('ń','n').replace('ó','o').replace('v','u')
    return s
tot=match=0; nsign=0; mism=collections.Counter(); unk=collections.Counter(); bad=[]
for L,c,g in pairs:
    clear=[w.lower() for w in re.findall(r'"([^"]*)"',c)]
    c2=re.sub(r'"[^"]*"',' ',c)
    toks=re.findall(r'\[blot\]|\d+',c2)
    dec=''
    for t in toks:
        if t=='[blot]': dec+='?'; continue
        nsign+=1
        dec+=key.get(t,'?') if key.get(t)!='#' else ''
        if t not in key: unk[t]+=1
    gl=re.sub(r'\[[^\]]*\]','',g)
    gl=re.sub(r'\([^)]*\)','',gl)
    words=gl.split()
    # drop clear words
    cw=' '.join(clear).split()
    keep=[]
    for w in words:
        if w.lower() in cw: cw.remove(w.lower()); continue
        keep.append(w)
    gs=norm(''.join(re.sub(r'[^\w]','',w) for w in keep))
    ds=norm(dec)
    sm=difflib.SequenceMatcher(None,ds,gs,autojunk=False)
    m=sum(b.size for b in sm.get_matching_blocks())
    tot+=len(ds); match+=m
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal': bad.append((L,op,ds[i1:i2],gs[j1:j2]))
print('lines',len(pairs),'numbers',nsign,'decoded letters',tot,'agree with gloss',match,round(match/tot,4),'unkeyed',dict(unk))
for b in bad: print(*b)
