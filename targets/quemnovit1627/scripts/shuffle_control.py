# shuffle_control.py: German character 4-gram score of each decode, against 5,000 keys made by shuffling the key's
# plain values over its signs, for seeds 20261112 and 7. Same model and stream as b97 scripts/dec_B.py.
#   python3 -I scripts/shuffle_control.py [CORPUS_DIR]      (default: ../adfgvx/corpus, the repository's German texts)
# Guard: each corpus file must carry exactly one 'Language: German' header, Gutenberg body markers, and > 1,000 words.
import os,sys,re,math,random,unicodedata,collections,json
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P=lambda *a: os.path.join(R,*a)
CD=sys.argv[1] if len(sys.argv)>1 else os.path.join(R,'..','adfgvx','corpus')
FILES=['de_21000','de_22367','de_2229','de_6079']
key={}
for l in open(P('key_B.txt')):
    if l.startswith('#'): continue
    for x in l.split(): a,b=x.split('='); key[a]=b
def norm(s):
    s=s.lower().replace('ß','ss'); s=unicodedata.normalize('NFD',s); s=''.join(ch for ch in s if unicodedata.category(ch)!='Mn')
    return re.sub(r'[^a-z]','',s).replace('v','u').replace('j','i')
cs=[]
for f in FILES:
    t=open(os.path.join(CD,f+'.txt'),encoding='utf8',errors='replace').read()
    assert re.findall(r'^Language: *(.+)$',t,re.M)==['German'],f
    i=t.find('*** START'); j=t.find('*** END'); assert 0<=i<j,f
    w=[x for x in (norm(x) for x in re.findall(r"[^\W\d_]+",t[i:j])) if x]; assert len(w)>1000,f
    print('corpus %s: header German asserted, %d words'%(f,len(w))); cs+=w
cs='#'.join(cs)
N=4; cnt=collections.Counter(cs[i:i+N] for i in range(len(cs)-N+1)); ctx=collections.Counter(cs[i:i+N-1] for i in range(len(cs)-N+1))
print('corpus chars',len(cs))
def lp(s):
    tot=0;k=0
    for i in range(len(s)-N+1):
        g=s[i:i+N]; tot+=math.log((cnt.get(g,0)+0.1)/(ctx.get(g[:-1],0)+2.7)); k+=1
    return tot/k
# cipher units of each transcription, in KEY_B labels; signs without a key value decode to '?' and are dropped
S={}
S['reader1']=[s.split('|')[1].replace('-','') for s in open(P('transcriptions','reader1_units.seg'),encoding='utf-8') if not s.startswith('#') and not s.split('|')[1].isdigit()]
M2={'N':'P','0':'H','z':'S','g':'q','y':'q','x':'k','u':'?'}
S['reader2']=[''.join(M2.get(c,c) for c in w) for l in open(P('transcriptions','reader2_blind.txt'),encoding='utf-8') if l.startswith('L') for w in l.split()[1:] if not w.startswith('#')]
S['reader3']=[''.join({'O':'H','S':'s'}.get(c,c) for c in u['cipher'] if c!='?') for u in json.load(open(P('decryptions','reader3_blind.json'),encoding='utf-8')) if not u['code']]
S['adjudicated']=[l.split('\t')[2] for l in open(P('transcriptions','adjudicated.tsv'),encoding='utf-8') if not l.startswith('#') and not l.split('\t')[2].isdigit()]
def dec1(u,k): return ''.join(k.get(c,'?') for c in u)
def stream(units,k): return '#'+'#'.join(dec1(u,k).replace('?','') for u in units)+'#'
syms=sorted(key); vals=[key[s] for s in syms]
for name,units in S.items():
    true=lp(stream(units,key))
    for seed in (20261112,7):
        random.seed(seed); ge=0; best=-9
        for _ in range(5000):
            v=vals[:]; random.shuffle(v); sc=lp(stream(units,dict(zip(syms,v)))); best=max(best,sc); ge+=sc>=true
        print('%-11s units %3d  true %.4f  seed %-8d shuffled keys at or above true: %d/5000  best shuffled %.4f'%(name,len(units),true,seed,ge,best))
