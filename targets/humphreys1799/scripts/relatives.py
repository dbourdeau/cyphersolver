"""Test whether the Humphreys 994 code is a relative of a code whose table is held. For each held table T and each
additive offset k in -1700..1700 (a shifted or re-based copy of the same list), count the pairs (g, v) of our frozen
table for which T[g + k] == v (case-insensitive, punctuation groups and multi-part name pieces excluded). Report the
best offset per table, and the same statistic for 200 shuffled copies of each held table (values permuted among its
groups) as the control. Usage: python3 -I relatives.py"""
import csv, os, random, re, collections
# Run in the working folder: HC = the local project folder holding the held tables (not in this repository).
HC = os.environ.get('HC', '.')
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'key')
def norm(v): return re.sub(r'[^a-z]', '', v.lower())
ours = {}
for r in csv.DictReader(open(B + '/table_frozen_v1.tsv'), delimiter='\t'):
    v = norm(r['value'])
    if v and r['value'] not in ('stop', 'comma', 'semicolon') and '[' not in r['value']: ours[int(r['group'])] = v
tables = collections.defaultdict(dict)
for r in csv.DictReader(open(HC + '/sources/raw/weber_ill_2026-11-10/weber_1600_family_elements.tsv'), delimiter='\t'):
    tables[r['code']][int(r['number'])] = norm(r['element'])
def load(name, path, gcol, vcol, skip='#'):
    for line in open(path):
        if line.startswith(skip) or not line.strip(): continue
        f = line.rstrip('\n').split('\t')
        if len(f) <= max(gcol, vcol) or not f[gcol].strip().isdigit(): continue
        tables[name][int(f[gcol])] = norm(f[vcol].split('/')[0])
load('Code16_v4', HC + '/output/code16_merged_2026-11-10/code16_key_v4.tsv', 0, 1)
R = B + '/work/reltables'
load('King769(king1797)', R + '/king1797_key.tsv', 0, 1)
load('Carmichael1196(jefferson1787)', R + '/jefferson1787_key.tsv', 0, 1)
load('legation1788', R + '/legation1788_key.tsv', 1, 2)
load('Pinckney1651', R + '/pinckney1651_key.tsv', 0, 1)
def best(T):
    bestk, bests = 0, -1
    for k in range(-1700, 1701):
        s = sum(1 for g, v in ours.items() if T.get(g + k) == v)
        if s > bests: bestk, bests = k, s
    return bestk, bests
out = []
for name, T in sorted(tables.items()):
    T = {g: v for g, v in T.items() if v}
    k, s = best(T)
    s0 = sum(1 for g, v in ours.items() if T.get(g) == v)
    gs, vs = list(T), list(T.values()); ctrl = []
    for seed in range(1, 201):
        random.seed(seed); v2 = vs[:]; random.shuffle(v2); T2 = dict(zip(gs, v2))
        ctrl.append(sum(1 for g, v in ours.items() if T2.get(g) == v))
    # control for the offset search: best offset on 20 shuffled copies
    ctrl_best = []
    for seed in range(1, 21):
        random.seed(1000 + seed); v2 = vs[:]; random.shuffle(v2); ctrl_best.append(best(dict(zip(gs, v2)))[1])
    out.append((name, len(T), s0, max(ctrl), k, s, max(ctrl_best)))
print(f'our groups compared: {len(ours)}')
print('table\tsize\tsame_number_matches\tshuffled_max(200)\tbest_offset\tmatches_at_best_offset\tshuffled_best_offset_max(20)')
for r in out: print('\t'.join(map(str, r)))
