"""Score every set of three shifts (out of 24) on the printed ciphertext, and on shuffled ciphertext as control."""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import poly, multishift as ms
segs, labels = poly.read_ct(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'transcription', 'pass1.txt'))
res = []
for t in itertools.combinations(range(24), 3):
    sc, _ = ms.run(segs, t); res.append((sc, t))
res.sort(reverse=True)
print('real top 10:', [(round(s,3), t) for s, t in res[:10]])
print('real median:', round(res[len(res)//2][0], 3))
for seed in (1, 2, 3):
    allc = list(''.join(segs)); random.Random(seed).shuffle(allc); it = iter(allc)
    sh = [''.join(next(it) for _ in s) for s in segs]
    r2 = sorted(((ms.run(sh, t)[0], t) for t in itertools.combinations(range(24), 3)), reverse=True)
    print(f'shuffled {seed} top 3:', [(round(s,3), t) for s, t in r2[:3]])
