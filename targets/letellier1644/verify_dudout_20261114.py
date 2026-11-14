"""letellier1644: independent decoder and reading-side alignment (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY contributed/data/key.tsv, contributed/data/transcription_f50.txt and the line table of
contributed/docs/READING.en.md. Code groups are not in key.tsv; their values are taken from Tomokiyo's table
(cryptiana louisxiv0.htm, image louisxiv_0marca1644.png: =9 pour, =11 que, =12 qui, =26 vous, =32 Barcelone,
=34 ambassadeur, 39 Catalogne, 81 faire, n-o la Roine?) and from the contributor's METHOD.en.md (=y Monsieur le
Mareschal, =3 de La Motte, =11 =o la Reyne, =83 le Gouverneur). Not used: measure.py, decoded_f50.txt for decoding.

1. Bare decode (main value of each sign), compared letter by letter with contributed/data/decoded_f50.txt.
2. Reading-side DP: per line, the reading's letters (marks kept) are aligned with the signs (any key value or
   code word). Lists the reading letters that no sign gives and that are NOT in [ ] (silent supplies), and the
   signs left without a letter.
Run: python3 verify_dudout_20261114.py <path to targets/letellier1644>
"""
import re, sys, os, unicodedata
T = sys.argv[1] if len(sys.argv) > 1 else '.'
C = os.path.join(T, 'contributed')
CODES = {'=9': 'pour', '=11': 'que', '=12': 'qui', '=26': 'vous', '=32': 'barcelone', '=34': 'ambassadeur',
         '39': 'catalogne', '81': 'faire', '=y': 'monsieurlemareschal', '=3': 'delamotte', '=83': 'legouverneur'}
PAIR = {('=11', '=o'): 'lareyne'}

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s.replace('j', 'i').replace('v', 'u').replace('y', 'i'))

key = {}
for l in open(os.path.join(C, 'data', 'key.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t')
    vals = [f[1]] + [v for v in (f[2].split(',') if len(f) > 2 else []) if v]
    key[f[0]] = [norm(v) for v in vals if v != '?' and norm(v)]

lines = []
for l in open(os.path.join(C, 'data', 'transcription_f50.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lid, *toks = l.split(); lines.append((lid, toks))

def CODEVARS(w):
    """code word, normalised; 'que' also elided (qu'), 'Monsieur' also abbreviated (M.)"""
    w = norm(w); v = [w]
    if w == 'que': v.append('qu')
    if w.startswith('monsieur'): v.append('m' + w[8:])
    return v

def units(toks):
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if i + 1 < len(toks) and (t, toks[i + 1]) in PAIR:
            out.append((t + ' ' + toks[i + 1], [norm(PAIR[(t, toks[i + 1])])])); i += 2; continue
        if t.startswith('['): out.append((t, [norm(t)]))
        elif t in CODES: out.append((t, CODEVARS(CODES[t])))
        else: out.append((t, key.get(t, [])))
        i += 1
    return out

# 1. bare decode vs decoded_f50.txt
dec = {}
for l in open(os.path.join(C, 'data', 'decoded_f50.txt'), encoding='utf-8'):
    p = l.split(None, 1)
    if len(p) == 2: dec[p[0]] = norm(p[1])
same = tot = 0; diffs = []
for lid, toks in lines:
    mine = ''.join(c[0] if c else '' for _, c in units(toks))
    theirs = dec.get(lid, '')
    import difflib
    sm = difflib.SequenceMatcher(None, mine, theirs, autojunk=False)
    same += sum(b.size for b in sm.get_matching_blocks()); tot += max(len(mine), len(theirs))
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != 'equal': diffs.append((lid, op, mine[a1:a2], theirs[b1:b2]))
print(f'1. bare decode vs decoded_f50.txt: {same}/{tot} letters agree')
for d in diffs: print('   ', *d)

# 2. reading-side DP
read = {}
for l in open(os.path.join(C, 'docs', 'READING.en.md'), encoding='utf-8'):
    m = re.match(r'\|\s*([rv]\d\d)\s*\|\s*(.*?)\s*\|', l)
    if m and m.group(1) not in read: read[m.group(1)] = m.group(2)

def marked(s):
    """[(letter, supplied?)] ; signs in ⟨ ⟩ dropped."""
    s = re.sub(r'⟨[^⟩]*⟩', ' ', s); out = []; sup = False
    for ch in s:
        if ch == '[': sup = True; continue
        if ch == ']': sup = False; continue
        n = norm(ch)
        if n: out.append((n, sup))
    return out

INF = 10 ** 9
silent, unused, nlet, nsup = [], [], 0, 0
for lid, toks in lines:
    us = units(toks); rl = marked(read.get(lid, '')); txt = ''.join(c for c, _ in rl)
    nlet += len(rl); nsup += sum(s for _, s in rl)
    n, m = len(us), len(rl)
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] >= INF: continue
            if i < n and D[i][j] + 1 < D[i + 1][j]: D[i + 1][j] = D[i][j] + 1; B[i + 1][j] = (i, j, 'sign')
            if j < m:
                c = 0 if rl[j][1] else 1          # supplied letters cost nothing
                if D[i][j] + c < D[i][j + 1]: D[i][j + 1] = D[i][j] + c; B[i][j + 1] = (i, j, 'let')
            if i < n:
                for v in us[i][1]:
                    if v and txt.startswith(v, j) and D[i][j] < D[i + 1][j + len(v)]:
                        D[i + 1][j + len(v)] = D[i][j]; B[i + 1][j + len(v)] = (i, j, 'm')
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, k = B[i][j]
        if k == 'sign': unused.append((lid, i, us[pi][0]))
        if k == 'let' and not rl[pj][1]: silent.append((lid, pj, rl[pj][0], txt))
        i, j = pi, pj
print(f'2. reading letters {nlet}, supplied in [ ] {nsup}; letters given by no sign and not in [ ]: {len(silent)}')
for lid, pos, ch, txt in sorted(silent):
    print(f'    {lid} letter {pos + 1} "{ch}"  ({txt[max(0, pos - 6):pos]}|{ch}|{txt[pos + 1:pos + 7]})')
print(f'   signs that fall on no letter: {len(unused)}')
for u in sorted(unused): print('    ', u[0], 'sign', u[1], u[2])
