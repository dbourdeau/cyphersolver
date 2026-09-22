"""Fourth pass on R9414's single-sign gaps.

reading_v3.txt marks an unread sign as [..1] inside an otherwise-read word. gapfill.py only
offered readings that were alternatives of the sign as transcribed; this pass treats the gap as a
wildcard over the whole alphabet, takes every word of the de-1500s corpus that matches the pattern,
and scores the candidates by the language model in their real context. Prints only the gaps where
one candidate wins clearly, for checking against the images.
"""
import re, sys, os, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

m = lm.load('de-1500s')
text = lm.norm(corpora.text(['de-dta-1470-1610']), 'early')
VOCAB = collections.Counter(text.split())
print(f'lexicon {len(VOCAB)} word types', file=sys.stderr)

lines = [l.rstrip('\n') for l in open('reading_v3.txt', encoding='utf8') if l[:1] == 'P']
flat = []
for l in lines:
    lid, rest = l.split(' ', 1)
    flat.append((lid, rest))

WORD = re.compile(r'\S*\[\.\.1\]\S*')
out = []
for i, (lid, rest) in enumerate(flat):
    clean = re.sub(r'<[^>]*>', ' ', rest)
    for mo in WORD.finditer(clean):
        tok = mo.group(0)
        pat = tok.strip('.,;:?')
        if pat.count('[..1]') != 1: continue
        pre, post = pat.split('[..1]')
        pre, post = pre.strip('.,;:'), post.strip('.,;:')
        if not (pre or post): continue          # a whole word unread: no pattern to match
        rx = re.compile('^' + re.escape(pre) + '.' + re.escape(post) + '$')
        cands = [(c, n) for c, n in VOCAB.items() if rx.match(c)]
        if not cands: continue
        # context: the rest of the line with the other marks stripped
        ctx = re.sub(r'\[\.\.\d+\]', ' ', clean)
        ctx = re.sub(r'[^a-z ]', ' ', lm.norm(ctx, 'early'))
        left = ' '.join(ctx.split()[:8])
        scored = []
        for c, n in cands:
            s = m.per_char(' ' + left + ' ' + c + ' ') + 0.12 * (n ** 0.25)
            scored.append((s, c, n))
        scored.sort(reverse=True)
        best = scored[0]
        gap = best[0] - scored[1][0] if len(scored) > 1 else 9.0
        out.append((gap, lid, pat, best[1], best[2], [c for _, c, _ in scored[1:4]]))

out.sort(reverse=True)
print(f'{len(out)} single-sign gaps with a pattern; candidates found for all of them\n')
for gap, lid, pat, best, n, rest in out:
    flag = 'CLEAR ' if gap > 0.30 else ('close ' if gap > 0.10 else 'weak  ')
    print(f'{flag}{lid}  {pat:28s} -> {best:20s} (corpus {n}; margin {gap:.2f}; next {", ".join(rest)})')
