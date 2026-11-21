"""Compare the letter-for-letter decryptions of testi1630 with the printed text of
Fulvio Testi, Lettere, ed. M. L. Doglio, vol. 1 (Bari, Laterza 1967), as OCR'd by the Internet Archive
(item 236TestiLettere1Si254, file 236_Testi_Lettere_1_si254_djvu.txt, public domain mark per the item page).

usage: python3 compare_doglio.py <path to 236_Testi_Lettere_1_si254_djvu.txt>
       (download: https://archive.org/download/236TestiLettere1Si254/236_Testi_Lettere_1_si254_djvu.txt)
Run from targets/testi1630/dudout/. Prints a TSV: for each decryption, the share of its letters found in order
(longest common subsequence via difflib matching blocks) in the printed letter, and the best score against
any other printed letter of Feb-Mar 1630 as a control.
Normalisation on both sides: lower case, accents off, v->u, j->i, k->c, z->t, h dropped, doubled letters collapsed
(the edition modernises spelling: retentione/retenzione, Sabioneta/Sabbioneta).
"""
import sys, re, difflib, pathlib, hashlib
OCR = pathlib.Path(sys.argv[1])
lines = OCR.read_text(encoding='utf-8').split('\n')
# line ranges of Doglio nos. 205-216 in that OCR file (1-based, inclusive)
RANGES = {'205': (10520, 10541), '206': (10542, 10590), '207': (10591, 10615), '208': (10616, 10634),
          '209': (10635, 10807), '210': (10808, 10874), '211': (10875, 10922), '213': (10964, 11016),
          '214': (11017, 11056), '216': (11074, 11105)}
DOCS = {'cc07r_1630-02-07': '205', 'cc09_1630-02-15': '206', 'cc11r_1630-02-15': '207',
        'cc13r_1630-02-22_lines1-8': '210', 'cc16_1630-02-22': '211', 'cc20_1630-03-01': '213',
        'cc23r_1630-03-14': '216'}
def norm(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('k', 'c')
    for a, b in (('[àá]', 'a'), ('[èé]', 'e'), ('[ìí]', 'i'), ('[òó]', 'o'), ('[ùú]', 'u')):
        s = re.sub(a, b, s)
    s = re.sub(r'[^a-z]', '', s)
    s = re.sub(r'(.)\1', r'\1', s)
    return s.replace('z', 't').replace('h', '')
def printed(n):
    a, b = RANGES[n]
    t = '\n'.join(lines[a - 1:b]).replace('¬\n', '')
    t = re.sub(r'(LETTERE.*|FEBBRAIO 1630|MARZO 1630|\n\s*\d+\s*\n)', '\n', t)
    return norm(t)
P = {n: printed(n) for n in RANGES}
here = pathlib.Path(__file__).resolve().parent.parent
print('ocr_sha256\t' + hashlib.sha256(OCR.read_bytes()).hexdigest())
print('decryption\tdoglio_no\tletters\tmatched_own\tshare_own\tbest_other_no\tshare_best_other')
for d, n in DOCS.items():
    t = (here / f'decryption_{d}.txt').read_text(encoding='utf-8')
    dec = ''.join(l.split(':', 1)[1] for l in t.split('\n') if ':' in l and not l.startswith('#'))
    dec = norm(re.sub(r'[\[\]?]', '', dec))
    def m(x): return sum(b.size for b in difflib.SequenceMatcher(None, dec, x, autojunk=False).get_matching_blocks())
    own = m(P[n]); best = max((m(P[k]), k) for k in P if k != n)
    print(f'{d}\t{n}\t{len(dec)}\t{own}\t{own/len(dec):.3f}\t{best[1]}\t{best[0]/len(dec):.3f}')
