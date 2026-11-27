"""More restarts for align_verses.py: argv = mode (true|shuf|ctrl) seed."""
import sys, random
from align_verses import V, run, lines
mode, seed = sys.argv[1], int(sys.argv[2]); plain = V.replace(' ', '')
if mode == 'ctrl':
    letters = sorted(set(plain)); random.seed(7); key = {c: 'S%d' % i for i, c in enumerate(random.sample(letters, len(letters)))}
    toks = [key[c] for c in plain]
    for _ in range(20): toks.insert(random.randrange(len(toks)), random.choice(list(key.values())))
else:
    toks = [t for l in lines for t in l if t != '|']
    if mode == 'shuf':
        w = V.split(); random.seed(100 + seed); random.shuffle(w); plain = ''.join(w)
sc, k = run(toks, plain, 10 + seed, 3000)
print(mode, seed, sc, round(sc / len(plain), 3), flush=True)
