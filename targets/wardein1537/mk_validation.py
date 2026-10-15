"""Build validation.tsv for docs/_validate.py from R9414 (German, the largest of the three records).

Signs: r9414/transcription_p12.txt + transcription_p34.txt (the current re-transcriptions), P5 from transcription_v2.txt.
Per-sign values: the raw decrypts cp12/dec_p12_new.txt, cp12/dec_p34_new.txt (P5: decrypt_v2.txt), i.e. keyb.txt with
the look-alike alternatives chosen by the Viterbi pass. Signs are paired with decrypt letters by a small DP (a sign
may also be dropped as a null). Then each decrypt letter is kept only where it agrees with the current reading
r9414/reading_v5.txt (difflib matching blocks per line); letters in unread words ([..n]) or changed by the reading
are written '?'. The code sign e (= F.G.) and the word signs K are written '?'.
R9403 is left out (its sign transcription was rebuilt from the reading, so it cannot test it); R9415 (Latin,
another system) is left out because one validation file takes one key and one language."""
import re, os, difflib
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r9414')

def load(fn, sign):
    d = {}; pg = None
    for l in open(os.path.join(H, fn), encoding='utf8'):
        if l.startswith('=='): pg = l.split()[1]; continue
        m = re.match(r'(\d\d) (.*)', l)
        if not m: continue
        s = re.sub(r'\[F\.G\.\]', '§', m.group(2)) if not sign else m.group(2)
        s = re.sub(r'\[[^\]]*\]', '', s)
        if sign: s = re.sub(r'\{[^}]*\}', '', s).replace('o/', '0')
        d[(pg, m.group(1))] = s.strip()
    return d

T = {}; D = {}
for f in ('transcription_p12.txt', 'transcription_p34.txt'): T.update(load(f, 1))
for f in ('cp12/dec_p12_new.txt', 'cp12/dec_p34_new.txt'): D.update(load(f, 0))
for k, v in load('transcription_v2.txt', 1).items():
    if k not in T: T[k] = v
for k, v in load('decrypt_v2.txt', 0).items():
    if k not in D: D[k] = v

cand = {}
for fn in ('keyb.txt', 'alt_v2.txt', 'cp12/alt_p12.txt'):
    for kv in re.split(r'[,\s]+', open(os.path.join(H, fn), encoding='utf8').read().strip()):
        if not kv: continue
        k, v = ('=', kv[2:]) if kv.startswith('==') else kv.split('=', 1)
        cand.setdefault(k, set()).update(x for x in v.split('/') if len(x) == 1)

def dp(signs, dec):
    n, m = len(signs), len(dec)
    INF = 1e9
    C = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    C[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            c = C[i][j]
            if c >= INF: continue
            if i < n and j < m:
                s, ch = signs[i], dec[j]
                ok = ch in cand.get(s, ()) or (s == '?' and ch == '?') or (s == 'e' and ch == '§')
                nc = c + (0 if ok else 1)
                if nc < C[i+1][j+1]: C[i+1][j+1] = nc; B[i+1][j+1] = (i, j, 'pair')
            if i < n:
                nc = c + (0.3 if signs[i] in ('e', 'K', '/', '?') else 1.2)
                if nc < C[i+1][j]: C[i+1][j] = nc; B[i+1][j] = (i, j, 'null')
            if j < m:
                nc = c + 1.2
                if nc < C[i][j+1]: C[i][j+1] = nc; B[i][j+1] = (i, j, 'extra')
    out = [None] * n; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, t = B[i][j]
        if t == 'pair': out[pi] = pj
        i, j = pi, pj
    return out

R = {}
for l in open(os.path.join(H, 'reading_v5.txt'), encoding='utf8'):
    m = re.match(r'(P\d)\.(\d\d) (.*)', l)
    if not m: continue
    s = re.sub(r'<[^>]*>', '', m.group(3)).replace('F.G.', '§')
    s = re.sub(r'\[\.\.\d\]', '#', s).lower()
    R[(m.group(1), m.group(2))] = ''.join(c for c in s if c.isalpha() or c in '#§')

def nz(c): return {'v': 'u', 'j': 'i', 'y': 'i'}.get(c, c)

rows = []
for k in sorted(T, key=lambda k: (k[0], k[1])):
    signs = list(T[k]); dec = D.get(k, ''); rd = R.get(k, '')
    if not signs: continue
    pos = dp(signs, dec)
    dn = ''.join(nz(c) for c in dec); rn = ''.join(nz(c) for c in rd)
    ok = set()
    for a, b, size in difflib.SequenceMatcher(None, dn, rn, autojunk=False).get_matching_blocks():
        ok.update(range(a, a + size))
    for s, p in zip(signs, pos):
        if s in ('e', 'K'): rows.append((s, '?'))
        elif p is None: rows.append((s, '-' if s not in ('?',) else '?'))
        elif p in ok and dec[p].isalpha(): rows.append((s, dec[p]))
        else: rows.append((s, '?'))
with open(os.path.join(os.path.dirname(H), 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: de-1500s\n# source: R9414 only: r9414/transcription_p12/_p34/_v2 signs, cp12/dec_*_new.txt + decrypt_v2.txt per-sign values, kept where they agree with r9414/reading_v5.txt (mk_validation.py)\n')
    f.write('# note: R9403 (sign codes rebuilt from its reading) and R9415 (Latin, another system) left out; signs the DP leaves unpaired are written as nulls (-); e (F.G.) and K code signs unread\n')
    for s, r in rows: f.write(f'{s}\t{r}\n')
import collections
c = collections.Counter('read' if r not in '?-' else r for s, r in rows); print(len(rows), c)
