"""Pass 5 word count (python3 -I): sure words per text by the house rule (RULES_V5.md).
Tag sources: 'pass4' = the tag in pass4/WORDS_P4.tsv for an identical word at the same place (text, line, index);
'agent' = this agent's tag in TAGS_P5.tsv (Claude Opus 5.5, after the decode, one tagger, no separate judge).
A word with [?] is always a hole. The script stops if a word has no tag. The checks were done with AI tools and no person checked each record by hand."""
import sys
R = sys.argv[1].rstrip('/') + '/'; W4 = sys.argv[2]; MODE = sys.argv[3] if len(sys.argv) > 3 else 'score'
p4 = {}
for ln in open(W4, encoding='utf-8'):
    c = ln.rstrip('\n').split('\t')
    if c[0] == 'text' or len(c) < 5: continue
    p4[(c[0], c[1], int(c[2]))] = (c[3], c[4])
units = []; pend = None
for ln in open(R + 'DECODE_P5.txt', encoding='utf-8'):
    if ln.startswith('#') or '\t' not in ln: continue
    head, txt = ln.rstrip('\n').split('\t'); text, lid = head.rsplit(' ', 1)
    for i, w in enumerate(txt.split()):
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
for ln in open(R + 'TAGS_P5.tsv', encoding='utf-8') if MODE != 'need0' else []:
    if ln.startswith('#') or not ln.strip(): continue
    c = ln.rstrip('\n').split('\t'); tags[(c[0], c[1], int(c[2]))] = (c[3], c[4] if len(c) > 4 else '', c[5] if len(c) > 5 else '')
res = {}; need = []; rows = []
for t, lid, i, w, parts in units:
    tag = None
    if (t, lid, i) in tags:
        tw, tg, why = tags[(t, lid, i)]; assert tw == w, (t, lid, i, tw, w); tag = tg; src = 'agent'
    else:
        ok = all(p4.get((t, l2, i2), ('', ''))[0] == w2 for l2, i2, w2 in parts) and (t, lid, i) in p4
        if ok and len(parts) == 1: tag = 'S' if p4[(t, lid, i)][1] == 'sure' else 'H'; src = 'pass4'; why = ''
        elif ok: tag = 'S' if p4[(t, lid, i)][1] == 'sure' else 'H'; src = 'pass4'; why = ''
    if tag is None: need.append((t, lid, i, w)); continue
    if '[?]' in w and tag == 'S': tag = 'H'
    key = t if t not in ('S1', 'S2', 'S2i', 'F54', 'F97') else t + ':' + lid
    r = res.setdefault(key, [0, 0]); r[0] += 1; r[1] += (tag != 'S')
    rows.append('\t'.join([t, lid, str(i), w, 'sure' if tag == 'S' else 'hole', src, why]))
if MODE.startswith('need'):
    for x in need: print('\t'.join(map(str, x)))
    sys.exit()
assert not need, need[:5]
def fl(n, h): return n < 40 and h <= max(2, n * 0.05)
out = ['# SCORE_P5: sure words per text (cipher words only), pass 5, house rule of RULES_V5.md. Tag sources: pass4 (identical word, same place, pass4/WORDS_P4.tsv) or agent (TAGS_P5.tsv). The checks were done with AI tools and no person checked each record by hand.',
       'unit\tcipher_words\tholes\tsure\tread_share\tarithmetic\tfloor_holds\tover_65']
agg = {}
for k in sorted(res, key=lambda x: (x.split(':')[0], x)):
    n, h = res[k]; s = n - h
    out.append('\t'.join([k, str(n), str(h), str(s), '%.4f' % (s / n), '%d/%d = %.2f%%' % (s, n, 100 * s / n), str(fl(n, h)).lower(), str(s / n >= 0.65).lower()]))
    if ':' in k:
        a = agg.setdefault(k.split(':')[0], [0, 0, 0, 0, 0]); a[0] += n; a[1] += h; a[2] += (h <= 2); a[3] += 1; a[4] += (s / n >= 0.65)
for k, (n, h, le2, m, o65) in agg.items():
    out.append('# %s all parts: %d/%d = %.2f%% sure words; parts with 2 holes or fewer: %d of %d; parts at or over 65%%: %d of %d (listing only; each part is its own text)' % (k, n - h, n, 100 * (n - h) / n, le2, m, o65, m))
open(R + 'SCORE_P5.tsv', 'w').write('\n'.join(out) + '\n'); open(R + 'WORDS_P5.tsv', 'w').write('text\tline\tidx\tword\ttag\tsource\twhy\n' + '\n'.join(rows) + '\n')
print('\n'.join(out))
