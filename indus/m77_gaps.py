"""Mahadevan's 1977 reading (M77) of the signs ICIT marks illegible in the restoration worklist (set 255): each gap
line is aligned with the M77 lines of the same length whose other signs agree with it (at most one mismatch in lines
of 5+ signs), and M77's sign at the gap (mapped to ICIT through data/icit_m77_map.tsv) is taken when all aligned M77
lines agree and it is legible. Writes results/restoration_m77.tsv. Does not read the predictions.
Usage: python m77_gaps.py [path to m77_indusscript_real_corpus.csv]"""
import csv
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = os.path.join(os.environ.get('LANG_DATA', 'C:/Users/dbour/indus_data'), 'indus_decipher', 'data', 'm77_indusscript_real_corpus.csv')


def m77_lines(path):
    inv = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'data', 'icit_m77_map.tsv'), encoding='utf-8'), delimiter='\t'):
        c = int(r['pairs'])
        if r['m77'] not in inv or c > inv[r['m77']][1]:
            inv[r['m77']] = (r['icit'], c)
    out = []
    for r in csv.DictReader(open(path, encoding='utf-8')):
        seq = ['000' if g == 'MSg0' else inv[g][0] if g in inv else '?' for g in r['sign_sequence'].split()]
        out.append((r['inscription_id'], seq))
    return out


def main(path=DEFAULT):
    lines = m77_lines(path)
    work = list(csv.DictReader(open(os.path.join(HERE, 'results', 'restoration_worklist.tsv'), encoding='utf-8'), delimiter='\t'))
    rows = []
    for w in work:
        t = w['text_with_gap'].split()
        k = t.index('???')
        hits = []
        for mid, s in lines:
            if len(s) != len(t):
                continue
            mis = sum(a != b for i, (a, b) in enumerate(zip(t, s)) if i != k)
            if mis <= (1 if len(t) >= 5 else 0):
                hits.append((mid, s[k]))
        vals = Counter(v for m, v in hits)
        reading = ''
        if hits and len(vals) == 1:
            v = next(iter(vals))
            reading = v if v not in ('000', '?') else 'illegible'
        elif len(vals) > 1:
            reading = 'conflict'
        rows.append((w['id'], w['line'], w['pos'], w['cisi'], w['text_with_gap'], ' '.join(m for m, v in hits), ' '.join(sorted(vals)), reading or 'no match'))
    with open(os.path.join(HERE, 'results', 'restoration_m77.tsv'), 'w', encoding='utf-8', newline='') as f:
        f.write('id\tline\tpos\tcisi\ttext_with_gap\tm77_ids\tm77_values\treading\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print(Counter(r[-1] if r[-1] in ('no match', 'conflict', 'illegible') else 'read' for r in rows))


if __name__ == '__main__':
    main(*sys.argv[1:])
