"""Measure the share of decrypted tokens that read as words: segment each cipher run (clear [..] removed) into words
by a unigram DP over a period lexicon (lang/ corpus), then count tokens found in the lexicon (len>=2, or a, i/e, u).
  python sense.py DECRYPT  de|la"""
import re, sys, os, math, collections, pickle
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm
src, lang = sys.argv[1], sys.argv[2]
corp = {'de': 'de-dta-1470-1610', 'la': 'la-gutenberg'}[lang]
scheme = 'early' if lang == 'de' else 'latin'
cache = os.path.join(os.path.dirname(__file__), f'lex_{lang}.pkl')
if os.path.exists(cache): C = pickle.load(open(cache, 'rb'))
else:
    t = open(os.path.join(os.path.dirname(__file__), '..', '..', 'lang', 'corpora', corp + '.txt'), encoding='utf8').read()
    C = collections.Counter(w for w in re.findall(r'[a-z]+', lm.norm(t, scheme)) if len(w) < 25)
    C = {w: c for w, c in C.items() if c >= 3}; pickle.dump(C, open(cache, 'wb'))
N = sum(C.values()); lp = {w: math.log(c / N) for w, c in C.items()}
def seg(s):
    n = len(s); best = [(0.0, [])] + [(-1e18, [])] * n
    for j in range(1, n + 1):
        for i in range(max(0, j - 20), j):
            w = s[i:j]; sc = lp.get(w, -25.0 - 3 * len(w)) if (len(w) > 1 or w in 'aeiou') else -40.0
            v = best[i][0] + sc
            if v > best[j][0]: best[j] = (v, best[i][1] + [w])
    return best[n][1]
toks = []; lines = []
for l in open(src, encoding='utf8'):
    m = re.match(r'(\d\d) (.*)', l)
    if not m: continue
    for run in re.split(r'\[[^\]]*\]', m.group(2)):
        run = lm.norm(run, scheme).replace(' ', '')
        if run: ws = seg(run); toks += ws; lines.append(' '.join(w if w in lp else w.upper() for w in ws))
good = [w for w in toks if w in lp]
print(f'tokens {len(toks)}  read-as-words {len(good)}  share {100*len(good)/len(toks):.1f}%  (unknown shown in CAPS)')
open(src + '.seg', 'w', encoding='utf8').write('\n'.join(lines) + '\n')
