"""Count the cipher tokens of no. 171 given a value, by grade and by key source (cipher171.tsv)."""
import csv, collections, pathlib
rows = [r for r in csv.reader(open(pathlib.Path(__file__).with_name('cipher171.tsv'), encoding='utf-8'), delimiter='\t')
        if r and not r[0].startswith('#') and r[0] != 'run']
n = len(rows); valued = [r for r in rows if r[2] != '?']
g = collections.Counter(r[4] for r in valued); s = collections.Counter(r[3] for r in valued)
print(f'tokens {n}, given a value {len(valued)} ({len(valued)/n:.3f}); open {n-len(valued)}')
print('grades', dict(g)); print('source', dict(s))
hm = sum(1 for r in valued if r[4] in 'HM'); print(f'H+M {hm} ({hm/n:.3f})')
