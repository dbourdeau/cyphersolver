"""dieguez1914: compare key.tsv with every key file under targets/ in a git revision.

A key file is any targets/**/key*.tsv, .csv or .txt (case ignored), other than this folder's. Its rows whose first field
is a two-figure group are read as group -> value (the first value column; for targets/villa1914/key.tsv each of its
three columns separately). For each file the script counts the groups both keys define and how many get the same
letter, and prints the files with the most agreements, then Clave Extra 3 (murguia1914) and Allen's villa1914 key.

Run from the repository root:  python targets/dieguez1914/scripts/compare_keys.py [revision]   (default HEAD)
"""
import re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
REV = sys.argv[1] if len(sys.argv) > 1 else 'HEAD'


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout


ours = {}
for line in open(HERE / 'key.tsv', encoding='utf-8'):
    if line.startswith('#') or line.startswith('group\t'):
        continue
    p = line.rstrip('\n').split('\t')
    if re.fullmatch(r'\d\d', p[0]) and p[1] != '?':
        ours[p[0]] = p[1].lower()


def table(text, col=1):
    m = {}
    for l in text.splitlines():
        p = re.split(r'[\t,]', l)
        if len(p) > col and re.fullmatch(r'\d{2}', p[0].strip()):
            v = p[col].strip().lower()
            if v not in ('', '-', '?'):
                m.setdefault(p[0].strip(), v)
    return m


def compare(m):
    shared = [g for g in ours if g in m]
    return sum(ours[g] == m[g] for g in shared), len(shared)


files = [f for f in git('ls-tree', '-r', '--name-only', REV, 'targets').split()
         if re.search(r'key[^/]*\.(tsv|csv|txt)$', f, re.I) and not f.startswith('targets/dieguez1914/')]
res = []
for f in files:
    a, n = compare(table(git('show', '%s:%s' % (REV, f))))
    if n:
        res.append((a, n, f))
print('revision %s: %d key files, %d share groups with this key' % (REV, len(files), len(res)))
print('most agreements:')
for a, n, f in sorted(res, key=lambda r: (-r[0], r[2]))[:6]:
    print('  %d of %d  %s' % (a, n, f))
for f, cols in (('targets/murguia1914/key.tsv', [1]), ('targets/murguia1914/key_frozen.tsv', [1]),
                ('targets/villa1914/key.tsv', [1, 2, 3])):
    text = git('show', '%s:%s' % (REV, f))
    for c in cols:
        head = [l for l in text.splitlines() if not l.startswith('#')][0].split('\t')[c]
        a, n = compare(table(text, c))
        print('%s (%s): %d of %d shared groups agree' % (f, head, a, n))
