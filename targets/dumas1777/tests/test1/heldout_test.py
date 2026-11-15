"""Held-out test: build key from 0009/0010/0013, freeze, decode 0020, compare with gloss and with shuffled keys."""
import json, hashlib, random, collections, os, sys
D = os.path.dirname(os.path.abspath(__file__))
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(D, 'pairs.tsv'))][1:]
train = [r for r in rows if r[0] != '0020' and r[3] != '-']
test = [r for r in rows if r[0] == '0020' and r[3] != '-']

votes = collections.defaultdict(collections.Counter)
for r in train:
    votes[int(r[2])][r[3]] += 1
key = {}
conflicts = {}
for n, c in sorted(votes.items()):
    key[n] = c.most_common(1)[0][0]
    if len(c) > 1:
        conflicts[n] = dict(c)
kp = os.path.join(D, 'key_frozen.json')
blob = json.dumps({str(k): v for k, v in sorted(key.items())}, indent=0, sort_keys=False)
open(kp, 'w').write(blob)
sha = hashlib.sha256(open(kp, 'rb').read()).hexdigest()
plan = os.path.join(D, 'TEST_PLAN.md')
t = open(plan).read()
if 'Frozen key sha256: (filled' in t:
    t = t.replace('Frozen key sha256: (filled in by heldout_test.py step 1, before step 2 runs)',
                  f'Frozen key sha256: `{sha}` ({len(key)} numbers; written before 0020 was decoded)')
    open(plan, 'w').write(t)
print('frozen key', len(key), 'numbers; sha256', sha)
print('training conflicts:', conflicts)

def score(k):
    cov = [r for r in test if int(r[2]) in k]
    m = sum(1 for r in cov if k[int(r[2])] == r[3])
    return m, len(cov)

m, cov = score(key)
print(f'real: {m}/{cov} agree ({m/cov:.1%}); coverage {cov}/{len(test)}')
print('disagreements:', [(r[1], r[2], 'key=' + key[int(r[2])], 'gloss=' + r[3]) for r in test if int(r[2]) in key and key[int(r[2])] != r[3]])
rng = random.Random(20261114)
nums, vals = list(key), list(key.values())
null = []
for _ in range(200):
    v = vals[:]; rng.shuffle(v)
    null.append(score(dict(zip(nums, v)))[0] / cov)
null.sort()
p = sum(1 for x in null if x >= m / cov) / 200
print(f'shuffled: mean {sum(null)/200:.1%}, min {null[0]:.1%}, max {null[-1]:.1%}, empirical p {p}')
dec = ''.join(key.get(int(r[2]), f'[{r[2]}]') for r in rows if r[0] == '0020')
print('0020 decoded with frozen key:', dec)
json.dump({'sha256': sha, 'n_key': len(key), 'agree': m, 'covered': cov, 'scorable': len(test),
           'null_mean': sum(null) / 200, 'null_max': null[-1], 'null_min': null[0], 'p': p,
           'training_conflicts': conflicts, 'decoded_0020': dec},
          open(os.path.join(D, 'heldout_result.json'), 'w'), indent=1)
