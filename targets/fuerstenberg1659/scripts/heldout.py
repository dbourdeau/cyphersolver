"""Held-out test for fuerstenberg1659. Standard library only.

    python scripts/heldout.py

The two shifts are fitted blind (German/Latin letter frequencies, no cribs) on runs P1-P3 only, then applied to
P4-P5, which played no part in the fit; the result is compared letter by letter with the reading of P4-P5
(reading_fuerstenberg1659.md). The reverse fold (fit on P4-P5, test on P1-P3) is printed as well.
"""
import math, pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from decrypt import runs
A = 'abcdefghiklmnopqrstuwxyz'
# rough letter frequencies (per cent) for 17th-century German/Latin chancery text, j->i, v->u
F = dict(zip(A, [6.5, 1.9, 3.0, 5.1, 16.5, 1.7, 3.0, 4.8, 8.0, 1.2, 3.4, 2.5, 9.8, 2.8, 0.8, 0.1, 7.0, 7.3, 6.2,
                 5.2, 1.9, 0.1, 0.1, 1.1]))
R = {}
for lab, run, ct in runs(ROOT / 'transcription_fuerstenberg1659.txt'):
    R[run] = R.get(run, '') + ct.replace('?', '')  # '?' marks an uncertain sign, not a sign

def fit(rs):
    best = []
    for parity in (0, 1):
        s = ''.join(R[r][parity::2] for r in rs)
        sc = [(sum(math.log(F[A[(A.index(c) - k) % 24]]) for c in s), k) for k in range(24)]
        sc.sort(reverse=True)
        best.append((sc[0][1], round(sc[0][0] - sc[1][0], 1)))
    return best

def dec(rs, k):
    return {r: ''.join(A[(A.index(c) - k[i % 2]) % 24] for i, c in enumerate(R[r])) for r in rs}

md = (ROOT / 'reading_fuerstenberg1659.md').read_text(encoding='utf-8')
block = md.split('```marked')[1].split('```')[0]
read = {}
for line in block.strip().splitlines():
    run, txt = line.split(':', 1)
    t = re.sub(r'\{([a-z]*)/([a-z]*)\}', r'\2', txt)
    read[run.strip()] = re.sub(r'[^a-z]', '', t.lower().replace('j', 'i').replace('v', 'u'))

for train, test in ((['P1', 'P2', 'P3'], ['P4', 'P5']), (['P4', 'P5'], ['P1', 'P2', 'P3'])):
    (k1, m1), (k2, m2) = fit(train)
    d = dec(test, (k1, k2))
    n = sum(len(d[r]) for r in test)
    ok = sum(a == b for r in test for a, b in zip(d[r], read[r]))
    print(f'fit on {"+".join(train)}: shifts {k1} (margin {m1}) and {k2} (margin {m2}); frozen key has 1 and 8')
    print(f'  held-out {"+".join(test)}: {ok}/{n} letters = {100*ok/n:.1f}% agree with the reading')
    for r in test:
        print('   ', r, d[r])
