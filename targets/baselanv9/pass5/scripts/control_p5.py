"""Shuffle controls, pass 5 (python3 -I). (a) key shuffle as in pass 3, on KEY_V5.tsv and every pass-4 text; (b) ciphertext shuffle: the real key on the signs of each text shuffled across its word slots (word lengths kept), 5,000 per seed, real text ranked. The checks were done with AI tools and no person checked each record by hand.
Pass 3 docstring: Own code. The values of the 73 single-sign tokens of KEY_V5.tsv are permuted among the tokens (pairs, word forms, marks and
rules C1-C5 unchanged); 5,000 keys per seed; each decodes the frozen transcriptions with the frozen decoder. Statistic: mean log10 probability per character
under a Latin letter 4-gram model (add-0.01 smoothing, alphabet a-z + space) trained on la-latlib-letters.txt (sha256 asserted). Per section and per rim."""
import sys,re,random,math,hashlib,statistics,collections
R=sys.argv[1].rstrip('/')+'/'; sys.path.insert(0,R+'scripts')
import decode_p5 as d
C='/home/claude/keyless/_cs/lang/corpora/la-latlib-letters.txt'
raw=open(C,'rb').read(); assert hashlib.sha256(raw).hexdigest().startswith('c0299efd2c769384')
t=re.sub('[^a-z]+',' ',raw.decode('utf-8','ignore').lower().replace('v','u').replace('j','i'))
c4=collections.Counter(t[i:i+4] for i in range(len(t)-3)); c3=collections.Counter(t[i:i+3] for i in range(len(t)-2))
def lp(s):
    s='   '+re.sub(' +',' ',s.strip())+' '
    if len(s)<5: return -9.0
    tot=0
    for i in range(3,len(s)): tot+=math.log10((c4[s[i-3:i+1]]+0.01)/(c3[s[i-3:i]]+0.27))
    return tot/(len(s)-3)
def clean(x): return re.sub('[^a-z ]','',x.replace('[?]',' ').replace('~','').replace('=','').replace('u','u').replace('v','u').replace('j','i'))
K=d.load_key(R+'KEY_V5.tsv'); toks=sorted(K)
U=[]
for sec,f in [('TRAIN f4r','tx/f004r.txt'),('TRAIN f4v','tx/f004v.txt'),('H1r','tx/f015r_H1r.txt'),('H2','tx/f159r.txt'),('H3','tx/f034r_p34.txt'),('H4','tx/f025r_H4.txt'),('S1','tx/PENT_S1_v4.txt'),('S2','tx/PENT_S2_v4.txt'),('S2i','tx/S2_INNER_v5.txt'),('F54','tx/F054R_v5.txt'),('F97','tx/F097_v5.txt')]:
    for ln in open(R+f,encoding='utf-8'):
        if ln.startswith('#') or '\t' not in ln: continue
        lid,txt=ln.rstrip('\n').split('\t'); U.append((sec,lid,[w.split() for w in txt.split(' / ') if w.split() and w.split()!=['Fill']]))
def units(key,UU=None):
    r={}
    for sec,lid,ws in (UU or U):
        s=clean(' '.join(d.decode_word(w,key)[0] for w in ws))
        r.setdefault(sec,[]).append(s)
        if sec in('S1','S2','S2i','F54','F97'): r[lid]=[s]
    return {k:lp(' '.join(v)) for k,v in r.items()}
real=units(K); out=['# control pass 5 (a) key shuffle: %d tokens permuted; model la 4-gram own; statistic log10 p per char'%len(toks)]
for seed in (20261112,7):
    rnd=random.Random(seed); acc={k:[] for k in real}
    for _ in range(5000):
        vals=[K[x] for x in toks]; rnd.shuffle(vals)
        sc=units(dict(zip(toks,vals)))
        for k in real: acc[k].append(sc[k])
    for k in real:
        a=acc[k]; mu=statistics.mean(a); sd=statistics.pstdev(a); ge=sum(1 for x in a if x>=real[k])
        out.append('seed %d\t%s\treal %.3f\tshuffle mean %.3f sd %.3f best %.3f\tz %.1f\tshuffles>=real %d/5000'%(seed,k,real[k],mu,sd,max(a),(real[k]-mu)/sd,ge))

out.append('# (b) ciphertext shuffle: signs of each text permuted across its word slots, real key')
for seed in (20261112,7):
    rnd=random.Random(seed); acc={k:[] for k in real}
    for _ in range(5000):
        UU=[]; bysec={}
        for sec,lid,ws in U: bysec.setdefault(sec,[]).extend(x for w in ws for x in w)
        for sec in bysec: rnd.shuffle(bysec[sec])
        pos={sec:0 for sec in bysec}
        for sec,lid,ws in U:
            nw=[]
            for w in ws: nw.append(bysec[sec][pos[sec]:pos[sec]+len(w)]); pos[sec]+=len(w)
            UU.append((sec,lid,nw))
        sc=units(K,UU)
        for k in real: acc[k].append(sc[k])
    for k in real:
        a=acc[k]; mu=statistics.mean(a); sd=statistics.pstdev(a); ge=sum(1 for x in a if x>=real[k])
        out.append('seed %d\t%s\treal %.3f\tshuffle mean %.3f sd %.3f best %.3f\tz %.1f\tshuffled-ciphertext>=real %d/5000 (rank of real %d of 5001)'%(seed,k,real[k],mu,sd,max(a),(real[k]-mu)/sd,ge,ge+1))
open(R+'CONTROL_P5.txt','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
