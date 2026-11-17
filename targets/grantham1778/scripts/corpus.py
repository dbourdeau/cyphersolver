"""The fifteen crib despatches, in the order the table was built from, with the second reading's corrections applied.
Run the scripts from the target folder: python scripts/build_table.py ; python scripts/run_test.py"""
import re, csv, os
from parse import parse
HERE = os.path.dirname(os.path.abspath(__file__))
CRIBS = os.path.join(os.path.dirname(HERE), 'transcriptions', 'cribs')
# order and the short folder labels (h1..h4 = four helper readers, mine = the worker) are those of the original run;
# the labels are kept because corrections_after_second_reading.tsv names the files by them
ORDER = [('h1', 'SP94-205_ff12-13_img18-19.txt'), ('h1', 'SP94-205_ff14-15_img20-21.txt'), ('h1', 'SP94-205_ff36-37_img44-45.txt'),
         ('h1', 'SP94-205_ff48-50_img59-61.txt'), ('h2', 'SP94-205_ff102-103_img122-123.txt'), ('h2', 'SP94-205_ff65-66_img80-81.txt'),
         ('h2', 'SP94-205_ff73-76_img90-93.txt'), ('h3', 'SP94-205_ff132-133_img158-159.txt'), ('h3', 'SP94-205_ff185-186_img214-215.txt'),
         ('h3', 'SP94-205_ff80-83_img98-101.txt'), ('h4', 'SP94-205_ff219-222_img252-255.txt'), ('h4', 'SP94-205_ff253-256_img289-292_No33.txt'),
         ('h4', 'SP94-205_ff253-256_img289-292_No34.txt'), ('mine', 'SP94-205_ff269-270_img309-310_No36.txt'), ('mine', 'SP94-205_ff271-273_img312-314_No37.txt')]
FILES = [lab + '/' + ('n36_mine.txt' if 'No36' in f else 'n37_mine.txt' if 'No37' in f else f) for lab, f in ORDER]
PATH = {k: os.path.join(CRIBS, f) for k, (lab, f) in zip(FILES, ORDER)}
def words(g):
    g = re.sub(r'\[\?\]', '', g)
    return [w for w in re.findall(r"[A-Za-z][A-Za-z'’]*", g)]
CORR = {}
_c = os.path.join(CRIBS, 'corrections_after_second_reading.tsv')
if os.path.exists(_c):
    for r in list(csv.reader(open(_c, encoding='utf-8'), delimiter='\t'))[1:]:
        CORR.setdefault((r[0], r[1], int(r[2])), []).append((int(r[3]), r[4], r[5]))
_X = [0]
def load(f):
    d = parse(PATH[f]); d['file'] = f
    # apply the reconciled second reading: replace a numeral, or exclude it (unique negative number, never matched)
    page = ''; li = 0
    for k, v in d['items']:
        if k == 'P': page = v; li = 0
        elif k == 'F':
            li += 1
            for first, act, new in CORR.get((f, page, li), []):
                for t in v:
                    if t.get('n') == first:
                        if act == 'replace': t['n'] = int(new)
                        else: _X[0] -= 1; t['n'] = _X[0]
                        break
    lines = []; g = []; page = ''
    for k, v in d['items']:
        if k == 'P': page = v
        elif k == 'G':
            if v != '(none)': g += words(v)
        elif k == 'F':
            lines.append({'g': g, 'f': [t['n'] for t in v if 'n' in t], 'ul': [t['ul'] for t in v if 'n' in t], 'alt': [t['alt'] for t in v if 'n' in t], 'page': page, 'clear': ' '.join(t['w'] for t in v if 'w' in t)})
            g = []
    if g: lines.append({'g': g, 'f': [], 'ul': [], 'alt': [], 'page': page, 'clear': ''})
    return {'file': f, 'head': d['head'], 'lines': lines}
if __name__ == '__main__':
    for f in FILES:
        d = load(f)
        print(f, d['head'][:50], sum(len(l['f']) for l in d['lines']), 'numbers', sum(len(l['g']) for l in d['lines']), 'words')
