"""Make we025_poinsett.tsv: the rows of WE025 (Weber 1979, pp. 470-480) for the groups that occur in the Poinsett
documents of this target, and nothing else of Weber's table.

    python3 extract_key.py FULL_TABLE           write we025_poinsett.tsv from our full transcription of WE025
    python3 extract_key.py FULL_TABLE --check   rebuild in memory and compare with the committed file

FULL_TABLE is our we025_table.tsv (number, element, source; 1592 rows), which is not in the repository: it is a
transcription of Weber's printed table. Its sha256 was recorded before any decoding (we025_SHA256.txt); this script
prints the hash of the file it is given so the two can be compared.

Groups taken (all numbers with no unread digit):
  1813  our frozen numerals (../transcription/numerals_1813_frozen.txt, every alternative {a|b}), the numbers the
        reading uses (../groups_1813-02-20.tsv), Daniel Bourdeau's transcription (../../transcription.tsv), and 807,
        the one group legible in P0;
  1814  ../../ciphertext_1814.txt, and 338 and 485 (image rereads of 337 and 435);
  1811  the 19 groups of Poinsett's 29 June 1811 despatch (../../dudout/README.md, key_1811_additions.tsv);
  cited 1209 and 1201, named in a note of the reading (a possible 'confusion'); they do not occur in the letters.
"""
import csv, hashlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
BEL = HERE.parent
TGT = BEL.parent
OUT = HERE / 'we025_poinsett.tsv'
COLS = ['number', 'element', 'grade', 'weber_text', 'post_freeze', 'occurs', 'key_1814', 'dudout_1811']
TEXT = {'weber_ocr_ok': 'text layer', 'weber_ocr_repaired': 'text layer, repaired in extraction',
        'image_checked': 'checked on the page image'}


def nums(s):
    return [int(x) for x in re.findall(r'(?<![\d?])(\d+)(?![\d?])', s)]


def groups():
    occ = {}
    def add(n, tag):
        occ.setdefault(n, [])
        if tag not in occ[n]: occ[n].append(tag)
    for L in open(BEL / 'transcription' / 'numerals_1813_frozen.txt', encoding='utf-8'):
        if L.startswith('#') or not L.strip(): continue
        body = re.sub(r'\[[^\]]*\]', ' ', L.split(' ', 1)[1])
        for t in body.split():
            for n in nums(t): add(n, '1813')
    for r in csv.DictReader(open(BEL / 'groups_1813-02-20.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if r['used']: add(int(r['used']), '1813')
    for L in open(TGT / 'transcription.tsv', encoding='utf-8'):
        if L.startswith('#') or L.startswith('passage'): continue
        f = L.rstrip('\n').split('\t')
        if f[3] == 'ILLEGIBLE': continue
        for t in f[3].split():
            if '...' in t or t.count('?') > 1: continue
            for n in nums(t.replace('?', '')): add(n, '1813')
    add(807, '1813')
    for L in open(TGT / 'ciphertext_1814.txt', encoding='utf-8'):
        for n in nums(L): add(n, '1814')
    for n in (338, 485): add(n, '1814')
    m = re.search(r'^\s+(1121 713 .*)$', (TGT / 'dudout' / 'README.md').read_text(encoding='utf-8'), re.M)
    for n in nums(m.group(1)): add(n, '1811')
    for n in (1209, 1201): add(n, 'cited')
    return occ


def side_key(path, col_g, col_v):
    d = {}
    for L in open(path, encoding='utf-8'):
        if L.startswith('#') or L.startswith('group'): continue
        f = L.rstrip('\n').split('\t')
        d[int(f[col_g])] = f[col_v]
    return d


def build(full):
    we = {int(r['number']): r for r in csv.DictReader(open(full, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)}
    post = {int(r['number']): r['corrected'] for r in csv.DictReader(open(HERE / 'we025_postfreeze_corrections.tsv', encoding='utf-8'),
                                                                     delimiter='\t', quoting=csv.QUOTE_NONE)}
    k14 = side_key(TGT / 'key_1814.tsv', 0, 1)
    k11 = side_key(TGT / 'dudout' / 'key_1811_additions.tsv', 0, 1)
    rows = ['\t'.join(COLS)]
    occ = groups()
    for n in sorted(occ):
        r = we.get(n)
        if r is None:
            rows.append('\t'.join([str(n), '', '', 'not in WE025 (above 1592)', '', ','.join(occ[n]), k14.get(n, ''), k11.get(n, '')]))
            continue
        rows.append('\t'.join([str(n), r['element'], 'H', TEXT[r['source']], post.get(n, ''), ','.join(occ[n]),
                               k14.get(n, ''), k11.get(n, '')]))
    return '\n'.join(rows) + '\n'


if __name__ == '__main__':
    full = sys.argv[1]
    print('sha256 of the full table given:', hashlib.sha256(open(full, 'rb').read()).hexdigest())
    print('frozen hash (we025_SHA256.txt):  ', open(HERE / 'we025_SHA256.txt').read().split('we025_table.tsv')[0].split()[-1])
    text = build(full)
    if '--check' in sys.argv:
        same = text == OUT.read_text(encoding='utf-8')
        print('we025_poinsett.tsv', 'matches' if same else 'DIFFERS FROM', 'a rebuild from the full table')
        sys.exit(0 if same else 1)
    OUT.write_text(text, encoding='utf-8')
    print(f'wrote {OUT.name}: {text.count(chr(10)) - 1} groups')
