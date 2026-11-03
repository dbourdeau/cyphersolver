"""Apply key_1814.tsv plus dudout/key_1811_additions.tsv to transcription.tsv; print the passages and the coverage."""
import re
from pathlib import Path
H = Path(__file__).parent
key = {}
for f in (H.parent / 'key_1814.tsv', H / 'key_1811_additions.tsv'):
    for l in open(f, encoding='utf8'):
        if l.startswith(('#', 'group')) or not l.strip(): continue
        g, v = l.split('\t')[:2]; key.setdefault(int(g), v)
rows = [l.rstrip('\n').split('\t') for l in open(H.parent / 'transcription.tsv', encoding='utf8')
        if not l.startswith(('#', 'passage'))]
n = k = 0; cur = None
for r in rows:
    if r[0] != cur:
        cur = r[0]; print(f'\n{cur}  {r[4] if len(r) > 4 else ""}')
    out = []
    for t in r[3].split():
        m = re.match(r'(\[)?(\d+)', t)
        if not m: out.append(t); continue
        if m.group(1): continue
        g = int(m.group(2)); n += 1
        if g in key: k += 1; out.append(key[g] + ('s' if '°' in t else ''))
        else: out.append(f'[{g}]')
    print(f'  {r[1]} {r[2]:>3}: ' + ' '.join(out))
print(f'\ncovered {k}/{n} = {k/n:.3f}')
