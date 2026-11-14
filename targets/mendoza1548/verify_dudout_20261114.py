#!/usr/bin/env python3
"""mendoza1548: independent decode (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY key_1548.md (the 'value used' column of the sign table), the two rules stated in NOTES.md/key_1548.md
for the dotted signs (`ꝺ .` = que/da, `e .` = lo) and transcription/d1_transcription.md. It does not import
dec1548.py. It then (1) compares its decode token by token with decryption/d1_decode.txt and (2) aligns its decode
with the letters of decryption/d1_reading.md and lists the reading's letters that the decode does not give,
inside and outside the [ ] brackets.

    python3 verify_dudout_20261114.py targets/mendoza1548
"""
import re, sys, unicodedata, pathlib
T = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
N = lambda s: unicodedata.normalize('NFC', s)

key = {}
for l in N((T / 'key_1548.md').read_text(encoding='utf8')).split('\n'):
    m = re.match(r'\|\s*`([^`]+)`\s*\|\s*\d+\s*\|\s*([^|]*?)\s*\|', l)
    if m: key[m.group(1)] = m.group(2)

def val(tok, dotted):
    if tok == 'ꝺ' and dotted: return ['que', 'da']
    if tok == 'e' and dotted: return ['lo']
    v = key.get(tok)
    if v is None or v in ('—', ''): return None            # no value
    if v in ('(null)', '–'): return ['']
    if v.startswith('['): return [v.strip('[]')]
    return v.split('/')

lines = []
for l in N((T / 'transcription' / 'd1_transcription.md').read_text(encoding='utf8')).split('\n'):
    m = re.match(r'^([LM]\d+)\t[^\t]*\t(.*)$', l)
    if m: lines.append((m.group(1), m.group(2).split()))

dec = {}
for lab, toks in lines:
    out = []
    for i, t in enumerate(toks):
        if t == '.': continue
        dotted = i + 1 < len(toks) and toks[i + 1] == '.'
        out.append((t, val(t, dotted)))
    dec[lab] = out

def show(v, t):
    if v is None: return f'[{t}]'
    if v == ['']: return ''
    return '/'.join(v) if len(v[0].split()) == 1 else f'[{v[0]}]'

# (1) against the published decode
pub = {}
dl = N((T / 'decryption' / 'd1_decode.txt').read_text(encoding='utf8')).split('\n')
for i, l in enumerate(dl):
    m = re.match(r'^([LM]\d+)\s', l)
    if m and i + 1 < len(dl): pub[m.group(1)] = dl[i + 1].split()
tot = agree = 0; diffs = []
for lab, out in dec.items():
    mine = [show(v, t) for t, v in out if show(v, t) != '']
    mine = ' '.join(mine).split()
    p = pub.get(lab, [])
    import difflib
    sm = difflib.SequenceMatcher(a=mine, b=p, autojunk=False)
    tot += len(mine); agree += sum(b.size for b in sm.get_matching_blocks())
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != 'equal': diffs.append((lab, ' '.join(mine[a1:a2]), ' '.join(p[b1:b2])))
n_tok = sum(len(o) for o in dec.values()); n_none = sum(1 for o in dec.values() for t, v in o if v is None)
n_two = sum(1 for o in dec.values() for t, v in o if v and len(v) > 1)
print(f'tokens {n_tok}, without value {n_none}, with two values {n_two}')
print(f'(1) decode vs d1_decode.txt: {agree}/{tot} items agree')
for d in diffs: print('   ', d)

# (2) letters of the reading against the decode (best option per token, edit-distance alignment)
rd = N((T / 'decryption' / 'd1_reading.md').read_text(encoding='utf8'))
def fold(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if c.isalpha() and not unicodedata.combining(c))
letters, inbr = [], []
for m in re.finditer(r'\[([^\]]*)\]|([^\[]+)', rd):
    seg = m.group(1) if m.group(1) is not None else m.group(2)
    for c in fold(seg): letters.append(c); inbr.append(m.group(1) is not None)
R = ''.join(letters)
def pairs(fn):
    g = {}
    for l in N((T / fn).read_text(encoding='utf8')).split('\n'):
        if not l or l.startswith('#'): continue
        lab, rest = l.split('\t', 1)
        items = [x for x in rest.split() if x != '.']
        g[lab] = [x.rsplit('=', 1) for x in items]
    return g
GL, CR = pairs('key_pairs_gloss.txt'), pairs('key_pairs_crib.txt')
def extra(src, lab, k, t):
    """value paired with the k-th non-dot sign of line lab, when the sign names agree"""
    row = src.get(lab)
    if not row or k >= len(row): return []
    s_, v_ = row[k]
    if s_.rstrip('.') != t or v_ in ('?', '–', '') or '?' in v_: return []
    return [fold(v_)]
def build(use_gl, use_cr):
    seq = []
    for lab, out in dec.items():
        for k, (t, v) in enumerate(out):
            o = [] if v is None else [fold(x) for x in v if x]
            if v == [''] and not (use_gl or use_cr): continue
            if use_gl: o += extra(GL, lab, k, t)
            if use_cr: o += extra(CR, lab, k, t)
            o = list(dict.fromkeys(x for x in o if x))
            if v == [''] and not o: continue
            seq.append((lab, t, o or ['?']))
    return seq
def run(seq):
    INF = 10**9; n, m = len(seq), len(R)
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0] = list(range(m + 1))
    for i in range(1, n + 1): D[i][0] = D[i-1][0] + 1; B[i][0] = ('skip',)
    for j in range(1, m + 1): B[0][j] = ('extra',)
    for i in range(1, n + 1):
        opts = seq[i-1][2]
        for j in range(0, m + 1):
            best = D[i][j]; bb = B[i][j]
            if j > 0 and D[i][j-1] + 1 < best: best, bb = D[i][j-1] + 1, ('extra',)
            if D[i-1][j] + 1 < best: best, bb = D[i-1][j] + 1, ('skip',)
            for o in opts:
                L = 1 if o == '?' else len(o)
                if j - L >= 0:
                    c = 1 if o == '?' else sum(1 for a, b in zip(o, R[j-L:j]) if a != b)
                    if D[i-1][j-L] + c < best: best, bb = D[i-1][j-L] + c, ('tok', o, L, c)
            D[i][j], B[i][j] = best, bb
    i, j = n, m; given = [False] * m; bad = []
    while i > 0 or j > 0:
        b = B[i][j]
        if b[0] == 'extra': j -= 1
        elif b[0] == 'skip': bad.append((seq[i-1][0], seq[i-1][1], '/'.join(seq[i-1][2]), '(no letters)')); i -= 1
        else:
            _, o, L, c = b
            for k in range(L):
                if o != '?' and o[k] == R[j-L+k]: given[j-L+k] = True
            if c: bad.append((seq[i-1][0], seq[i-1][1], o, R[j-L:j]))
            i -= 1; j -= L
    return given, bad
m = len(R); outside = sum(1 for k in range(m) if not inbr[k])
res = {}
for name, ug, uc in (('decode (key value used)', 0, 0), ('decode + 1548 gloss pairs', 1, 0), ('decode + gloss + crib pairs', 1, 1)):
    given, bad = run(build(ug, uc)); res[name] = (given, bad)
    og = sum(1 for k in range(m) if not inbr[k] and given[k]); ig = sum(1 for k in range(m) if inbr[k] and given[k])
    print(f'(2) {name}: reading letters outside brackets given {og}/{outside} ({og/outside:.3f}); inside brackets {ig}/{m-outside}')
given, bad = res['decode + 1548 gloss pairs']
runs, k = [], 0
while k < m:
    if not inbr[k] and not given[k]:
        s0 = k
        while k < m and not inbr[k] and not given[k]: k += 1
        runs.append(R[max(0, s0-8):s0] + '<' + R[s0:k] + '>' + R[k:k+8])
    else: k += 1
print(f'    letters outside brackets given neither by the decode nor by a 1548 gloss: {len(runs)} runs')
for ctx in runs: print('     ', ctx)
bad = res['decode (key value used)'][1]
print('    token mismatches on the decode-only alignment:', len(bad))
for b in reversed(bad): print('     ', b)
