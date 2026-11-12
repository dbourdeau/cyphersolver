# counts.py: every strict count in NOTES.md and counts.txt, recomputed from the files in this folder. Standard library only.
#   python3 -I scripts/counts.py
# Strict = S/(S+E+N): S a German word as decoded; E a code number, or reads only with one emendation / uncertain sign
# (reader 3: decodes fully but not a correct word); N not read. Each reader's labels are their own, made before any
# comparison; this script only checks the labels against the decodes and does the arithmetic.
import os,re,json,collections,difflib
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P=lambda *a: os.path.join(R,*a)
key={}
for l in open(P('key_B.txt')):
    if l.startswith('#'): continue
    for x in l.split(): a,b=x.split('='); key[a]=b
def pct(a,n): return '%d/%d = %.2f%%'%(a,n,100*a/n)
out=[]
# ---- reader 1 (b97, the breaker) ----
toks=[]
for l in open(P('transcriptions','reader1_frozen.txt'),encoding='utf-8'):
    if re.match(r'\d\d ',l): toks+=[(l[:2],t) for t in re.sub(r'<[^>]*>',' ',l[3:]).split()]
units=[];i=0
while i<len(toks):
    lid,t=toks[i]
    if t.endswith('-') and i+1<len(toks): units.append((lid,t+toks[i+1][1])); i+=2
    else: units.append((lid,t)); i+=1
units=[(l,u) for l,u in units if u not in('3000','20')]          # clear numerals, not cipher
segs=[l.rstrip('\n').split('|') for l in open(P('transcriptions','reader1_units.seg'),encoding='utf-8') if not l.startswith('#')]
assert [(s[0],s[1]) for s in segs]==units
c1=collections.Counter(); half=collections.defaultdict(collections.Counter)
for s in segs:
    d=s[1] if s[1].isdigit() else ''.join(key.get(ch,'?') for ch in s[1] if ch!='-')
    assert d==s[2],(s,d)
    c1[s[3]]+=1; half['01-10' if int(s[0])<=10 else '11-19'][s[3]]+=1
n1=sum(c1.values())
out.append('READER 1 (b97, breaker; tx md5 836d644f, frozen 02:18:36 UTC 12 Nov 2026)')
out.append('  units %d = S %d + E %d + N %d; strict %s  [filed on #450, now WITHDRAWN as the headline]'%(n1,c1['S'],c1['E'],c1['N'],pct(c1['S'],n1)))
for h in ('01-10','11-19'):
    m=sum(half[h].values()); out.append('  lines %s: %s'%(h,pct(half[h]['S'],m)))
A=[s for s in segs if int(s[0])<=10]; Bh=[s for s in segs if int(s[0])>10]
symsA=set(ch for s in A if not s[1].isdigit() for ch in s[1] if ch!='-')
rk={k:v for k,v in key.items() if k in symsA}
hS=sum(1 for s in Bh if not s[1].isdigit() and '?' not in ''.join(rk.get(ch,'?') for ch in s[1] if ch!='-') and s[3]=='S')
full=sum(1 for s in Bh if not s[1].isdigit() and '?' not in ''.join(rk.get(ch,'?') for ch in s[1] if ch!='-'))
words=sum(1 for s in Bh if not s[1].isdigit())
out.append('  held-out (key signs seen in lines 01-10 only, on lines 11-19): %d of %d cipher words decode in full; strict %s (not blind: key not fitted on 01-10 alone)'%(full,words,pct(hS,len(Bh))))
out.append('  key: %d signs with a value (%s); 1 sign (n) without'%(len(key),' '.join(sorted(key))))
# ---- reader 2 (b129, blind) ----
M2={'N':'P','0':'H','z':'S','g':'q','y':'q','x':'k','u':'?'}
dec2=[]
for l in open(P('transcriptions','reader2_blind.txt'),encoding='utf-8'):
    if l.startswith('L'):
        dec2+=[''.join(key.get(M2.get(c,c),'?') for c in w) for w in l.split()[1:] if not w.startswith('#')]
L2=[l.split() for l in open(P('transcriptions','reader2_labels.txt'),encoding='utf-8') if l.startswith('L')]
assert [w for _,w,_ in L2 if not w.isdigit()]==dec2
c2=collections.Counter(x[2] for x in L2); n2=len(L2)
out.append('READER 2 (b129, blind; tx frozen md5 de87c01d 09:49:43 UTC; label erratum md5 6e25e08b)')
out.append('  units %d = S %d + E %d + N %d; strict %s; S+E %s'%(n2,c2['S'],c2['E'],c2['N'],pct(c2['S'],n2),pct(c2['S']+c2['E'],n2)))
# E units that differ from reader 1's reading only by the look-alike classes q/g (d<->c) and pi/Z (g<->z)
r1S={}
for s in segs: r1S.setdefault(s[2],s[3])
cls=[]
def cl_only(x,y): return len(x)==len(y) and x!=y and all(p==q or (p,q) in(('d','c'),('g','z')) for p,q in zip(x,y))
used=set()
for ln,x,lb in L2:                       # same manuscript line, in order; reader 1's unit must be S
    if lb!='E': continue
    for k,s in enumerate(segs):
        if k in used or int(s[0])!=int(ln[1:]) or s[3]!='S': continue
        if cl_only(x,s[2]): cls.append((x,s[2])); used.add(k); break
out.append('  E units that differ from reader 1 only by the q/g or pi/Z sign class: %d (%s)'%(len(cls),', '.join('%s~%s'%c for c in cls)))
out.append('  if those were counted S: %s  [arithmetic only, as filed on #450]'%pct(c2['S']+len(cls),n2))
# ---- reader 3 (b137, blind) ----
U3=json.load(open(P('decryptions','reader3_blind.json'),encoding='utf-8'))
J3=[l.rstrip('\n').split('\t') for l in open(P('transcriptions','reader3_labels.tsv'),encoding='utf-8') if not l.startswith('# Rules')]
assert len(J3)==len(U3) and all(a['plain']==b[0] for a,b in zip(U3,J3))
for a,b in zip(U3,J3):
    if a['unmapped']: assert b[1]=='N'
    if a['code']: assert b[1]=='E'
c3=collections.Counter(b[1] for b in J3); n3=len(J3)
out.append('READER 3 (b137, blind; tx md5 6d642c8b frozen 11:22:40 UTC)')
out.append('  units %d = S %d + E %d + N %d (code units in E: %d); strict %s'%(n3,c3['S'],c3['E'],c3['N'],sum(a['code'] for a in U3),pct(c3['S'],n3)))
# ---- adjudicated (frozen before its one decode) ----
ad=[l.rstrip('\n').split('\t') for l in open(P('decryptions','adjudicated.txt'),encoding='utf-8') if not l.startswith('#')]
for col,name in ((4,'majority, >=2 of 3 readers per sign'),(7,'unanimous, all 3 readers per sign')):
    c=collections.Counter(r[col] for r in ad); n=len(ad)
    out.append('ADJUDICATED (%s; decoded once, 13:17:19 UTC): S %d + E %d + N %d = %d; strict %s'%(name,c['S'],c['E'],c['N'],n,pct(c['S'],n)))
open(P('checks','counts_strict.out'),'w').write('\n'.join(out)+'\n')
print('\n'.join(out))
# ---- sign occurrences in reader 1's cipher words (for key.tsv) ----
occ=collections.Counter(ch for s in segs if not s[1].isdigit() for ch in s[1] if ch!='-')
line='reader-1 sign occurrences (%d signs, %d tokens): %s'%(len(occ),sum(occ.values()),' '.join('%s:%d'%kv for kv in sorted(occ.items())))
print(line); open(P('checks','counts_strict.out'),'a').write(line+'\n')
