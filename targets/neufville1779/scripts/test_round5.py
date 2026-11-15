"""Round 5 (TEST_PLAN.md): the p.579 glossed pairs as a held-out set for the frozen key_full_r4 (T5), then the key K6
(key_full_r5.json) and the bare passages decoded again. Usage: python test_round5.py <target folder>"""
import json, random, hashlib, unicodedata, re, sys, collections, os
D = sys.argv[1]
R4_SHA = '146207b09c866ee26c1b11c7ad0d4ab5f17a05fb241dc46e902beaab7325f460'


def norm(u):
    u = unicodedata.normalize('NFD', u.lower()); u = ''.join(c for c in u if unicodedata.category(c) != 'Mn')
    u = u.replace("'", '').replace('&', 'et')
    return re.sub(r'(.)\1+', r'\1', u)


def rows(fn):
    for l in open(os.path.join(D, fn), encoding='utf-8'):
        if l.startswith('#') or not l.strip() or l.startswith('number\t') or l.startswith('page\t'): continue
        yield l.rstrip('\n').split('\t')


def sources_r4():
    """The round 4 sources, exactly as scripts/test_round4.py reads them."""
    out = []
    for f in rows('key/key_source_pairs_pp600-603_609.tsv'): out.append((int(f[0]), f[1], 'p.' + f[2]))
    for f in rows('transcriptions/p604-606_cipher_with_p599_draft.tsv'):
        if len(f) >= 3 and not f[0].endswith('s') and f[2] != '?': out.append((int(f[1]), f[2], 'p.' + f[0]))
    for f in rows('key/key_additions_round2.tsv'): out.append((int(f[0]), f[1], 'p.' + f[2]))
    for f in rows('key/p608_truth_complete.tsv'):
        if f[1] != '?': out.append((int(f[0]), f[1], 'p.608'))
    for f in rows('key/key_pairs_classB_glosses.tsv'):
        if not 516 <= int(f[2]) <= 548: out.append((int(f[0]), f[1], 'p.' + f[2]))
    for f in rows('transcriptions/glossed_pp516-548.tsv'):
        if f[5] == 'G' and f[2].isdigit(): out.append((int(f[2]), f[4], 'p.' + f[0]))
    return out


def build(src):
    v = collections.defaultdict(collections.Counter)
    for n, u, _ in src: v[n][u] += 1
    return {n: c.most_common(1)[0][0] for n, c in v.items()}, v


raw = open(os.path.join(D, 'key/key_full_r4.json'), 'rb').read()
sha = hashlib.sha256(raw).hexdigest()
print('key_full_r4 sha256', sha, 'matches FREEZE' if sha == R4_SHA else 'DOES NOT MATCH')
if sha != R4_SHA: sys.exit(1)
K5 = {int(n): u for n, u in json.loads(raw.decode('utf-8'))}

new = [f for f in rows('transcriptions/glossed_p579.tsv')]
held = [(int(f[2]), f[4]) for f in new if f[5] == 'G' and f[7] == 'no']
cov = [(n, u) for n, u in held if n in K5]
hit = sum(norm(K5[n]) == norm(u) for n, u in cov)
print('T5 held-out groups', len(held), 'covered', len(cov), 'match', hit)
print('T5 per group', [(n, u, K5.get(n), norm(K5.get(n, '')) == norm(u)) for n, u in held])
rnd = random.Random(1782); nums = list(K5); vals = list(K5.values()); sh = []
for _ in range(200):
    rnd.shuffle(vals); k = dict(zip(nums, vals)); sh.append(sum(norm(k[n]) == norm(u) for n, u in cov))
print('T5 shuffles mean %.2f max %d reach %d/200' % (sum(sh) / 200, max(sh), sum(s >= hit for s in sh)))

src = sources_r4() + [(int(f[2]), f[4], 'p.579') for f in new if f[5] == 'G' and f[7] == 'no']
K6, V6 = build(src)
blob = json.dumps(sorted(K6.items()), ensure_ascii=False)
open(os.path.join(D, 'key/key_full_r5.json'), 'w', encoding='utf-8').write(blob)
print('K6', len(K6), 'numbers, sha256', hashlib.sha256(blob.encode()).hexdigest())
print('changed from key_full_r4', [(n, K5.get(n), K6[n], dict(V6[n])) for n in sorted(K6) if K5.get(n) != K6[n]])
print('ties in K6', [(n, dict(V6[n])) for n in sorted(V6) if len(V6[n]) > 1 and V6[n].most_common(2)[0][1] == V6[n].most_common(2)[1][1]])
OPEN = (3, 58, 227, 369, 349, 162, 507, 501, 30, 405, 387, 390, 447, 327, 441)
print('open numbers in K6', [(n, K6.get(n), dict(V6[n]) if n in V6 else None) for n in OPEN])

for name in ('B573', 'B491', 'B492', 'B527'):
    print('#', name)
    for f in rows(f'letters/{name}_groups.txt'):
        line = f[0].split()
        o5, o6 = [], []
        for g in line[1:]:
            g = g.strip('[]')
            if '/' in g: o5.append('[' + g + ']'); o6.append('[' + g + ']'); continue
            o5.append(K5.get(int(g), f'[{g}]')); o6.append(K6.get(int(g), f'[{g}]'))
        print(line[0] + ':', ' '.join(o6), '' if o5 == o6 else '   (r4: ' + ' '.join(o5) + ')')
