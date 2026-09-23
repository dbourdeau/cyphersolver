"""Apply key.json to ct_neal.txt, mark the unread spans, measure the fraction read, write the reveal file.

    python decode.py            # prints the decrypt with unread letters as '?', and the counts
    python decode.py --reveal   # also writes ../docs/reveal/baner1640.json (segment S3)
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'key.json'), encoding='utf-8'))

# unread spans: (segment, first index, last index inclusive) over the segment's tokens, codes included in indexing
UNREAD = {
    'S2': [(10, 20)],          # ohrs?acbuet: the name after "Johann"
    'S5': [(29, 29),           # the stray e of "sobaldt e ich"
           (61, 74),           # eisen o vi rechte
           (82, 83)],          # o ? before "ein guten"
}
# emendations: (segment, index) -> letter read in place of the key's value
CODELETTERS = {'766': 'w', '770': 'm', '772': 'f', '778': 'f', '783': 'g'}   # 7xx codes read as letters (C/M)
EMEND = {('S4', 20): 'n'}   # the manuscript has 93 (i) where Schlesien needs n: encipherer's slip

segs = {}
for l in open(os.path.join(HERE, 'ct_neal.txt'), encoding='utf-8'):
    if l.startswith('S'):
        p = l.split(); segs[p[0]] = p[1:]

tot = read = codes = 0
out = {}
for s, toks in segs.items():
    row = []
    for i, t in enumerate(toks):
        if len(t) == 3:
            codes += 1
            row.append((t, CODELETTERS[t].upper() if t in CODELETTERS else f'[{t}]', 'code')); continue
        tot += 1
        un = any(a <= i <= b for a, b in UNREAD.get(s, []))
        p = EMEND.get((s, i), key.get(t, '?'))
        if un or p == '?':
            row.append((t, '?', 'unk'))
        else:
            read += 1
            row.append((t, p, 'unc' if (s, i) in EMEND else ''))
    out[s] = row
    print(s, ''.join(p if c != 'code' else f' {p} ' for _, p, c in row))
print(f'cipher tokens {tot}, read {read} ({read / tot:.1%}), unread {tot - read}; code words {codes} (all open)')

if '--reveal' in sys.argv:
    toks = [{'g': '', 'p': 'Continance erleiden will,', 'cls': 'plain'}]
    for t, p, c in out['S3']:
        toks.append({'g': t, 'p': p, 'cls': c})
    toks.append({'g': '', 'p': 'loszugehen', 'cls': 'plain'})
    rev = {'slug': 'baner1640', 'anchor': 'reading', 'title': 'Watch it decipher: the march on the Upper Palatinate',
           'caption': 'Segment S3 of the letter (APUG 568 f. 239r), deciphered with the key rebuilt here.',
           'unit': 'number', 'key_note': 'Homophonic key rebuilt from context cribs (baner1640/key.json); 442 is a code word, left open.',
           'tokens': toks}
    path = os.path.join(HERE, '..', 'docs', 'reveal', 'baner1640.json')
    json.dump(rev, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', path)
