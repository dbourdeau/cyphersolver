"""heldout.py: share of glossed numbers in heldout_118.tsv that the frozen key gives as glossed; control = 2000 random
permutations of the key's letter values over the same numbers."""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import load_key
K = load_key(); D = os.path.join(os.path.dirname(__file__), '..')
P = [l.rstrip('\n').split('\t') for l in open(os.path.join(D, 'heldout_118.tsv'), encoding='utf8') if not l.startswith(('#', 'number'))]
P = [(int(n), g) for n, g, _ in P if g != '-']
def agree(k): return sum(k.get(n) == g or (g == 'u' and k.get(n) == 'w') or (g == 'w' and k.get(n) == 'u') for n, g in P)
hit = agree(K); print('held-out: %d / %d = %.3f' % (hit, len(P), hit / len(P)))
for n, g in P:
    if K.get(n) != g: print('  miss', n, 'gloss', g, 'key', K.get(n))
nums = [n for n in K if K[n] not in ('(null)', '?')]; vals = [K[n] for n in nums]; random.seed(1648); best = 0; tot = 0
for _ in range(2000):
    random.shuffle(vals); a = agree(dict(zip(nums, vals))); best = max(best, a); tot += a
print('control: mean %.2f, best %d of %d' % (tot / 2000, best, len(P)))
