# align.py: sign alignment of the three transcriptions of the 'Quem novit' letter, and the agreement figures.
# Standard library only. Run from anywhere:  python3 -I scripts/align.py
# Writes alignment/*.tsv and prints the agreement figures. It does not decode anything.
import os,re,difflib,collections
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=lambda *a: os.path.join(R,*a)
T1=P('transcriptions','reader1_frozen.txt'); T2=P('transcriptions','reader2_blind.txt'); T3=P('transcriptions','reader3_blind.txt')

# ---- parsers -------------------------------------------------------------
def r1_lines():                      # line -> concatenated cipher signs (clear German <..>, numerals, hyphens removed)
    d={}
    for l in open(T1,encoding='utf-8'):
        m=re.match(r'^(\d\d) (.*)',l)
        if not m: continue
        b=re.sub(r'<[^>]*>',' ',m.group(2)); b=re.sub(r'\d+',' ',b).replace('-','')
        d[int(m.group(1))]=''.join(b.split())
    return d
def r1_words():                      # b129 compare.py convention: words, hyphen halves kept as separate words
    out=[]
    for l in open(T1,encoding='utf-8'):
        if not re.match(r'\d\d ',l): continue
        for w in re.sub(r'<[^>]*>',' ',l[3:]).split():
            w=w.strip('-')
            if w and not w.isdigit(): out.append(w)
    return out
def r2_lines():
    d={}
    for l in open(T2,encoding='utf-8'):
        m=re.match(r'^L(\d\d) (.*)',l)
        if m: d[int(m.group(1))]=''.join(w for w in m.group(2).split() if not w.startswith('#'))
    return d
def r2_words():
    return [w for l in open(T2,encoding='utf-8') if l.startswith('L') for w in l.split()[1:] if not w.startswith('#')]
def r3_lines():
    d={}
    for l in open(T3,encoding='utf-8'):
        if not l.startswith('L'): continue
        n,b=l.split(':',1); b=re.sub(r'\[[^\]]*\]',' ',b)
        ws=[w.replace('?','').rstrip('.') for w in b.split()]
        d[int(n[1:])]=''.join(w for w in ws if w and w!='H')
    return d
def tr(s,m): return ''.join(m.get(c,c) for c in s)

# ---- A. reader 2 vs reader 1, method of b129 scripts/compare.py (word-level difflib, then sign-level) ----
M2={'N':'P','0':'H','z':'S','g':'q','y':'q','x':'k','u':'?'}      # reader 2 MAPPING.md, frozen before decoding
def b129_compare(collapse):
    mine=r2_words(); th=r1_words()
    mm=[tr(w,M2) for w in mine]
    tt=[w.replace('L','l') for w in th]
    if collapse: tt=[w.replace('g','q').replace('Z','P').replace('n','P') for w in tt]
    agree=tot=0
    for op,a1,a2,b1,b2 in difflib.SequenceMatcher(None,mm,tt,autojunk=False).get_opcodes():
        if op=='equal':
            n=sum(len(w) for w in mm[a1:a2]); agree+=n; tot+=n; continue
        A=mm[a1:a2]; Bw=tt[b1:b2]
        if len(A)==len(Bw):
            for x,y in zip(A,Bw):
                for o,i1,i2,j1,j2 in difflib.SequenceMatcher(None,x,y,autojunk=False).get_opcodes():
                    if o=='equal': agree+=i2-i1; tot+=i2-i1
                    else: tot+=max(i2-i1,j2-j1)
        else: tot+=max(sum(map(len,A)),sum(map(len,Bw)))
    return agree,tot,len(mine),len(th)

# ---- B. reader 3 vs readers 1 and 2, method of b137 scripts/compare.py (line-level difflib, matched blocks) ----
R3_FROM_R1={'H':'O','S':'Z','Z':'n','s':'S'}            # declared by b137 before running (into reader-3 symbols)
R3_FROM_R2={'0':'O','z':'Z','s':'S','N':'n','g':'q','y':'g'}
COLL={'g':'G','q':'G','y':'G','P':'N','n':'N','c':'C','e':'C','L':'L','l':'L'}
def b137_agree(a,b):
    ta=tb=match=0
    for k in sorted(a):
        x=a[k]; y=b.get(k,'')
        match+=sum(bl.size for bl in difflib.SequenceMatcher(None,x,y,autojunk=False).get_matching_blocks()); ta+=len(x); tb+=len(y)
    return match,ta,tb

# ---- C. three-way alignment in reader-1 frame, all in KEY_B label space ----
# Value-identical KEY_B labels merged for comparison only: L and l (both s), S and h (both k). No other merging.
MERGE={'L':'l','h':'S'}
M3={'P':'P','O':'H','S':'s','Z':'Z','g':'g','q':'q','c':'c','e':'e','d':'d','L':'L','l':'l','a':'a','b':'b','f':'f','h':'h',
    'i':'i','k':'k','m':'m','o':'o','p':'p','r':'r','t':'t'}          # reader 3 MAPPING.md as frozen; n, y, R, E, x, u, c-cedilla, in-word H -> '?' (unmapped)
def kb1(s): return tr(s,MERGE)
def kb2(s): return tr(tr(s,M2),MERGE)
def kb3(s): return tr(''.join(M3.get(c,'?') for c in s),MERGE)
def per_pos(x,y):
    """for each position of x: the aligned sign of y (None if no 1:1 partner); and insertions of y before position i"""
    al=[None]*len(x); ins=collections.defaultdict(str)
    for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,x,y,autojunk=False).get_opcodes():
        if op in('equal',) or (op=='replace' and i2-i1==j2-j1):
            for k in range(i2-i1): al[i1+k]=y[j1+k]
        elif op=='insert': ins[i1]+=y[j1:j2]
    return al,ins
def three_way():
    L1=r1_lines(); L2=r2_lines(); L3=r3_lines()
    rows=[]
    for ln in sorted(L1):
        x=kb1(L1[ln]); y=kb2(L2.get(ln,'')); z=kb3(L3.get(ln,''))
        a2,i2=per_pos(x,y); a3,i3=per_pos(x,z)
        for p in range(len(x)+1):
            ins2=i2.get(p,''); ins3=i3.get(p,'')
            if ins2 or ins3: rows.append((ln,p,'+',ins2 or '-',ins3 or '-'))
            if p<len(x): rows.append((ln,p,x[p],a2[p] or '-',a3[p] or '-'))
    return rows,L1

if __name__=='__main__':
    os.makedirs(P('alignment'),exist_ok=True)
    out=[]
    a,t,n2,n1=b129_compare(False); out.append('A1 reader2 vs reader1 (b129 method): words %d vs %d; agree %d of %d = %.2f%%'%(n2,n1,a,t,100*a/t))
    a,t,_,_=b129_compare(True);   out.append('A2 same, q/g and pi/Z/n collapsed: agree %d of %d = %.2f%%'%(a,t,100*a/t))
    M3l={k:v for k,v in ((l,s) for l,s in r3_lines().items())}
    A=r1_lines(); Bl=r2_lines()
    for tag,o,coll in (('B1 reader3 vs reader1, strict',{k:tr(v,R3_FROM_R1) for k,v in A.items()},False),
                       ('B2 reader3 vs reader2, strict',{k:tr(v,R3_FROM_R2) for k,v in Bl.items()},False),
                       ('B3 reader3 vs reader1, look-alikes collapsed',{k:tr(v,R3_FROM_R1) for k,v in A.items()},True),
                       ('B4 reader3 vs reader2, look-alikes collapsed',{k:tr(v,R3_FROM_R2) for k,v in Bl.items()},True)):
        mine={k:(tr(v,COLL) if coll else v) for k,v in M3l.items()}; oth={k:(tr(v,COLL) if coll else v) for k,v in o.items()}
        m,ta,tb=b137_agree(mine,oth)
        out.append('%s (b137 method): matched %d; reader3 %d; other %d; %d/%d = %.2f%% of reader3; %d/%d = %.2f%% of other'%(tag,m,ta,tb,m,ta,100*m/ta,m,tb,100*m/tb))
    rows,L1=three_way()
    with open(P('alignment','three_way_signs.tsv'),'w',encoding='utf-8') as f:
        f.write('# line\tpos\treader1\treader2\treader3   (KEY_B labels; L->l and h->S merged as value-identical; ? = unmapped sign; - = no 1:1 partner; + = insertion before pos)\n')
        for r in rows: f.write('%02d\t%d\t%s\t%s\t%s\n'%r)
    sig=[r for r in rows if r[2]!='+']
    c=collections.Counter()
    for r in sig:
        a,b,d=r[2],r[3],r[4]
        c['r1r2']+=a==b; c['r1r3']+=a==d; c['r2r3']+=(b==d and b not in '-?'); c['all3']+=(a==b==d); c['maj']+=(a==b or a==d or (b==d and b not in '-?'))
    n=len(sig)
    out.append('C three-way in reader-1 frame, KEY_B space: reader-1 signs %d; R1=R2 %d (%.2f%%); R1=R3 %d (%.2f%%); R2=R3 %d (%.2f%%); all three %d (%.2f%%); at least two agree %d (%.2f%%); insertion rows %d'%(
        n,c['r1r2'],100*c['r1r2']/n,c['r1r3'],100*c['r1r3']/n,c['r2r3'],100*c['r2r3']/n,c['all3'],100*c['all3']/n,c['maj'],100*c['maj']/n,len(rows)-n))
    open(P('alignment','agreement.txt'),'w').write('\n'.join(out)+'\n')
    print('\n'.join(out))
