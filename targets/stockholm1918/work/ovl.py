import re, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
sec = {'13040 specimens': (1197, 2060), 's8-15': (2351, 7094), 's16-26': (7094, 10393),
       's27 specimens': (10393, 13700), 's28 family': (13700, 14900), 'III methods': (14900, 15686)}
for k, (a, b) in sec.items():
    gs = collections.Counter(re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', ' '.join(m[a:b])))
    print(k, 'distinct groups', len(gs))
    for t, g in T.items():
        hits = [x for x in g if len(x) >= 4 and x in gs]
        print(f'  {t:6s} {len(g):4d} hits {len(hits):3d} {round(100*len(hits)/len(g))}% {hits[:12]}')
print('Bernstorff 1917 two-part code')
A = set(re.findall(r'\b\d{4,5}\b', open('../bernstorff1917/transcription.txt', encoding='utf-8').read()))
for t, g in T.items():
    h = [x for x in g if x in A]
    print(f'  {t:6s} {len(g):4d} hits {len(h):3d} {round(100*len(h)/len(g))}% {h[:12]}')
print('within-batch repeats between telegrams')
ids = list(T)
for i, a in enumerate(ids):
    for b in ids[i+1:]:
        s = set(x for x in T[a] if len(x) >= 4) & set(T[b])
        if len(s) >= 3: print(' ', a, b, len(s), sorted(s)[:12])
print('group-length and range profile')
for t, g in T.items():
    n = [int(x) for x in g if len(x) in (4, 5)]
    c = collections.Counter(g)
    print(f'  {t:6s} n={len(g):3d} 4fig={sum(len(x)==4 for x in g):3d} 5fig={sum(len(x)==5 for x in g):3d} '
          f'lead0={sum(x[0]=="0" for x in g):3d} max={max(n)} >31000={sum(v>31000 for v in n):3d} rep={[k for k,v in c.items() if v>1][:10]}')
