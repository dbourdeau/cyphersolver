"""Frozen key.tsv against the held-out glosses of fol. 491v; then the same count for 2000 shuffled tables
(the letter values of key.tsv permuted at random over its groups). Standard library only."""
import pathlib, random
R = pathlib.Path(__file__).resolve().parent.parent
key = {}
for l in (R / 'key.tsv').read_text(encoding='utf8').splitlines():
    if l and not l.startswith(('#', 'group')):
        f = l.split('\t')
        if len(f[1]) <= 3: key[f[0]] = f[1].split('/')
pairs = []
for l in (R / 'heldout_f491v.tsv').read_text(encoding='utf8').splitlines():
    if l and not l.startswith(('#', 'cipher')):
        c, g, e = l.split('\t')[:3]; gs, es = c.split('.'), e.split('.')
        assert len(gs) == len(es), (c, e)
        pairs += list(zip(gs, es))
def score(k): return sum(1 for g, e in pairs if e in k.get(g, []))
n = len(pairs); s = score(key)
print(f'held-out letters {n}; frozen key agrees on {s} = {100*s/n:.1f}%')
miss = [(g, e, key.get(g)) for g, e in pairs if e not in key.get(g, [])]
print('disagreements (group, gloss letter, key):', miss)
random.seed(1632); gs = list(key); vals = [key[g] for g in gs]; sc = []
for _ in range(2000):
    random.shuffle(vals); sc.append(score(dict(zip(gs, vals))))
sc.sort(); print(f'shuffled tables: mean {sum(sc)/len(sc):.1f}, max {sc[-1]} of {n}; frozen key beats all {len(sc)}: {s > sc[-1]}')
