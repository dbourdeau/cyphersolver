#!/usr/bin/env python3
"""matignon1586tuple: independent check of the decode (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads ONLY key.json, transcription/f*.txt, and (for comparison) decryption/f*.txt,
glosses_multivalued.tsv and texts/f*_reading.md. It does not use any decoding script.

Usage: python3 verify_dudout_20261114.py [path/to/targets/matignon1586tuple]

1. Every group of the transcription is looked up in key.json; the value chosen in
   decryption/ must be one of the key's values for that label (labels L and M are
   not in the key, as legend.md says).
2. The decrypted line must equal the concatenation of the chosen values.
3. Each row of glosses_multivalued.tsv must point at a group with the same label
   and the same decoder value as decryption/.
4. The decoded letters of each page are aligned with the reading (supplied letters
   in [..] removed, [?] dropped, [?word] kept; case, accents and u/v, i/j folded).
"""
import json, os, re, sys, difflib, unicodedata

D = sys.argv[1] if len(sys.argv) > 1 else '.'
key = json.load(open(os.path.join(D, 'key.json'), encoding='utf-8'))
PAGES = ['234r', '234v', '235r', '235v', '236r', '236v', '237r', '237v', '238r', '238v']


def lines(path):
    return [l.rstrip('\n') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and c.isascii())
    return s.replace('v', 'u').replace('j', 'i')


def reading_letters(md):
    body = '\n'.join(l for l in md.splitlines() if l.strip() and not l.startswith('#') and not l.startswith('>'))
    body = re.sub(r'\[\?\]', ' ', body)
    body = re.sub(r'\[\?([^\]]*)\]', r'\1', body)
    body = re.sub(r'\[[^\]?]*\]', '', body)
    return norm(body)


tot = {'groups': 0, 'notkey': 0, 'outside': 0, 'linebad': 0, 'multi': 0}
dec_by_page = {}
problems = []
for p in PAGES:
    tr = lines(os.path.join(D, 'transcription', f'f{p}.txt'))
    dl = lines(os.path.join(D, 'decryption', f'f{p}.txt'))
    heads = [l for l in dl if re.match(r'^L\d\d ', l)]
    grp = [l for l in dl if not re.match(r'^L\d\d ', l)]
    assert len(tr) == len(heads) == len(grp), (p, len(tr), len(heads), len(grp))
    groups = {}
    letters = ''
    for i, (t, h, g) in enumerate(zip(tr, heads, grp), 1):
        labs = t.split()
        pairs = [x.split('=', 1) for x in g.split()]
        if [a for a, _ in pairs] != labs:
            problems.append(f'{p} l.{i}: label sequence differs from decryption')
        for j, (a, v) in enumerate(pairs, 1):
            tot['groups'] += 1
            groups[(i, j)] = (a, v)
            if a not in key:
                tot['notkey'] += 1
                problems.append(f'{p} l.{i} g.{j}: label {a} not in key.json (decoded {v!r})')
            else:
                if len(key[a]) > 1:
                    tot['multi'] += 1
                if v not in key[a]:
                    tot['outside'] += 1
                    problems.append(f'{p} l.{i} g.{j}: {a}={v!r} not among key values {key[a]}')
        line = ''.join(v for _, v in pairs)
        if h.split(' ', 1)[1].strip() != line:
            tot['linebad'] += 1
            problems.append(f'{p} l.{i}: line {h.split(" ",1)[1]!r} != join {line!r}')
        letters += line
    dec_by_page[p] = (groups, letters)

# 3. glosses table
gl = [l.split('\t') for l in lines(os.path.join(D, 'glosses_multivalued.tsv'))][1:]
gl_bad = 0
contra = []
for r in gl:
    p, li, pos, lab, decv, gloss, agrees = r[0], int(r[1]), int(r[2]), r[3], r[4], r[5], r[6]
    g = dec_by_page[p][0].get((li, pos))
    if g is None or g[0] != lab:
        gl_bad += 1
        problems.append(f'glosses {p} l.{li} pos.{pos} {lab}: decryption has {g}')
    elif agrees == 'no':
        # the gloss contradicts the first decode; the reading follows the gloss
        contra.append(f'{p} l.{li} g.{pos} {lab}: first decode {decv!r}, gloss {gloss!r}, decryption/ now {g[1]!r}'
                      + ('  <- not synced with the reading' if g[1] == decv else ''))
    elif g[1] != decv:
        gl_bad += 1
        problems.append(f'glosses {p} l.{li} pos.{pos} {lab}={decv!r}: decryption has {g}')

print(f"groups {tot['groups']}, multi-valued {tot['multi']}, labels not in key {tot['notkey']}, "
      f"values outside key {tot['outside']}, lines != join {tot['linebad']}")
print(f'glosses rows {len(gl)}, not matching decryption {gl_bad}')
for c in contra: print('   contradicted:', c)
print()
print('page  decoded  reading  matched  share_of_decoded')
for p in PAGES:
    dec = norm(dec_by_page[p][1])
    rd = reading_letters(open(os.path.join(D, 'texts', f'f{p}_reading.md'), encoding='utf-8').read())
    sm = difflib.SequenceMatcher(None, dec, rd, autojunk=False)
    m = sum(b.size for b in sm.get_matching_blocks())
    print(f'{p}  {len(dec):7d}  {len(rd):7d}  {m:7d}  {m/len(dec):.3f}')
    if '-v' in sys.argv:
        for op, a1, a2, b1, b2 in sm.get_opcodes():
            if op != 'equal':
                print(f'   {op:8s} dec[{a1}]={dec[max(0,a1-8):a1]}|{dec[a1:a2]}|{dec[a2:a2+8]}  read={rd[b1:b2]!r}')
print()
for x in problems:
    print('  ', x)
