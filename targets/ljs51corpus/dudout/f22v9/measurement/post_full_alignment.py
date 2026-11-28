# Exploratoire, APRÈS la mesure : clé apprise sur les 81 signes entiers (non validée), alignement et écarts.
import sys, json, collections
sys.path.insert(0, sys.argv[1])
import procedure as P
seq = P.load_cipher(sys.argv[1] + '/arbitrage.txt')
merged, hamza = P.load_plain(sys.argv[1] + '/clair_23r.txt')
for alph, words in (('merged', merged), ('hamza', hamza)):
  for first in ('lbny', 'bny'):
    pla = P.plain_letters(words, 'asis', first)
    key, pairs, C = P.learn(seq, pla)
    loo = P.loo(seq, pla, pairs, C)
    print('==', alph, first, 'n_letters', len(pla), 'aligned', len(pairs), 'LOO %.3f' % loo)
    if alph == 'merged' and first == 'bny':
        ai = {i: j for i, j in pairs}; aj = {j: i for i, j in pairs}
        rows = []
        for i, c in enumerate(seq):
            rows.append((i + 1, c, pla[ai[i]] if i in ai else '∅', ai.get(i, -1) + 1))
        print('signes nuls :', [(i + 1, c) for i, c in enumerate(seq) if i not in ai])
        print('lettres omises :', [(j + 1, pla[j]) for j in range(len(pla)) if j not in aj])
        inv = collections.defaultdict(collections.Counter)
        for c, v in C.items():
            for l, n in v.items(): inv[l][c] += n
        print('classes par lettre :', {l: dict(v) for l, v in sorted(inv.items())})
        print('lettres par classe :', {c: dict(v) for c, v in sorted(C.items(), key=lambda x: int(x[0][1:]))})
        json.dump(dict(alignment=rows, counts=C), open(sys.argv[2], 'w', encoding='utf8'), ensure_ascii=False, indent=0)
