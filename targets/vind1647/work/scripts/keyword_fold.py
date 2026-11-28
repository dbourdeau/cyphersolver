"""After the solve (post hoc): is the reciprocal key a keyword alphabet folded on itself (S[i] <-> S[23-i]) or set in
two rows (S[i] <-> S[i+12])? 24-letter alphabet without j and v. Keywords: every word of the da, de, la lexicons
(freq >= 2) and the plain alphabet itself; both directions of the rest of the alphabet."""
import gzip, json, os, re
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]          # targets/vind1647/work/scripts -> repository root
A = 'abcdefghiklmnopqrstuwxyz'
PAIRS = {frozenset(p) for p in ['ax', 'by', 'cz', 'dh', 'ep', 'fo', 'gn', 'im', 'kl', 'qr', 'tu', 'sw']}
def norm(w):
    w = w.lower().replace('æ', 'ae').replace('ø', 'oe').replace('å', 'aa').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    return re.sub('[^a-z]', '', w).replace('j', 'i').replace('v', 'u')
words = {''}
for l in ('da', 'de', 'la'):
    d = json.load(gzip.open(REPO / 'lang' / 'lexicons' / ('%s.json.gz' % l)))
    words |= {norm(w) for w, f in d.items() if f >= 2}
best = []
for w in words:
    for rest in (A, A[::-1]):
        s = ''.join(dict.fromkeys(w + rest))
        for kind, pr in (('fold', [frozenset((s[i], s[23 - i])) for i in range(12)]), ('rows', [frozenset((s[i], s[i + 12])) for i in range(12)])):
            n = sum(p in PAIRS for p in pr)
            best.append((n, kind, w, s))
best.sort(reverse=True)
print('keywords tried: %d; best pair agreements (of 12):' % len(words))
for b in best[:10]: print(b)
