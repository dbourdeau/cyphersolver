import re,collections,sys
def up():
    pg=None;out=collections.defaultdict(list)
    for l in open('up_transcription.txt',encoding='utf-8'):
        m=re.match(r'### p\.(\d+)',l)
        if m: pg=int(m.group(1));continue
        m=re.match(r'L\d+: (.*)',l)
        if m and pg: out[pg].append(m.group(1))
    return out
def new():
    out=collections.defaultdict(list)
    for l in open('/home/claude/siblings/gerlach1252/p124_137/BLIND_all.tsv',encoding='utf-8'):
        f=l.rstrip('\n').split('\t')
        if f[0]=='page':continue
        out[int(f[0])].append(f[2])
    return out
def words(lines):
    s=' '.join(lines).replace('=','')
    ws=[]
    for w in re.split(r'\s[,;:.]\s?|\s[,;:.]$',s):
        t=[x.rstrip('?') for x in w.split() if x not in ',;:.']
        if t: ws.append(tuple(t))
    return ws
U=up();N=new()
labs=['4L','4R','4U','PHI','OL','ARW','G','SIG','DQ','HRT','MM','FL','FL2','PI','HB','S3','ST2','THE','DEL']
for name,D in [('up pp.7-19',{k:v for k,v in U.items() if k<=19}),('up partial',{k:v for k,v in U.items() if k>19}),('new 124-137',N)]:
    c=collections.Counter();tot=0
    for p,ls in D.items():
        for l in ls:
            for t in l.split():
                t=t.rstrip('?')
                if re.match(r'^[A-Z0-9]+$',t): c[t]+=1;tot+=1
    print(name,'signs',tot)
    print('  '+'  '.join(f"{x}:{c[x]}({100*c[x]/tot:.1f}%)" for x in labs))
    # 'und' forms: 3-sign words ending X DQ / H SIG etc
    wc=collections.Counter(w for p,ls in D.items() for w in words(ls) if len(w)==3 and w[1] in('X','H') and w[2] in ('DQ','SIG'))
    print('  und-like:',wc.most_common(8))
