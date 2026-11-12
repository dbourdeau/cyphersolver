"""declines.py TRANSCRIPTION KEY_CODES_TSV : line-by-line decoding (codes shown as WORD-with-caps, letters lower)."""
import sys, re
sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/protocol')
from measure import SIGNS, NULLS, load_key
K = load_key(sys.argv[2])
for line in open(sys.argv[1], encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    f = line.split(); out = []
    for t in f[1:]:
        u = t.rstrip('?')
        if t.startswith('='): out.append('«' + t[1:] + '»')
        elif u in NULLS: out.append('·')
        elif u in SIGNS: out.append(SIGNS[u])
        elif u in K: out.append(' ' + K[u].upper() + ' ')
        elif t.startswith('['): out.append(' … ')
        else: out.append(' ?' + u + ' ')
    print(f[0], re.sub(' +', ' ', ''.join(out)).strip())
