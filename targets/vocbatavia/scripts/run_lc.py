import sys, random
sys.path.insert(0,'/home/claude/hunts40/G3/M4/trackB/scripts')
import score as S
W,_=S.wordlist()
NAMES={'jan','ian','john','iohn','ioan','pieter','willem','jacob','thomas','london','londen','engelant','engelandt','bantam','batavia','amsterdam','suratte','malacca','iapan','japan'}
NAMES={S.norm(x) for x in NAMES}
key={}
for l in open(sys.argv[1]).read().splitlines()[1:]:
    c,p,_=l.split('\t'); key[c]=p.split('/')[0]
words=sys.argv[2].split(',')
def dec(w,k): return ''.join(k.get(ch,'?') for ch in w.lower())
def ok(d): return '?' not in d and (S.norm(d) in W or S.norm(d) in NAMES)
def sc(ws,k): return sum(ok(dec(w,k)) for w in ws)
real=sc(words,key); L=sum(len(w) for w in words); kc=sum(1 for w in words for ch in w.lower() if ch in key)
for w in words: print(w, dec(w,key), 'READ' if ok(dec(w,key)) else '-')
print(f'letters keyed {kc}/{L} = {100*kc/L:.2f}%'); print(f'FIGURE OF RECORD: {real}/{len(words)} = {100*real/len(words):.2f}%')
ks=sorted(key); vs=[key[k] for k in ks]
for seed in (20261112,7):
    r=random.Random(seed); ge=mx=0
    for _ in range(5000):
        v=vs[:]; r.shuffle(v); s=sc(words,dict(zip(ks,v))); ge+=s>=real; mx=max(mx,s)
    print(f'key shuffle seed {seed}: >= real {ge}/5000; max {mx}')
letters=[ch for w in words for ch in w.lower()]; lens=[len(w) for w in words]
for seed in (20261112,7):
    r=random.Random(seed); ge=mx=0
    for _ in range(5000):
        x=letters[:]; r.shuffle(x); ws=[]; i=0
        for n in lens: ws.append(''.join(x[i:i+n])); i+=n
        s=sc(ws,key); ge+=s>=real; mx=max(mx,s)
    print(f'matched control (letters shuffled) seed {seed}: >= real {ge}/5000; max {mx}')
