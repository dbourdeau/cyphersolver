"""The main structural findings on a fuller ICIT-derived corpus (4,578 objects, 5,559 texts).

Source: the ICIT-style corpus built into indusscript.net (Yajnadevam's site), same Wells/ICIT sign numbers and
storage convention as the indus-website dump used elsewhere in this folder (texts stored in visual order; reading
order = reversed, as build_corpus.py). The data are ICIT's (Wells, Fuls); they are used here locally to check the
findings and are not redistributed. Lines are split at 000; lines with a break mark ([ or ]) are left out.

Runs the tests of replicate_m77.py (RP1-RP6) and noun_class-style ending classes on it, and on the part of it that
the indus-website dump lacks (texts not in data/corpus.tsv).

Usage: python replicate_full.py path/to/icit_full_records_indusscript_net.csv
Writes results/replicate_full.md.
"""
import csv
import os
import sys
from collections import Counter

import replicate_m77 as rp
from signs import FISH, SPLIT, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def parse(path):
    rows = []
    for rec in csv.reader(open(path, encoding='utf-8')):
        if len(rec) < 35:
            continue
        txt = next((x for x in rec if x.startswith('+') or x.endswith('+') or '-' in x and x[:1] in '+['), '')
        txt = rec[34] if rec[34].startswith(('+', '[')) else txt
        if not txt:
            continue
        otype = rec[20]
        lines = []
        for part in txt.strip('+').split('-000-'):
            if '[' in part or ']' in part:
                continue
            toks = [t for t in part.strip('+').split('-') if t.isdigit()]
            ln = []
            for t in reversed(toks):
                g = str(int(t))
                if g == '0':
                    continue
                ln.extend(SPLIT.get(g, [g]))
            if ln:
                lines.append(ln)
        if lines:
            rows.append({'sealid': rec[0], 'cisi': rec[1], 'site': rec[3], 'type': otype, 'seq': lines,
                         'flat': [g for ln in lines for g in ln], 'motif': ''})
    return rows


def run(label, rows):
    texts = [ln for r in rows for ln in r['seq'] if len(ln) >= 2]
    say('## %s (%d objects, %d lines of 2+ signs)' % (label, len(rows), len(texts)))
    say()
    say('- RP1 endings fixed per name: %s.' % rp.rp1(texts))
    say('- RP2 520 after a fish-final name: %s.' % rp.rp2(texts))
    say('- RP3 %s.' % rp.rp3(texts))
    say('- RP4 %s.' % rp.rp4(rows))
    say('- RP5 opening formula: %s.' % rp.rp5(rows))
    say('- RP6 short against long strokes: %s.' % rp.rp6(rows))
    pos = Counter()
    for r in rows:
        for ln in r['seq']:
            for i, g in enumerate(ln):
                if g == '90':
                    pos['after 740' if i and ln[i - 1] == '740' else ('text-initial' if i == 0 else 'other')] += 1
    say('- word order: the man sign 90 %s.' % ', '.join('%s %d' % kv for kv in pos.most_common()))
    say()


def main(path):
    full = parse(path)
    say('# The main findings on the fuller ICIT-derived corpus (indusscript.net export)')
    say()
    say('Local check only: the data are ICIT\'s (Wells, Fuls), taken from the corpus built into indusscript.net; not '
        'redistributed. Unbroken lines only.')
    say()
    run('fuller corpus', full)
    have = {tuple(tuple(ln) for ln in r['seq']) for r in load()}
    new = [r for r in full if tuple(tuple(ln) for ln in r['seq']) not in have]
    run('texts not in the indus-website dump', new)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'replicate_full.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
