"""Martinique 1778-79 (Bouille code, French). Calibration: f.123 (1779) has an interlinear decipherment, so
truth = its pairs; start = truth with 12 groups given a wrong value. Open run: f.88 (1778), start = key_bouille + tentative."""
import os, re, json, random, unicodedata
H = os.path.dirname(os.path.abspath(__file__))
M = os.path.join(H, '..', '..', 'targets', 'martinique1778')

def norm(s):
    s = unicodedata.normalize('NFKD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s)

pairs = {}
order = []
for line in open(os.path.join(M, 'pairs1779_f123.txt'), encoding='utf-8'):
    if not re.match(r'l\d+:', line): continue
    for item in line.split(':', 1)[1].split():
        g, _, v = item.partition('=')
        if g.isdigit():
            pairs[g] = norm(v)
            order.append(g)
open(os.path.join(H, 'martinique_f123_tokens.txt'), 'w', encoding='utf-8').write(
    '\n'.join(f'C{n+1}: ' + l.strip() for n, l in enumerate(open(os.path.join(M, 'groups1779_f123.txt'), encoding='utf-8'))) + '\n')
toks = set(t for l in open(os.path.join(H, 'martinique_f123_tokens.txt'), encoding='utf-8') for t in l.split()[1:])
truth = {t: pairs.get(t, '') for t in toks}
missing = [t for t in toks if t not in pairs]
print(len(toks), 'distinct groups in f.123;', len(order), 'pair tokens;', 'not in pairs:', missing)
from collections import Counter
cnt = Counter(t for l in open(os.path.join(H, 'martinique_f123_tokens.txt'), encoding='utf-8') for t in l.split()[1:])
eligible = [t for t in toks if truth[t]]
pool = sorted(set(truth[t] for t in eligible))
base = dict(name='martinique1779-f123', model='fr-modern', norm='modern', spaces=False,
            token_files=['martinique_f123_tokens.txt'], truth_key=truth)
for seed in (1, 2, 3):
    r = random.Random(seed); k = dict(truth)
    for t in r.sample(eligible, 12):
        k[t] = r.choice([v for v in pool if v != truth[t]])
    json.dump(dict(base, start_key=k, name=base['name'] + f'-c{seed}'), open(os.path.join(H, f'martinique_task_c{seed}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# open run: f.88
key = {}
for l in open(os.path.join(M, 'key_bouille.tsv'), encoding='utf-8'):
    if l[:1].isdigit():
        g, v = l.split('\t')[:2]
        key[g] = norm(v.split('/')[0].replace('M.', 'monsieur').replace('1er', 'premier'))
for l in open(os.path.join(M, 'tentative.tsv'), encoding='utf-8'):
    if l[:1].isdigit():
        g, v = l.split('\t')[:2]
        key.setdefault(g, norm(v.split('/')[0]))
open(os.path.join(H, 'martinique_f88_tokens.txt'), 'w', encoding='utf-8').write(
    '\n'.join(f'C{n+1}: ' + l.strip() for n, l in enumerate(x for x in open(os.path.join(M, 'transcription.txt'), encoding='utf-8') if x[0] != '#' and x.strip())) + '\n')
t88 = [t for l in open(os.path.join(H, 'martinique_f88_tokens.txt'), encoding='utf-8') for t in l.split()[1:]]
start = {t: key.get(t, '') for t in set(t88)}
json.dump(dict(name='martinique1778-f88', model='fr-modern', norm='modern', spaces=False,
               token_files=['martinique_f88_tokens.txt'], truth_key={t: '' for t in start}, start_key=start),
          open(os.path.join(H, 'martinique_task_f88.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('f.88:', len(t88), 'tokens;', len(set(t88)), 'distinct;', sum(1 for t in t88 if key.get(t)), 'valued')
