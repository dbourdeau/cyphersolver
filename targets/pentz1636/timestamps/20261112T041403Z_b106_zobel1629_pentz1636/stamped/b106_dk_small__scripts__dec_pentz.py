import sys,re,math,random,unicodedata,collections
tx=sys.argv[1]; corp=sys.argv[2:]
AL="abcdefghiklmnopqrstuwxyz"
T1={37-i:AL[i] for i in range(9)}; T1.update({14+i:AL[9+i] for i in range(15)})
T2={38+i:AL[i] for i in range(9)}; T2.update({61:'n',60:'o',57:'r',56:'s',54:'u'})
toks=[]
for l in open(tx,encoding='utf8'):
    if not re.match(r'\d\d ',l): continue
    for t in re.sub(r'<[^>]*>',' | ',l[3:]).split(): toks.append((l[:2],t))
# words: split at dots, clear text and codes; table set by 62 / 13
units=[];cur=[];tab=None;curtab=None
def flush():
    global cur
    if cur: units.append(('W',curtab,cur)); cur=[]
i=0
while i<len(toks):
    lid,t=toks[i]
    if t in('.','|'):
        # a dot inside ein.n.ga.ngk and a line break do not end a word unless followed by a new word; word ends are set in SEG below
        cur.append(t); i+=1; continue
    cur.append(t); i+=1
stream=cur
# explicit segmentation (word ends chosen by sense; listed in full so the count can be checked by hand)
SEG=[("62","I"),("64","C"),("34 33 17","1"),("226x","C"),("13","I"),("12","C"),("41 46 42","2"),("168","C"),("13","I"),("56 38 40 45 42","2"),
("62","I"),("63","C"),("36 33 21 30 24 21 33 17","1"),("25 18 25 33 17","1"),("62","I"),("33 29 17 29 31 33","1"),("21 33 37 15 33","1"),
("34 29 33 17 22 23 33","1"),("22 25 33 21","1"),("28 24 33 21 30 37 15 23 33 17","1"),("22 33 29 17","1"),("226","C"),("62","I"),("29 17","1"),
("29? 33 21 19 33 23 24 24 16","1"),("8","C"),("9","C"),("32 29 25","X"),("85","C"),("62","I"),("33 29 17 31 37 17 31 14","1"),("34 29 22 33 16","1"),
("62","I"),("34 29 33","1"),("168","C"),("13","I"),("12","C"),("43 57 46 41 42 57 46 40 54 56","2"),("62","I"),("34 29 33 17 22 23 33","1"),
("13","I"),("11","C"),("41 42 57 54 60 61","2"),("168","C")]
flat=[t for t in stream if t not in('.','|')]
assert flat==[x for s,_ in SEG for x in s.split()], 'segmentation does not match the frozen figures'
EXP={"wowen":"E","?erpetuum":"E"}
def dec(seg,T1,T2):
    out=[]
    for s,k in seg:
        if k in'12': out.append(''.join(({'1':T1,'2':T2}[k]).get(int(x),'?') if x.isdigit() else '?' for x in s.split()))
    return out
tally=collections.Counter(); words=[]
for s,k in SEG:
    if k=='I': print('  index',s); continue
    if k=='C': tally['E']+=1; print('E code',s); continue
    if k=='X': tally['N']+=1; print('N unread',s,'(table 1 would give',''.join(T1[int(x)] for x in s.split())+')'); continue
    d=dec([(s,k)],T1,T2)[0]; c=EXP.get(d,'S'); assert c=='E' or '?' not in d
    tally[c]+=1; words.append(d); print(c,'table',k,s,'=',d)
n=sum(tally.values()); print('units',n,dict(tally),'strict %d/%d = %.2f%%'%(tally['S'],n,100*tally['S']/n))
lw=tally['S']+2+1; print('letter words only: %d S of %d = %.2f%%'%(tally['S'],lw,100*tally['S']/lw))
if not corp: sys.exit()
def norm(s):
    s=s.lower().replace('ß','ss'); s=unicodedata.normalize('NFD',s); s=''.join(ch for ch in s if unicodedata.category(ch)!='Mn')
    return re.sub(r'[^a-z]','',s).replace('v','u').replace('j','i')
cs=[]
for f in corp:
    t=open(f,encoding='utf8',errors='replace').read()
    assert re.search(r'^Language: German',t,re.M),f
    i=t.find('*** START'); j=t.find('*** END'); assert 0<i<j; cs+=[norm(w) for w in re.findall(r"[^\W\d_]+",t[i:j])]
cs='#'.join(w for w in cs if w)
N=4; cnt=collections.Counter(cs[i:i+N] for i in range(len(cs)-N+1)); ctx=collections.Counter(cs[i:i+N-1] for i in range(len(cs)-N+1))
def lp(ws):
    s='#'+'#'.join(w.replace('?','') for w in ws)+'#'; tot=0;m=0
    for i in range(len(s)-N+1):
        g=s[i:i+N]; tot+=math.log((cnt.get(g,0)+0.1)/(ctx.get(g[:-1],0)+2.7)); m+=1
    return tot/m
true=lp(dec(SEG,T1,T2)); print('corpus chars',len(cs),'true score %.4f'%true)
random.seed(20261112); ge=0;best=-99
for _ in range(5000):
    a=dict(zip(sorted(T1),random.sample(list(T1.values()),len(T1)))); b=dict(zip(sorted(T2),random.sample(list(T2.values()),len(T2))))
    sc=lp(dec(SEG,a,b)); best=max(best,sc); ge+=sc>=true
print('shuffled keys at or above true: %d/5000 (best %.4f)'%(ge,best))
