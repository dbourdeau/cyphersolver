"""Score the blind Dec 17 control against the separate clear text (M31/14/40-45), and compare key-fit rates across letters."""
import re,json,difflib,csv,collections
W='sources/raw/morris_reversal_wave_2026-10-30/';D='sources/raw/morris_dec17_1813_alignment_2026-10-24/'
K={int(e['code']):(e['historical_reading'] or '') for e in json.load(open('sources/raw/historical1385_review_2026-10-27/historical1385_reference.json'))['entries']}
mp=lambda m:100*(15-(m-1)//100)+(m-100*((m-1)//100))
norm=lambda s:re.sub(r'[^a-z]','',s.lower()).replace('v','u').replace('j','i')
truth=open(D+'historical_plaintext_reading_A.txt').read()
tw=[norm(x) for x in truth.split() if norm(x)]
b=open(W+'control_dec17/blind_reading_plain.txt').read()
# tokenise: inferred, holes, plain
toks=re.findall(r'\[\?[^\]]+\]|\[[^\]]*\]|[A-Za-z\']+',b)
seq=[];kind=[]
for t in toks:
    if t.startswith('[?'):
        for w in t[2:-1].split():seq.append(norm(w));kind.append('I')
    elif t.startswith('['):seq.append('#'+str(len(seq)));kind.append('H')
    else:seq.append(norm(t));kind.append('W')
sm=difflib.SequenceMatcher(None,seq,tw,autojunk=False)
ok=[False]*len(seq)
for m in sm.get_matching_blocks():
    for i in range(m.a,m.a+m.size):ok[i]=True
c=collections.Counter()
for k,o in zip(kind,ok):c[(k,o)]+=1
print('blind words:',dict(c));print('truth words',len(tw))
print('inferred wrong:',[s for s,k,o in zip(seq,kind,ok) if k=='I' and not o])
print('inferred right:',[s for s,k,o in zip(seq,kind,ok) if k=='I' and o])
# key fit by letter: A spans
rows=list(csv.DictReader(open(D+'A_span_harvest.tsv'),delimiter='\t'));print(list(rows[0].keys())[:10])
tc='codes';pc='plaintext'
e=f=n=0;miss=[]
for r in rows:
    t=[int(x) for x in re.findall(r'\d+',r[tc])]
    if not t or not all(1<=x<=1600 for x in t):continue
    g=''.join(norm(K[mp(x)]) for x in t);p=norm(r[pc]);n+=1
    if g==p:e+=1
    elif difflib.SequenceMatcher(None,g,p).ratio()>=.75:f+=1
    else:miss.append((r[tc],r[pc],[K[mp(x)] for x in t]))
print('Dec17 A spans: n',n,'exact',e,'loose',f,'miss',len(miss));print(miss[:30])

# numeric-only scoring: mask writer's uncoded prose
lit=open(D+'literal_reviewed_v4.txt').read()
pl=[norm(x) for c in re.findall(r'\[([A-Za-z_\-]+)\]',lit) for x in c.replace('-','_').split('_') if norm(x)]
def mask(a):
    s=difflib.SequenceMatcher(None,a,pl,autojunk=False);m=[False]*len(a)
    for b in s.get_matching_blocks():
        if b.size>=2:
            for i in range(b.a,b.a+b.size):m[i]=True
    return m
ms=mask(seq);mt=mask(tw)
print('plain-chunk words',len(pl),'truth coded words',mt.count(False),'of',len(tw))
c=collections.Counter()
for k,o,x in zip(kind,ok,ms):
    if not x:c[(k,o)]+=1
print('blind coded-part tokens:',dict(c))
sm2=difflib.SequenceMatcher(None,seq,tw,autojunk=False);cov=0
for b in sm2.get_matching_blocks():
    for j in range(b.b,b.b+b.size):
        if not mt[j]:cov+=1
print('truth coded words recovered in order',cov,'of',mt.count(False),round(cov/mt.count(False),3))
