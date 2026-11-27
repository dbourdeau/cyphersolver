"""Sense-steered choice among look-alikes: align each cipher line with its reading, letting every sign take any of
the classifier's top six labels (cost -log p), be dropped as a non-sign (cost 4), and letting the reading skip
a letter (cost 6). The chosen labels go to work/forced_<letter>.tsv with a flag per sign:
   = machine top label kept     ~ another of its top six chosen (a look-alike steered by the reading)
   - dropped                    ! a mismatch remains (needs the eye)
Only signs flagged ~ or - change the machine transcription; every ! goes to the eye pass (diff_strips.py).

    python scripts/forced.py 13oct
"""
import sys, math, pickle, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from transcribe import emit_letters, toks
L = sys.argv[1]
out, probs = pickle.load(open(ROOT / 'work/machine.pkl', 'rb'))
reading = {}
for l in open(ROOT / f'reading_{L}.txt', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, t = l.rstrip('\n').split('\t'); reading[k] = t
beam = {}
for l in open(ROOT / f'work/beam_{L}.tsv', encoding='utf8'):
    f = l.rstrip('\n').split('\t'); beam[f'{f[0]}.{f[1]}'] = (f[0], int(f[1]), [int(x) for x in f[6].split()], f[3].split())
DROP, SKIP, MIS = 4.0, 6.0, 5.0
res = []; nchg = nmis = ndrop = 0; total = 0
for k, (p, j, idx, labs) in beam.items():
    rd = toks(reading.get(k, ''))
    cands = []
    for n, i in enumerate(idx):
        c = [(lab, pr) for lab, pr in probs[(p, j)][i]][:6]
        if labs[n] not in [x for x, _ in c]: c = [(labs[n], 0.3)] + c
        cands.append([(lab, -math.log(pr + 0.01), emit_letters(lab)) for lab, pr in c])
    N, M = len(cands), len(rd)
    INF = 1e9
    D = [[INF] * (M + 1) for _ in range(N + 1)]; B = [[None] * (M + 1) for _ in range(N + 1)]
    D[0][0] = 0
    for i in range(N + 1):
        for jj in range(M + 1):
            v = D[i][jj]
            if v >= INF: continue
            if jj < M and v + SKIP < D[i][jj + 1]:
                D[i][jj + 1] = v + SKIP; B[i][jj + 1] = ('skip', i, jj, None)
            if i == N: continue
            if v + DROP < D[i + 1][jj]:
                D[i + 1][jj] = v + DROP; B[i + 1][jj] = ('drop', i, jj, None)
            for lab, c, e in cands[i]:
                n = len(e)
                if jj + n > M:
                    # allow mismatch by emitting past the end: treat extra letters as mismatches
                    continue
                mis = sum(1 for a, b in zip(e, rd[jj:jj + n]) if a != b)
                w = v + c + MIS * mis
                if w < D[i + 1][jj + n]:
                    D[i + 1][jj + n] = w; B[i + 1][jj + n] = ('lab', i, jj, (lab, mis))
    # backtrack
    i, jj = N, M; ch = [None] * N; flags = [None] * N
    while i > 0 or jj > 0:
        b = B[i][jj]
        if b is None: break
        kind, pi, pj, x = b
        if kind == 'lab':
            lab, mis = x; ch[pi] = lab
            flags[pi] = '!' if mis else ('=' if lab == labs[pi] else '~')
        elif kind == 'drop':
            ch[pi] = labs[pi]; flags[pi] = '-'
        else:
            # reading letter not given by any sign: mark neighbours
            if pi > 0 and flags[pi - 1] in (None, '=', '~'): flags[pi - 1] = '!'
        i, jj = pi, pj
    for n in range(N):
        if ch[n] is None: ch[n] = labs[n]; flags[n] = '!'
    total += N; nchg += flags.count('~'); ndrop += flags.count('-'); nmis += flags.count('!')
    res.append((k, p, j, idx, labs, ch, flags))
with open(ROOT / f'work/forced_{L}.tsv', 'w', encoding='utf8') as f:
    for k, p, j, idx, labs, ch, flags in res:
        f.write('\t'.join([k, ' '.join(labs), ' '.join(ch), ''.join(flags), ' '.join(map(str, idx))]) + '\n')
print(f'{L}: {total} signs; look-alike changes {nchg}, dropped {ndrop}, still mismatched {nmis}')
