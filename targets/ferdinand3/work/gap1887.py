# Last attempt (9 Oct 2026) on the two open R1887 pieces: every value each sign takes in this letter (and the
# family's other vowels), pruned to strings that segment into Latin words of the la-gutenberg corpus, ranked by the
# `la` LM in the sentence context.
import sys, re, collections, pickle, os
sys.path.insert(0, r'C:\Users\dbour\cypher')
from lang import lm
M = lm.load('la')
cache = os.path.join(os.path.dirname(__file__), '__pycache__', 'la_words.pkl')
if os.path.exists(cache):
    W = pickle.load(open(cache, 'rb'))
else:
    txt = open(r'C:\Users\dbour\cypher\lang\corpora\la-gutenberg.txt', encoding='utf-8').read().lower()
    for a, b in (('j', 'i'), ('v', 'u'), ('y', 'i'), ('k', 'c'), ('w', 'u'), ('æ', 'ae'), ('œ', 'oe')):
        txt = txt.replace(a, b)
    W = {w: c for w, c in collections.Counter(re.findall(r'[a-z]+', txt)).items() if c >= 3}
    pickle.dump(W, open(cache, 'wb'))
P = set()
for w in W:
    for i in range(1, len(w) + 1): P.add(w[:i])
def ok(w): return w in W and (len(w) > 1 or w in 'aeo')
def search(opts, maxw):
    out = set()
    def rec(k, words, cur):
        if k == len(opts):
            if cur == '' or ok(cur):
                ws = words + ([cur] if cur else [])
                if len(ws) <= maxw: out.add(' '.join(ws))
            return
        for o in opts[k]:
            s = cur + o
            # split s into (completed words..., partial) greedily over all break points
            def br(s, words):
                if len(words) > maxw: return
                if s == '' or s in P: rec(k + 1, words, s)
                for j in range(1, len(s)):
                    if ok(s[:j]): br(s[j:], words + [s[:j]])
            br(s, words)
    rec(0, [], ''); return out
V = 'aeiou'
def run(name, L, R, opts, maxw, top=40):
    cands = search(opts, maxw)
    base = M.score(L + ' ' + R)
    res = sorted(((M.score(L + ' ' + t + ' ' + R) - base) / max(1, len(t)), t) for t in cands)[::-1]
    print('==', name, len(cands), 'segmentable candidates (score = LM gain per char in context)', flush=True)
    for sc, t in res[:top]: print(round(sc, 2), t, [W[w] for w in t.split()], flush=True)
o1 = [['c', 't', 'g', 'ct'], ['r', ''], ['i', 'e', 'a'], ['s', 'ti', 'si', 'ss', ''], ['d' + v for v in V] + ['d'], ['s', 'ss', '']]
run('P2.02 n+ m/ a+ 45 hu tt', 'cum eventus uero inde', 'non minoris emolumenti uel detrimenti', o1, 2)
# The letter groups show their vowel openly (ad = na, xir = ti, ten = re), so only the singletons and the
# ambiguous 4 vary: 4 in {m, n, s, -}, 4) and h^ga any letter or none, e~ a vowel ending or none.
m4 = ['m', 'n', 's', '']
AL = list('abcdefghilmnopqrstux') + ['']
o2 = [m4, ['mi'], ['na'], ['n'], ['ti'], ['r'], ['i'], m4, AL, ['ti'], m4, ['re'], AL + ['ga', 'gu', 'qu', 'li', 'la'], ['a'], ['t'],
      ['o', 'i', 'io', 'e', 'u', 'um', 'is', 'us', 'ur', 'ae', '']]
run('P2.14-15 16-token span', 'facilius mihi ad peragendum hunc ipsorumque', 'negotium armorum suorum motu et diuersione', o2, 5)
