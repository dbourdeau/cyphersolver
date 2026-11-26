"""Structure of the partial table: is number order alphabetical (one-part) or not (two-part)? Reviewer's own code."""
import csv, random, sys
from collections import defaultdict
rows = [r for r in csv.DictReader(open(sys.argv[1]), delimiter='\t') if r['class'] in ('A', 'B')]
pairs = sorted((int(r['group']), r['value'].split('/')[0].lower()) for r in rows)
def ranks(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0] * len(xs)
    for k, i in enumerate(o): r[i] = k
    return r
def spearman(a, b):
    ra, rb = ranks(a), ranks(b); n = len(a)
    return 1 - 6 * sum((x - y) ** 2 for x, y in zip(ra, rb)) / (n * (n * n - 1))
nums = [p[0] for p in pairs]; vals = [p[1] for p in pairs]
rho = spearman(nums, vals)
rng = random.Random(1); ctrl = []
for _ in range(2000):
    v = vals[:]; rng.shuffle(v); ctrl.append(spearman(nums, v))
ctrl.sort()
print('entries', len(pairs), 'spearman number vs alphabetical value', round(rho, 3), 'shuffled 99.5pct', round(ctrl[1989], 3))
# local order: share of adjacent (in number order) entries whose values are in alphabetical order
asc = sum(1 for i in range(len(vals) - 1) if vals[i] <= vals[i + 1]) / (len(vals) - 1)
c2 = []
for _ in range(2000):
    v = vals[:]; rng.shuffle(v); c2.append(sum(1 for i in range(len(v) - 1) if v[i] <= v[i + 1]) / (len(v) - 1))
c2.sort(); print('adjacent pairs ascending', round(asc, 3), 'shuffled mean', round(sum(c2) / len(c2), 3), '99.5pct', round(c2[1989], 3))
# first letter blocks by hundreds
by = defaultdict(list)
for n, v in pairs: by[n // 100].append(v[0])
for k in sorted(by): print(f'{k*100:4d}-{k*100+99:4d}', ''.join(sorted(by[k])))
# homophones: values with 2+ numbers, gap between numbers
hv = defaultdict(list)
for n, v in pairs: hv[v].append(n)
gaps = [(v, sorted(ns)) for v, ns in hv.items() if len(ns) > 1]
adj = sum(1 for v, ns in gaps if max(ns) - min(ns) <= len(ns) + 2)
print('values with 2+ numbers', len(gaps), 'of which all numbers within a small block', adj)
print([g for g in gaps if max(g[1]) - min(g[1]) > len(g[1]) + 2])
