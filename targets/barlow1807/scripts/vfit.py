"""Dictionary fit allowing omitted vowels: a decoded cipher word fits if some English word reduces to it by deleting
vowels (a e i o u y). Greedy hill-climb of single symbols to maximise fitted letters. Prints suggested changes only."""
import sys,re,collections
sys.path.insert(0,'scripts'); from parse import words
V=set('aeiou')
corp=open('corpus/federalist.txt',encoding='utf8').read().lower()
vocab={w for w,c in collections.Counter(re.findall('[a-z]+',corp)).items() if c>=1 and len(w)>1}
vocab|=set(open('corpus/extra_words.txt').read().split())
sk=collections.defaultdict(list)
for w in vocab: sk[''.join(c for c in w if c not in V)].append(w)
def issub(d,w):
    it=iter(w); return all(c in it for c in d)
def fits(d):
    if not d or '?' in d: return False
    for w in sk.get(''.join(c for c in d if c not in V),()):
        if len(w)>=len(d) and issub(d,w): return True
    return False
key=dict(l.split('=') for l in open(sys.argv[1]).read().split())
cw=[]
for p in sys.argv[2].split(','):
    for k,v in words(open(f'trans_raw/p{p}_A.txt',encoding='utf8').read()):
        if k=='C' and all(len(t)<=3 for t in v): cw.append(v)
def score(key): return sum(len(w) for w in cw if fits(''.join(key.get(t,'?') for t in w)))
base=score(key); tot=sum(len(w) for w in cw); print('fit letters',base,'of',tot)
syms=sorted({t for w in cw for t in w})
for rnd in range(3):
    improved=False
    for s in syms:
        best=(score(key),key.get(s,'?'))
        for c in 'abcdefghijklmnopqrstuvwxyz':
            old=key.get(s); key[s]=c; sc=score(key)
            if sc>best[0]: best=(sc,c)
            if old is None: del key[s]
            else: key[s]=old
        if best[1]!=key.get(s,'?'):
            print('change',s,key.get(s,'?'),'->',best[1],best[0]); key[s]=best[1]; improved=True
    if not improved: break
open(sys.argv[3],'w').write('\n'.join(f'{k}={v}' for k,v in sorted(key.items(),key=lambda x:(len(x[0]),x[0]))))
unf=[''.join(key.get(t,'?') for t in w) for w in cw if not fits(''.join(key.get(t,'?') for t in w))]
print('unfit',len(unf),' '.join(unf))
