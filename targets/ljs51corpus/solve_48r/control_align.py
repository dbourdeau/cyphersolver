"""Positive control for align_verses.py: encipher verses 1-5 with a random key, add 20 random insertions, rerun the climb."""
import random
from align_verses import V, run
plain = V.replace(' ', ''); letters = sorted(set(plain))
random.seed(7); key = {c: 'S%d' % i for i, c in enumerate(random.sample(letters, len(letters)))}
toks = [key[c] for c in plain]
for _ in range(20): toks.insert(random.randrange(len(toks)), random.choice(list(key.values())))
for seed in range(2):
    sc, _ = run(toks, plain, seed, 1500); print('control seed', seed, 'LCS', sc, round(sc / len(plain), 3), flush=True)
