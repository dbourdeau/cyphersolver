"""Compare DECODE's transcriptions of R446 (vetesi1705) with R582 and R583 (bay1706/keys), and R446 with every
other DECODE key file under targets/bay1706/keys. Run from the repository root:
    python targets/vetesi1705/key/compare_R446_R582_R583.py
Each code maps to its first value in the file, lower-cased; a pair agrees when the two values are identical."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
R446 = os.path.join(ROOT, 'targets/vetesi1705/key/DOC_R446_D2629_2629.txt')
KEYS = os.path.join(ROOT, 'targets/bay1706/keys')


def load(p):
    m = {}
    for line in open(p, encoding='utf-8', errors='ignore'):
        line = line.rstrip('\n')
        if line.startswith('#') or ' - ' not in line:
            continue
        codes, value = line.split(' - ', 1)
        for c in codes.split('|'):
            c = c.strip()
            if c:
                m.setdefault(c, value.strip().lower())
    return m


def cmp(a, b):
    shared = set(a) & set(b)
    agree = sum(a[c] == b[c] for c in shared)
    return len(shared), agree, len(shared) - agree


k446 = load(R446)
k582 = load(os.path.join(KEYS, 'DOC_R582_D2716_2716.txt'))
k583 = load(os.path.join(KEYS, 'DOC_R583_D2717_2717.txt'))
for name, a, b in (('R446 vs R582', k446, k582), ('R446 vs R583', k446, k583), ('R582 vs R583', k582, k583)):
    s, ag, d = cmp(a, b)
    print(f'{name}: shared codes {s} = agree {ag} + differ {d}')
print('R446 against every other key file in targets/bay1706/keys (agree / shared):')
rows = []
for f in sorted(os.listdir(KEYS)):
    if f.startswith('DOC_') and f.endswith('.txt'):
        s, ag, d = cmp(k446, load(os.path.join(KEYS, f)))
        rows.append((ag, s, f))
rows.sort(reverse=True)
print(f'  {len(rows)} files')
for ag, s, f in rows[:5]:
    print(f'  {ag} / {s}  {f}')
print('R446 vs R582, codes that differ (R446 | R582):')
for c in sorted(set(k446) & set(k582), key=lambda x: (len(x), x)):
    if k446[c] != k582[c]:
        print(f'  {c}: {k446[c]} | {k582[c]}')
