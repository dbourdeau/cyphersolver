"""c. 42r: key from the pairs, frozen on L00-L06; held-out on L07-L13; reading_marked_c42r.txt from the alignment.
Writes key_c42r.tsv, decryption_c42r.txt, reading_marked_c42r.txt, validation/heldout_c42r.txt"""
import sys, math, random, collections, re
sys.path.insert(0, __import__('os').path.dirname(__file__))
from learn import align, SEED, NULL, SKIP
def rd(f): return {l.split('\t')[0]: l.rstrip('\n').split('\t')[1] for l in open(f, encoding='utf8') if l.startswith('c0')}
T, G = rd('transcription_c42r.txt'), rd('clear_c42r.txt')
PAIRS = {('o', 'v'), ('o', '+'), ('n', 'o'), ('h', 'c')}  # raised o + v (r), o + (e), n + raised o (s), n + raised c (m): one sign each in this hand
def merge(seq):
    out, i = [], 0
    while i < len(seq):
        a = seq[i].rstrip('?'); b = seq[i + 1].rstrip('?') if i + 1 < len(seq) else None
        if (a, b) in PAIRS:
            out.append(a + '_' + b + ('?' if seq[i].endswith('?') or seq[i + 1].endswith('?') else '')); i += 2
        else:
            out.append(seq[i]); i += 1
    return out
def letters(s): return re.sub(r'[^a-z]', '', s.lower())
# Sign runs that carry the writer's superscript 6 or 4 and have no decipherment above them, read on the image (not from
# the clear): validation/unglossed_c42r.tsv. They may only be left unread by the alignment. The held-out score below does
# not use them (plain alignment, as before).
FORCED = collections.defaultdict(set)
for l in open('validation/unglossed_c42r.tsv', encoding='utf8'):
    if l.startswith('c0'):
        n, a, b = l.split('	')[:3]; FORCED[n] |= set(range(int(a), int(b) + 1))
def unit_forced(n):
    """indices of merged units that contain a forced raw sign"""
    out, i = set(), 0
    for k, u in enumerate(merge(T[n].split())):
        w = len(u.split('_')) if '_' in u.rstrip('?') else 1
        if FORCED[n] & set(range(i, i + w)): out.add(k)
        i += w
    return out
def alignf(S, L, P, forced):
    n, m = len(S), len(L); INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF: continue
            if i < n and d + NULL < D[i + 1][j]: D[i + 1][j] = d + NULL; B[i + 1][j] = (i, j, S[i], '')
            if j < m and d + SKIP < D[i][j + 1]: D[i][j + 1] = d + SKIP; B[i][j + 1] = (i, j, '', L[j])
            for k in (1, 2):
                if i + k <= n and j < m and not forced & set(range(i, i + k)):
                    u = ' '.join(S[i:i + k]); c = d + P(u, L[j]) + (0.8 if k == 2 else 0)
                    if c < D[i + k][j + 1]: D[i + k][j + 1] = c; B[i + k][j + 1] = (i, j, u, L[j])
    path = []; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, u, l = B[i][j]; path.append((u, l)); i, j = pi, pj
    return D[n][m], path[::-1]
def em(lines, it=8):
    cnt = collections.Counter({(u, l): 5 for u, l in SEED.items()})
    for _ in range(it):
        tot = collections.Counter()
        for (u, l), c in cnt.items(): tot[u] += c
        P = lambda u, l, cnt=cnt, tot=tot: -math.log((cnt[(u, l)] + 0.05) / (tot[u] + 3.3))
        new = collections.Counter(); paths = {}
        for n in lines:
            S = [x.rstrip('?') for x in merge(T[n].split())]
            _, p = alignf(S, letters(G[n]), P, unit_forced(n)); paths[n] = p
            for u, l in p:
                if u and l: new[(u, l)] += 1
        cnt = new + collections.Counter({(u, l): 1 for u, l in SEED.items()})
    return new, paths
names = sorted(T)
frozen, _ = em([n for n in names if n <= 'c0L06'])
full, paths = em(names)
fk = collections.defaultdict(collections.Counter)
for (u, l), c in frozen.items(): fk[u][l] += c
# held-out: align L07-L13 with the frozen key only (no re-estimation)
def P_of(k):
    return lambda u, l: 6.0 if u not in k else -math.log((k[u][l] + 0.05) / (sum(k[u].values()) + 1.5))
def score(k):
    h = t = 0
    for n in names:
        if n <= 'c0L06': continue
        L = letters(G[n]); _, p = align([x.rstrip('?') for x in merge(T[n].split())], L, P_of(k)); t += len(L)
        h += sum(1 for u, l in p if u and l and u in k and k[u].most_common(1)[0][0] == l)
    return h, t
h, t = score(fk); random.seed(2); us = list(fk); vs = [fk[u] for u in us]; sh = []
for _ in range(500):
    random.shuffle(vs); sh.append(score(dict(zip(us, vs)))[0])
msg = (f'held-out c. 42r L07-L13 (key frozen on L00-L06): {t} clear letters; frozen key top value matches {h} '
       f'({100*h/t:.1f}%); 500 shuffled tables: mean {100*sum(sh)/len(sh)/t:.1f}%, max {100*max(sh)/t:.1f}%')
print(msg); open('validation/heldout_c42r.txt', 'w', encoding='utf8').write(msg + '\n')
fu = collections.defaultdict(collections.Counter)
for (u, l), c in full.items(): fu[u][l] += c
with open('key_c42r.tsv', 'w', encoding='utf8') as f:
    f.write('# c. 42r key from the pairs (scripts/read42r.py). unit = sign or sign pair (names: validation/legend.md).\n'
            '# values: letter:count over all 14 lines; frozen: letter:count on L00-L06 only (the frozen key).\n'
            '# check_marks.py accepts a value seen at least twice; a value seen once must be marked in the reading.\nunit\tvalues\tfrozen\n')
    for u, c in sorted(fu.items(), key=lambda x: -sum(x[1].values())):
        f.write(f"{u}\t{' '.join(f'{l}:{k}' for l, k in c.most_common())}\t{' '.join(f'{l}:{k}' for l, k in fk[u].most_common())}\n")
# reading_marked from the full alignment
ok = {u: {l for l, k in c.items() if k >= 2} for u, c in fu.items()}
rl, dl = [], []
for n in names:
    S = merge(T[n].split()); i = 0; toks = []; words = G[n].split(); wl = [len(letters(w)) for w in words]
    p = paths[n]; li = 0; bounds = set(); acc = 0
    for w in wl: acc += w; bounds.add(acc)
    for u, l in p:
        if u:
            k = len(u.split()); raw = S[i:i + k]; i += k; dq = any(x.endswith('?') for x in raw); un = '_'.join(x.rstrip('?') for x in raw)
            if not l: toks.append(f'[{un}?]')
            elif dq: toks.append(f'{{?{un}={l}}}')
            elif l in ok.get(u, ()): toks.append(f'{un}={l}')
            else: toks.append(f'{{{un}={l}}}')
        else: toks.append(f'{{+{l}}}')
        if l:
            li += 1
            if li in bounds and li != sum(wl): toks.append('|')
    rl.append(f'{n}\t' + ' '.join(toks))
    dl.append(f'{n}\t' + ' '.join(('/'.join(x for x, _ in fu[u.replace(" ", " ")].most_common(2)) if u in fu else '?') for u in [s.rstrip('?') for s in T[n].split()]))
open('reading_marked_c42r.txt', 'w', encoding='utf8').write(
    '# c. 42r reading, unit by unit: unit=letter (value seen >= 2 times); {unit=x} value seen once; {?unit=x} on a doubtful\n'
    '# sign; {+x} letter with no sign; [unit?] sign not covered by the clear (unglossed or unexplained); | word break.\n' + '\n'.join(rl) + '\n')
open('decryption_c42r.txt', 'w', encoding='utf8').write(
    '# c. 42r decryption, sign by sign with the full c. 42r key (top two values per sign; ? = sign not in the key).\n'
    '# Sign pairs (o +, n o, h c) are units in the reading; here each sign is shown alone.\n' + '\n'.join(dl) + '\n')
