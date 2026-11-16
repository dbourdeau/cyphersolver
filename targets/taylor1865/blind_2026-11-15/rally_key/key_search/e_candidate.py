import sys, re, random, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from lib import *
KEY='RALLYTOTHEFRONT'; k=arr(KEY)
for r in readers('T11'):
    pair, frame, ti, _ = UNITS['T11']
    t=load(r); ks=[x for x in t if x[0]==frame]; rows=t[ks[ti]]
    pos=0; print('==',r)
    for row in rows:
        raw=row['group']; g=re.sub('[^A-Z]','',pref(raw).upper())
        c=arr(g); p=(c-k[(pos+np.arange(len(c)))%15])%26
        # alternatives
        alts=re.findall(r'\[([A-Z?])/([A-Z?])\]',raw.upper())
        altplain=''
        if alts:
            # decrypt with each alternative letter at its place
            s=raw.upper(); out=[]; j=0; i=0; letters=[]
            while i<len(s):
                if s[i]=='[':
                    m=re.match(r'\[([A-Z?])/([A-Z?])\]',s[i:]); letters.append((m.group(1),m.group(2))); i+=m.end()
                elif s[i].isalpha(): letters.append((s[i],None)); i+=1
                else: i+=1
            for li,(a,b) in enumerate(letters):
                if b and b!='?':
                    out.append(f"{a}->{b} at {li+1}: plain {txtof([(ord(b)-65-k[(pos+li)%15])%26])}")
            altplain='; '.join(out)
        print(f"{row['group_no']:>3} {g:<11} key {txtof(k[(pos+np.arange(len(c)))%15]):<11} plain {txtof(p):<11} {altplain}")
        pos+=len(c)
# score and controls on both readers: fixed key, 400 shuffles, and 400 random keys at all 15 offsets
rng=random.Random(1865)
for r in readers('T11'):
    c=arr(''.join(groups('T11',r)))
    s=float(qs((c-k[np.arange(len(c))%15])%26))
    sh=[]
    for t in range(400):
        l=list(c); rng.shuffle(l); l=np.array(l); sh.append(max(float(qs((l-k[(np.arange(len(l))+o)%15])%26)) for o in range(15)))
    print(r,'score',round(s,3),'shuffle max over 15 offsets',round(max(sh),3))
# other telegrams of the week at all offsets, both readers
for uid in ['T07','T08','T09','T10','S2']:
    for r in readers(uid):
        c=arr(''.join(groups(uid,r)))
        b=max((float(qs((c-k[(np.arange(len(c))+o)%15])%26)),o) for o in range(15))
        print(uid,r,'RALLYTOTHEFRONT best',round(b[0],3),'offset',b[1],txtof((c-k[(np.arange(len(c))+b[1])%15])%26)[:50])
