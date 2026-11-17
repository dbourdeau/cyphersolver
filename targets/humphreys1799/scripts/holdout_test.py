"""Held-out test (TEST_PLAN.md): score the frozen table on the held-out transcription and on 200 shuffled tables.
Usage: python3 -I holdout_test.py TABLE.tsv HOLDOUT.txt"""
import sys, re, random, csv
tab = {}
for r in csv.DictReader(open(sys.argv[1]), delimiter='\t'): tab[r['group']] = r['value'].lower()
items, excl = [], 0
for line in open(sys.argv[2]):
    m = re.match(r'H\d+:\s*(.*)', line.strip())
    if not m: continue
    for tok in m.group(1).split():
        g, v = tok.split('=', 1)
        if '?' in g or v.endswith('#') or v == '?': excl += 1; continue
        items.append((g, v.lower()))
def norm(v): return re.sub(r'\[\d/\d\]', '', v)
def score(t):
    hit = sum(1 for g, v in items if g in t and norm(t[g]) == v)
    cov = sum(1 for g, v in items if g in t)
    return hit / len(items), cov / len(items), (hit / cov if cov else 0)
s, cov, prec = score(tab)
groups, vals = list(tab), list(tab.values())
sh = []
for seed in range(1, 201):
    random.seed(seed); v2 = vals[:]; random.shuffle(v2)
    sh.append(score(dict(zip(groups, v2)))[0])
print(f'held-out groups scored: {len(items)} (excluded: {excl})')
print(f'frozen table: score {s:.3f}  coverage {cov:.3f}  precision {prec:.3f}')
print(f'200 shuffled tables: max {max(sh):.3f}  mean {sum(sh)/len(sh):.3f}')
print('PASS' if s >= 0.55 and prec >= 0.85 and s > max(sh) else 'FAIL')
print('misses:', ' '.join(f'{g}={v}->{tab.get(g,"-")}' for g, v in items if not (g in tab and norm(tab[g]) == v)))
