"""Pass 4 word count (python3 -I): sure words per text, holes, read_share, short-text floor.
Tags: the pass-2 separate judge's tag where the pass-4 word equals the pass-2 decode at the same place
(keyleaf/judge/JUDGE_OUT.tsv), else this agent's tag from TAGS_P4.tsv (hole list; a word not listed there and
not inherited must be listed as sure in TAGS_P4.tsv too, or the script stops).
The checks were done with AI tools and no person checked each record by hand."""
import sys, re, json
R = sys.argv[1].rstrip('/') + '/'; J = sys.argv[2]; MODE = sys.argv[3] if len(sys.argv) > 3 else 'score'
SEC2 = {'TRAIN f4r':'TRAIN f4r','TRAIN f4v':'TRAIN f4v','H2':'H2','H3':'H3','S1':'PENT'}
p2 = {}
for ln in open(J, encoding='utf-8'):
    c = ln.rstrip('\n').split('\t')
    if len(c) < 7 or c[0] in ('section','TOTAL','TOTALS',''): continue
    p2[(c[0], c[1])] = [(m.group(1), m.group(2)) for m in re.finditer(r'(\S+?)/([SEN])(?:\([^)]*\))?(?=\s|$)', c[6])]
# pass-4 decode -> word units [text, line, idx, word, parts]
units = []; pend = None
for ln in open(R + 'DECODE_P4.txt', encoding='utf-8'):
    if ln.startswith('#') or '\t' not in ln: continue
    head, txt = ln.rstrip('\n').split('\t'); text, lid = head.rsplit(' ', 1)
    ws = txt.split()
    for i, w in enumerate(ws):
        if pend is not None and i == 0 and pend[0] == text:
            pend[3] += w; pend[4].append((lid, i, w)); u = pend; pend = None
            if w.endswith('='): pend = u
            continue
        if pend is not None: units.append(pend); pend = None
        u = [text, lid, i, w, [(lid, i, w)]]
        if w.endswith('='): pend = u
        else: units.append(u)
if pend is not None: units.append(pend)
tags = {}
try:
    for ln in open(R + 'TAGS_P4.tsv', encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        c = ln.rstrip('\n').split('\t'); tags[(c[0], c[1], int(c[2]))] = (c[3], c[4] if len(c) > 4 else '')
except FileNotFoundError: pass
res = {}; need = []; rows = []
for t, lid, i, w, parts in units:
    tag = None; src = ''
    if (t, lid, i) in tags: tag, why = tags[(t, lid, i)]; src = 'agent'
    elif t in SEC2:
        ok = True; tt = []
        for (l2, i2, w2) in parts:
            L = p2.get((SEC2[t], l2))
            if not L or i2 >= len(L) or L[i2][0] != w2: ok = False; break
            tt.append(L[i2][1])
        if ok: tag = 'S' if all(x == 'S' for x in tt) and '[?]' not in w else 'H'; src = 'pass2-judge'; why = ''.join(tt)
    if tag is None: need.append((t, lid, i, w)); continue
    if '[?]' in w and tag == 'S': tag = 'H'
    key = t if t not in ('S1','S2') else t + ':' + lid
    r = res.setdefault(key, [0, 0]); r[0] += 1; r[1] += (tag != 'S')
    rows.append('\t'.join([t, lid, str(i), w, 'sure' if tag == 'S' else 'hole', src, why]))
if MODE == 'need':
    for x in need: print('\t'.join(map(str, x)))
    sys.exit()
assert not need, need[:5]
def line(k, n, h):
    s = n - h; floor = n < 40 and h <= max(2, int(n * 0.05)) and h > round(n * 0.05) or False
    share = s / n
    return k, n, h, s, share
out = ['# SCORE_P4: sure words per text (cipher words only), pass 4. Tag sources: pass2-judge = the pass-2 separate judge\'s tag for an identical word at the same place (S sure; E or N hole); agent = this agent\'s tag (TAGS_P4.tsv). The checks were done with AI tools and no person checked each record by hand.',
       'unit\tcipher_words\tholes\tsure\tread_share\tarithmetic\tfloor_holds\tover_65']
def fl(n, h): return n < 40 and h <= max(2, n * 0.05)
agg = {}
for k in sorted(res, key=lambda x: (x.split(':')[0], x)):
    n, h = res[k]; s = n - h
    out.append('\t'.join([k, str(n), str(h), str(s), '%.4f' % (s / n), '%d/%d = %.2f%%' % (s, n, 100 * s / n), str(fl(n, h)).lower(), str(s / n >= 0.65).lower()]))
    if ':' in k:
        a = agg.setdefault(k.split(':')[0], [0, 0, 0, 0]); a[0] += n; a[1] += h; a[2] += (h <= 2); a[3] += 1
for k, (n, h, le2, m) in agg.items():
    out.append('# %s all rims: %d/%d = %.2f%% sure words; rims with 2 holes or fewer: %d of %d (listing only; each rim is its own text)' % (k, n - h, n, 100 * (n - h) / n, le2, m))
open(R + 'SCORE_P4.tsv', 'w').write('\n'.join(out) + '\n'); open(R + 'WORDS_P4.tsv', 'w').write('text\tline\tidx\tword\ttag\tsource\twhy\n' + '\n'.join(rows) + '\n')
print('\n'.join(out))
