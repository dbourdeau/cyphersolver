"""Build validation.tsv for no. 18 (Latin): signs from transcripts/no18v.txt (cipher words split by ' / ' and by the
clear text in [ ]), readings from transcripts/no18_reading.txt PER LINE (one <word> per cipher word). Lines whose
cipher-word count differs from the reading's are left unread. Each word's signs are aligned with its reading by the
same small DP as targets/siena14/mk_validation.py (each sign takes 0-2 letters; cost where the letters differ from the
working key keys/no18_key.txt plus the sign classes the reading settles). Doubtful (?), unread ([..]) and struck
words are '?'. Written 14 Oct 2026 when no. 18 became its own entry (split from siena1421)."""
import os, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
K = {k: {v} for k, v in (x.split('=', 1) for x in open('keys/no18_key.txt', encoding='utf-8').read().split())}
# sign classes settled in the reading (NOTES: hooked n = q, plain n = e; o = g or o; OO = i or ll; 2 = h; PHI = pp; HX = rr)
for k, v in {'n': {'q', 'e', 'a'}, 'o': {'g', 'o'}, 'OO': {'i', 'll'}, '2': {'h'}, 'PHI': {'pp', 'l'}, 'HX': {'rr', 'r'}}.items():
    K.setdefault(k, set()).update(v)
def nz(s):
    s = re.sub(r'\([^)]*\)', '', s)
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s).replace('v', 'u').replace('j', 'i')
def align(signs, text):
    memo = {}
    def go(i, p):
        if i == len(signs): return (0, []) if p == len(text) else None
        if (i, p) in memo: return memo[(i, p)]
        best = None; vals = {nz(v) for v in K.get(signs[i], set())}
        for L in (1, 0, 2):
            if p + L > len(text): continue
            sub = text[p:p + L]
            c = 0 if sub in vals else (1 if L == 1 else 2)
            r = go(i + 1, p + L)
            if r is not None and (best is None or r[0] + c < best[0]): best = (r[0] + c, [sub] + r[1])
        memo[(i, p)] = best; return best
    return go(0, 0)
def cipher_words(line):
    line = re.split(r'\s{2,}\(|<<chg', line)[0]
    words = []
    for seg in re.split(r'\[[^\]]*\]', line):
        for w in seg.split(' / '):
            t = w.split()
            if t: words.append(t)
    return words
src = {m.group(1): m.group(2) for m in (re.match(r'(L\d+\.\d+)\s+(.*)', l) for l in open('transcripts/no18v.txt', encoding='utf-8')) if m}
rd = open('transcripts/no18_reading.txt', encoding='utf-8').read().split('PER LINE')[1].split('COUNTS')[0]
out = ['# model: la', '# source: transcripts/no18v.txt (signs) and transcripts/no18_reading.txt PER LINE (readings), key keys/no18_key.txt',
       '# note: no. 18 only; signs aligned to reading words by DP; doubtful, unread and struck words unread']
stats = {'ok': 0, 'bad': 0, 'unread': 0, 'lines_skipped': 0}
for m in re.finditer(r'^(L\d+\.\d+)\s+(.*)$', rd, re.M):
    ln, text = m.groups()
    if ln not in src: continue
    cw = cipher_words(src[ln]); rw = re.findall(r'<([^>]*)>(\{struck\})?', text)
    if len(cw) != len(rw):
        stats['lines_skipped'] += 1; stats['unread'] += sum(map(len, cw)); out.extend(f'{s}\t?' for w in cw for s in w); continue
    for signs, (r, struck) in zip(cw, rw):
        read = not struck and '?' not in r and '..' not in r and '[' not in r
        a = align(signs, nz(r)) if read and nz(r) else None
        if a is None or a[0] > len(signs) // 2 + 1:
            stats['bad' if read else 'unread'] += len(signs); out.extend(f'{s}\t?' for s in signs); continue
        stats['ok'] += len(signs)
        out.extend(f'{s}\t{v if v else "-"}' for s, v in zip(signs, a[1]))
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(stats)
