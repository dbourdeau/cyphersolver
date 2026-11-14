#!/usr/bin/env python3
"""nevers1587: independent decode of the cipher items (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY key.md (alphabet table, small-word capitals, numbered names) and ciphertext.txt, then compares with
reading.tsv. Does not use dec.py, edits.py or enum_readings.py.
Usage: python3 verify_dudout_20261114.py [path/to/targets/nevers1587]
Each sign is looked up (1) in the key's own column, (2) in 'this writer's forms' column, (3) among the capitals
(small words) and the numbered names. Signs found nowhere are nulls by the key's rule.
"""
import os, re, sys, csv
D = sys.argv[1] if len(sys.argv) > 1 else '.'
md = open(os.path.join(D, 'key.md'), encoding='utf-8').read()

key, writer = {}, {}
for row in re.findall(r'^\| ([a-z /]+) \| ([^|]*) \| ([^|]*) \|$', md, re.M):
    plain = row[0].split(' / ')[0].strip()
    if plain == 'plain': continue
    for col, dst in ((row[1], key), (row[2], writer)):
        for s in re.split(r',\s*', col):
            s = s.strip()
            if not s: continue
            g = s.split()[0].split('/')[0]          # first glyph of a description ("◊ with a tail" -> ◊)
            for gg in s.split('/'):
                gg = gg.strip().split()[0] if gg.strip() else ''
                if gg and len(gg) <= 3: dst.setdefault(gg, set()).add(plain)
            dst.setdefault(g, set()).add(plain)
small = dict((c, w) for w, c in re.findall(r'([a-z]+) ([A-Z])\b', md.split('## Small words')[1].split('##')[0]))
names = dict(re.findall(r'\*\*(\d+) ([^*]+)\*\*', md))

rows = [r for r in csv.DictReader(open(os.path.join(D, 'reading.tsv'), encoding='utf-8'), delimiter='\t')]
items = []
for l in open(os.path.join(D, 'ciphertext.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    rec, folio, item, *signs = l.split()
    if item == 'code': signs = signs[1:] if signs[0] == 'code' else signs
    for s in signs: items.append((rec, folio, item, s))
assert len(items) == len(rows), (len(items), len(rows))
agree = 0
for (rec, folio, item, s), r in zip(items, rows):
    assert r['sign'] == s
    if item == 'code':
        mine = 'name: ' + names.get(s, '?')
        ok = s in names
    else:
        k, w, c = key.get(s, set()), writer.get(s, set()), small.get(s)
        mine = f"key {sorted(k) or '-'} writer {sorted(w) or '-'} capital {c or '-'}"
        v = r['value']
        ok = (v in k) or (v in w) or (v == c) or (r['class'] in ('null', 'cancelled') and not k and not w) \
             or r['class'] == 'cancelled' and (v in k or v in w)
        if r['class'] == 'null' and (k or w): ok = False
    agree += ok
    print(f"{rec} {folio} {item:8s} {s:3s} published={r['value']!r:22s} ({r['class']:9s}) {mine}  {'OK' if ok else '<- differs'}")
print(f'\n{agree} of {len(rows)} units agree with a value the key or the writer column allows')
