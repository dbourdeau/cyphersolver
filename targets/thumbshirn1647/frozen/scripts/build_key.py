# Construit K (PREREG) : K0 (vue 0003) + valeurs majoritaires des paires d'apprentissage A.
import sys, collections, json
base = sys.argv[1]
k0 = {}
for l in open(base + '/KEY0-0003.tsv', encoding='utf-8'):
    if l.startswith('#') or l.startswith('nombre'): continue
    p = l.rstrip('\n').split('\t'); k0[p[0]] = p[1]
votes = collections.defaultdict(collections.Counter); first = {}
for l in open(base + '/BUILD-PAIRES.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    pid, nums, plain = l.rstrip('\n').split('\t')[:3]
    nums = nums.split('.')
    if len(nums) != len(plain):
        sys.exit(f'{pid}: {len(nums)} nombres / {len(plain)} lettres')
    for n, c in zip(nums, plain):
        if n == 'x' or c == '_': continue
        votes[n][c] += 1; first.setdefault(n, c)
K = dict(k0); src = {n: 'K0' for n in k0}
for n, cnt in votes.items():
    top = max(cnt.values()); tied = [c for c, v in cnt.items() if v == top]
    if len(tied) == 1: v = tied[0]
    elif k0.get(n) in tied: v = k0[n]
    else: v = first[n] if first[n] in tied else tied[0]
    K[n] = v; src[n] = 'A ' + ' '.join(f'{c}:{v}' for c, v in cnt.most_common())
with open(base + '/KEY.tsv', 'w', encoding='utf-8') as f:
    f.write('nombre\tlettre\tsource (votes A)\n')
    for n in sorted(K, key=int): f.write(f'{n}\t{K[n]}\t{src[n]}\n')
inv = collections.defaultdict(list)
for n in sorted(K, key=int):
    if src[n] != 'K0': inv[K[n]].append(n)
print({c: inv[c] for c in sorted(inv)})
print('conflits:', {n: src[n] for n in votes if len(votes[n]) > 1})
print('K0 contredite par A:', {n: (k0[n], K[n]) for n in votes if n in k0 and k0[n] != K[n]})
