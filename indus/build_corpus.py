"""Build a flat Indus corpus from the yajnadevam/indus-website SQL dump.

Source: https://github.com/yajnadevam/indus-website (population-script.sql, GPL-3.0),
an ICIT-derived digitisation: 2,543 objects with CISI numbers, sites, direction,
completeness and glyph sequences. Glyph ids are that database's sign numbers; the
glyph -> Unicode (private-use) map drives the site's Indus font, which we render
to identify signs by shape (see render_glyphs.py).

Output: data/corpus.tsv with one row per object:
  sealid  cisi  site  type  complete  direction  signs_visual  signs_reading  motif
signs_visual is the stored order (IDX 0,1,...), normalised to the usual right-to-left
layout; signs_reading reverses it for every object (also those written L/R, which the
dump stores mirrored), so that the first sign is the first one read. Both are space-separated glyph ids. motif is the field-symbol
code from the ICONOGRAPHY table (Bull1 = 'unicorn' and its sub-types, Elep, Rhin, Zebu ...).

Usage: python build_corpus.py path/to/population-script.sql
"""
import csv
import io
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def tuples(block, n):
    out = []
    for m in re.finditer(r'\(([^()]*)\)', block):
        row = next(csv.reader(io.StringIO(m.group(1)), skipinitialspace=True), None)
        if row is None:
            continue
        row = [f.strip().strip('"') for f in row]
        if len(row) == n:
            out.append(row)
    return out


def block(sql, table):
    k = sql.find('INSERT INTO %s (' % table)
    if k < 0:
        k = sql.index('INSERT INTO %s(' % table)          # ICONOGRAPHY is written without a space
    i = sql.index('VALUES', k)  # skip the column list
    j = sql.find('INSERT INTO', i)
    return sql[i:j if j > 0 else None]


def main(sql_path):
    sql = open(sql_path, encoding='utf-8').read()
    sites = dict(tuples(block(sql, 'SITE'), 2))
    seals = {r[0]: r for r in tuples(block(sql, 'SEAL'), 8)}
    insc = {r[0]: r for r in tuples(block(sql, 'INSCRIPTION'), 3)}
    feats = dict(tuples(block(sql, 'FEATURE'), 2))
    types = defaultdict(list)
    for sid, q in tuples(block(sql, 'ICONOGRAPHYFEATURES'), 2):
        types[sid].append(feats.get(q, q))
    seq = defaultdict(list)
    for sid, g, idx in tuples(block(sql, 'GLYPHSEQUENCE'), 3):
        seq[sid].append((int(idx), g))
    glyphs = tuples(block(sql, 'GLYPH'), 2)
    motif = dict(tuples(block(sql, 'ICONOGRAPHY'), 2))

    os.makedirs(os.path.join(HERE, 'data'), exist_ok=True)
    with open(os.path.join(HERE, 'data', 'glyphs.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['glyph', 'codepoints'])
        for g, u in glyphs:
            cps = ' '.join(re.findall(r'#x([0-9A-Fa-f]+);', u))
            w.writerow([g, cps])

    n = 0
    with open(os.path.join(HERE, 'data', 'corpus.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['sealid', 'cisi', 'site', 'type', 'complete', 'direction',
                    'signs_visual', 'signs_reading', 'motif'])
        for sid in sorted(seq, key=int):
            s = [g for _, g in sorted(seq[sid])]
            seal = seals.get(sid)
            ins = insc.get(sid, [sid, '', ''])
            direction = ins[2]
            # the dump stores every text in one normalised order (the jar, which ends texts,
            # is at IDX 0 for 839 of 840 R/L and 29 of 30 L/R objects); DIRECTION records only
            # how the object was written, so the reading order is the reverse for all objects
            reading = list(reversed(s))
            w.writerow([sid, (seal[3] if seal and seal[3] != 'NULL' else ''),
                        sites.get(seal[1], seal[1]) if seal else '',
                        '|'.join(types.get(sid, [])), ins[1], direction,
                        ' '.join(s), ' '.join(reading), motif.get(sid, '')])
            n += 1
    print('objects written:', n)


if __name__ == '__main__':
    main(sys.argv[1])
