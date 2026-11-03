"""Second target: Soglia 1848 (Italian, 2-digit syllabic table). Truth = targets/soglia1848/key.json."""
import json, os, random, re, collections
H = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(H, '..', '..', 'targets', 'soglia1848')
key = json.load(open(os.path.join(S, 'key.json'), encoding='utf-8'))
ct = open(os.path.join(S, 'ct2.txt')).read().strip()
words = []
for r in ct.split('5'):
    i = 0; w = []
    while i < len(r):
        if r[i] == '8' and i + 4 <= len(r): w.append(r[i:i+4]); i += 4
        elif i + 2 <= len(r): w.append(r[i:i+2]); i += 2
        else: w.append('x' + r[i]); i += 1
    if w: words.append(w)
lines = []
for i in range(0, len(words), 10):
    lines.append(' '.join(t for w in words[i:i+10] for t in w))
open(os.path.join(H, 'soglia_tokens.txt'), 'w', encoding='utf-8').write(
    '\n'.join(f'C{n+1}: {l}' for n, l in enumerate(lines)) + '\n')
toks = sorted(set(t for l in lines for t in l.split()))
def val(t):
    v = key.get(t, '')
    return re.sub(r'[^a-zA-Z]', '', v) if v.startswith('[') else v
truth = {t: val(t) for t in toks}
cnt = collections.Counter(t for l in lines for t in l.split())
two = [t for t in toks if len(t) == 2 and truth[t] and cnt[t] >= 4]
pool = sorted(set(truth[t] for t in two))
print(len(toks), 'tokens;', len(two), 'two-digit groups eligible;', len(pool), 'distinct values;', sum(cnt.values()), 'occurrences')
base = dict(name='soglia1848', model='it-modern', norm='modern', spaces=False,
            token_files=['soglia_tokens.txt'], truth_key=truth)
for seed in (1, 2, 3):
    r = random.Random(seed); k = dict(truth)
    for t in r.sample(two, 12):
        k[t] = r.choice([v for v in pool if v != truth[t]])
    sp = dict(base, start_key=k, name=f'soglia1848-c{seed}')
    json.dump(sp, open(os.path.join(H, f'soglia_task_c{seed}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(seed, sum(k[t] != truth[t] for t in k), 'wrong tokens')
