"""Align each glossed despatch's code groups with the clerk's interlinear plaintext and write one row per group.
Usage: python3 -I make_pairs.py <pusch_table.tsv> <out pairs.tsv> <glossed transcription>...
Pusch's table is used only to segment the clerk's running plaintext into per-group pieces; every pair's
plaintext is the clerk's, and 'how' says whether it agreed with Pusch ('match'), differed ('conflict'),
or the group is not in Pusch / not legible on the image ('free')."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import parse, norm, load_table, align

table = load_table(sys.argv[1])
rows = []
for path in sys.argv[3:]:
    desp = os.path.basename(path).replace('glossed_', '').replace('.txt', '')
    pages = parse(path)
    groups, locs, text = [], [], ''
    for p in pages:
        for L in p['lines']:
            text += norm(L['gloss'])
            for k, g in enumerate(L['codes']):
                groups.append(g)
                locs.append((p['page'], p['folio'], L['n'], k + 1))
    out, skipped, cost = align(groups, text, table)
    skippedtxt = ''.join(text[j] for j in skipped)
    print(desp, 'groups', len(groups), 'chars', len(text), 'cost %.1f' % cost, 'skipped chars', len(skipped), repr(skippedtxt[:200]))
    for gi, sl, how in out:
        g = groups[gi]
        pg, fo, ln, pos = locs[gi]
        rows.append((desp, pg, fo, ln, pos, g['raw'], g['code'] if g['code'] is not None else '', g['top'] or '', sl or '', how,
                     '|'.join(table.get(g['code'], [])) if g['code'] is not None else ''))
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    f.write('despatch\timage\tfolio\tline\tpos\traw\tcode\ttop\tclerk_plain\thow\tpusch\n')
    for r in rows:
        f.write('\t'.join(str(x) for x in r) + '\n')
from collections import Counter
print(Counter(r[9] for r in rows))
