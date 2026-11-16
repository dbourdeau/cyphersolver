"""Cut key/we025_crawford1814.tsv (the WE025 rows for the numbers that occur in this letter) from our full transcription
of Weber's table, frozen 2026-11-11T10:37:23Z (sha256 26dad03e814111e1ae9b52e995882b02f3933465efa0c5ed4189c55f5510bbee;
the same table as ../../poinsett1813/beling/key/, whose we025_poinsett.tsv holds the rows for the Poinsett letters).

    python key/extract_key.py FULL_TABLE.tsv     write key/we025_crawford1814.tsv
    python key/extract_key.py FULL_TABLE.tsv --check   verify it

The full table is not in this repository (Weber 1979 is in copyright); the rows used are."""
import hashlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FULL_SHA = '26dad03e814111e1ae9b52e995882b02f3933465efa0c5ed4189c55f5510bbee'
full = sys.argv[1]
assert hashlib.sha256(open(full, 'rb').read()).hexdigest() == FULL_SHA, 'not the frozen table'
used = set()
for line in open(os.path.join(HERE, '..', 'crawford1814_transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or ':' not in line:
        continue
    body = re.sub(r'"[^"]*"|\[struck:[^\]]*\]', ' ', line.split(':', 1)[1])
    used |= {int(n) for n in re.findall(r'(?<!\d)\d+(?!\d)', body)}
rows = ['number\telement\tsource']
for i, l in enumerate(open(full, encoding='utf-8')):
    if i == 0:
        continue
    p = l.rstrip('\n').split('\t')
    if int(p[0]) in used:
        if p[0] == '668':  # the one correction logged after the freeze (fect, not feet); 668 does not occur here
            p[1] = 'fect'
        rows.append('\t'.join(p))
out = '\n'.join(rows) + '\n'
dest = os.path.join(HERE, 'we025_crawford1814.tsv')
if '--check' in sys.argv:
    print('ok' if open(dest, encoding='utf-8').read() == out else 'DIFFERS')
else:
    open(dest, 'w', encoding='utf-8').write(out)
    print(len(rows) - 1, 'rows written')
