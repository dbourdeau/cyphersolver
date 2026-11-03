import re,collections,math,random
def load(f):
    L=[]
    for ln in open(f,encoding='utf8'):
        if ln.startswith('#'):continue
        ln=re.sub(r'\[[^\]]*\]',' ',ln.split(' ',1)[1]);ln=re.sub(r'\(blot\)','|',ln)
        L.append(ln)
    return re.sub(r'[^0-9|?]','', ''.join(L))
a=load('cc48/transcription_c48_pass1.txt');b=load('cc49_50/transcription_c49r_pass1.txt')
print('c48 digits',sum(c.isdigit() for c in a),'c49',sum(c.isdigit() for c in b))
def clean(s):return re.split(r'[|?]+',s)
parts=clean(a)+clean(b);D=''.join(parts)
print('single digit freq',sorted(collections.Counter(D).items(),key=lambda x:-x[1]))
# phase test on each run: repeated pairs at same/different parity
def phase(runs):
    c=[collections.Counter(),collections.Counter()]
    off=0
    for r in runs:
        for i in range(len(r)-1):c[(i+off)%2][r[i:i+2]]+=1
        off+=len(r)
    ioc=[sum(v*(v-1) for v in x.values())/max(1,sum(x.values())*(sum(x.values())-1)) for x in c]
    return ioc,[x.most_common(12) for x in c]
print('phase IoC',phase(parts))
# restart phase per run: best phase in sliding windows
tri=collections.Counter(D[i:i+3] for i in range(len(D)-2));print('top3',tri.most_common(15))
q=collections.Counter(D[i:i+4] for i in range(len(D)-3));print('top4',q.most_common(12))
s=collections.Counter(D[i:i+6] for i in range(len(D)-5));print('rep6',[x for x in s.most_common(10) if x[1]>1])
# distance of repeated 4-grams: parity
pos=collections.defaultdict(list)
for i in range(len(D)-3):pos[D[i:i+4]].append(i)
d=[p[j]-p[i] for p in pos.values() for i in range(len(p)) for j in range(i+1,len(p))]
print('rep4 pairs',len(d),'even dist',sum(x%2==0 for x in d),'mod3=0',sum(x%3==0 for x in d))
# control: same digit frequency shuffled
rnd=list(D);r=[]
for t in range(200):
    random.shuffle(rnd);S=''.join(rnd);pp=collections.Counter(S[i:i+4] for i in range(len(S)-3));r.append(sum(v*(v-1)//2 for v in pp.values()))
print('rep4 pairs shuffled mean',sum(r)/200,'max',max(r))
# first-digit / second-digit structure of pairs
for ph in (0,1):
    c=collections.Counter(D[i:i+2] for i in range(ph,len(D)-1,2));print('phase',ph,'distinct',len(c),c.most_common(14))
# digit after 1: 1 followed by?; which digits follow which
m=collections.Counter(D[i:i+2] for i in range(len(D)-1))
print('rows: first digit, columns second digit')
for x in '0123456789':print(x,[m[x+y] for y in '0123456789'])
