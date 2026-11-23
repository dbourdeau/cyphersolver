"""Decode No. 29 (19/31 Oct 1810; NARA M35 reel 2 frames 185R-189L) with the key sheet alone, from both transcriptions.

python decode_no29.py > no29_decode.txt

The key sheet is the State Department code sheet, NARA M97 roll 13 frames 1056-1057 (Weber WE028), as transcribed in
../../morris1813/beling/key/codebook_M97_13_transcription.csv (column code_number, reading; unchanged). For comparison
each group also gets ../code_table.tsv's value. Line by line, for the first transcription (transcriptions/no29_first.txt,
frozen 23 Oct 2026) and the blind second one (transcriptions/no29_second.txt, 22 Nov 2026): number=sheet value, with
the table's value after a slash where it differs, '?' where neither has one. Alternatives [a/b] are decoded both ways.
No context, no correction: the unedited output of the key. Python standard library only.
"""
import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sheet = {}
for r in csv.DictReader(open(os.path.join(HERE, '..', '..', 'morris1813', 'beling', 'key', 'codebook_M97_13_transcription.csv'), encoding='utf8')):
    sheet[int(r['code_number'])] = r['reading'] or '?'
table = {}
for l in open(os.path.join(HERE, '..', 'code_table.tsv'), encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if not l.startswith('#') and len(p) > 1 and p[0].isdigit():
        table[int(p[0])] = p[1]

def val(n):
    s, t = sheet.get(n, '?'), table.get(n)
    return s if t is None or t == s else f'{s}/{t}'

def decode_line(s):
    out = []
    for tok in s.split():
        m = re.fullmatch(r'\[?(\d+)(?:/(\d+))?\]?(.*)', tok.replace('.', ''))
        if not m:
            out.append(tok if re.fullmatch(r'[A-Za-z]+', tok) else tok)
            continue
        a, b, rest = m.group(1), m.group(2), m.group(3)
        mark = ''.join(ch for ch in rest if ch in '°^+?')
        txt = f'{a}{mark}={val(int(a))}'
        if b:
            txt += f' [or {b}={val(int(b))}]'
        out.append(txt)
    return ' '.join(out)

for name, label in (('no29_first.txt', 'FIRST TRANSCRIPTION (frozen 23 Oct 2026)'), ('no29_second.txt', 'BLIND SECOND TRANSCRIPTION (22 Nov 2026)')):
    print(f'######## {label}: transcriptions/{name}')
    for line in open(os.path.join(HERE, 'transcriptions', name), encoding='utf8'):
        s = line.rstrip('\n')
        if not s.strip() or s.startswith('#'):
            continue
        m = re.match(r'^\s*(\d{1,2})[:\s]\s*(.*)$', s)
        if m and re.search(r'\d{2,}', m.group(2)):
            body = re.sub(r'\(.*?\)|\{.*?\}', ' ', m.group(2))
            print(f'{m.group(1):>3}  {decode_line(body)}')
        else:
            print(s)
    print()
