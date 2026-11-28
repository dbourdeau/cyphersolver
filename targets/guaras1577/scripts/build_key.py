"""Run from targets/guaras1577 with TSPLIT=1 (as frozen). Build the 1577 key by aligning the cipher (transcription_final.txt) with Kervyn's printed text.
Held-out lines P2L01-P2L07 are never read here: part 1 = P1L01-P1L33 aligned from the start of the print,
part 2 = P2L08-P2L14 aligned to the end of the print. Viterbi training (alignment -> counts -> costs), 12 rounds.
Writes build/key_1577.json and build/alignment_*.tsv."""
import re, json, math, collections, sys, os
os.makedirs('build', exist_ok=True)
sys.path.insert(0, 'scripts')
from kervyn_units import units
TRANS = 'transcription/transcription_final_v2.txt'
HELDOUT = {f'P2L{n:02d}' for n in range(1, 8)}
def load():
    lines = {}
    for ln in open(TRANS, encoding='utf-8'):
        m = re.match(r'(P[12]L\d\d):\s*(.*)$', ln.rstrip('\n'))
        if not m: continue
        s = re.sub(r'\[\[.*?\]\]', ' ', m.group(2))
        toks = []
        for t in s.split():
            if t == '|': continue
            if t.startswith('W1'): toks += ['uy', 'T' + t[2:]]      # u-y cluster + crossed tall stroke
            elif t.startswith('W2'): toks += ['uy', 'P' + t[2:]]    # u-y cluster + looped tall stroke
            else: toks.append(t)
        out = []
        for t in toks:                                              # u followed by y = the same u-y cluster
            if t == 'y' and out and out[-1] == 'u': out[-1] = 'uy'
            else: out.append(t)
        lines[m.group(1)] = out
    return lines
L = load(); U = units()
import os
if os.environ.get('TSPLIT'):   # optional: crossed-bar t (class C in work_D/class_t.tsv) as its own sign t2
    for ln in open('transcription/class_t.tsv'):
        k, c = ln.split(); lab, i = k.split('.')
        if c == 'C': L[lab][int(i)] = 't2'
assert not (HELDOUT & set()), 'never'
p1 = [(lab, k, t) for lab in sorted(L) if lab.startswith('P1') for k, t in enumerate(L[lab])]
p2 = [(lab, k, t) for lab in sorted(L) if lab.startswith('P2') and lab not in HELDOUT for k, t in enumerate(L[lab])]
LET = sorted({u for u in U if len(u) == 1})
isnum = lambda t: t.startswith('#')
BIG = 1e9
PAIR, DOUBLE = 1.5, 1.5      # extra cost for two tokens -> one letter, one token -> two letters
def costs(counts):
    C = {}
    for s, cnt in counts.items():
        tot = sum(cnt.values())
        C[s] = (tot, {e: c for e, c in cnt.items()})
    return C
def mcost(C, s, l, it):
    """cost of cipher unit s (token or 'a+b' pair) emitting plain string l (1 or 2 letters)."""
    if it == 0: return 2.5 if len(l) == 1 and '+' not in s else 9.0
    if s not in C: return 3.0 if '+' not in s else 6.0
    tot, cnt = C[s]
    return min(-math.log((cnt.get(l, 0) + 0.1) / (tot + 0.1 * 30)), 6.5)
SKIPC, SKIPP, SKIPW = 4.5, 4.5, 7.0
def align(toks, U, C, it, anchor):
    n, m = len(toks), len(U)
    ratio = m / max(1, n) if anchor == 'start' else None
    D = [[BIG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    if anchor == 'start': D[0][0] = 0
    else:
        for j in range(m + 1): D[0][j] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= BIG: continue
            if i < n:   # skip cipher token
                if d + SKIPC < D[i+1][j]: D[i+1][j] = d + SKIPC; B[i+1][j] = (i, j, 'nullc')
            if j < m:   # skip plain unit
                c = SKIPW if len(U[j]) > 1 else SKIPP
                if d + c < D[i][j+1]: D[i][j+1] = d + c; B[i][j+1] = (i, j, 'skipp')
            if i < n and j < m:
                t, u = toks[i], U[j]
                if isnum(t):
                    if len(u) > 1:
                        if d + 0.5 < D[i+1][j+1]: D[i+1][j+1] = d + 0.5; B[i+1][j+1] = (i, j, 'code')
                    else:
                        for k in range(2, 15):
                            if j + k > m or any(len(x) > 1 for x in U[j:j+k]): break
                            c = d + 3 + 0.1 * k
                            if c < D[i+1][j+k]: D[i+1][j+k] = c; B[i+1][j+k] = (i, j, 'code')
                elif u == '{GAP}':
                    for k in range(1, 61):
                        if i + k > n: break
                        c = d + 1 + 0.3 * k
                        if c < D[i+k][j+1]: D[i+k][j+1] = c; B[i+k][j+1] = (i, j, 'gap')
                elif len(u) == 1:
                    c = d + mcost(C, t, u, it)
                    if c < D[i+1][j+1]: D[i+1][j+1] = c; B[i+1][j+1] = (i, j, 'match')
                    if j + 1 < m and len(U[j+1]) == 1:          # one token, two letters
                        c = d + DOUBLE + mcost(C, t, u + U[j+1], it)
                        if c < D[i+1][j+2]: D[i+1][j+2] = c; B[i+1][j+2] = (i, j, 'match2')
                    if i + 1 < n and not isnum(toks[i+1]):     # two tokens, one letter
                        c = d + PAIR + mcost(C, t + '+' + toks[i+1], u, it)
                        if c < D[i+2][j+1]: D[i+2][j+1] = c; B[i+2][j+1] = (i, j, 'pair')
    if anchor == 'start': jend = min(range(m + 1), key=lambda j: D[n][j])
    else: jend = m
    path = []; i, j = n, jend
    while B[i][j] is not None:
        pi, pj, op = B[i][j]; path.append((pi, i, pj, j, op)); i, j = pi, pj
    return path[::-1], D[n][jend], (j, jend)
def run():
    # progressive training: part 1 is aligned on a growing prefix (40, 80, 160 ... tokens) so that the first
    # correct local alignments teach the model before drift sets in; then both parts in full.
    C = {}; counts = None; it = 0
    sched = [(w, r) for w in (40, 80, 160, 320, 640, 1280) for r in range(3)] + [(None, r) for r in range(6)]
    for w, r in sched:
        counts = collections.defaultdict(collections.Counter); res = {}
        parts = (('part1', p1, 'start'),) if w else (('part1', p1, 'start'), ('part2', p2, 'end'))
        for name, part, anchor in parts:
            part = part[:w] if w else part
            toks = [t for _, _, t in part]
            Uw = U[:int(w * 1.3) + 20] if w else U
            path, cost, span = align(toks, Uw, C, it, anchor); res[name] = (path, cost, span, part)
            for i0, i1, j0, j1, op in path:
                if op == 'match': counts[toks[i0]][U[j0]] += 1
                elif op == 'match2': counts[toks[i0]][U[j0] + U[j0+1]] += 1
                elif op == 'pair': counts[toks[i0] + '+' + toks[i0+1]][U[j0]] += 1
        C = costs(counts); it += 1
        print(w, r, {k: (round(v[1], 1), round(v[1] / len(v[3]), 2), v[2]) for k, v in res.items()}, flush=True)
    return res, counts
if __name__ == "__main__":
    res, counts = run()
    key = {}
    for s, cnt in sorted(counts.items()):
        if isnum(s): continue
        l, c = cnt.most_common(1)[0]; tot = sum(cnt.values())
        key[s] = {'plain': l, 'aligned': tot, 'agree': c, 'others': dict(cnt.most_common()[1:4])}
    codes = collections.defaultdict(list)
    for name, (path, cost, span, part) in res.items():
        with open(f'build/alignment_{name}.tsv', 'w') as fh:
            fh.write('line\tpos\ttoken\top\tplain\n')
            for i0, i1, j0, j1, op in path:
                pl = ''.join(U[j0:j1]); 
                for i in range(i0, i1) if i1 > i0 else [None]:
                    if i is None: fh.write(f'-\t-\t-\t{op}\t{pl}\n'); continue
                    lab, k, t = part[i]; fh.write(f'{lab}\t{k}\t{t}\t{op}\t{pl if i == i0 else ""}\n')
                    if op == 'code': codes[t].append(pl)
    spans = {k: v[2] for k, v in res.items()}
    json.dump({'_about': 'Key of Guaras 1577 rebuilt by aligning transcription_final.txt (held-out lines P2L01-07 excluded) with Kervyn IX no. 3359 (Viterbi training, scripts/build_key.py). plain = most frequent aligned letter.',
               'key': key, 'codes': {k: v for k, v in codes.items()}, 'plain_spans_used': spans,
               'heldout_reference_units': [spans['part1'][1], spans['part2'][0]]},
              open('build/key_1577.json', 'w'), indent=1, ensure_ascii=False)
    print('signs', len(key), 'spans', spans)
