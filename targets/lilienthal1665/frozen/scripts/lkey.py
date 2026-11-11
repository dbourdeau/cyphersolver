# Construit K_L depuis PAIRES-LILIENTHAL.tsv : image<TAB>codes (points)<TAB>valeurs alignées (espaces, '_' = non attribué)
import sys, collections
P = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else None
votes = collections.defaultdict(collections.Counter); bad = 0
for ln in open(P, encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    img, cs, vs = ln.rstrip('\n').split('\t')[:3]
    cs = cs.split('.'); vs = vs.split()
    if len(cs) != len(vs): print('LONGUEUR', img, len(cs), len(vs), cs, vs); bad += 1; continue
    for c, v in zip(cs, vs):
        if v != '_': votes[c][v] += 1
conf = {c: v for c, v in votes.items() if len(v) > 1}
for c, v in sorted(conf.items(), key=lambda x: int(x[0])): print('CONFLIT', c, dict(v))
print(len(votes), 'codes,', sum(sum(v.values()) for v in votes.values()), 'occurrences, conflits', len(conf), 'erreurs', bad)
by = collections.defaultdict(list)
for c, v in votes.items(): by[v.most_common(1)[0][0]].append(int(c))
print(' '.join(f'{k}:{sorted(v)}' for k, v in sorted(by.items())))
if out:
    with open(out, 'w', encoding='utf-8') as f:
        f.write('# K_L — Lilienthal, tirée des paires chiffré/glose (PAIRES-LILIENTHAL.tsv). code\tvaleur\toccurrences\n')
        for c in sorted(votes, key=int):
            if c in conf: continue
            v, n = votes[c].most_common(1)[0]; f.write(f'{c}\t{v}\t{n}\n')
