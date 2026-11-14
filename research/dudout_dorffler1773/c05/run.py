import json,random,re,hashlib,os
T=json.load(open(os.environ['INPUT_DIR']+'/TABLE.json')); T={k:v for k,v in T.items() if not k.startswith('_')}
LEX=set(w.strip().lower() for w in open(os.environ['INPUT_DIR']+'/LEXICON.txt') if w.strip())
lines=[(l.split(':',1)[0],l.split(':',1)[1].split()) for l in open('T-C05.txt') if not l.startswith('#')]
def tokenize(tab):
    words=[];dec=[]
    for lab,gs in lines:
        cur='';out=[]
        for g in gs:
            if g in('?','|') or g not in tab or int(g)>=146:
                if cur: words.append(cur);cur=''
                if g=='|': out.append('|');continue
                if g=='?': out.append('?');continue
                if g not in tab: out.append(f'[{g}]');continue
                words.append(tab[g]); out.append(tab[g].upper() if int(g)>=146 else tab[g]); continue
            cur+=tab[g]; out.append(tab[g])
        if cur: words.append(cur)
        dec.append(f"{lab}: "+' '.join(out))
    return words,dec
def W(tab):
    w=[x.lower() for x in tokenize(tab)[0]]; w3=[x for x in w if len(re.sub('[^a-zäöüß]','',x))>=3]
    return sum(x in LEX for x in w3)/len(w3) if w3 else 0, len(w3), sum(x in LEX for x in w3)
import sys
if sys.argv[1]=='decode':
    words,dec=tokenize(T); open('D-C05.txt','w').write('\n'.join(dec)+'\n')
elif sys.argv[1]=='measure':
    w,n,h=W(T); print(f'W = {w:.4f} ({h}/{n} words len>=3 in LEXICON)')
    keys=list(T); vals=list(T.values()); cs=[]
    for s in range(200):
        v=vals[:]; random.Random(s).shuffle(v); cs.append(W(dict(zip(keys,v)))[0])
    mx=max(cs); mn=sum(cs)/len(cs); print(f'controls: max={mx:.4f} mean={mn:.4f}')
    ng=sum(g not in('?','|') for _,gs in lines for g in gs)
    print('groups transcribed (readable):',ng)
    c1=w>=0.55; c2=w>=mx+0.25; c3=ng>=150
    print('W>=0.55:',c1,' W>=max+0.25:',c2,' >=150 groups:',c3); print('VERDICT:','PASS' if c1 and c2 and c3 else 'FAIL')
