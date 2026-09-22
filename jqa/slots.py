"""Alphabetical-slot bracket for unread groups (grade I at best).
The code is a one-part syllabary only within short runs: values climb alphabetically for a few numbers, then the run
breaks (e.g. 1384 that, 1385 the, 1388 then, 1391 there, 1392 these, 1393 they, 1394 think, 1399 this). For each
number asked, print the nearest H/C-graded values below and above it and whether they are in alphabetical order
(if they are, the unknown value should sort between them).
python slots.py 1434 158 83 ...   (no argument: every {n} left in gap88.txt and rem88.txt)"""
import sys, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tab = {}
for l in open('code_table.tsv', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if l.startswith('#') or len(p) < 3 or not p[0].isdigit():
        continue
    tab[int(p[0])] = (p[1], p[2][:1])
def k(s):
    return re.sub(r'[^a-z]', '', re.sub(r'\(.*?\)', '', s.lower()))
nums = [int(a) for a in sys.argv[1:]]
if not nums:
    for f in ('gap88.txt', 'rem88.txt'):
        for t in open(f, encoding='utf8').read().split():
            if t.isdigit() and int(t) not in tab and int(t) not in nums:
                nums.append(int(t))
for n in nums:
    lo = [(m, tab[m][0]) for m in range(n - 1, n - 9, -1) if m in tab and tab[m][1] in 'HC'][:3]
    hi = [(m, tab[m][0]) for m in range(n + 1, n + 9) if m in tab and tab[m][1] in 'HC'][:3]
    ordered = bool(lo and hi and k(lo[0][1]) < k(hi[0][1]))
    lo_s = ', '.join(f'{m} {v}' for m, v in reversed(lo))
    hi_s = ', '.join(f'{m} {v}' for m, v in hi)
    br = f"between '{lo[0][1]}' and '{hi[0][1]}'" if ordered else 'run broken here: no bracket'
    print(f'{n}: [{lo_s}] < {n} < [{hi_s}]  -> {br}')
