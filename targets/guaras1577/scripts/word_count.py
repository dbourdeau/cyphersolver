"""Strict word count of the decode against Kervyn's printed words (run from targets/guaras1577, TSPLIT=1).
Each printed word of the cipher part counts as read only if every one of its letters is matched, letter for letter,
by the key's decode (normalisation of the protocol: v=u, j=i, y=i, f=s, plus the OCR classes c=e and l=t).
Bracketed words and gaps of the print are not counted. Held-out lines (P2L01-07) and build lines are reported apart."""
import json, os, re, sys
os.environ.setdefault('TSPLIT', '1'); sys.path.insert(0, 'scripts')
import build_key as B
from kervyn_units import KV
TR = {'y': 'i', 'f': 's', 'e': 'c', 't': 'l'}
f = lambda x: ''.join(TR.get(c, c) for c in x)
key = {s: f(v) for s, v in json.load(open('verification/key_1577_v1.json'))['key'].items()}
U = B.U
# printed words: rebuild word boundaries from the OCR text with the same unit extraction
import unicodedata
words = []; cur = []
t = ' '.join(open(KV, encoding='utf-8').read().split('\n')[10764:10849]); a = t.index('Es  increyble'); b = t.index('Nuestro-Sc')
s = re.sub(r'DES\s+PAYS-BAS\s+ET\s+DE\s+L.ANGLETERRE\.\s+201', ' ', t[a:b]); s = re.sub(r"\s\S*m\s+DES", ' DES', s)
s = s.replace('fue  preso El', 'fue  preso ..... El').replace('puesto  en y', 'puesto  en ..... y')
s = re.sub(r'\[[^\]]*\]', ' # ', s); s = re.sub(r'(\.\s*){3,}|\.\s*\.\.\s*\.', ' # ', s); s = re.sub(r'-\s+', '', s)
for w in s.split():
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if not unicodedata.combining(c))
    w = re.sub(r'[^a-z#]', '', w.replace('v', 'u').replace('j', 'i').replace('w', 'u'))
    if w: words.append(w)
letters = [u for u in U if len(u) == 1]
assert sum(len(w) for w in words if w != '#') == len(letters), (sum(len(w) for w in words if w != '#'), len(letters))
def decoded(lines):
    return ''.join(key.get(t, '#') for lab in lines for t in B.L[lab] if not t.startswith('#'))
def edit_ok(a, b):
    n, m = len(a), len(b); D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1): D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    ok = [False] * m; i, j = n, m
    while i > 0 and j > 0:
        if D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]): ok[j-1] = a[i-1] == b[j-1]; i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
    return ok
spans = json.load(open('verification/key_1577_v1.json'))['plain_spans_used']; ho = json.load(open('verification/PROTOCOL_v1.json'))['reference_units']
order = sorted(B.L, key=lambda x: (x[:2], int(x[3:])))
groups = {'build part 1 (P1L01-33)': ([l for l in order if l.startswith('P1')], spans['part1']),
          'held-out (P2L01-07)': ([l for l in order if l in B.HELDOUT], ho),
          'build part 2 (P2L08-14)': ([l for l in order if l.startswith('P2') and l not in B.HELDOUT], spans['part2'])}
# map unit index -> letter index
li = []; k = 0
for u in U: li.append(k); k += (len(u) == 1)
li.append(k)
wstart = []; k = 0
for w in words:
    wstart.append(k); k += 0 if w == '#' else len(w)
# Strict count (cold check, 28 Nov 2026): the c=e and l=t classes are for the OCR of the print, not for the key. A word
# counts as sure when the decode equals the OCR letter for letter with only y=i, f=s (strict), or when the OCR word is
# one of the c/e or l/t slips below, where the decode gives the real Spanish word (e.g. OCR 'lienen', decode 'tienen').
# 'ello' is not among them: there the OCR is right and the decode 'elto' is wrong.
OCR_SLIPS = {'lienen', 'eslados', 'olra', 'paricnle', 'pareccr', 'lomar', 'pcro', 'tencr', 'lener', 'ausenlo', 'cndondc',
             'auquc', 'perucrso', 'scr'}
g = lambda x: ''.join({'y': 'i', 'f': 's'}.get(c, c) for c in x)
key_strict = {s: g(v) for s, v in json.load(open('verification/key_1577_v1.json'))['key'].items()}
def decoded_strict(lines):
    return ''.join(key_strict.get(t, '#') for lab in lines for t in B.L[lab] if not t.startswith('#'))
T = {'tot': 0, 'merged': 0, 'sure': 0}
for name, (lines, (j0, j1)) in groups.items():
    L0, L1 = li[j0], li[j1]; ref = ''.join(f(x) for x in letters[L0:L1]); ok = edit_ok(decoded(lines), ref)
    ok2 = edit_ok(decoded_strict(lines), ''.join(g(x) for x in letters[L0:L1]))
    tot = rd = sure = 0
    for w, st in zip(words, wstart):
        if w == '#' or st < L0 or st + len(w) > L1: continue
        tot += 1; a = all(ok[st - L0:st - L0 + len(w)]); b = all(ok2[st - L0:st - L0 + len(w)])
        rd += a; sure += b or (a and w in OCR_SLIPS)
    T['tot'] += tot; T['merged'] += rd; T['sure'] += sure
    print(f'{name}: {rd} of {tot} printed words reproduced letter for letter ({rd / tot:.3f}); sure {sure} of {tot}')
nb = sum(w == '#' for w in words)
print(f"all: {T['merged']} of {T['tot']} with the OCR classes; sure {T['sure']} of {T['tot']}; "
      f"{nb} places where the print has a bracketed word or a gap are outside these counts (holes)")
