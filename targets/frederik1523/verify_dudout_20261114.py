"""frederik1523: independent check of image 94 against key.tsv and the edition's apparatus
(Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads only key.tsv and transcription_094.txt (labels {XX} and the label-to-Ch concordance in its header), plus
decryption_094.txt for the comparison. The edition's sequence of Ch numbers for witness K1 (= image 94) is typed
below from the apparatus of Hanserecesse III/8 n. 292 (pp. 324-325 = PDF pp. 344-345 of
hanserecesse_3_8_low.pdf): footnotes b, a, c, d, ... b*, in text order, reading "L K K1" notes as K1's sign and
note a* ("knechte adir rutere ebenfalls chiffrirt K1") as Ch. 65, 64.
1. every sign of the transcription, in order, against the edition's K1 sequence;
2. the signs resolved with key.tsv against the capitals of decryption_094.txt.
Run: python3 verify_dudout_20261114.py <path to targets/frederik1523>
"""
import re, sys, os
T = sys.argv[1] if len(sys.argv) > 1 else '.'
key = {}
for l in open(os.path.join(T, 'key.tsv'), encoding='utf-8'):
    if l.startswith('#') or l.startswith('ch\t') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); key[int(f[0])] = f[1]
tx = open(os.path.join(T, 'transcription_094.txt'), encoding='utf-8').read()
conc = dict((a, int(b)) for a, b in re.findall(r'\b([A-Za-z0-9]+) (\d+)(?=[,(\s])', tx.split('Label-to-key concordance')[1].split('\n# [?]')[0]))
seq = []
for l in tx.splitlines():
    m = re.match(r'(\d\d) (.*)', l)
    if m:
        for lab in re.findall(r'\{([A-Za-z0-9]+)\}', m.group(2)): seq.append((int(m.group(1)), lab))
# edition, K1, footnotes in text order (lines 3-30 of image 94)
ED = [('b', 57), ('a', 28), ('c', 47), ('d', 28), ('d', 28), ('e', 66), ('g', 27), ('h', 64), ('i', 65), ('d', 28),
      ('l', 57), ('n', 28), ('o', 41), ('p', 64), ('q', 65), ('r', 41), ('s', 40), ('v', 28), ('w', 28), ('w', 28),
      ('x', 41), ('y', 64), ('z', 65), ('aa', 62), ('bb', 27), ('cc', 28), ('dd', 41), ('ee', 64), ('ff', 65),
      ('gg', 62), ('kk', 58), ('kk', 59), ('kk', 56), ('kk', 60), ('mm', 27), ('nn', 28), ('oo', 33), ('pp', 28),
      ('qq', 42), ('rr', 39), ('ss', 65), ('uu', 27), ('ww', 41), ('xx', 28), ('xx', 28), ('xx', 28), ('zz', 33),
      ('a*', 65), ('a*', 64), ('xx', 28), ('b*', 33)]
print(f'1. signs on image 94: {len(seq)}; K1 signs in the apparatus: {len(ED)}')
agree = 0
for (line, lab), (fn, ch) in zip(seq, ED):
    ok = conc.get(lab) == ch; agree += ok
    if not ok: print(f'   l.{line:02d} {{{lab}}} = Ch. {conc.get(lab)} ({key.get(conc.get(lab))}); edition note {fn}) Ch. {ch} ({key.get(ch)})')
print(f'   agree {agree}/{len(ED)}')
# 2. resolved names against the decryption
dec = {}
for l in open(os.path.join(T, 'decryption_094.txt'), encoding='utf-8'):
    m = re.match(r'(\d\d) (.*)', l)
    if m: dec[int(m.group(1))] = m.group(2)
ok = n = 0
for line, lab in seq:
    v = key[conc[lab]].upper().replace('Ü', 'U').split(' (')[0]
    n += 1
    words = v.replace('GRAVE UNND ', '').split()
    hit = any(w[:5] in dec.get(line, '').upper().replace('Ü', 'U') for w in words)
    ok += hit
    if not hit: print(f'   l.{line:02d} {{{lab}}} -> {v}: not in the decryption line: {dec.get(line)}')
print(f'2. resolved values found in decryption_094.txt: {ok}/{n}')
