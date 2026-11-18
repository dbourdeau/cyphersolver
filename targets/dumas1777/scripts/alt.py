"""alt.py N [N ...]: for each cipher number show the key letter and the letters at plausible misreadings/slips:
N-1, N+1 (Dumas counting slip), and single-digit confusions 1/7, 3/5, 4/9, 0/6, 2/3, 3/8, 5/6 (scribe/reader misreading)."""
import json, os, sys, unicodedata
K = {int(k): v for k, v in json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'key', 'key_positions.json')))['positions'].items()}
L = lambda n: (unicodedata.normalize('NFD', K[n])[0].lower() if n in K else '-')
conf = {'1': '7', '7': '1', '3': '58', '5': '36', '4': '9', '9': '4', '0': '6', '6': '05', '2': '3', '8': '3'}
for a in sys.argv[1:]:
    n = int(a); s = str(n); alts = set()
    for i, d in enumerate(s):
        for r in conf.get(d, ''):
            alts.add(int(s[:i] + r + s[i+1:]))
    print(f'{n}={L(n)}  slips: {n-1}={L(n-1)} {n+1}={L(n+1)}  misreads: ' + ' '.join(f'{m}={L(m)}' for m in sorted(alts) if 0 < m <= 682))
