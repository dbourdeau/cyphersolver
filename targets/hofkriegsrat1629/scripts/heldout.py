"""Held-out test: apply key_frozen.tsv to Donath's glossed specimens, count sign-letter agreement.
Usage: python -I heldout.py <heldout_specimens.tsv> <key_frozen.tsv>"""
import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from decrypt import load_key
k = load_key(sys.argv[2]); tot = ok = 0; per = {}; miss = []
for ln in open(sys.argv[1], encoding='utf8'):
    if ln.startswith('#') or not ln.strip(): continue
    doc, toks, gloss = ln.rstrip('\n').split('\t'); toks = toks.split()
    if len(toks) != len(gloss):
        miss.append((doc, ' '.join(toks), gloss, 'length differs')); continue
    for t, g in zip(toks, gloss):
        v = k.get(t, '?'); good = (v == g) or ({v, g} <= {'u', 'v'})
        tot += 1; ok += good; d = per.setdefault(doc, [0, 0]); d[0] += 1; d[1] += good
        if not good: miss.append((doc, t, g, 'key gives ' + v))
for d, (n, g) in per.items(): print(f'{d}: {g}/{n} = {g/n:.3f}')
print(f'all: {ok}/{tot} = {ok/tot:.3f}')
for m in miss: print('  mismatch', *m)
