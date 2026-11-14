import json, random, hashlib, unicodedata, re, sys, collections, os
D = sys.argv[1]
def norm(u):
    u = unicodedata.normalize('NFD', u.lower()); u = ''.join(c for c in u if unicodedata.category(c) != 'Mn')
    u = u.replace("'", '').replace('&', 'et'); return re.sub(r'(.)\1+', r'\1', u)
def rows(fn):
    for l in open(os.path.join(D, fn), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        yield l.rstrip('\n').split('\t')
v = collections.defaultdict(collections.Counter)
for f in rows('key/key_source_pairs_pp600-603_609.tsv'): v[int(f[0])][f[1]] += 1
for f in rows('transcriptions/p604-606_cipher_with_p599_draft.tsv'):
    if len(f) >= 3 and not f[0].endswith('s') and f[2] != '?': v[int(f[1])][f[2]] += 1
for f in rows('key/key_additions_round2.tsv'): v[int(f[0])][f[1]] += 1
K2 = {n: c.most_common(1)[0][0] for n, c in v.items()}
blob = json.dumps(sorted(K2.items()), ensure_ascii=False); open(os.path.join(D, 'key/key_K2.json'), 'w').write(blob)
print('K2 entries', len(K2), 'sha256', hashlib.sha256(blob.encode()).hexdigest())
T = [(int(f[0]), f[1]) for f in rows('key/heldout_p608_truth.tsv')]
def sc(k): c = [(n, u) for n, u in T if n in k]; return sum(norm(k[n]) == norm(u) for n, u in c), len(c)
h, c = sc(K2); print('held-out p.608:', h, '/', c, 'covered of', len(T), round(h / c, 3))
print('misses', [(n, K2[n], u) for n, u in T if n in K2 and norm(K2[n]) != norm(u)], 'uncovered', [n for n, u in T if n not in K2])
r = random.Random(1780); ns = list(K2); vs = list(K2.values()); s = []
for _ in range(200): r.shuffle(vs); s.append(sc(dict(zip(ns, vs)))[0])
print('shuffles mean %.1f max %d reach %d/200' % (sum(s) / 200, max(s), sum(x >= h for x in s)))
