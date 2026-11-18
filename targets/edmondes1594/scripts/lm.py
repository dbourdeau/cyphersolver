"""Letter n-gram model of 1590s English in original spelling.
Corpus: Stevenson (ed.), Correspondence of Sir Henry Unton, Roxburghe Club 1847 (archive.org cu31924027964471,
Unton's own despatches from Henri IV's camp, 1591-92, original spelling), plus the clear text of Edmondes's own
letters printed by Butler 1913 (pp. 141-147, copied from HathiTrust into corpus_butler.txt).
Plain alphabet is 24 letters: j is folded into i and v into u (Elizabethan usage; the cipher has no j)."""
import os, re, math, collections, json
HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, '..', 'corpus')
PA = 'abcdefghiklmnopqrstuwxyz'
def norm(t):
    t = t.lower().replace('j', 'i').replace('v', 'u')
    return re.sub('[^a-z]', '', t)
def corpus():
    parts = []
    p = os.path.join(CORPUS, 'unton_cu31924027964471_djvu.txt')
    raw = open(p, errors='ignore').read()
    # keep lines with old-spelling markers to bias toward the letters themselves
    parts.append(raw)  # whole volume: letters in original spelling plus Stevenson's notes
    b = os.path.join(CORPUS, 'corpus_butler.txt')
    if os.path.exists(b):
        parts.append(open(b).read() * 3)
    return norm(' '.join(parts))
def build(n=4, out=None):
    t = corpus()
    c = collections.Counter(t[i:i+n] for i in range(len(t)-n+1))
    tot = sum(c.values())
    floor = math.log10(0.01/tot)
    m = {k: math.log10(v/tot) for k, v in c.items()}
    out = out or os.path.join(HERE, '..', f'lm{n}.json')
    json.dump({'n': n, 'floor': floor, 'm': m, 'chars': len(t)}, open(out, 'w'))
    return len(t), len(c)
def load(n=4):
    d = json.load(open(os.path.join(HERE, '..', f'lm{n}.json')))
    return d['m'], d['floor']
if __name__ == '__main__':
    for n in (3, 4):
        print(n, build(n))
