"""Build the code table from ../key/pairs_build_v1.tsv (the pairs as frozen, sources marked ! = gloss): python build_table.py OUT.tsv
For each group: values lower-cased; rows with uncertain group digits dropped; the value is the most frequent among
certain rows (ties broken by number of clerk-gloss '!' rows); if a group has only uncertain rows, the most frequent of
those, flagged 'weak'. Columns: group, value, n_rows, n_gloss, n_agree, other_values, grade (sure / weak / conflict)."""
import csv, sys, collections
BASE = __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..')
rows = list(csv.DictReader(open(BASE + '/key/pairs_build_v1.tsv'), delimiter='\t'))
by = collections.defaultdict(list)
for r in rows:
    if r['uncertain'] == 'g': continue
    v = r['value'].strip().lower()
    if v in ('', '?') or v.startswith('slip'): continue
    by[r['group']].append((v, r['source'], r['uncertain']))
out = []
for g, lst in by.items():
    cert = [x for x in lst if x[2] != 'u'] or lst
    c = collections.Counter(v for v, _, _ in cert)
    gl = collections.Counter(v for v, s, _ in cert if s == '!')
    ranked = sorted(c, key=lambda v: (-c[v], -gl[v]))
    best = ranked[0]
    # tie between incompatible values (neither contains the other) -> group left out of the table
    if len(ranked) > 1 and c[ranked[1]] == c[best] and gl[ranked[1]] == gl[best] and best not in ranked[1] and ranked[1] not in best:
        print('left out (tie):', g, dict(c), file=sys.stderr); continue
    allc = collections.Counter(v for v, _, _ in lst)
    others = {v: n for v, n in allc.items() if v != best}
    grade = 'weak' if all(x[2] == 'u' for x in lst) else ('conflict' if others and c[best] < 2 * sum(n for v, n in others.items()) else 'sure')
    out.append((int(g), best, len(lst), sum(1 for x in lst if x[1] == '!'), allc[best], ';'.join(f'{v}:{n}' for v, n in others.items()), grade))
out.sort()
with open(sys.argv[1], 'w') as o:
    o.write('group\tvalue\tn_rows\tn_gloss\tn_agree\tother_values\tgrade\n')
    for r in out: o.write('\t'.join(map(str, r)) + '\n')
print(len(out), 'groups;', collections.Counter(r[6] for r in out))
