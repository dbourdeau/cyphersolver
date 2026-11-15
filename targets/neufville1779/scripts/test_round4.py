"""Round 4 (TEST_PLAN.md): held-out letter pp.529-531 (T4), full key K5 (key_full_r4.json), decodes of the bare passages,
and the re-score of K2 on the complete p.608 truth. Usage: python test_round4.py <target folder>"""
import json, random, hashlib, unicodedata, re, sys, collections, os
D = sys.argv[1]


def norm(u):
    u = unicodedata.normalize('NFD', u.lower()); u = ''.join(c for c in u if unicodedata.category(c) != 'Mn')
    u = u.replace("'", '').replace('&', 'et')
    return re.sub(r'(.)\1+', r'\1', u)


def rows(fn):
    for l in open(os.path.join(D, fn), encoding='utf-8'):
        if l.startswith('#') or not l.strip() or l.startswith('number\t') or l.startswith('page\t'): continue
        yield l.rstrip('\n').split('\t')


def sources(exclude_pages=()):
    """(number, unit, source) for every key source of round 4."""
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
        if f[5] == 'G' and f[2].isdigit() and int(f[0]) not in exclude_pages: out.append((int(f[2]), f[4], 'p.' + f[0]))
    return out


def build(src):
    v = collections.defaultdict(collections.Counter)
    for n, u, _ in src: v[n][u] += 1
    return {n: c.most_common(1)[0][0] for n, c in v.items()}, v


def freeze(K, fn):
    blob = json.dumps(sorted(K.items()), ensure_ascii=False)
    open(os.path.join(D, fn), 'w', encoding='utf-8').write(blob)
    return hashlib.sha256(blob.encode()).hexdigest()


HELD = (529, 530, 531)
K4, _ = build(sources(exclude_pages=HELD))
print('K4', len(K4), 'numbers, sha256', freeze(K4, 'key/key_K4.json'))
test = [(int(f[2]), f[4]) for f in rows('transcriptions/glossed_pp516-548.tsv')
        if f[5] == 'G' and f[2].isdigit() and int(f[0]) in HELD]
cov = [(n, u) for n, u in test if n in K4]
hit = sum(norm(K4[n]) == norm(u) for n, u in cov)
print('T4 held-out glossed groups', len(test), 'covered by K4', len(cov), 'match', hit, '(%.3f)' % (hit / len(cov)))
print('T4 misses', [(n, u, K4[n]) for n, u in cov if norm(K4[n]) != norm(u)])
print('T4 not covered', [(n, u) for n, u in test if n not in K4])
rnd = random.Random(1781); nums = list(K4); vals = list(K4.values()); sh = []
for _ in range(200):
    rnd.shuffle(vals); k = dict(zip(nums, vals)); sh.append(sum(norm(k[n]) == norm(u) for n, u in cov))
print('T4 shuffles mean %.2f max %d reach %d/200' % (sum(sh) / 200, max(sh), sum(s >= hit for s in sh)))

K5, V5 = build(sources())
print('K5', len(K5), 'numbers, sha256', freeze(K5, 'key/key_full_r4.json'))
with open(os.path.join(D, 'results/key_full_r4_votes.tsv'), 'w', encoding='utf-8') as o:
    o.write('# number\tunit (majority)\tvotes (round 4 sources)\n')
    for n in sorted(V5):
        o.write(f"{n}\t{K5[n]}\t{'; '.join(f'{u}x{c}' for u, c in V5[n].most_common())}\n")

# Re-score of round 2's frozen K2 against the whole of p.608
K2 = {int(n): u for n, u in json.load(open(os.path.join(D, 'key/key_K2.json'), encoding='utf-8'))}
t = [(int(f[0]), f[1], f[3]) for f in rows('key/p608_truth_complete.tsv') if f[1] != '?']
for label, sel in (('T3 pairs only', [x for x in t if x[2] == 'yes']), ('whole page', t)):
    c = [(n, u) for n, u, _ in sel if n in K2]
    h = sum(norm(K2[n]) == norm(u) for n, u in c)
    print(f'K2 on p.608 {label}: {h} of {len(c)} covered ({len(sel)} aligned groups)', [(n, u, K2[n]) for n, u in c if norm(K2[n]) != norm(u)])

for name in ('B573', 'B491', 'B492', 'B527'):
    print('#', name)
    for f in rows(f'letters/{name}_groups.txt'):
        line = f[0].split()
        out = []
        for g in line[1:]:
            g = g.strip('[]')
            if '/' in g: out.append('[' + g + ']'); continue
            out.append(K5.get(int(g), f'[{g}]'))
        print(line[0] + ':', ' '.join(out))
