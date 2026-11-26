#!/usr/bin/env python3
"""Does any numeric key held in the repository agree with the partial table of this code? (24 Nov 2026)

The 2 Nov 2026 scan (solver/keyscan.py) could only score the French that seven keys gave on the 653 groups. With the
contributor's partial table in hand (beling2026/key/code_table_F_partial.tsv) the comparison is direct: for every key
file under targets/ that lists numbers with values, count the numbers that this letter uses and that carry the same
value in both. The null is the same key with its values shuffled over its own numbers (200 times).

A key that was this code, or a near edition of it, would agree on most shared numbers. Read-only, stdlib only.

usage: python key_compare.py            (from anywhere; paths are taken from this file's place)
"""
import csv, pathlib, random, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
TARGETS = HERE.parent


def norm(s):
    d = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z]', '', ''.join(c for c in d if unicodedata.category(c) != 'Mn'))


table = {}
for r in csv.DictReader(open(HERE / 'beling2026/key/code_table_F_partial.tsv', encoding='utf-8'), delimiter='\t'):
    if r['class'] == 'C':
        continue
    vals = {norm(r['value'])}
    for a in (r.get('all_values') or '').split(';'):
        a = re.sub(r'\s*x\d+\s*$', '', a.strip())
        if a:
            vals.add(norm(a))
    vals.discard('')
    if vals:
        table[int(r['group'])] = vals


def load(path):
    """number -> value for a key file whose rows hold one whole number and one value in letters."""
    key = {}
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except OSError:
        return key
    for line in text.splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        cells = [c.strip() for c in re.split(r'[\t,;]', line)]
        nums = [c for c in cells if re.fullmatch(r'\d{1,4}', c)]
        words = [c for c in cells if norm(c) and not re.search(r'\d', c)]
        if len(nums) >= 1 and words:
            n = int(nums[0])
            if n not in key:
                key[n] = norm(words[0])
    return key


rows = []
files = sorted(p for p in TARGETS.glob('*/**/*')
               if p.is_file() and p.suffix.lower() in ('.tsv', '.csv')
               and re.search(r'key|table|code|nomencl', p.name, re.I)
               and HERE not in p.parents)
rng = random.Random(1797)
for p in files:
    key = load(p)
    shared = [n for n in key if n in table]
    if len(key) < 40 or len(shared) < 20:
        continue
    hit = sum(key[n] in table[n] for n in shared)
    nums, vals, null = list(key), list(key.values()), []
    for _ in range(200):
        rng.shuffle(vals)
        k2 = dict(zip(nums, vals))
        null.append(sum(k2[n] in table[n] for n in shared))
    rows.append((hit - max(null), hit, len(shared), max(null), sum(null) / len(null), len(key), p.relative_to(TARGETS).as_posix()))

rows.sort(key=lambda r: (-r[1], r[6]))
print(f'table F: {len(table)} numbers with a sure or single-use value; key files compared: {len(rows)} of {len(files)} found')
print('agree  shared  null_max  null_mean  entries  file')
for d, hit, sh, nmax, nmean, n, f in rows[:12]:
    print(f'{hit:5d}  {sh:6d}  {nmax:8d}  {nmean:9.2f}  {n:7d}  {f}')
best = rows[0]
print(f'best agreement: {best[1]} of {best[2]} shared numbers ({best[6]}); '
      f'files agreeing on more than 3 numbers: {sum(r[1] > 3 for r in rows)}')
# the seven French numeric keys of the 2 Nov 2026 scan, named one by one
FRENCH = ['bouille1778/key.tsv', 'damas1787/key.tsv', 'martinique1778/key_bouille.tsv', 'mercier1761/key1761.tsv',
          'mercier1761/key1765_ennery.tsv', 'affry1757/key_X.tsv', 'champigny1744/key.tsv']
print('the French keys of the 2 Nov scan:')
for f in FRENCH:
    r = next((r for r in rows if r[6] == f), None)
    print(f'  {f}: ' + (f'{r[1]} of {r[2]} shared numbers agree' if r else 'not compared (absent or under 20 shared numbers)'))
