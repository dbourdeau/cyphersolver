import json, random, hashlib, unicodedata, re, sys, collections, os
D = sys.argv[1]
def norm(u):
    u = unicodedata.normalize('NFD', u.lower()); u = ''.join(c for c in u if unicodedata.category(c) != 'Mn')
    u = u.replace("'", '').replace('&', 'et')
    return re.sub(r'(.)\1+', r'\1', u)
def load_pairs(fn):
    out = []
    for l in open(os.path.join(D, fn), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t'); out.append(f)
    return out
ks = load_pairs('key/key_source_pairs_pp600-603_609.tsv')
votes = collections.defaultdict(collections.Counter)
for n, u, *_ in ks: votes[int(n)][u] += 1
K1 = {n: c.most_common(1)[0][0] for n, c in votes.items()}
blob = json.dumps(sorted(K1.items()), ensure_ascii=False)
open(os.path.join(D, 'key/key_K1.json'), 'w').write(blob)
print('K1 entries', len(K1), 'sha256', hashlib.sha256(blob.encode()).hexdigest())
truth = [(p, int(n), u) for p, n, u in (r[:3] for r in load_pairs('transcriptions/p604-606_cipher_with_p599_draft.tsv') if not r[0].endswith('s'))]
def score(key, rows):
    cov = [(n, u) for p, n, u in rows if u != '?' and n in key]
    hit = sum(norm(key[n]) == norm(u) for n, u in cov); return hit, len(cov)
h, c = score(K1, truth)
print('T1 real', h, '/', c, round(h / c, 3), '; groups total', len(truth), 'truth-known', sum(u != '?' for *_, u in truth))
rnd = random.Random(1779); nums = list(K1); vals = list(K1.values()); sh = []
for _ in range(200):
    rnd.shuffle(vals); sh.append(score(dict(zip(nums, vals)), truth)[0])
print('T1 shuffles mean %.1f max %d reach %d/200' % (sum(sh) / 200, max(sh), sum(s >= h for s in sh)))
miss = [(p, n, K1[n], u) for p, n, u in truth if u != '?' and n in K1 and norm(K1[n]) != norm(u)]
print('T1 mismatches', miss)
# T2
gl = [(p, n, u) for p, n, u in truth if p.split('.')[0] == '605' and int(p.split('.')[1]) >= 3 and u != '?']
rnd = random.Random(1779); idx = list(range(len(gl))); rnd.shuffle(idx)
held = []
for i in idx:
    p, n, u = gl[i]
    others = [g for j, g in enumerate(gl) if j != i and j not in [k for k, _ in held]]
    if n in K1 or any(o[1] == n for o in others): held.append((i, gl[i]))
    if len(held) == 10: break
hidx = {i for i, _ in held}
v2 = collections.defaultdict(collections.Counter)
for n, u in ((int(a), b) for a, b, *_ in ks): v2[n][u] += 1
for j, (p, n, u) in enumerate(gl):
    if j not in hidx: v2[n][u] += 1
K2 = {n: c.most_common(1)[0][0] for n, c in v2.items()}
test = [g for _, g in held]
h2 = sum(norm(K2[n]) == norm(u) for p, n, u in test)
print('T2 held-out', [(n, u, K2[n]) for p, n, u in test], 'real', h2, '/10')
rnd = random.Random(1779); nums = list(K2); vals = list(K2.values()); sh2 = []
for _ in range(200):
    rnd.shuffle(vals); k = dict(zip(nums, vals)); sh2.append(sum(norm(k[n]) == norm(u) for p, n, u in test))
print('T2 shuffles mean %.2f max %d reach %d/200' % (sum(sh2) / 200, max(sh2), sum(s >= h2 for s in sh2)))
