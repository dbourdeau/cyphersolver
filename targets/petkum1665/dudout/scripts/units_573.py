"""Decode the image-573 units with key T2 (frozen) plus the reading additions, and label each unit.

Usage (from the dudout/ folder):  python3 -I scripts/units_573.py
Reads   key/table_T2.json, key/table_T.json, key/reading_additions_573.tsv, reading/573_units_source.tsv
Writes  reading/573.units.tsv and prints the counts.

Strict class, following the folder's rule (NOTES.md, "The counting rule"):
  S = every token has a spelled value (letter, sign or syllable; tier A or B) and the decoded word
      is the word as read (a-z comparison), or one of the listed spelling variants;
  E = the unit is or contains a code word (whole word or name), all tokens valued and none rank-only;
  N = any token without a value, a rank-only value, or a decoded spelling that does not give the word.
By-sense mark (our sheet): sure / probable / unresolved, as in reading/573_reading.md.
"""
import json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)

T2 = json.load(open(P('key', 'table_T2.json'), encoding='utf-8'))['T']
T1 = json.load(open(P('key', 'table_T.json'), encoding='utf-8'))
INT = set(T1['int'])                       # interpolated in a block (tier B)
ADD = {}                                   # key -> (value, tier) from reading_additions_573.tsv
for l in open(P('key', 'reading_additions_573.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    k, v, tier = l.rstrip('\n').split('\t')[:3]
    ADD[k] = (v, tier)

SIGNS = {'g', '9', 'x', 'beta', 'lambda', 'll', '4', 'm7', '6', 'd', 'ct', 'theta', 'y', 'T', '#', '2', 'f', 'ff', 'U4'}
BLOCKS = [170, 182, 200, 217, 229, 241, 252, 266, 276, 298, 316, 339, 352, 364, 380]
SPELLED = set(str(n) for n in range(14, 37)) | SIGNS | {str(b + i) for b in BLOCKS for i in range(5)} | {'334', '335', '336', '337'}
# decoded spelling accepted as the read word (as written by Petkum; listed, not inferred)
VARIANTS = {('ce', 'ces'), ('ami', 'amie'), ('ami', 'amy'), ('de', 'du'), ('de', 'd'), ('a', 'au'), ('rapel', 'rappel'), ('parti', 'party'), ('ici', 'icy')}

def norm(s):
    return re.sub('[^a-z]', '', unicodedata.normalize('NFD', s.lower()))

def value(tok):
    if tok.startswith('=') and tok.endswith('='):          # plain letters written between groups
        return tok.strip('='), 'plain'
    if tok in T2:
        if tok in INT:
            return T2[tok], 'B'
        return T2[tok], 'A'
    if tok in ADD:
        return ADD[tok]
    return None, 'none'

rows, out = [], []
for l in open(P('reading', '573_units_source.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    line, toks, reading, mark, note = (l.rstrip('\n').split('\t') + [''] * 5)[:5]
    vals = [value(t) for t in toks.split('.')]
    dec = ''.join(v if v is not None else '[%s]' % t for t, (v, _) in zip(toks.split('.'), vals))
    tiers = [tr for _, tr in vals]
    code = any(t not in SPELLED and tr not in ('plain',) for t, (_, tr) in zip(toks.split('.'), vals))
    if any(tr in ('none', 'rank') for tr in tiers):
        cls, why = 'N', 'token without a value' if 'none' in tiers else 'rank-only value'
    elif code:
        cls, why = 'E', 'code word'
    elif norm(dec) == norm(reading) or (norm(dec), norm(reading)) in VARIANTS:
        cls, why = 'S', 'spelled'
    else:
        cls, why = 'N', 'decoded spelling does not give the word'
    out.append((line, toks, dec, reading, mark, cls, why, note))

with open(P('reading', '573.units.tsv'), 'w', encoding='utf-8') as f:
    f.write('# unit\tline\tcipher tokens\tdecoded (T2 + reading additions)\tread as\tby sense\tstrict class\treason\tnote\n')
    for i, r in enumerate(out, 1):
        f.write('%d\t%s\n' % (i, '\t'.join(r)))

n = len(out)
c = {k: sum(1 for r in out if r[5] == k) for k in 'SEN'}
m = {k: sum(1 for r in out if r[4] == k) for k in ('sure', 'probable', 'unresolved')}
print(json.dumps({'units': n, 'strict': c, 'strict_share_S': '%d/%d = %.2f%%' % (c['S'], n, 100 * c['S'] / n),
                  'by_sense': m, 'read_by_sense': '%d/%d = %.2f%%' % (m['sure'] + m['probable'], n, 100 * (m['sure'] + m['probable']) / n),
                  'sure_only': '%d/%d = %.2f%%' % (m['sure'], n, 100 * m['sure'] / n)}, indent=1))
