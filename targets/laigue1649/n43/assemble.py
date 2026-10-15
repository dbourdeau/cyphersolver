"""Assemble the full text of no. 43 from the per-page gloss pairs (pairs_c245..c251.txt) plus the read opening.
Glosses are joined in order (underlined groups reversed back to reading order is NOT needed: the glosser already
wrote the reversed syllable as read), unglossed groups dropped, clear words kept; the cipher runs are then
segmented into words with the period-French word list (as in ../decode2.py)."""
import re, glob, math, functools, os
W = {}
for l in open('../../matignon1586/corpus_words.txt', encoding='utf-8'):
    w, n = l.split('\t'); W[w] = int(n)
for w in ['archiduc', 'larchiduc', 'cardinal', 'parlement', 'conference', 'couronnes', 'mazarin']: W[w] = W.get(w, 0) + 500
TOT = sum(W.values())
def seg(s):
    s0 = s; s = s.lower().replace('v', 'u').replace('j', 'i'); n = len(s)
    @functools.lru_cache(None)
    def f(i):
        if i == n: return (0.0, ())
        best = (-1e9, ())
        for j in range(i + 1, min(n, i + 18) + 1):
            w = s[i:j]
            sc = math.log10(W[w] / TOT) if w in W and (len(w) > 1 or w in 'ayol') else -4.0 * (j - i) - 2
            r = f(j); c = (sc + r[0], (s0[i:j],) + r[1])
            if c[0] > best[0]: best = c
        return best
    return ' '.join(f(0)[1])
out = []
op = open('opening_decoded.txt', encoding='utf-8').read()
for f in ['pairs_c245.txt', 'pairs_c246.txt', 'pairs_c247.txt', 'pairs_c248.txt', 'pairs_c249.txt', 'pairs_c250.txt', 'pairs_c251.txt']:
    if not os.path.exists(f): out.append(f'\n[{f}: missing]\n'); continue
    out.append(f'\n== {f[6:10]} ==')
    for line in open(f, encoding='utf-8'):
        m = re.match(r'L(\d+):\s*(.*)', line.strip())
        if not m: continue
        res, run = [], ''
        for tok in m.group(2).split():
            if tok.startswith('#'):
                if run: res.append(seg(run)); run = ''
                res.append('<' + tok[1:] + '>'); continue
            if '=' not in tok: continue
            g = tok.split('=', 1)[1]
            if g in ('', '+'): continue
            run += g
        if run: res.append(seg(run))
        out.append(f'L{m.group(1)}: ' + ' '.join(res))
txt = '\n'.join(out); open('body_assembled.txt', 'w', encoding='utf-8').write(txt + '\n'); print(txt[:6000])
