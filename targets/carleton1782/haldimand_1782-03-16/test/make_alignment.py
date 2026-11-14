"""Write alignment.tsv: both cipher copies decoded with the unchanged Army List key, against the letterbook
copy (LAC MG21 B.148 p. 21) and the 1781 American translation (PCC item 51 vol. 1 p. 738).
    python targets/carleton1782/haldimand_1782-03-16/test/make_alignment.py"""
import sys, pathlib
H = pathlib.Path(__file__).resolve().parent; F = H.parent
sys.path.insert(0, str(H))
from parse import parse
key = {}
for l in (F.parent / 'key/armylist_titlepage_1778.txt').read_text(encoding='utf-8').splitlines():
    if '\t' in l and not l.startswith('#'):
        n, s = l.split('\t', 1); key[int(n)] = [c.lower() for c in s if c.isalpha() or c == '&']
def dec(c):
    if c == '@': return 'q'
    if not isinstance(c, tuple): return '?'
    row = key.get(c[0]); return row[c[1]-1] if row and 1 <= c[1] <= len(row) else '?'
LB = ('A few days ago I wrote more fully This [will I hope] go directly to you [I have not] heard from you since your '
      'letter of the [2d] Augt nor received the least Intelligence of Moment from Any Quarter since that Time Common '
      'Reports [make me] anxious to hear from You [& I] intreat you will let me have that [Pleasure] not trusting to a '
      'single messenger [but by] different Routes I request [the same] of Govr. Robinson St_Johns March 16th (paraph)')
TR = ('A few days ago I wrote more fully This [will I hope] go directly to you [I have not] heard from you since your '
      'Letter of (omitted) [2d] August nor received any other Intelligence of Moment from any Quarter since that Time Common '
      'Reports [make me] anxious to hear from you [and I] entreat you would let me have that [Pleasure] not trusting to a '
      'single Messenger [but by] different Routes I request [the same] of Governor Robertson Sorel March sixteenth (perhaps)_A._F.')
def words(s):
    out, buf = [], []
    for t in s.split():
        if t.startswith('[') or buf:
            buf.append(t)
            if t.endswith(']'): out.append(' '.join(buf)); buf = []
            continue
        out.append(t)
    # attach bracketed clear words to the following word
    res, pre = [], ''
    for w in out:
        if w.startswith('['): pre = w + ' '; continue
        res.append(pre + w.replace('_', ' ')); pre = ''
    return res
a = parse(H / "transcription_reading.txt"); b = parse(F / 'transcription_pcc51v1p737.txt')
lb, tr = words(LB), words(TR)
assert len(a) == len(b) == len(lb) == len(tr) == 66, (len(a), len(b), len(lb), len(tr))
fmt = lambda cs: ' '.join('%d.%d' % c if isinstance(c, tuple) else c for c in cs)
rows = ['word\tclear_in_cipher\tp227_cipher\tp227_decode\tp737_cipher\tp737_decode\tletterbook_B148_p21\ttranslation_1781_p738']
for i, (x, y, l, t) in enumerate(zip(a, b, lb, tr), 1):
    rows.append('\t'.join([str(i), ' '.join(x[0]), fmt(x[1]), ''.join(dec(c) for c in x[1]), fmt(y[1]),
                           ''.join(dec(c) for c in y[1]), l, t]))
(F / 'alignment.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
print('wrote alignment.tsv,', len(rows) - 1, 'words')
