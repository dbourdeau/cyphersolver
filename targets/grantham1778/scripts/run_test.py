#!/usr/bin/env python3
"""The test of tests/TEST_PLAN.md, as run once on 15 Nov 2026 (seed 35, 200 shuffles). Run from the target folder:
    python scripts/run_test.py            prints the result; add --write to rewrite tests/RESULT.json
Only the file paths differ from the script that was hashed before the run (see tests/README.md)."""
import sys, os, csv, json, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from align import same, norm
import lcs_test
T = json.load(open(os.path.join(ROOT, 'key', 'table_frozen.json')))['table']
tab = {int(g): e['top'] for g, e in T.items() if e['grade'] == 'firm'}
rows = [r for r in csv.reader((l for l in open(os.path.join(ROOT, 'transcriptions', 'n35_office_copy.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t')][1:]
groups = [int(r[4]) for r in rows]
above = [[norm(w) for w in re.findall(r"[A-Za-z][A-Za-z']*", r[6])] for r in rows]
words = [w for a in above for w in a]
out = {'firm_entries': len(tab), 'groups': len(groups), 'words': len(words)}
# Test A
cov, real, sh = lcs_test.run(groups, words, tab, 200, seed=35)
out['A'] = {'covered': cov, 'matched': real, 'share': round(real/max(cov, 1), 3), 'shuffled_mean': sum(sh)/len(sh), 'shuffled_max': max(sh), 'shuffled_ge_real': sum(1 for s in sh if s >= real),
            'pass': bool(cov >= 10 and real/cov >= 0.6 and real > max(sh)), 'decidable': cov >= 10}
# Test B
def b_score(t):
    c = m = 0
    for g, a in zip(groups, above):
        if a and g in t:
            c += 1; m += any(same(t[g], w) for w in a)
    return c, m
c, m = b_score(tab); rng = random.Random(35); keys = sorted(tab); vals = [tab[k] for k in keys]; shb = []
for _ in range(200):
    v = vals[:]; rng.shuffle(v); shb.append(b_score(dict(zip(keys, v)))[1])
out['B'] = {'covered': c, 'matched': m, 'share': round(m/max(c, 1), 3), 'shuffled_mean': sum(shb)/len(shb), 'shuffled_max': max(shb), 'pass': bool(c and m/c >= 0.6)}
# Test C
tail = [g for g in groups[-15:] if g in tab]; lastw = words[-15:]
out['C'] = {'tail_covered': len(tail), 'tail_headwords': [tab[g] for g in tail], 'matched_in_last_15_words': lcs_test.lcs([tab[g] for g in tail], lastw),
            'first4_headwords': [tab.get(g) for g in groups[:4]]}
out['C']['verdict'] = 'tail carries text' if out['C']['matched_in_last_15_words'] >= 2 else 'not shown'
out['decoded_in_order'] = [[g, tab.get(g)] for g in groups]
if '--write' in sys.argv: json.dump(out, open(os.path.join(ROOT, 'tests', 'RESULT.json'), 'w'), indent=1)
print(json.dumps({k: out[k] for k in ('firm_entries', 'groups', 'words', 'A', 'B', 'C')}, indent=1))
if '--check' in sys.argv:
    old = json.load(open(os.path.join(ROOT, 'tests', 'RESULT.json')))
    print('identical to tests/RESULT.json:', old == out)
