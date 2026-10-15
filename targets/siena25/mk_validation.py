"""Build validation.tsv for no. 25 (transcripts/no25_reading.txt, rev. 2, PER LINE). Split on 14 Oct 2026 from
targets/siena1421/mk_validation.py, which validated nos. 14 and 25 together; each letter has its own key and entry. Each cipher word's signs are aligned with its reading
word by a small DP (each sign takes 0-2 letters; cost where the letters differ from the sign's key value, key14.txt /
keys/no25_key.txt plus the sign classes the readings settle). Only words the reading leaves untagged (read as sense)
are used; doubtful/unread words ({?} {x} {code}, '(?)', [TH]) and words the DP cannot align cheaply are '?'.
No. 18 (Latin) and no. 4 (144 signs, own key) are left out: one model per file, Italian dominant."""
import os, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
def kv(path): return dict(x.split('=', 1) for x in open(path, encoding='utf-8').read().split())
K25 = {k: {v} for k, v in kv('keys/no25_key.txt').items()}
K25.update({'XB': {'z'}, 'R': {'u'}, 'PHI': {'u', 'b'}, 'Y': {'m'}, 'X': {'r'}})
DEBUG = __import__('sys').argv[1:] == ['-v']
ZERO = {'PAREN', 'TILDE', 'BAR', 'ITICK', '/'}
def nz(s):
    s = re.sub(r'\([^)]*\)', '', s)
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s).replace('v', 'u').replace('j', 'i')
def label(s): return s.rstrip('?').split('^')[0]
def align(signs, text, K):
    memo = {}
    def go(i, p):
        if i == len(signs): return (0, []) if p == len(text) else None
        if (i, p) in memo: return memo[(i, p)]
        best = None; vals = {nz(v) for v in K.get(label(signs[i]), set())}
        for L in (1, 0, 2):
            if p + L > len(text): continue
            sub = text[p:p + L]
            c = 0 if sub in vals else (0 if L == 0 and label(signs[i]) in ZERO else (1 if L == 1 else 2))
            r = go(i + 1, p + L)
            if r is not None and (best is None or r[0] + c < best[0]): best = (r[0] + c, [sub] + r[1])
        memo[(i, p)] = best; return best
    return go(0, 0)
out = ['# model: it-cinquecento',
       '# source: transcripts/no25_reading.txt (PER LINE), key keys/no25_key.txt',
       '# note: no. 25 only; signs aligned to reading words by DP; doubtful words unread']
stats = {'ok': 0, 'bad': 0, 'unread': 0}
def emit(prefix, signs, text, K, read):
    signs = [s for s in signs if s and s not in ('??',)]
    if not signs: return
    r = align(signs, nz(text), K) if read and nz(text) else None
    if r is None or r[0] > len(signs) // 2 + 1:
        stats['bad' if read else 'unread'] += len(signs)
        if read and DEBUG: print(prefix, signs, text, r)
        out.extend(f'{prefix}{label(s)}\t?' for s in signs); return
    stats['ok'] += len(signs)
    for s, v in zip(signs, r[1]): out.append(f'{prefix}{label(s)}\t{v if v else "-"}')
# no. 25
lines = open('transcripts/no25_reading.txt', encoding='utf-8').read().split('PER LINE')[1].split('RUNNING TEXT')[0].splitlines()
for a, b in zip(lines, lines[1:]):
    if not re.match(r'L\d\d ', a): continue
    sw = [w.split() for w in re.sub(r'\[struck:[^\]]*\]', '', a[4:]).split(' / ')]
    tw = [w.strip() for w in b.split(' / ')]
    if len(sw) != len(tw): stats['bad'] += sum(map(len, sw)); out.extend(f'n25:{label(s)}\t?' for w in sw for s in w); continue
    for s, t in zip(sw, tw): emit('n25:', s, t, K25, '(?)' not in t and '[' not in t)
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(stats)
