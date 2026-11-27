import re, sys, difflib, json
RAW='/home/claude/voc_blind/raw/'
OURS='/home/claude/cs_fresh/targets/vocbatavia/letters/1623_1634/T1623_transcription.txt'
MART='/home/claude/hunts40/G3/M4/martin1696/transcription_v1.txt'
out=[]
def P(*a): out.append(' '.join(str(x) for x in a))

def parse_pkg_1623(path):
    rows=[]; marg=None
    for ln in open(path,encoding='utf-8'):
        ln=ln.rstrip('\n')
        m=re.match(r'^(M?\d\d)[:\t]\s*(.*)$',ln)
        if not m: continue
        if m.group(1).startswith('M'): marg=(m.group(1),m.group(2)); continue
        rows.append((m.group(1),m.group(2)))
    def toks(row,s):
        t=[]; pos=0
        for piece in re.findall(r'\[illeg\]|\d+\[\?\]|\d+\[illeg\]|\d+|/|×|=',s):
            if piece=='/': t.append(('/',row,None)); continue
            if piece in '×=': t.append((piece,row,None)); continue
            pos+=1
            if piece=='[illeg]': v='ILLEG'
            elif piece.endswith('[illeg]'): v=piece[:-7]+'~'   # partial: digits seen, rest illegible
            elif piece.endswith('[?]'): v=piece[:-3]+'?'
            else: v=piece
            t.append((v,row,pos))
        return t
    seq=[]
    for row,s in rows:
        tt=toks(row,s)
        for x in tt:
            if x[0]=='×' and marg:
                seq.extend(y for y in toks(marg[0],marg[1]) if y[0] not in '×=')
            elif x[0] in '×=': continue
            else: seq.append(x)
    return seq

def parse_ours(block):
    for ln in open(OURS,encoding='utf-8'):
        if ln.startswith(block+' |'):
            s=re.sub(r'\[[^\]]*\]','',ln.split('|',1)[1])
            seq=[]; w=1
            for p in re.findall(r'\{\d+\}|\d+|/',s):
                if p=='/': seq.append(('/',w)); w+=1
                elif p.startswith('{'): seq.append((p[1:-1]+'{}',w))
                else: seq.append((p,w))
            return seq

def base(v): return v.rstrip('?{}~')
def compare(name,pkg,ours):
    pg=[x for x in pkg if x[0]!='/']; og=[x for x in ours if x[0]!='/']
    # divider positions as 'divider after group i'
    def divs(seq):
        d=set(); i=0
        for x in seq:
            if x[0]=='/':
                if i>0: d.add(i)
            else: i+=1
        return d
    P(f'== {name}: package groups (cipher tokens incl. [illeg]) = {len(pg)}; our groups = {len(og)}')
    a=[base(x[0]) if x[0]!='ILLEG' else 'ILLEG' for x in pg]; b=[base(x[0]) for x in og]
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    exact=0; flagged_eq=0; dis=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal':
            for k in range(i2-i1):
                pv=pg[i1+k][0]; ov=og[j1+k][0]
                if pv==base(pv) and ov==base(ov): exact+=1
                else: flagged_eq+=1; dis.append(('agree-but-flagged',pg[i1+k],og[j1+k]))
        else:
            dis.append((tag,pg[i1:i2],og[j1:j2]))
    agree=exact+flagged_eq
    P(f'   same value: {agree}/{len(og)} = {100*agree/len(og):.1f}% of our groups (of which {flagged_eq} carry a doubt flag on one side: [?], [illeg]-partial, or our {{}} gutter fill from inv. 1079)')
    P(f'   clean agreement (no flag either side): {exact}/{len(og)} = {100*exact/len(og):.1f}%')
    dp,do=divs(pkg),divs(ours)
    P(f'   word dividers: package {len(dp)}, ours {len(do)}, same position {len(dp&do)}; package only after group# {sorted(dp-do)}; ours only after group# {sorted(do-dp)}')
    for d in dis:
        if d[0]=='agree-but-flagged':
            P(f'   - flagged-agree: package row {d[1][1]} pos {d[1][2]} "{d[1][0]}" ~ ours word {d[2][1]} "{d[2][0]}"')
        else:
            P(f'   - {d[0]}: package {[(x[0],"row"+x[1],"pos"+str(x[2])) for x in d[1]]} vs ours {[(x[0],"word"+str(x[1])) for x in d[2]]}')
    return dict(pkg=len(pg),ours=len(og),agree=agree,exact=exact)

res={}
for page,block in [('VOC-1080-0376.txt','A'),('VOC-1080-0380.txt','B')]:
    res[page]=compare(f'{page} vs our T1623 block {block}',parse_pkg_1623(RAW+page),parse_ours(block))
# extras not in our block
for page in ['VOC-1080-0376.txt','VOC-1080-0380.txt']:
    ex=[l.rstrip() for l in open(RAW+page,encoding='utf-8') if re.match(r'^(B:|P-)',l)]
    P(f'   extras in {page} outside the cipher lines (not in our block): {ex}')

# Martin 0038 line by line
def pm(path):
    d={}
    for ln in open(path,encoding='utf-8'):
        m=re.match(r'^(\d\d)\t(.*)$',ln.rstrip('\n'))
        if not m: continue
        s=m.group(2)
        s=re.sub(r'<sup>[^<]*</sup>','',s).replace('<rule/>','')
        t=[]
        for tok in [x for x in s.split(':') if x.strip() and x.strip()!='.']:
            tok=tok.strip(); ov='<over>' in tok
            tok=re.sub(r'</?over>','',tok)
            q=tok.endswith('[?]'); tok=tok.replace('[?]','')
            for sub in tok.split():   # '321[?]34' style handled below
                t.append((sub,ov,q))
        d['L'+m.group(1)]=t
    return d
def om(path):
    d={}
    for ln in open(path,encoding='utf-8'):
        m=re.match(r'^(L\d\d): (.*)$',ln.rstrip('\n'))
        if m: d[m.group(1)]=[(x.rstrip("'?"),"'" in x,'?' in x) for x in m.group(2).split()]
    return d
pk=pm(RAW+'VOC-1575-0038.txt'); ou=om(MART)
tot=sum(len(v) for v in ou.values()); totp=sum(len(v) for v in pk.values())
eq=0; oveq=0; ovn=0; dl=[]
for L in sorted(ou):
    a=[x[0] for x in pk.get(L,[])]; b=[x[0] for x in ou[L]]
    # map package 'L' letter-sign to our 'P' for comparison only
    an=['P' if x=='L' else x for x in a]
    sm=difflib.SequenceMatcher(None,an,b,autojunk=False)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal':
            eq+=i2-i1
            for k in range(i2-i1):
                ovn+=1; oveq+= pk[L][i1+k][1]==ou[L][j1+k][1]
                if pk[L][i1+k][1]!=ou[L][j1+k][1]: dl.append(f'{L} pos{j1+k+1} "{b[j1+k]}": overbar package={pk[L][i1+k][1]} ours={ou[L][j1+k][1]}')
        else: dl.append(f'{L} {tag}: package {a[i1:i2]} (pos {i1+1}-{i2}) vs ours {b[j1:j2]} (pos {j1+1}-{j2})')
P(f'== VOC-1575-0038.txt vs our martin1696 transcription_v1 (frozen), line by line (package letter sign "L" compared as our "P")')
P(f'   tokens: package {totp}, ours {tot}; same value {eq}/{tot} = {100*eq/tot:.1f}%; overbar agrees on {oveq}/{ovn} matched tokens = {100*oveq/ovn:.1f}%')
for x in dl: P('   - '+x)
open('/home/claude/voc_blind/alignment/alignment_output.txt','w').write('\n'.join(out)+'\n')
print('\n'.join(out))
