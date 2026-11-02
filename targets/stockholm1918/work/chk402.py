"""Look at the +402/+400/+302 outliers for family B: do the hit groups carry sense in Mendelsohn's specimens?"""
import re, sys, collections, random
sys.stdout.reconfigure(encoding='utf-8')
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
m = open('refs/m.txt', encoding='utf-8').read().split('\n')[10393:13700]
idx = collections.defaultdict(list)
for i, l in enumerate(m):
    for x in re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', l):
        idx[int(x)].append(i)
B = [g for t in ('w749', 'w746', 'w512', 'w513') for g in T[t] if len(g) in (4, 5)]
for d in (402, 400, 302):
    print('--- d =', d)
    for g in B:
        v = int(g) + d
        if v in idx:
            i = idx[v][0]
            print(g, '->', v, '|', ' / '.join(x.strip()[:24] for x in m[i:i+3]))
# significance against a same-shape control: shuffle within pages (keep the page histogram of B, redraw last two digits)
S = set(idx)
rng = random.Random(1)
pages = [int(g) // 100 for g in B]
best = []
for trial in range(200):
    fake = [p * 100 + rng.randrange(100) for p in pages]
    best.append(max(sum((f + d) in S for f in fake) for d in range(-999, 1000)))
print('control: max hits over all additives, redrawn last two digits:',
      'mean', sum(best)/len(best), 'max', max(best), 'p(>=25)=', sum(b >= 25 for b in best)/len(best))
