# Doc 627 control shuffle (copied from blind633/shuffle.py; only the input changed), same as blind/shuffle.py (dictionary cover, 5,000 shuffles at seeds 20261112 and 7).
# Word list: wordlist_ariosto_dante.txt, sha256 b88a189459bb..., not in this repository (contributor working folder); key and decode paths are absolute paths of the contributor machine.
import json,csv,re,random
k=json.load(open('/home/claude/wt_cv/targets/corsi1513/key_corsi_w17_frozen.json'))
W=set(w.strip().lower() for w in open('wordlist_ariosto_dante.txt',encoding='utf-8',errors='ignore') if len(w.strip())>=3)
ML=max(map(len,W))
txt=open('/home/claude/corsi627_control/decode_once.txt').read().split('# key tokens')[1].split('#')[0]
L={'C':[l.split('\t',1)[1].split() for l in txt.strip().splitlines() if '\t' in l]}
def dec(t,bare,base,vow,num):
    t=t.rstrip('?')
    if t in ('.',''): return ''
    if t.startswith('#') or t in num: return ''
    if t in bare: return bare[t]
    m=re.match(r'^(.+?)(\d)$',t)
    if m and m.group(1) in base and m.group(2) in vow: return base[m.group(1)]+vow[m.group(2)]
    return '#'
def cover(s):
    n=len(s);b=[0]*(n+1)
    for i in range(1,n+1):
        b[i]=b[i-1]
        for l in range(3,min(ML,i)+1):
            if s[i-l:i] in W: b[i]=max(b[i],b[i-l]+l)
    return b[n],n
def score(letter,bare,base,vow,num):
    c=t=0
    for toks in L[letter]:
        s=''.join(dec(x,bare,base,vow,num) for x in toks); a,b_=cover(s); c+=a;t+=b_
    return c/t
for letter in 'C':
    real=score(letter,k['bare'],k['base'],k['vowel'],k['num']); print(letter,'real',round(real,4))
    for seed in (20261112,7):
        r=random.Random(seed); ge=0; mx=0
        bk=list(k['bare']); bv=list(k['bare'].values()); sk=list(k['base']); sv=list(k['base'].values()); vk=list(k['vowel']); vv=list(k['vowel'].values())
        for _ in range(5000):
            a=bv[:];r.shuffle(a); b=sv[:];r.shuffle(b); c=vv[:];r.shuffle(c)
            sc=score(letter,dict(zip(bk,a)),dict(zip(sk,b)),dict(zip(vk,c)),k['num'])
            mx=max(mx,sc); ge+=sc>=real
        print(letter,'seed',seed,'>=real',ge,'/5000 max',round(mx,4))
